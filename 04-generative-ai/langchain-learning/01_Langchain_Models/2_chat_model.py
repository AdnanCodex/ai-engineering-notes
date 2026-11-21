from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_openai import ChatOpenAI

# Chat model = takes messages, returns an AIMessage
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, max_completion_tokens=200)
result = model.invoke("Write a 5-line poem on cricket")
print(result.content)
