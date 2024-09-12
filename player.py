from game_object import GameObject
from tile import Tile
from ship import Ship

class Player(GameObject):
  def __init__(self, id, active):
    super().__init__()
    self.id = id
    self.active = active #boolean

    self.board = []
    self.__build_board_of_tiles(self.board)

    self.opps = []
    self.__build_board_of_tiles(self.opps)

    self.ship_list = []

  def __build_board_of_tiles(self, board):
    for row in range(10):
      board.append([]) # add row
      for col in range(10):
        tile = Tile(row, col)
        board[row].append(tile) # place tiles

  def print_board(self, board):
    print("  A B C D E F G H I J")
    for i, row in enumerate(board): # This just prepends the numbers to the rows
      tiles_as_strings = [str(tile) for tile in row]
      print(f"{i} " + " ".join(tiles_as_strings))

  def set_ship_list(self, num_ships):
    # Add the proper number of properly sized ships to self.ship_list. Ship(name, size, symbol)
    self.ship_list = [
      Ship(
        self.ship_size_to_name[f"1x{i}"],  # Ship name (e.g. "Destroyer")
        f"1x{i}",                          # Ship size (e.g. "1x3")
        self.ship_size_to_symbol[f"1x{i}"] # Ship symbol (e.g. "#")
      )
      for i in range(1, num_ships + 1)
    ]

    self.ship_list.reverse() # Desc. order

  def selected_ship(self):
    return self.ship_list[0]

  def selected_ship_length(self):
    return int(self.selected_ship().size[-1])

  def hide_ships(self):
    while self.ship_list != []: # Hide all ships
      while self.selected_ship().has_valid_coords == False: # Until the ship is placed in a completely valid zone
        self.selected_ship().coords = []

        print(f"Player {self.id} - Hiding their {self.selected_ship().name}...")
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

  def __hide_ship(self, col, row):
    self.board[row][col] = self.selected_ship() # Initial placement

    if self.selected_ship_length() > 1: # If we can orient this ship...
      self.__orient_ship(row, col)

    self.ship_list.pop(0) # Remove it from our list of remaining ships

    if self.ship_list != []:
      print("Remaining ships:")
      self.print_ship_list()

  def __orient_ship(self, row, col):
    coord = self.__row_col_to_coord_pair(row, col)

    # if self.valid_coord(coord):
    print("u = Up\nd = Down\nl = Left\nr = Right")

    direction = "" # Init for while loop
    while direction not in ["u","d","l","r"]:
      # u: up
      # d: down
      # l: left
      # r: right
      direction = input("Which direction do you want your ship to be oriented?: ").lower()

      if direction in ["u","d","l","r"]:
        for i in range(self.selected_ship_length()):
          # pass in the next adjacent coord until the ship is placed down fully
          self.__place_ship_tile(self.direction_to_coord(direction, row, col, i))
      else:
        print("Pick one: u d l r")

  def __place_ship_tile(self, coord):
      row, col = coord[0], coord[1]
      try: # If the coordinate is in bounds
        if  type(self.board[row][col]) == Tile:
          self.board[row][col] = self.selected_ship() # Make it part of the Ship
          self.selected_ship().coords.append([row,col]) # Add this section of the ship to the coords
      except:
        print("That went off the edge... try again...")
        print(self.selected_ship().coords)
        self.selected_ship().coords.append([row,col]) # Add this setion of the ship to the coords, this will be wiped

  def __row_col_to_coord_pair(self, row, col):
      return self.col_index_to_letter[col] + str(row) # Return LetterNumber coordinate that works with GameObject.valid_coord()

  def direction_to_coord(self, direction, row, col, i):
    direction_to_coord = {
      "u": [row - i, col],
      "d": [row + i, col],
      "l": [row, col - i],
      "r": [row, col + i]
    }
    return direction_to_coord[direction]

  def attack_ships(self, coord):
    # TODO: Attack ships
    return

  def print_ship_list(self):
    for ship in self.ship_list:
      print(f"{ship.name} ({ship.size})")