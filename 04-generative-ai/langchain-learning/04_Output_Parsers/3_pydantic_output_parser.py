from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City the person lives in")

parser = PydanticOutputParser(pydantic_object=Person)
prompt = PromptTemplate(
    template="Generate a fictional {nationality} person.\n{format_instructions}",
    input_variables=["nationality"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
print((prompt | model | parser).invoke({"nationality": "Indian"}))
