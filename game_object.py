class GameObject:
  def __init__(self):
    self.list_of_synonyms_for_quit_lol = ["exit", "q", "quit", "EXIT", "Q", "QUIT"]
    self.ship_size_to_name_map = {
      "1x1": "Cruiser",
      "1x2": "Submarine",
      "1x3": "Destroyer",
      "1x4": "Battleship",
      "1x5": "Aircraft Carrier"
    }
    self.letter_to_row_index_map = {
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

  def valid_coord(self, coord): # Is this a valid coord?
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
      print("Invalid Coordinate. Ensure your input ends with a valid row header (e.g. C3)")
      return False

    if row < 0 or row > 9:
      print("Invalid Coordinate. Ensure your input lies within the bounds of the 10x10 board. (Zero indexed)")
      return False

    return True