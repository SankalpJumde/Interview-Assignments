import requests
from config import PEXELS_API_KEY

def get_image_urls(query, count=2):
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={count}"
    response = requests.get(url, headers=headers).json()
    return [photo["src"]["landscape"] for photo in response.get("photos", [])]
