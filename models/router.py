from models.groq_model import groq_sql_generator
from models.ollama_model import ollama_sql_generator

def sql_generator(provider,schema,relation,query):
    if provider=="groq":
        return groq_sql_generator(schema,relation,query)
    elif provider=="ollama":
        return ollama_sql_generator(schema,relation,query)
    else:
        raise ValueError("Invalid Provider")