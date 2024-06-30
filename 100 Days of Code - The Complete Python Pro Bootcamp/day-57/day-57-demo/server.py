from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

GENDERIZE_URL = 'https://api.genderize.io/'
AGIFY_URL = 'https://api.agify.io/'


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = dt.datetime.now().year
    return render_template('./index.html',
                           num=random_number,
                           year=year)


# TODO 1. Set up a route to /guess/some_name.
@app.route('/guess/<name>')
# TODO 2. Parse the URL to extract the name at the end of the URL.
def guess_my_info(name):
    params = {
        'name': name
    }

    # TODO 4. Make API call to genderize.io to obtain the gender.
    gender_request = requests.get(url=GENDERIZE_URL, params=params)
    gender_request.raise_for_status()
    gender = gender_request.json()['gender']

    # TODO 5. Make API call to agify.io to obtain the age.
    age_request = requests.get(url=AGIFY_URL, params=params)
    age_request.raise_for_status()
    age = age_request.json()['age']

    # TODO 3. Create a template and dynamically insert the name from the URL in title case.
    return render_template('./guess.html',

                           # TODO 6. Insert the result from the API call into the template.
                           name=name.title(),
                           age=age,
                           gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/f14658c6e58c834c01e0'
    blog_data = requests.get(url=blog_url)
    blog_data.raise_for_status()
    posts = blog_data.json()
    return render_template('blog.html',
                           posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
