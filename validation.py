keywords=["DROP","DELETE","UPDATE","INSERT","ALTER","TRUNCATE"]

def valid(text):
    text_upper=text.upper()
    for word in keywords:
        if word in text_upper:
            return{"valid":False,"message":f"Dangerous query detected: {word}"}
    
    return{"valid":True,"message":f"Valid SQL query"}
def valid_sql(sql):
    sql_upper=sql.upper()
    for word in keywords:
        if word in sql_upper:
            return{"valid":False,"message":f"Dangerous query detected: {word}"}
    
    return{"valid":True,"message":f"Valid SQL query"}

def get_schema(schema):
    columns=set()

    for table,info in schema.items():
        columns.add(table.lower())
        for column in info["columns"]:
            columns.add(column.lower())

    return column

def is_query_valid(query,schema):
    schemas=get_schema(schema)

    words=query.lower().split()
    matched=False
    for word in words:
        if word in schemas:
            matched=True
            break
    if not matched:
        return{
            "valid":False,
            "message":"No matching table or column found"
        }
    
    return{
        "valid":True,
        "message":"Query is valid"
    }