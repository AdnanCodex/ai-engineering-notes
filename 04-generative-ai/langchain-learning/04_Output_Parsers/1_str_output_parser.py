from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
prompt = PromptTemplate.from_template("Write a 2-line summary about {topic}")
chain = prompt | model | StrOutputParser()
print(chain.invoke({"topic": "black holes"}))
