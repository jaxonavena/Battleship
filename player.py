from game import Game
from game_object import GameObject

class Player(GameObject):
  def __init__(self, id, active):
    super().__init__()
    self.id = id
    self.active = active #boolean
    self.board = [
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",]
]
    self.opps = [
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",],
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",]
]
    self.ship_list = []

  def hide_ships(self):
    while self.ship_list != []: # Hide all ships
      print(f"Player {self.id} - Hiding their {self.selected_ship_name()}...")
      self.print_board(self.board)

      coord = input("Hide the ship: ")

      if coord in self.list_of_synonyms_for_quit_lol: # QUIT GAME?
        exit()

      if self.valid_coord(coord):
        # coord = "a5"
        # coord => GameObject.letter_to_col_index => __hide_ship(0,5) => col, row
        # TODO: UPDATE THIS COMMENT (AND FUNCTION) FROM 05 WHEN ROW NUMBERS CHANGE
        self.__hide_ship(int(self.letter_to_col_index[coord[0].upper()]), int(coord[1])) # Not to be confused with hide_ships()
        # self.print_board(self.board)
      else:
        self.hide_ships() # This will replay the turn if the input was invalid otherwise it will start the next turn

  def print_board(self, board):
    print("  A B C D E F G H I J")
    for i, row in enumerate(board, start=0): # This just prepends the numbers to the rows
      print(f"{i} " + " ".join(row))

  def attack_ships(self, coord):
    # TODO: Attack ships
    # call mark hit or miss 
    return

  def mark_hit(self, coord):
    row = coord[0]
    row = self.letter_to_row_index[row]
    col = coord[1]
    self.opps[row][col] = "H"
    return
  
  def mark_miss(self, coord):
    row = coord[0]
    col = coord[1]
    self.opps[row][col] = "M"
    return
  
  def sunk_ship(self):
    return

  def set_ship_list(self, num_ships):
    self.ship_list = [f"1x{i}" for i in range(1, num_ships + 1)]
    self.ship_list.reverse() # Desc. order
    print(self.ship_list)

  def selected_ship_name(self):
    return self.ship_size_to_name[self.ship_list[0]]

  def selected_ship_symbol(self):
    return self.ship_size_to_symbol[self.ship_list[0]]

  def selected_ship_size(self):
    return int(self.ship_list[0][-1])

  def __hide_ship(self, col, row):
    self.board[row][col] = self.selected_ship_symbol() # Initial placement

    if self.selected_ship_size() > 1: # If we can orient this ship...
      self.__orient_ship(row, col)

    self.ship_list.pop(0) # Remove it from our list of remaining ships

    if self.ship_list != []:
      print(f"Remaining ships: {self.ship_list}")


  def __orient_ship(self, row, col):
    # u: up
    # d: down
    # l: left
    # r: right
    coord = self.__row_col_to_coord_pair(row, col)

    if self.valid_coord(coord):
      print("u = Up\nd = Down\nl = Left\nr = Right")

      direction = "" # Init for while loop
      while direction not in ["u","d","l","r"]:
        direction = input("Which direction do you want your ship to be oriented?: ").lower()

        if direction in ["u","d","l","r"]:
          for i in range(self.selected_ship_size()):
            # pass in the next adjacent coord until the ship is placed down fully
            self.__place_ship_tile(self.direction_to_coord(direction, row, col, i))
        else:
          print("Pick one: u d l r")


  def __row_col_to_coord_pair(self, row, col):
      return self.col_index_to_letter[col] + str(row) # Return LetterNumber coordinate that works with GameObject.valid_coord()

  def __place_ship_tile(self, coord):
      row, col = coord[0], coord[1]

      if self.board[row][col] == "*":
        self.board[row][col] = self.selected_ship_symbol()

  def direction_to_coord(self, direction, row, col, i):
    direction_to_coord = {
      "u": [row - i, col],
      "d": [row + i, col],
      "l": [row, col - i],
      "r": [row, col + i]
    }
    return direction_to_coord[direction]