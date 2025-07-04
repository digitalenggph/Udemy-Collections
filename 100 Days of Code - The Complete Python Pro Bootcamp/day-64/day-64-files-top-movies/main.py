import sqlalchemy
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, result_tuple
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# API

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
# initialize the app with the extension
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking:Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)


# CREATE EDIT FORM

class MovieForm(FlaskForm):
    new_rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    movie_to_add = StringField('Movie Title', validators=[DataRequired()])
    add = SubmitField('Add')


# CREATE API CALL

MOVIEDB_API = os.getenv('MOVIEDB_API_KEY')
MOVIEDB_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIEDB_TOKEN = os.getenv('MOVIEDB_API_TOKEN')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MOVIEDB_TOKEN}"
}

def query_movie_title(movie_name):
    params = {
        "query": movie_name,
    }

    response = requests.get(MOVIEDB_URL, headers=headers, params=params)
    output = response.json()
    results = output['results']
    return results


def query_movie_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "language": "en-US"
    }

    response = requests.get(url, headers=headers, params=params)
    output = response.json()
    return output



@app.route("/")
def home():
    result = db.session.execute(db.select(Movie)).scalars().all()

    rating_list = list(set([movie.rating for movie in result]))
    sorted_rating_list = sorted(rating_list, reverse=True)

    for movie in result:
        movie.ranking = sorted_rating_list.index(movie.rating) + 1
        db.session.commit()


    result = db.session.execute(
                db.select(Movie).order_by(sqlalchemy.desc(Movie.ranking))
                ).scalars().all()

    print(sorted_rating_list)
    return render_template("index.html", all_movies=result)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = MovieForm()

    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit() and request.method == "POST":
        new_rating = request.form.get('new_rating')
        new_review = request.form.get('new_review')

        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete/<movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit() and request.method == "POST":
        movie_to_add = request.form.get('movie_to_add')
        movie_list = query_movie_title(movie_to_add)
        return render_template("select.html", movie_list=movie_list)

    return render_template("add.html", form=form)

@app.route("/select/<movie_id>", methods=["GET", "POST"])
def select(movie_id):
    result = query_movie_id(movie_id)

    new_movie = Movie(
        title=result['title'],
        year=result['release_date'][:4],
        description=result['overview'],
        rating=round(result['vote_average'],2),
        ranking=0,
        review="None",
        img_url="https://image.tmdb.org/t/p/w500"+result['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.filter_by(title=result['title']).first()
    return redirect(url_for('edit', movie_id=movie.id))


# -------------------- ADD FIRST NEW MOVIE -------------------- #

# with app.app_context():
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# -------------------- ADD SECOND NEW MOVIE -------------------- #

# with app.app_context():
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#
#     db.session.add(second_movie)
#     db.session.commit()

# -------------------------------------------------------------- #

# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
