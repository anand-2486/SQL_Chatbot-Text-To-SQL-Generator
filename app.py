import streamlit as st
import pandas as pd
from pre_processing import pre_processing
from db import save_in_db

st.title("SQL Chatbot(Text to SQL Converter)")

files=st.file_uploader("Upload your CSV/EXCEL file",type=["csv","xlsx","xls"],accept_multiple_files=True)

tables={}

if files:
    for file in files:
        table_name=file.name.split(".")[0]

        if file.name.endswith(".csv"):
            df=pd.read_csv(file)
        else :
            df=pd.read_excel(file)

        tables[table_name]=df

    st.sidebar.title("Tables")
    selected_table=st.sidebar.selectbox("Select a table to view",list(tables.keys()))

    st.subheader(f"Preview of {selected_table}")
    st.dataframe(tables[selected_table].head(10))

    

        