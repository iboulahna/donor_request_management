### **2. Query Handling with GPT-4**

import openai

openai.api_key = "your_openai_api_key"

def generate_response(query):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()