import os
import sys
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5-mini"

user_input = sys.argv[1] if len(sys.argv) > 1 else None
if not user_input:
    print("No prompt provided.")
    sys.exit(1)
    
source_lang="English"
target_lang="French"

prompt=f"Translate the following {source_lang} text to {target_lang}: {user_input}"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful iterator that translates text from one language to another.",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=model
)

print(response.choices[0].message.content)

