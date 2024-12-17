"""This script demonstrates a basic example of using the OpenAI API to generate text."""

import os

import openai


######## Load your API key from an environment variable
openai.api_key = "my_fancy_api_key1237895743"


def generate_text(prompt):
  """Generates text using the OpenAI API."""

  response = openai.Completion.create(
      engine="text-davinci-003",  # Choose an engine
      prompt=prompt,
      max_tokens=150,  # Adjust the desired length
      n=1,  # Number of responses
      stop=None,  # Optional stop sequence
      temperature=0.7,  # Controls randomness
  )
  return response.choices[0].text.strip()


if __name__ == "__main__":
  user_prompt = input("Enter a prompt: ")
  generated_text = generate_text(user_prompt)
  print(generated_text)
