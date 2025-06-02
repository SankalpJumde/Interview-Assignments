# 🧠 GenAI Video Generation Tool 🎥

Automatically generate 30–60 second AI-powered videos from trending news topics using cutting-edge Generative AI tools including GPT, TTS, and MoviePy.

---

## 🚀 Features

- 📈 **Trending News Scraping**: Uses NewsAPI to extract the latest trending news headlines.
- ✍️ **Script Generation**: Uses OpenAI or local LLMs to write a short, engaging news script.
- 🖼️ **Image Fetching**: Retrieves relevant images from Google or Pexels based on news topic.
- 🔊 **Text-to-Speech**: Converts script to speech using gTTS or other TTS models.
- 🎬 **Video Creation**: Combines audio and visuals using MoviePy into a short video.
- 💾 **Output**: Saves final video in `output_videos/` folder.

---

## 🗂️ Project Structure

GenAI-Video-Generator/

├── main.py
├── config.py
├── README.md
├── utils/
│ ├── news_scraper.py # Scrapes trending news
│ ├── script_generator.py # Generates script with LLM
│ ├── image_fetcher.py # Downloads relevant images
│ ├── tts.py # Converts script to speech
│ └── video_creator.py # Generates final video
├── Assets/
│ ├── Audio/
│ └── Images/
└── Output videos/ # Final generated videos

🧪 Sample Output
Topic: Operation Sindoor (Indian Army Rescue)
Video Length: ~40 seconds
Voiceover: gTTS (English)
Images: Pulled from Google Images / Pexels
Final Video: output_videos/operation_sindoor.mp4

## 📦 Dependencies
- openai
- gtts
- moviepy
- requests
- beautifulsoup4

## 🔮 To-Do / Improvements
- Add subtitles to videos
- Use ElevenLabs or Bark for better voiceover
- Add UI with Streamlit or Gradio
- Schedule daily auto-video generation

## 👨‍💻 Author
**Sankalp Jumde**  
🎓 B.Tech AI, Class of 2026  
🔗 [[LikendIn](https://www.linkedin.com/in/sankalp-jumde/)] | [[GitHub](https://github.com/SankalpJumde)] | [[Mail](sankalpkrishna1103@gmail.com)]

## 📄 License
This project is licensed under the MIT License.

---

Let me know if you'd like me to:
- Add a `requirements.txt` that matches this
- Generate example screenshots or a video preview thumbnail
- Help deploy this as a web app with Streamlit or Flask

Would you like me to save this as a downloadable file too?
