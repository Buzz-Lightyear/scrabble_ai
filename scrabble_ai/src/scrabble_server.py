#!/usr/bin/env python

from flask import Flask, jsonify,request
from scrabble_ai.src.scrabble_board import ScrabbleBoard

app = Flask(__name__)

with open('static/dict.txt', 'r') as f:
    DICTIONARY = set([item[:-2] for item in f.readlines()])

@app.route("/move", methods=['POST'])
def make_move_post():
    return make_move()

@app.route("/", methods=['POST'])
def make_move():
    input = request.json
    if not input:
        raise Exception('POST request needs a body')

    scrabble_board = ScrabbleBoard(dictionary=DICTIONARY)

    return  jsonify({
                "action": "move",
                "move": {
                    "word": "cape",
                    "x": 7,
                    "y": 7,
                    "orientation": "vertical",
                },
         })

if __name__=='__main__':
    app.run(debug=True)