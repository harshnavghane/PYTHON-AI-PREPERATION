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

from pydantic import BaseModel
class ticket(BaseModel) :
    name : str
    email : str
    issue:str

schema = ticket.model_json_schema()

response_format= {
   "type": "json_object"
}



system_prompt= f"""
extract the information strictly based in this schema and give output in json format{schema}
"""

message_system = {
    "role" : "system",
    "content":system_prompt
}


text = "hello my name is harsh i have purchased the iphone from your store and stopped working please help me , this is my phone number 767576576 and this my email harshnavhane75@gmail.com"
prompt=f"""
this is customer ticket plese extract personal information from this{text}
"""

message  = {
    "role":role,
    "content":prompt
}

messages=[message_system,message]
response=client.chat.completions.create(model=model, messages=messages ,  response_format=response_format)

answer = response.choices[0].message.content
print(answer)


import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = ticket(**data_file)
print(ticket.name)
print(ticket.issue)
print(ticket.email)