import faiss
import numpy as np

def create_faiss_index(embeddings):
    embeddings = np.array(embeddings)
    if len(embeddings.shape) == 1:
        embeddings = embeddings.reshape(1, -1)
    dimension = embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings,dtype="float32"))
    return index