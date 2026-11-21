from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
vector = embedding.embed_query("Delhi is the capital of India")
print(len(vector), vector[:5])
