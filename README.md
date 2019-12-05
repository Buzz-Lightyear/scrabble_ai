#Arthur
##A Scrabble AI server written in Python
- Refer [Game Server Repo](http://goga.bsprague.com/bsprague/scrabble) for documentation for game flow.

## AI API Requirements
- Single POST `/move` endpoint that consumes board state, tiles available and tiles remaining and returns a response with the move made.
- Move can be one of three things:
    - Place word starting at (x, y) horizontally or vertically.
    - Exchange a subset of tiles for new ones subject to tile availability.
    - Pass

## Strategy
- Have a first move strategy to produce word with max score. If not:
- Sort the incoming tiles by score.
- Populate board from request.
- Figure out strategy to pick _the_ letter to use
- If said letter is vowel, pick two consonants from pile and make word
- If consonant, pick one vowel and one consonant and make word. 
- Bonus: Iterate over all possbilities and get one with max score.
- If none works, exchange low scoring 3 tiles.
