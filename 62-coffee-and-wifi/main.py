from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

COFFEE_RATINGS = [(0, '✘'), (1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')]
WIFI_RATINGS = [(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')]
POWER_RATINGS = [(0, '✘'), (1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening time', validators=[DataRequired()])
    close = StringField('Closing time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', choices=COFFEE_RATINGS, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi rating', choices=WIFI_RATINGS, validators=[DataRequired()])
    power_rating = SelectField('Power outlet rating', choices=POWER_RATINGS, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            csv_file.write("\n")
            csv_file.write(f"{form.data['cafe']},{form.data['location']},{form.data['open']},{form.data['close']},"
                           f"{COFFEE_RATINGS[int(form.data['coffee_rating'])][1]},"
                           f"{WIFI_RATINGS[int(form.data['wifi_rating'])][1]},"
                           f"{POWER_RATINGS[int(form.data['power_rating'])][1]}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
