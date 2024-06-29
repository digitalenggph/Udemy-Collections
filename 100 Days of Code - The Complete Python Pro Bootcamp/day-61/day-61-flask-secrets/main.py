import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

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
app.secret_key = os.environ.get('ENV_FLASK_SECRET_KEY')  # Set the secret key for the Flask application


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be at "
                                                                                                 "least 8 characters "
                                                                                                 "long.")])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data, form.password.data)
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

"""
FOR FLASK APP SECRET KEY DOCUMENTATION
https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY
https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask#:~:text=In%20order%20to%20use%20session,send%20them%20to%20the%20browser.&text=To%20fix%20this%20you%20just,SECRET_KEY%20in%20your%20config%20file.&text=It's%20always%20a%20good%20idea%20to%20store%20secrets%20away%20from%20versioned%20code.

PUTTING SECRET KEY IN THE APP
https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe
"""
