import google.generativeai as genai

genai.configure(api_key="add_your_api_key_here")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)