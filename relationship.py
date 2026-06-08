def relationship(table,schema):
    relation=[]
    for table1,df1 in table.items():
        for table2,df2 in table.items():
            if table1==table2:
                continue
            primary_key=schema[table2]["primary_key"]

            if primary_key is None:
                continue

            for column in df1.columns:
                if(df1[column].dtype != df2[primary_key].dtype):
                    continue

                foreign_key_value=set(df1[column].dropna())
                primary_key_value=set(df2[primary_key].dropna())

                if(len(foreign_key_value)>0 and foreign_key_value.issubset(primary_key_value)):
                    relation.append({
                        "from_table":table1,
                        "from_column":column,
                        "to_table":table2,
                        "to_column":primary_key
                    })
    
    return relation