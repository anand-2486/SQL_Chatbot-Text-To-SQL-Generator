from ollama import chat

def ollama_sql_generator(schema,relation,query):
    prompt=f"""
    You are an expert SQL query generator.

    Database Schema:
    {schema}

    Relationships:
    {relation}

    Question:
    {query}

    Rules:
    - Do NOT use markdown
    - Generate only SELECT queries
    - Return only raw SQL query
    - Do NOT use ```sql
    - Do NOT explain anything
    - Format SQL professionally
    - Keep SELECT columns on same line
    - Put FROM, JOIN, WHERE clauses on new lines
    - Provide understandable format for any user
    - Select ONLY columns explicitly requested by user
    - Do NOT add extra columns
    - Do NOT assume additional information
    - Avoid unnecessary JOINs
    - Use the minimum number of tables required
    - If all requested columns exist in one table, do NOT use JOIN
    """

    response=chat(
        model="llama3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"]