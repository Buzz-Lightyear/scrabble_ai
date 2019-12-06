#!/usr/bin/env python

from flask import Flask, jsonify,request
from scrabble_ai.src.scrabble_board import ScrabbleBoard

app = Flask(__name__)

@app.route("/move", methods=['POST'])
def make_move_post():
    return make_move()

@app.route("/", methods=['POST'])
def make_move():
    input = request.json
    if not input:
        raise Exception('POST request needs a body')

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