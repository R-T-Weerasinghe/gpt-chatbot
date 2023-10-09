import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("API_KEY")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "User", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower in ["exit", "quit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)