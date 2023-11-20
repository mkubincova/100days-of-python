from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

SECRET_KEY = "test123"


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafes_by_location():
    req_location = request.args.get('loc')
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == req_location)).scalars().all()
    if len(all_cafes):
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(int(request.form.get("has_sockets"))),
        has_toilet=bool(int(request.form.get("has_toilet"))),
        has_wifi=bool(int(request.form.get("has_wifi"))),
        can_take_calls=bool(int(request.form.get("can_take_calls"))),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def edit_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.form.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    return jsonify(error={"Not Found": "Sorry, a cafe with this id does not exist in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    req_api_key = request.args.get('api-key')
    if req_api_key != SECRET_KEY:
        return jsonify(error={"Not Found": "Sorry, that's not allowed. Make sure you have a correct api_key."}), 403
    elif cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "The cafe was successfully deleted."})
    return jsonify(error={"Not Found": "Sorry, a cafe with this id does not exist in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
