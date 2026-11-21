from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {"type": "string", "description": "A short summary"},
        "sentiment": {"type": "string", "enum": ["pos", "neg", "neutral"]},
    },
    "required": ["summary", "sentiment"],
}

review = "The phone is fast and the camera is great, but the battery drains quickly."
print(model.with_structured_output(json_schema).invoke(review))
