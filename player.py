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
    # Fills out a given list with 10 nested lists of 10 Tile items
    # ---------------------------------------------------------- #
    for row in range(10):
      board.append([]) # add row
      for col in range(10):
        tile = Tile(row, col)
        board[row].append(tile) # place tiles

  def print_board(self, board):
    # Prints a given board with the rows and columns labeled
    # ---------------------------------------------------------- #
    print("  A B C D E F G H I J")
    for i, row in enumerate(board): # This just prepends the numbers to the rows
      tiles_as_strings = [str(tile) for tile in row]
      print(f"{i} " + " ".join(tiles_as_strings))

  def set_ship_list(self, num_ships):
    # Add the proper number of properly sized ships to self.ship_list. Ship(name, size, symbol)
    # ---------------------------------------------------------- #
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
    # Return the ship that is currently selected, AKA at the front of self.ship_list
    # ---------------------------------------------------------- #
    return self.ship_list[0]

  def selected_ship_length(self):
    # Return the length of the selected ship. (e.g. The length of a 1x3 ship is 3)
    # ---------------------------------------------------------- #
    return int(self.selected_ship().size[-1])

  def __clear_selected_ship_from_board(self):
    # Restore the initial ship placement to be a Tile.
    # ---------------------------------------------------------- #
    for row in range(10):
      for col in range(10):
        if self.board[row][col] == self.selected_ship():
          self.board[row][col] = Tile(row, col)
    self.selected_ship().coords = []

  def hide_ships(self):
    # Loop until all ships are hidden. Gathers the root coord for the selected ship to be oriented from.
    # ---------------------------------------------------------- #
    while self.ship_list != []: # Hide all ships
      self.__clear_selected_ship_from_board() # Wipe invalid hide attempts. If the attempt was valid the ship would have been popped off ship_list. Otherwise it will still be the selected ship and the board will be cleaned.

      print(f"Player {self.id} - Hiding their {self.selected_ship().name}...")
      self.print_board(self.board)

      coord = input("Hide the ship: ")

      if coord in self.list_of_synonyms_for_quit_lol: # QUIT GAME?
        exit()

      if self.valid_coord(coord): # If it's on the board
        # Get integer indeces
        row = int(self.letter_to_col_index[coord[0].upper()])
        col = int(coord[1])
        if type(self.board[row][col]) == Tile: # If the targeted location is a vacant Tile
          self.__hide_ship(row, col) # Not to be confused with hide_ships(). Attempt to hide the ship

  def __hide_ship(self, col, row):
    # Hide the selected ship
    # ---------------------------------------------------------- #
    self.__orient_ship(row, col) # orient and place the full length of the ship

    if self.selected_ship_has_been_hidden_in_a_valid_location():
      self.ship_list.pop(0) # Remove it from our list of remaining ships
    else:
      print("You cannot place your ship out of bounds or over another ship. Try again.")

    self.print_remaining_ships_to_hide()

  def __orient_ship(self, row, col):
    # If the selected ship length is > 1, orient the ship on the board while hiding it.
    # u: up
    # d: down
    # l: left
    # r: right
    # ---------------------------------------------------------- #
    print("u = Up\nd = Down\nl = Left\nr = Right")

    direction = "" # Init for while loop
    while direction not in ["u","d","l","r"]:
      # Default for 1x1 ships to orient themselves
      direction = input("Which direction do you want your ship to be oriented?: ").lower() if self.selected_ship_length() > 1 else "u"

      if direction in ["u","d","l","r"]:
        for i in range(self.selected_ship_length()):
          # List the coords that this ship will occupy, if the coords are validated downstream
          self.selected_ship().coords.append(self.direction_to_coord(direction, row, col, i))
      else:
        print("Pick one: u d l r")

  def selected_ship_has_been_hidden_in_a_valid_location(self):
    # Verify if the selected ship's list of coordinates are all on the board and vacant Tiles
    # ---------------------------------------------------------- #
    flag = False
    if self.selected_ship().coords_are_inbounds(): # if we're at least placing the ship on the board...
      for coord in self.selected_ship().coords:
        if type(self.board[coord[0]][coord[1]]) == Tile: #...make sure we're not overlapping ships
          self.board[coord[0]][coord[1]] = self.selected_ship() # Set the Tile to be the Ship
          flag = True # Every coord needs to be valid
        else:
          return False
    return flag

  def direction_to_coord(self, direction, row, col, i):
    # Translate up, down, left, or right in relation to a coordinate into the new coordinate corresponding with the direction.
    # ---------------------------------------------------------- #
    direction_to_coord = {
      "u": [row - i, col],
      "d": [row + i, col],
      "l": [row, col - i],
      "r": [row, col + i]
    }
    return direction_to_coord[direction]

  def attack_ship(self, coord):
    # TODO: Attack ships
    return

  def print_ship_list(self):
    # Print the ship list
    # ---------------------------------------------------------- #
    for ship in self.ship_list:
      print(f"{ship.name} ({ship.size})")

  def print_remaining_ships_to_hide(self):
    if self.ship_list != []:
      print("Remaining ships:")
      self.print_ship_list()