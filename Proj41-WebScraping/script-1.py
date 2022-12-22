from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = [article_tag.find(name="a") for article_tag in soup.find_all(
    name="span", class_="titleline")]
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [
    int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")
]

largest_num = max(article_upvotes)
index = article_upvotes.index(largest_num)

res: str = f"""
Title: {article_texts[index]}
Link:  {article_links[index]}
Score: {article_upvotes[index]}
"""
print(res)
