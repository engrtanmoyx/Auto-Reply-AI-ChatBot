from openai import OpenAI
import time

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="Your-OpenAI-Key")

command="""
chat_history
"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Tanmoy who speaks english as well as hindi as well as bengali. He is from India and is a coder. You analyse chat history and pretend to be Tanmoy"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)