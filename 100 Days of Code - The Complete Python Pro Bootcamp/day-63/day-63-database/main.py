from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Column

app = Flask(__name__)

# ----------- start of sqlite3 sample ----------- #
# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books ("
#                "id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# ----------- end of sqlite3 sample ----------- #

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String(250), nullable=False, unique=True)
    author = Column(String(250), nullable=False)
    rating = Column(Float, nullable=False)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()