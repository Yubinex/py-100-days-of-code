from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies = soup.find_all(name="h3", class_="title")
titles = [movie.getText() for movie in movies]
ordered_movies = titles[::-1]
with open("Proj41-WebScraping/movies.txt", "w") as f:
    for movie in ordered_movies:
        f.write(f"{movie}\n")
