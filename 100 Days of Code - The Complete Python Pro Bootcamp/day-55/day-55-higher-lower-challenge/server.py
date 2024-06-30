from flask import Flask
from random import randint
from art import logo

app = Flask(__name__)

answer = randint(0, 9)
guess_the_number = "https://media1.tenor.com/m/dHyGpx4Q3NoAAAAC/guess-dog.gif"
too_high_gif = ('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3htOXFpZmQ5NmVnd2w4MGM1ZmR0enFuNGlvYmt2aGFmaXFseDA'
                'wcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDpF5MYgQdq6lcRSq2/giphy.webp')
too_low_gif = ('https://media0.giphy.com/media/v1'
               '.Y2lkPTc5MGI3NjExdWdzejRsdGcyM3dqc3gydWdseGFvazhpb2xxMWo2czBzcTNxcmQ1NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaW'
               'QmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.webp')
correct_gif = ('https://media0.giphy.com/media/v1'
               '.Y2lkPTc5MGI3NjExbDV5eHUxbWQ0YWZieHllOXY3Y2F5c3lleDU2cW5vNzRpb21waXg1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaW'
               'QmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.webp')


def print_image(function):
    def wrapper():
        start = ("<img src=" + function() + " width=40% >"
                                            "<h1> Guess the Number between 0-9! </h1>")
        return start

    return wrapper


@print_image
def logo():
    return guess_the_number


@app.route('/')
def start_game():
    return logo()


@app.route('/<int:guess>')
def game(guess):
    if guess > answer:
        too_high = ("<h1> Too high! Guess again :D  </h1>"
                    "<img src=" + too_high_gif + " width=40% >")
        return too_high
    elif guess < answer:
        too_low = (f"<h1> Too low. Guess again :D  </h1>"
                   "<img src=" + too_low_gif + " width=40% >")
        return too_low
    else:
        correct = (f"<h1> You got it! The answer was {answer} </h1>"
                   "<img src=" + correct_gif + " width=40% >")
        return correct


if __name__ == '__main__':
    app.run(debug=True)
