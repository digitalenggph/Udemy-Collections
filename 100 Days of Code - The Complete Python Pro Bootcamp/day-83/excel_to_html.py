import pandas as pd


xlsx = pd.ExcelFile("Credentials.xlsx")
sheets = xlsx.sheet_names
print(sheets)

dict_df = {sheet:pd.read_excel(io="Credentials.xlsx", sheet_name=sheet) for sheet in sheets}

dict_credentials, dict_project, dict_experience, dict_certifications = \
    dict_df['Credentials'].to_dict(orient='records'),\
    dict_df['Project'].to_dict(orient='records'),\
    dict_df['Experience'].to_dict(orient='records'),\
    dict_df['Online_Certifications'].to_dict(orient='records')
