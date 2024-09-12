from game_object import GameObject
from tile import Tile
from ship import Ship

class Player(GameObject):
  def __init__(self, id, active):
    super().__init__()
    self.id = id
    self.active = active #boolean
    self.attacked_coords = []
    self.opponent_object
    self.board = []
    self.__build_board_of_tiles(self.board)

    self.opps = []
    self.__build_board_of_tiles(self.opps)

    self.ship_list = []

  def set_opponent(self,opponent):
    self.opponent_object = opponent

  def __build_board_of_tiles(self, board):
    # Fills out a given list with 10 nested lists of 10 Tile items
    # ---------------------------------------------------------- #
    for row in range(10):
      board.append([]) # add row
      for col in range(10):
        tile = Tile(row, col)
        board[row].append(tile) # place tiles

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

      coord = self.get_input("Hide the ship: ")

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
    # need a boalean return for this so we can mark the opponents board when a hit(true)
    row = coord[0]
    col = coord[1]
    if isinstance(self.opponent_objective.board[row][col],Ship):
      self.mark_hit_opps_board(coord)
      self.opponent_objective.board[row][col].health -= 1
      return True
    
    return False

  def mark_hit_opps_board(self, coord):
    row = coord[0]
    col = coord[1]
    self.opps[row][col].symbol = "H"
    return
  
  def mark_miss_opps_board(self, coord):
    row = coord[0]
    col = coord[1]
    self.opps[row][col].symbol = "M"
    return
  
  def mark_hit_player_board(self, coord):
    row = coord[0]
    col = coord[1]
    self.board[row][col].symbol = "H"
    return
  
  def mark_miss_player_board(self, coord):
    row = coord[0]
    col = coord[1]
    self.board[row][col].symbol = "M"
    return
  
  def sunk_ship_opps(self, coord):
    row = coord[0]
    col = coord[1]
    if self.opps[row][col].health == 0:
      for i in self.opps[row][col].coord:
        ship_row = i[0]
        ship_col = i[1]
        self.opps[ship_row][ship_col].symbol = "S"
    return
  
  def sunk_ship_player(self, coord):
    row = coord[0]
    col = coord[1]
    if self.board[row][col].health == 0:
      for i in self.board[row][col].coord:
        ship_row = i[0]
        ship_col = i[1]
        self.board[ship_row][ship_col].symbol = "S"
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
    if self.coords_are_inbounds(self.selected_ship().coords): # if we're at least placing the ship on the board...
      for coord in self.selected_ship().coords:
        if type(self.board[coord[0]][coord[1]]) == Tile: #...make sure we're not overlapping ships
          self.board[coord[0]][coord[1]] = self.selected_ship() # Set the Tile to be the Ship
          flag = True
        else:
          return False # Every coord needs to be valid
    else:
      self.selected_ship().coords = [] # We're going to retry hiding the ship if we're out of bounds, so we wipe the ship's coords list
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