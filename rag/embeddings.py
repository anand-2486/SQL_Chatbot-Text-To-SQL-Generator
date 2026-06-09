from sentence_transformers import SentenceTransformer

embedding_model=SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(text):
    embedding=embedding_model.encode(text)
    return embedding