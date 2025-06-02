import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_script(topic):
    prompt = f"Make a short 60-second script for a video about: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
