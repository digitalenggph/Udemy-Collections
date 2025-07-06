import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm.exc import UnmappedInstanceError
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


# with app.app_context():
#     db.create_all()

def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe = {
                    "name": random_cafe.name,
                    "map_url": random_cafe.map_url,
                    "img_url": random_cafe.img_url,
                    "location": random_cafe.location,
                    "amenities": {
                        "seats": random_cafe.seats,
                        "has_toilet": random_cafe.has_toilet,
                        "has_wifi": random_cafe.has_wifi,
                        "has_sockets": random_cafe.has_sockets,
                        "can_take_calls": random_cafe.can_take_calls,
                        "coffee_price": random_cafe.coffee_price
                    }
                }
            )


@app.route("/all", methods=["GET"])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    cafe_list = [to_dict(cafe) for cafe in all_cafes]
    return jsonify(cafe=cafe_list)

@app.route('/search/')
def search_cafe():
    loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location.ilike(f"%{loc}%")))
    all_cafes = result.scalars().all()
    cafe_list = [to_dict(cafe) for cafe in all_cafes]

    if not cafe_list:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        }), 404

    return jsonify(cafe=cafe_list)


# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    seats = request.form.get("seats")
    has_toilet = bool(request.form.get("has_toilet"))
    has_wifi = bool(request.form.get("has_wifi"))
    has_sockets = bool(request.form.get("has_sockets"))
    can_take_calls = bool(request.form.get("can_take_calls"))
    coffee_price = request.form.get("coffee_price")

    new_cafe = Cafe(name=name,
                    map_url=map_url,
                    img_url=img_url,
                    location=location,
                    seats=seats,
                    has_toilet=has_toilet,
                    has_wifi=has_wifi,
                    has_sockets=has_sockets,
                    can_take_calls=can_take_calls,
                    coffee_price=coffee_price)

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."}), 201


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['patch'])
def update_price(cafe_id):
    new_price = request.form.get("new_price")
    try:
        cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalars().first()
        cafe_to_update.coffee_price = new_price
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    API_KEY_TOPSECRET = os.environ.get('API_KEY_TOPSECRET')
    api_key = request.args.get("api_key")
    if api_key == API_KEY_TOPSECRET:
        try:
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalars().first()
            db.session.delete(cafe_to_delete)
        except UnmappedInstanceError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})

    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403

if __name__ == '__main__':
    app.run(debug=True)
