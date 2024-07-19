from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/", verify=False)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
movie_tag = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_name = [movie.getText() for movie in movie_tag]
# movie_name = movie_name[::-1]

with open("movies.txt", "w", encoding="UTF-8") as file:
    for index in range(len(movie_name)-1, 0, -1):
        file.write(f"{movie_name[index]}\n")

