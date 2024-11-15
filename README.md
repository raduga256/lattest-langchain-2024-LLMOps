# lattest-langchain-2024-LLMOps
LangChain and LLMops 2024 Latest Implementations

# lattest-langchain-2024-LLMOps
LangChain and LLMops 2024 Latest Implementations

# LANCHAIN LATEST _ Basic --> Advanced

## How to run?
Create a new virtual env with conda
1. conda create -n llmapp-d python=3 -y

2. conda activate -n llmapp

3. pip install requirements.txt

4. Loading the environment variables from .env file

## Creating the RAG using Langchain Expression Language - LECL
You will need these two high level packages always whenever you need to perform Basic RAG Implementation with LCEL
- from langchain_core.output_parsers import StrOutputParser
- from langchain_core.runnables import RunnablePassthrough


## LangChain: Langchain Expression Language (LCEL) Advance

## RunnableLamda
* To use a custom function inside a LCEL chain we need to wrap it up with a RunnableLamda
* Let's define a very simple function to create Russian lastnames

## LangChain: Memory - Can LLM Apps Remember?


## Conversation Buffer Window Memory
Similar to the previous one, but you can limit the number of conversational exchanges stored in memory. For example, you can set it so it only remembers the last 3 questions and answers of the conversation