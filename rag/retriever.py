import numpy as np

def retrieve(query_embedding,index,schema,k=2):
    distance,indice=index.search(np.array([query_embedding],dtype="float32"),k)

    result=[]
    for idx in indice[0]:
        result.append(schema[idx])

    return result