#!/usr/bin/env python

from flask import Flask, jsonify,request
from scrabble_ai.src.scrabble_board import ScrabbleBoard

app = Flask(__name__)

def initialize_server():
    with open('static/dict.txt', 'r') as f:
        DICTIONARY = set([item[:-2] for item in f.readlines()])
    return ScrabbleBoard(dictionary=DICTIONARY)

board = initialize_server()

@app.route("/move", methods=['POST'])
def make_move_post():
    return make_move()

@app.route("/", methods=['POST'])
def make_move():
    input = request.json
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