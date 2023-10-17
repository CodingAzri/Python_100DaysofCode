import requests
from bs4 import BeautifulSoup
from pprint import PrettyPrinter

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
pp = PrettyPrinter()
# Write your code below this line 👇
response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup)
website_title = soup.title
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
# pp.pprint(movie_titles[::-1])
movies = movie_titles[::-1]

with open("100 Best Movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

