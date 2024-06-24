from flask import Flask, render_template

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('index.html')


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
