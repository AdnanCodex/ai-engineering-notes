from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

from langchain_core.runnables import RunnableParallel

notes = PromptTemplate.from_template("Generate short notes from:\n{text}") | model | parser
quiz = PromptTemplate.from_template("Generate 3 quiz questions from:\n{text}") | model | parser
merge = PromptTemplate.from_template("Merge into one document.\nNOTES:\n{notes}\nQUIZ:\n{quiz}") | model | parser

chain = RunnableParallel({"notes": notes, "quiz": quiz}) | merge
print(chain.invoke({"text": "Support Vector Machines find the hyperplane that best separates classes."}))
