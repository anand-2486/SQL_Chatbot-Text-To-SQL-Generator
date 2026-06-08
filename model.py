import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def sql_generator(schema,relation,question):
    prompt=f"""
    You are an expert SQL query generator.

    Database Schema:
    {schema}

    Relationships:
    {relation}

    Question:
    {question}

    Generate ONLY SQL query.
    Do not explain anything.
    """

    response=llm.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content


