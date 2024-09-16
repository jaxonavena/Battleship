"""
Program Name: Game Initialization

Description:
    This file initializes a Battleship game by creating two Player objects (Player 1 and Player 2),
    setting their opponent relationships, and then starting the game using the Game class. The game
    logic is handled by the Game and Player classes.

Output:
    - The game starts, displaying the boards and managing the turn-based gameplay for Player 1 and Player 2.

Author:
    Jaxon Avena

Creation Date:
    September 10, 2024
"""

from player import Player  # Import the Player class from the player module
from game import Game  # Import the Game class from the game module

# Initialize Player 1 with ID 1 and set them as the active player
p1 = Player(1, True)

# Initialize Player 2 with ID 2 and set them as inactive
p2 = Player(2, False)

# Set Player 2 as Player 1's opponent
p1.set_opponent(p2)

# Set Player 1 as Player 2's opponent
p2.set_opponent(p1)

# Create a list of the two players, which will be passed to the Game class
player_bank = [p1, p2]

# Initialize the Game object with the list of players (player_bank)
game = Game(player_bank)

# Start the game by calling the start method on the Game object
game.start()
