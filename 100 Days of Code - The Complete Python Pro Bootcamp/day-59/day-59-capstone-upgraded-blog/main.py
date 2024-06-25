from flask import Flask, render_template
import requests
import datetime as dt

app = Flask('__name__')


@app.route('/')
def home():
    # get post from API
    response = requests.get(url='https://api.npoint.io/dc4a4060e9c28046426a')
    response.raise_for_status()
    blog = response.json()

    # get today's date
    today = dt.datetime.now()
    date = today.strftime("%B %d, %Y")
    year = dt.datetime.now().year
    return render_template('index.html', blog=blog, date=date, year=year)


@app.route('/<nav_page>')
def get_nav(nav_page):
    year = dt.datetime.now().strftime('%Y')

    if nav_page.lower() == 'about':
        template = 'about.html'
    elif nav_page.lower() == 'contact':
        template = 'contact.html'
    else:
        return home()
    return render_template(template, nav_page=nav_page, year=year)


@app.route('/post/<post_id>')
def get_post(post_id):
    # get post from API
    response = requests.get(url='https://api.npoint.io/dc4a4060e9c28046426a')
    response.raise_for_status()
    blog = response.json()

    post_data = ""

    for post in blog:
        if post_id == 'index.html':
            return home()
        if post['id'] == int(post_id):
            post_data = post

    # get today's date
    today = dt.datetime.now()
    date = today.strftime("%B %d, %Y")

    return render_template('post.html', post_data=post_data, date=date)


if __name__ == '__main__':
    app.run(debug=True)
