from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_openai import OpenAI

# LLM = plain text-in / text-out completion model
llm = OpenAI(model="gpt-3.5-turbo-instruct")
print(llm.invoke("What is the capital of India?"))
