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

  def valid_coord_with_error_messages(self, coord): # Is this a valid coord? Takes LetterNumber combo coordinates (e.g. A8)
    try:
      col = coord[0].upper() # Assume it's a letter
      row = int(coord[1:]) # Assume it's a number, grab everything after the column letter
    except ValueError:
      print("Your coordinate must be a letter-number pair (e.g. A8)")
      return False

    if col not in ["A","B","C","D","E","F","G","H","I","J"]:
      print("Invalid Coordinate. Ensure your input starts with a valid column header (e.g. E4)")
      return False

    if row not in range(0,10):
      print("Invalid Coordinate. Ensure your input lies within the bounds of the 10x10 board.")
      return False

    return True

  def coords_are_inbounds(self, coords):
      flag = False
      for coord in coords:
        if coord[0] > 9 or coord[0] < 0 or coord[1] > 9 or coord[1] < 0:
          return False
        else:
          flag = True
      return flag

  def coord_translator(self, coord):
    # e.g. coord = A8
    col = self.letter_to_col_index[coord[0].upper()] # Letters are columns
    row = int(coord[1]) # Numbers are rows
    return row, col #return row number, column number to use as indeces

  def print_board(self, board):
    # Prints a given board with the rows and columns labeled
    # ---------------------------------------------------------- #
    print("  A B C D E F G H I J")
    for i, row in enumerate(board): # This just prepends the numbers to the rows
      tiles_as_strings = [str(tile) for tile in row]
      print(f"{i} " + " ".join(tiles_as_strings))

  def quit(self, input):
    if input in ["exit", "q", "quit", "EXIT", "Q", "QUIT"]:
      exit()

  def get_input(self, message):
    my_input = input(message)

    self.quit(my_input) # Quits game if the input is a quit command
    return my_input