from sentence_transformers import SentenceTransformer
import numpy as np

from rag.vectorstore import index, chunks

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve(query, k=3):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n"

    return context