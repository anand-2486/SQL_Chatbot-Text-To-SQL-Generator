import pandas as pd

def primary_key(df):
    for column in df.columns:
        if df[column].is_unique and df[column].notnull().all():
            return column
        
    return None

def schema(table,df):
    schema_table={
        "table_name":table,
        "columns":{},
        "rows":len(df),
        "primary_key":primary_key(df)
    }

    for column in df.columns:
        schema_table["columns"][column]={
            "dtype":str(df[column].dtype),
            "unique_count":int(df[column].nunique()),
            "null_count":int(df[column].isnull().sum())
        }

    return schema_table

def schema_to_text(schemas):
    text=""
    for table,schema in schemas.items():
        text+=f"\nTable : {table}\n"

        for column in schema["columns"]:
            dtype = schema["columns"][column]["dtype"]
            text+=f"-{column}  ({dtype})\n"

        if schema["primary_key"]:
            text+=(f"Primary Key: "f"{schema['primary_key']}\n")

    return text