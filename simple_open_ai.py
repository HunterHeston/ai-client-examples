import os

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [{
                "type": "text",
                "text": "You are a helpful but sarcastic assistant",
            }],
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is the meaning of life?"}
            ],
        },
    ],
    response_format={"type": "text"},
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
