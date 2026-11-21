from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

report = PromptTemplate.from_template("Write a detailed report on {topic}")
summary = PromptTemplate.from_template("Summarize the following text in 5 points:\n{text}")
chain = report | model | parser | summary | model | parser
print(chain.invoke({"topic": "unemployment in India"}))
