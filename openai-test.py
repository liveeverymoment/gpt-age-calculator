from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    temperature=0.1,
    messages=[
        {"role":"system","content":"you are a poetic assistant."},
        {"role":"user","content":"Compose a poem that explains the concept of recursion in programming."}
    ]
)
print(completion.choices[0].message)