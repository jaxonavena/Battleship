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
