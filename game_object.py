import random
from ship import Ship

class GameObject:
  def __init__(self):
    self.ship_size_to_name = {
      "1x1": "Cruiser",
      "1x2": "Submarine",
      "1x3": "Destroyer",
      "1x4": "Battleship",
      "1x5": "Aircraft Carrier"
    }
    self.ship_size_to_symbol = {
      "1x1": "&",
      "1x2": "%",
      "1x3": "#",
      "1x4": "$",
      "1x5": "@"
    }
    self.letter_to_col_index = {
      "A": 0,
      "B": 1,
      "C": 2,
      "D": 3,
      "E": 4,
      "F": 5,
      "G": 6,
      "H": 7,
      "I": 8,
      "J": 9
    }

    self.hit_syns = ["Hit!", "!!! H I T !!!", "BANNNNNNNNNNNGGGGGGGG!", "Bullseye!", "Noiiiiiiiceeee one mate"]
    self.miss_syns = ["Miss!", "You missed.", "L", "oof", "Go fish?", "BLOCKED BY JAMES!!!"]
    self.sink_syns = ["Nice Sink!"]
    self.win_syns = ["Sweet Victory!", "Winner! Winner! Chicken Dinner!", "congrats bro", "Might be the Greatest", "Proved Me Wrong"]

  def br(self, char="=", gap=0):
    # br like HTML <br>
    # Will print a breakline of = or any other char passed
    # Gap is the white space between each print of the char
    # If char is H or M then it will select a corresponding phrase in synonymizer_inator()
    char = (self.synonymizer_inator(char) if char in ["H", "M", "S", "W"] else char) + (" " * gap)
    print("\n" + (char * 50) + "\n")

  def synonymizer_inator(self, char):
    if char == "S":
      return random.choice(self.sink_syns)
    elif char == "M": 
      return random.choice(self.miss_syns) # Grab a hit/miss phrase
    elif char == "W":
      return random.choice(self.win_syns)
    else:
      return random.choice(self.hit_syns)

  def valid_coord_with_error_messages(self, coord): # Is this a valid coord? Takes LetterNumber combo coordinates (e.g. A8)
    try:
      col = coord[0].upper() # Assume it's a letter
      row = int(coord[1:]) # Assume it's a number, grab everything after the column letter
    except:
      print("Your coordinate must be a letter-number pair (e.g. A8)")
      return False

    if col not in ["A","B","C","D","E","F","G","H","I","J"]:
      print("Invalid Coordinate. Ensure your input starts with a valid column header (e.g. E4)")
      return False

    if row not in range(1,11):
      print("Invalid Coordinate. Ensure your input lies within the bounds of the 10x10 board.")
      return False

    return True

  def coords_are_inbounds(self, coords):
      flag = False
      for tile in coords:
        if tile.row > 9 or tile.row < 0 or tile.col > 9 or tile.col < 0:
          return False
        else:
          flag = True
      return flag

  def coord_translator(self, coord):
    # e.g. coord = A8
    col = self.letter_to_col_index[coord[0].upper()] # Letters are columns
    row = int(coord[1]) - 1 # Numbers are rows
    return row, col #return row number, column number to use as indeces

  def print_board(self, board):
    # Prints a given board with the rows and columns labeled
    # ---------------------------------------------------------- #
    print("   A B C D E F G H I J")
    row = 0
    for row_list in board:
      stringified_objs = []
      col = 0
      for obj in row_list:
        if isinstance(obj, Ship):
          for tile in obj.coords: # for literal Tile in the selected Ship.coords
            if tile.row == row and tile.col == col: # if the current coords match the Tile's coords
              obj = tile
        col += 1
        stringified_objs.append(obj.symbol)
      print(f"{row + 1}  " + " ".join(stringified_objs))
      row += 1

  def quit(self, input):
    if input in ["exit", "q", "quit", "EXIT", "Q", "QUIT"]:
      exit()

  def get_input(self, message):
    my_input = input(message)
    my_input = [my_input[0], my_input[1]]
    my_input[1] = int(my_input[1]) - 1
    my_input[1] = str(my_input[1])
    my_input = ''.join(my_input)

    self.quit(my_input) # Quits game if the input is a quit command
    return my_input