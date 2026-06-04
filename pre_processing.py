def pre_processing(df):
    df.columns=[column_name.lower().strip().replace(" ","_") for column_name in df.columns]
    df.drop_duplicates(inplace=True)
    df.fillna("Unknown",inplace=True)
    return df