"""
Program Name: Tile Class

Description: This file defines the Tile class which represent Tile in the game. 
Each tile has a row, a column, and a symbol. The class includes methods to check if the tile contains a sunk ship, and provides a way 
to display the tile's symbol in both string and console contexts.

Inputs:
    - Row and column positions.
    
Output:
    - The tile's symbol.
    - Return true or false Tile is sunk.


Author:
    Jaxon Avena

Creation Date:
    September 10, 2024
"""

# Tile class represents an individual tile on the game board
class Tile:
  
  # Constructor to initialize the Tile object with its row, column, and symbol
  def __init__(self, row, col):
    self.row = row  # Row position of the tile on the board
    self.col = col  # Column position of the tile on the board
    self.symbol = " "  # Default symbol for an empty tile (a blank space)

  # Method to check if the tile contains a sunk ship
  def is_sunk(self):
    return False  # Return False because a tile itself cannot be sunk (this is overridden for Ship tiles)

  # Method to return the tile's symbol when the object is used in a string context
  def str(self):
    return self.symbol  # Return the tile's symbol (used in print statements, etc.)

  # Method to return the tile's symbol when the object is represented in Python (e.g., in the console)
  def __repr__(self):
    return self.symbol  # Return the tile's symbol (used for debugging and interactive console display)
  