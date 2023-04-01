from flask import Flask
import random

app = Flask(__name__)

# Set min and max value for the random number
MIN: int = 0
MAX: int = 9

secret_number = random.randint(MIN, MAX)
print(secret_number)


@app.route('/')
def index():
    return f'<h1>Guess a number between {MIN} and {MAX}</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" />'


@app.route('/<int:num>')
def get_guess(num: int):
    if num < secret_number:
        return f'<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    elif num > secret_number:
        return f'<h1 style="color: magenta">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    else:
        return f'<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'


if __name__ == "__main__":
    # Activate debug mode
    app.run(debug=True)
