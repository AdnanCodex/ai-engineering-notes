from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
template = PromptTemplate.from_template("Summarize {topic} in {style} style, in 3 lines.")
prompt = template.invoke({"topic": "Transformers", "style": "beginner-friendly"})
print(prompt.text)
print(model.invoke(prompt).content)
