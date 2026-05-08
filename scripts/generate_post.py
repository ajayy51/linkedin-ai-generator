import os
import json
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TOPIC = os.getenv("TOPIC")


def generate_post(topic):

    prompt = f"""
Write a professional LinkedIn post about:

{topic}

Requirements:
- engaging hook
- professional tone
- concise
- emojis
- hashtags
"""

    response = requests.post(

        "https://api.groq.com/openai/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },

        json={
            "model": "llama-3.3-70b-versatile",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            "temperature": 0.7
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]


def generate_image(topic):

    return (
        "https://image.pollinations.ai/prompt/"
        + topic.replace(" ", "%20")
        + "%20linkedin%20post"
    )


post = generate_post(TOPIC)

image = generate_image(TOPIC)

result = {
    "post": post,
    "image": image
}

os.makedirs("generated", exist_ok=True)

with open(
    "generated/post.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))