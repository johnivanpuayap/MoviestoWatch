import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
all_movies = soup.find_all(name='h3', class_='title')

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in all_movies:
        try:
            name = movie.text.split(') ')[1]
        except IndexError:
            name = movie.text.split(': ')[1]
        finally:
            file.write(f"{name}\n")

