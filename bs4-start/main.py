from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/", verify=False  )
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.select(".storylink")
article_texts = []
article_links = []
for article in article_tag:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_score = article_upvote[0]
index_win = 0
for index in range(len(article_upvote)):
    if article_upvote[index] > highest_score:
        highest_score = article_upvote[index]
        index_win = index

print(f"Highest voted story: \ntitle: {article_texts[index_win]}, \nlink:{article_links[index_win]}, "
      f"\nupvote: {article_upvote[index_win]}")


# with open("./website.html", encoding="utf-8") as text:
#     content = text.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
