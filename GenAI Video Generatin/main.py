from utils.news_scraper import get_trending_news
from utils.script_generator import generate_script
from utils.image_fetcher import get_image_urls
from utils.tts import text_to_speech
from utils.video_creator import create_video
import os

os.makedirs("assets/images", exist_ok=True)
os.makedirs("assets/audio", exist_ok=True)
os.makedirs("output_videos", exist_ok=True)

news_list = get_trending_news()

for idx, news in enumerate(news_list):
    print(f"Processing topic: {news['title']}")
    script = generate_script(news['title'])
    
    image_urls = get_image_urls(news['title'], count=2)
    image_paths = []
    for i, url in enumerate(image_urls):
        img_path = f"assets/images/img_{idx}_{i}.jpg"
        with open(img_path, 'wb') as f:
            f.write(requests.get(url).content)
        image_paths.append(img_path)

    audio_path = text_to_speech(script, filename=f"audio_{idx}.mp3")
    create_video(script, image_paths, audio_path, output_file=f"news_video_{idx}.mp4")
