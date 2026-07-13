import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key :
    raise ValueError("where is api key")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="suggest me a name for my new food start-up in one word "

message  = {
    "role":role,
    "content":prompt
}

message_system = {

    "role":"system",
    "content":"you are a name suggestion specialist"
}

messages=[message_system,message]
response=client.chat.completions.create(model=model, messages=messages,temperature=2)
# print(response)

print("***************************************************************************")

print(response.choices[0].message.content)
