from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from typing import Literal, Optional
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

class Review(BaseModel):
    summary: str = Field(description="A short summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Overall sentiment")
    pros: Optional[list[str]] = Field(default=None, description="List of pros")
    cons: Optional[list[str]] = Field(default=None, description="List of cons")

review = "The phone is fast and the camera is great, but the battery drains quickly."
result = model.with_structured_output(Review).invoke(review)
print(result.sentiment)
print(result.model_dump())
