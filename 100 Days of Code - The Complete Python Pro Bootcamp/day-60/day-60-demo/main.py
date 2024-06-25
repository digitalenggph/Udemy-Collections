from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def valid_login(username, password):
    if len(username) > 0 or len(password) > 0:
        return True
    else:
        return False


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            username = request.form['username']
            password = request.form['password']
            return render_template('login.html', username=username, password=password)
        else:
            error = 'Invalid username/password'
    return render_template('error.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)


"""
REFERENCES:
https://stackoverflow.com/questions/26397683/flask-login-system

"""
