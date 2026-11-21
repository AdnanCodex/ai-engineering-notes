from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

import numpy as np
from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings(model="text-embedding-3-small")
documents = [
    "Virat Kohli is an Indian cricketer known for his batting.",
    "MS Dhoni is a former Indian captain known for finishing games.",
    "Jasprit Bumrah is a fast bowler famous for his yorkers.",
]
query = "Tell me about the bowler"

doc_vectors = np.array(embedding.embed_documents(documents))
query_vector = np.array(embedding.embed_query(query))

scores = doc_vectors @ query_vector / (np.linalg.norm(doc_vectors, axis=1) * np.linalg.norm(query_vector))
best = int(scores.argmax())
print("Query:", query)
print("Best match:", documents[best], "| score:", round(float(scores[best]), 3))
