from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

sections = soup.find_all(name="section", class_="gallery__content-item")
movie_titles = [movie.find(class_="title").getText() for movie in sections]
movie_titles.reverse()

with open("movies.txt", "w") as file:
    formatted_movies = [f"{movie}\n" for movie in movie_titles]
    file.writelines(formatted_movies)
