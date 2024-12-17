import google.generativeai as genai

genai.configure(api_key="exampleapikey")
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=(
        "You are a helpful assistant that provides concise answers."
    ),
)
response = model.generate_content("Explain how AI works")
print(response.text)