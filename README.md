# Battleship Game Project
# Introduction
This is a Python implementation of the classic game Battleship, where two players place ships on a 10x10 grid and take turns attacking each other's ships. The first player to sink all of their opponent's ships wins the game.

The game uses object-oriented programming concepts and is broken down into several modules, including GameObject, Player, Game, Ship, and Tile.

# How to Run
To start the game:

1. Ensure you have Python installed.
2. Clone or download this repository.
3. Navigate to the project directory and run the following command: python main.py

# Game Flow
- The game starts by prompting players to enter the number of ships (between 1 and 5) to use.
- Players will take turns hiding their ships on a 10x10 board.
- After ships are hidden, players take turns attacking each other's boards by selecting coordinates.
- The game continues until all of one player's ships have been sunk.

# Key Classes and Methods

# GameObject
This is the base class that contains common utilities and methods like:

- valid_coord(): Validates user input coordinates.
- print_board(): Prints the board with row and column labels.
- br(): Prints breaklines for formatting purposes.
# Player
Manages individual player actions and information, including:

- set_ship_list(): Initializes each player's ships.
- hide_ships(): Allows players to hide their ships on the board.
- attack_ship(): Handles attacks and determines hits or misses.
# Game
Handles the overall game flow, including:

- start(): Begins the game by setting up the boards and starting turns.
- __switch_turns(): Switches between players after each turn.
- end_game(): Ends the game and announces the winner.
# Ship
Represents individual ships with attributes like:

- hp: Represents the health points of the ship.
- is_sunk(): Checks if a ship has been sunk.
# Tile
Represents a single tile on the board. Each tile knows its position and can change its symbol based on game events.

# Features
- Random phrases for hits, misses, sinks, and wins to add variety to the game.
- User-friendly input validation for coordinates.
- Dynamic gameboard display with symbols representing ships, hits, and misses.

# Future Improvements
- Add multiplayer over the network.
- Implement a graphical user interface (GUI).
- Add more game modes and custom ship sizes.