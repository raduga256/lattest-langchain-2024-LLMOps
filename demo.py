# Run all the notebooks experiments here as a script.
# run: python demo.py in the terminal

# Let reimplement the notebook - 01 experiment here

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
# Loading openai key
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import OpenAI
llModel = OpenAI()

# Streaming multiple lines of the response
for chunk in llModel.stream(
    "Tell me one fun fact about the Kennedy family. I need a detailed response"
):
    
    
    print(chunk, end="", flush=True)
    
