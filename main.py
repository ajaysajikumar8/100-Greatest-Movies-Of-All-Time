import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_site = response.text
soup = BeautifulSoup(movies_site, "html.parser")
all_movies = [title.getText() for title in soup.findAll(name="h3" , class_ = "title")]
all_movies.reverse()
print(all_movies)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")