from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from typing import Annotated, Literal, Optional, TypedDict
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

class Review(TypedDict):
    summary: Annotated[str, "A short summary of the review"]
    sentiment: Annotated[Literal["pos", "neg", "neutral"], "Overall sentiment"]
    pros: Annotated[Optional[list[str]], "List of pros"]
    cons: Annotated[Optional[list[str]], "List of cons"]

review = "The phone is fast and the camera is great, but the battery drains quickly."
print(model.with_structured_output(Review).invoke(review))
