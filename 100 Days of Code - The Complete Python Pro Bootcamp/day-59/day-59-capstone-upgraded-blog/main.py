from flask import Flask, render_template
import requests
import datetime as dt

app = Flask('__name__')


@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/dc4a4060e9c28046426a')
    response.raise_for_status()
    blog = response.json()

    for post in blog:
        print(post['title'])

    today = dt.datetime.now()
    date = today.strftime("%B %d, %Y")
    return render_template('index.html', blog=blog, date=date)


@app.route('/<nav_page>')
def get_nav(nav_page):
    if nav_page.lower() == 'about':
        template = 'about.html'
    elif nav_page.lower() == 'contact':
        template = 'contact.html'
    else:
        template = 'index.html'
    return render_template(template, nav_page=nav_page)


if __name__ == '__main__':
    app.run(debug=True)
