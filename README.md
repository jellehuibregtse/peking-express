# Peking Express

## Problem description
This digital multi-player game is inspired by the [reality TV game Peking Express](https://en.wikipedia.org/wiki/Peking_Express), where participant couples engage in a hitchhiking race to the end destination Beijing (Peking).
 
You form a couple with another student and are together responsible for one character in the game. A map is given as a graph with locations and connections, where Peking is the destination location. Also given is a budget – same for each couple, and a start location - which is possibly different for each couple. In every turn, your character can move from the current location to a new one, along an available connection, or can choose to wait a round in the current location. Each move from a location to another has a cost (ticket price) associated with it. Some critical locations can only accommodate one player at a time, which means that the location, if occupied, is temporarily unavailable.

The challenge is to design and implement an algorithm that drives the moves of your character from the start location to Peking, in a minimal number of moves. Of course, the total amount spent on tickets for the whole route should fit in the budget.

## Getting started

### Prerequisites
- Python
- Pip

### Setup
First, clone the directory.

Then, install all Python requirements.
```
pip install -r requirements.txt 
```

Start the server.
```
uvicorn main:app --reload
```

## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) license.