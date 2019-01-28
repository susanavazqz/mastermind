[![Build Status](https://travis-ci.org/susanavazqz/mastermind.svg?branch=master)](https://travis-ci.org/susanavazqz/mastermind)

## Mastermind

Rest API that simulates the role of the [Masterminds](https://en.wikipedia.org/wiki/Mastermind_(board_game)) codemaker.  

At the moment only the basic version is available with following features:
* 2 players (codemaker, codebreaker)
* Pattern / Code has four colors
* Colors availables: 
    * 'black': 'B',
    * 'white': 'W',
    * 'red': 'R',
    * 'yellow': 'Y',
    * 'purple': 'P'
* Unlimited chances

### Requirements

* Python >= 3.5
* Flask==1.0.2
* Flask-RESTful==0.3.7
* Flask-SQLAlchemy==2.3.2


### Run

```bash
$ git clone https://github.com/susanavazqz/mastermind
$ cd mastermind
$ pip install -r requirements.txt
```


### Usage

You can use curl from command line or postman to play mastermind

##### Start to play
 
 1.- Create a new game with POST request. Returns a JSON object with game id.
 
 ```bash
 $ curl --request POST http://127.0.0.1:5000/game
 
 ```
 Response (JSON):
 ```json
 {
  "id": "1",
  "message": "Game has been created"
 }
 ```
 
 2.- Guess the pattern. Send a PUT request adding the guess pattern as a json. 
 
 ```bash
 $ curl -X PUT http://127.0.0.1:5000/game/1 \
  -H 'Content-Type: application/json' \
  -d '{ "code": "P,R,W,B"}'
 ```
 
 Response (JSON):
 ```json
 {
  "id": "1",
  "code": "P,R,W,B",
  "result": { 
      "black_pegs": 1,
      "white_pegs": 2
    },
   "status": "Keep Trying!"
 }
 ```
 
## TODO

* Custom length of pattern / code
* Custom colors
* Get history of the game


### Contributors

* Susana Vázquez




