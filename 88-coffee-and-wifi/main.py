from flask import Flask, render_template, redirect, jsonify, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

ADMIN_KEY = os.getenv('ADMIN_KEY')


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


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe location on Google maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Cover image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Has sockets')
    has_toilet = BooleanField('Has toilet')
    has_wifi = BooleanField('Has wifi')
    can_take_calls = BooleanField('Can take calls')
    seats = StringField('Number of seats', validators=[DataRequired()])
    coffee_price = StringField('Price of coffee', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    cafes_dict = [cafe.to_dict() for cafe in all_cafes]
    cafes_dict.sort(key=lambda x: x['id'], reverse=True)
    return render_template('cafes.html', cafes=cafes_dict)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.data["name"],
            map_url=form.data["map_url"],
            img_url=form.data["img_url"],
            location=form.data["location"],
            has_sockets=bool(int(form.data["has_sockets"])),
            has_toilet=bool(int(form.data["has_toilet"])),
            has_wifi=bool(int(form.data["has_wifi"])),
            can_take_calls=bool(int(form.data["can_take_calls"])),
            seats=form.data["seats"],
            coffee_price=form.data["coffee_price"],
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    req_admin_key = request.headers.get('Authorization')
    if req_admin_key != ADMIN_KEY:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have a correct admin key."}), 403
    elif cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"Success": "The cafe was successfully deleted."})
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with this id does not exist in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
