# 𓁹 user_memory.py - Vector-based user conversation memory

from chromadb import Client
from chromadb.config import Settings

CHROMA_DIR = "./db/chroma"

client = Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_DIR))
collection = client.get_or_create_collection("user_memory")

def store_message(user_id: str, message: str):
    collection.add(
        documents=[message],
        metadatas=[{"user_id": user_id}],
        ids=[f"{user_id}_{collection.count()}"]
    )

def retrieve_memory(user_id: str, top_k: int = 3):
    results = collection.query(
        query_texts=[""],
        n_results=top_k,
        where={"user_id": user_id}
    )
    return results["documents"]
