import streamlit as st
import pandas as pd
from pre_processing import pre_processing
from schema import schema
from schema import schema_to_text
from db import save_in_db
from relationship import relationship
from diagram import er_diagram
from model import sql_generator

st.title("SQL Chatbot(Text to SQL Converter)")

files=st.file_uploader("Upload your CSV/EXCEL file",type=["csv","xlsx","xls"],accept_multiple_files=True)

tables={}
schema_list={}

if files:
    for file in files:
        table_name=file.name.split(".")[0]

        if file.name.endswith(".csv"):
            df=pd.read_csv(file)
        else :
            df=pd.read_excel(file)

        tables[table_name]=df
        schema_list[table_name]=schema(table_name,df)

    st.sidebar.title("Tables")
    selected_table=st.sidebar.selectbox("Select a table to view",list(tables.keys()))

    st.subheader(f"Preview of {selected_table}")
    st.dataframe(tables[selected_table].head(10))

schema_text=schema_to_text(schema_list)
relation=relationship(tables,schema_list)
if files:
    if relation:
        st.subheader(f"ER Diagram")
        figure=er_diagram(tables,relation)  
        st.pyplot(figure)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if files:
    query=st.chat_input("Provide the query to generate SQL code")
    if query:
        sql_code=sql_generator(schema_text,relation,query)
        st.session_state.chat_history.append({"question": query,"sql": sql_code})

for chat in st.session_state.chat_history:
    st.write(f"Question: {chat['question']}")
    st.code(chat["sql"],language="sql")