from flask import Flask, render_template
from excel_to_html import dict_credentials, dict_project, dict_experience, dict_certifications

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           credentials=dict_credentials,
                           projects=dict_project,
                           experiences=dict_experience,
                           certifications=dict_certifications)


if __name__ == '__main__':
    app.run(debug=True, port=7777)



