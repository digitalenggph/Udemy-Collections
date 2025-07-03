from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Column

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"{{'title': '{self.title}', 'author': '{self.author}', 'rating': {self.rating}}}"



@app.route('/')
def home():
    # add to dictionary
    result = db.session.execute(db.select(Book)).scalars().all()
    return render_template('index.html', all_books=result)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # Get data from form
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        rating = request.form.get("rating")

        new_book = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))


    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    if request.method == "POST":
        # Get data from form
        new_rating = request.form.get("new_rating")
        book_to_update.rating = float(new_rating)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book_id=book_id, book_to_update=book_to_update)

@app.route("/delete/<int:book_id>", methods=['GET', 'POST'])
def delete_book(book_id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

