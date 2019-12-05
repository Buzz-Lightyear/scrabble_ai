#!/usr/bin/env python

from flask import Flask, render_template
from scrabble_ai.src.scrabble_board import ScrabbleBoard

app = Flask(__name__)

@app.route("/move", methods=['GET', 'POST'])
def make_move_post():
    return make_move()

@app.route("/", methods=['GET', 'POST'])
def make_move():
    sample_post_body = """
        Sample Post Body: {
            "board": [{"x": 0, "y": 5, "letter": "a"}],
            "tiles": ["a", "d", "d", "e", "x", "m", "n"],
            "pot": 92
        }
        """

    data = {'source': 'Hi there! I\'m Arthur the scrabble AI. If you send me a POST request, I\'ll make a valid scrabble move!',
            'sample_post_body': sample_post_body}

    ScrabbleBoard().print_board()

    return render_template(
        'scrabble.html',
        data=data,
        error=None)

if __name__=='__main__':
    app.run(debug=True)