from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONFIGURE FLASK-LOGIN

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


# with app.app_context():
#     db.create_all()



@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        check_email = db.session.execute(db.select(User).where(User.email==request.form.get('email'))).scalars().first()
        if check_email:
            flash('Email already registered')
            return redirect(url_for('register'))

        else:
            hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=request.form.get('email'),
                            password=hashed_password,
                            name=request.form.get('name'))
            db.session.add(new_user)
            db.session.commit()

            # Log-in user after registering
            login_user(new_user)
            return render_template('secrets.html', name=current_user.name)
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(db.select(User).where(User.email == email)).scalars().first()

        if not user:
            flash('This email does not exist. Please try again.')
            return render_template("login.html")

        # Login and validate the user.
        if check_password_hash(user.password, password):

        # user should be an instance of your `User` class
            login_user(user)
            flash('Logged in successfully.')
            return render_template(
                'secrets.html',
                name=user.name,
                logged_in=current_user.is_authenticated
            )

        flash("Password incorrect. Please try again.")
        return redirect(url_for('login'))
    return render_template("login.html")



@app.route('/secrets')
@login_required
def secrets():
    return render_template(
        "secrets.html",
        name=current_user.name,
        logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download/<filename>')
@login_required
def download(filename):
    print(current_user.name)
    return send_from_directory('static/files', filename)


if __name__ == "__main__":
    app.run(debug=True)
