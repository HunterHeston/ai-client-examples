"""Example code snippet for a custom LLM."""

from typing import List, Optional

from langchain.llms import base
import requests

LLM = base.LLM


class CustomLLM(LLM):
  """A custom LLM that interacts with a remote API."""

  def __init__(self, api_url: str, api_key: str, max_tokens: int = 100):
    self.api_url = api_url
    self.api_key = api_key
    self.max_tokens = max_tokens

  def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
    # API request payload
    payload = {"prompt": prompt, "max_tokens": self.max_tokens}

    # API headers
    headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
    }

    # Make the API request
    api_response = requests.post(self.api_url, json=payload, headers=headers)
    if api_response.status_code != 200:
      raise ValueError(
          f"Error in API call: {api_response.status_code} {api_response.text}"
      )

    # Parse the response
    response_data = api_response.json()
    return response_data.get("response", "")

  @property
  def _identifying_params(self):
    """Return parameters that uniquely identify this LLM."""
    return {"api_url": self.api_url, "max_tokens": self.max_tokens}


# Example usage
custom_llm = CustomLLM(
    api_url="https://api.mymodel.com/v1/generate",
    api_key="your-api-key",
    max_tokens=150,
)

prompt = "Tell me a story about a brave knight."
response = custom_llm(prompt)
print("Response:", response)
