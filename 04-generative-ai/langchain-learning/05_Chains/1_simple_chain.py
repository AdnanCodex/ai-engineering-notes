from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt = PromptTemplate.from_template("Give me 5 interesting facts about {topic}")
chain = prompt | model | parser
print(chain.invoke({"topic": "cricket"}))
