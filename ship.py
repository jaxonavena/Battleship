# Ship class defines attributes and methods related to the ships used in the game
class Ship:
  
  # Constructor to initialize the Ship object with its name, size, and symbol
  def __init__(self, name, size, symbol):
    self.name = name  # Ship's name (e.g., "Destroyer")
    self.size = size  # Ship's size (e.g., "1x3")
    self.symbol = symbol  # Symbol representing the ship on the board (e.g., "#")
    self.coords = []  # List to store the ship's coordinates on the board
    self.tiles = []  # List to store the specific tiles occupied by the ship
    self.hidden = False  # Boolean to track if the ship is hidden
    self.hp = int(self.size[-1])  # Health points for the ship, based on its size (e.g., 3 for a "1x3" ship)

  # Method to check if the ship is sunk (when its hp is 0)
  def is_sunk(self):
    return self.hp == 0  # Return True if the ship's health points are 0, meaning it has been sunk

  # Method to mark the ship as sunk by changing its symbol on all occupied tiles
  def sink(self):
    # Loop through each tile in the ship's tiles list
    for tile in self.tiles:
      tile.symbol = "S"  # Set the symbol for each tile to "S" to indicate the ship is sunk

  # Method to return the ship's symbol when the object is used in a string context
  def __str__(self):
    return self.symbol  # Return the ship's symbol (used in print statements, etc.)

  # Method to return the ship's symbol when the object is represented in Python (e.g., in the console)
  def __repr__(self):
    return self.symbol  # Return the ship's symbol (used for debugging and interactive console display)