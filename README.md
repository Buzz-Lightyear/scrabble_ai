#Arthur

##A Scrabble AI server written in Python
- Refer [Game Server Repo](http://goga.bsprague.com/bsprague/scrabble) for documentation for game flow.

## AI API Requirements
```
/* Package jsonhttp provides a scrabble.Actor implementation that calls out to
a remote AI over HTTP/JSON. The API is formatted as:

 POST /move
 {
   "board": [
		 {"letter": "c", "x": 7, "y": 7},
		 {"letter": "a", "x": 8, "y": 7},
		 {"letter": "t", "x": 9, "y": 7},
		 {"letter": "i", "x": 9, "y": 8},
		 {"letter": "n", "x": 9, "y": 9},
		 {"letter": "y", "x": 9, "y": 10},
	 ],
	 "tiles": ["a", "d", "e", "e", "p", "r", "q"],
	 "pot": 70,
 }

 Possible responses:
 {
		"action": "move",
		"move": {
			"word": "cape",
			"x": 7,
			"y": 7,
			"orientation": "vertical",
		},
 }

 ------------------------

 {
	 "action": "exchange",
	 "tiles": ["e", "q"],
 }

 ------------------------

 {
	 "action": "pass",
 }
*/
```

## Strategy
- Have a first move strategy to produce word with max score. If not:
- Sort the incoming tiles by score.
- Populate board from request.
- Figure out strategy to pick _the_ letter to use
- If said letter is vowel, pick two consonants from pile and make word
- If consonant, pick one vowel and one consonant and make word. 
- Bonus: Iterate over all possbilities and get one with max score.
- If none works, exchange low scoring 3 tiles.
