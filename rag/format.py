def create_schema_chunks(schema_list):
    chunks=[]
    for table,info in schema_list.items():
        text=f"Table {table}:\n"
        for column in info["columns"]:
            text+=f"{column}\n"
        chunks.append(text)
    return chunks