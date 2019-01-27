[![Build Status](https://travis-ci.org/susanavazqz/mastermind.svg?branch=0.1)](https://travis-ci.org/susanavazqz/mastermind)

## Mastermind
Rest API that simulates the role of the Masterminds codemaker


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
 $ curl -X PUT http://127.0.0.1:5000/game/1/play \
  -H 'Content-Type: application/json' \
  -d '{ "code": "A,B,C,D"}'
 ```
 
 Response (JSON):
 ```json
 {
  "id": "1",
  "code": "A,B,C,D",
  "result": { 
      "black_pegs": 1,
      "white_pegs": 2
    }
 }
 ```
    

### Contributors

* Susana Vázquez




