import pandas as pd

def excel_to_html(excel_file):
    """returns dictionary of credentials, project, experience, certifications, and socials in particular order"""
    xlsx = pd.ExcelFile(excel_file)
    sheets = xlsx.sheet_names

    dict_df = {sheet:pd.read_excel(io=excel_file, sheet_name=sheet) for sheet in sheets}

    dict_credentials, dict_project, dict_experience, dict_certifications, dict_socials = \
        dict_df['Credentials'].to_dict(orient='records'),\
        dict_df['Project'].to_dict(orient='records'),\
        dict_df['Experience'].to_dict(orient='records'),\
        dict_df['Certifications'].to_dict(orient='records'),\
        dict_df['Socials'].to_dict(orient='records')

    for project in dict_project:
        project['Tools'] = [tool.strip() for tool in str(project['Tools']).split(',')]

    return dict_credentials, dict_project, dict_experience, dict_certifications, dict_socials
