from flask import Flask, render_template, send_from_directory
from excel_to_html import excel_to_html

dict_credentials, dict_project, dict_experience, dict_certifications, dict_socials = excel_to_html("Credentials.xlsx")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           credentials=dict_credentials,
                           projects=dict_project,
                           experiences=dict_experience,
                           certifications=dict_certifications,
                           socials=dict_socials)

@app.route('/resume')
def resume():
    return send_from_directory('static', path="assets/resume/LOVEDORIAL_PORTFOLIO.pdf")


@app.route('/projects')
def projects():
    return render_template('projects.html',)

if __name__ == '__main__':
    app.run(debug=True, port=7777)



