from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

API_TOKEN = os.getenv("API_TOKEN")
API_HEADERS = {
    "Authorization": API_TOKEN,
    "accept": "application/json"
}


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


class EditMovieForm(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 6.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        params = {
            "query": request.form["title"],
            "include_adult": "false",
            "language": "en-US",
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=params, headers=API_HEADERS)
        search_results = response.json()['results']
        return render_template('select.html', movies=search_results)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={"language": "en-US"}, headers=API_HEADERS)
        new_movie = response.json()
        new_movie_obj = Movie(
            title=new_movie["title"],
            year=new_movie["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/original{new_movie['poster_path']}",
            description=new_movie["overview"]
        )
        db.session.add(new_movie_obj)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie_obj.id))


if __name__ == '__main__':
    app.run(debug=True)
