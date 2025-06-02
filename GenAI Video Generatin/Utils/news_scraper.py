import requests
from config import NEWS_API_KEY

def get_trending_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])[:3]
    return [{"Title of Article": a["title"], "Description about the Article": a["description"]} for a in articles]
