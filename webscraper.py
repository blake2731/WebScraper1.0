import requests
from bs4 import BeautifulSoup

response = requests.get("https://techcrunch.com/")


soup = BeautifulSoup(response.content, 'html.parser')



article_titles = soup.find_all('a', {'class': 'post-block__title__link'})

print("Article Titles: ")

for idx, title in enumerate(article_titles):
    if title is not None:
        print(f"{idx + 1}. {title.text.strip()}")