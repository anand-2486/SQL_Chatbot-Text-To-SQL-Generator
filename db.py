from sqlalchemy import create_engine
engine=create_engine("sqlite:///data.db")

def save_in_db(df,table_name):
    df.to_sql(table_name,engine,if_exists="replace",index=False)