import os
from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)