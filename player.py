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
    self.attacked_coords = []
    self.ship_list = []

    # Opponent information
    self.opp = None # The other Player
    self.opps_board = [] # Board to track where you have fired at your opponent
    self.__build_board_of_tiles(self.opps_board)

  def set_opponent(self,opponent):
    self.opp = opponent

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

      if self.valid_coord_with_error_messages(coord): # If it's on the board
        # Get integer indeces
        row, col = self.coord_translator(coord)
        if type(self.board[row][col]) == Tile: # If the targeted location is a vacant Tile
          self.__hide_ship(row, col) # Not to be confused with hide_ships(). Attempt to hide the ship

  def __hide_ship(self, row, col):
    # Hide the selected ship
    # ---------------------------------------------------------- #
    self.__orient_ship(row, col) # orient and place the full length of the ship

    if self.selected_ship_has_been_hidden_in_a_valid_location():
      self.ship_list.pop(0) # Remove it from our list of remaining ships
    else:
      print("You cannot place your ship out of bounds or over another ship. Try again.")

    self.print_remaining_ships_to_hide()

  def attack_ship(self, coord):
    # need a boalean return for this so we can mark the opponents board when a hit(true)
    row, col = self.coord_translator(coord)
    if isinstance(self.opp.board[row][col],Ship):
      self.hit(coord)
      return True
    else:
      self.miss(coord)
      return False

  def hit(self, coord):
    row, col = self.coord_translator(coord)
    self.mark_shot(self.opps_board, coord, "H") # Hit your opponent's ship. Tracking it for yourself.
    self.mark_shot(self.opp.board, coord, "H") # Hit your opponent's ship. Update their board
    self.opp.sunk_ship_player(coord) # Change symbol to S if ship is sunk
    self.opp.board[row][col].hp -= 1 # Decrement oponnent's ship health
    if self.opp.board[row][col].hp == 0:
      self.print_shot_result("S")
      self.sunk_ship_opps(coord)
      self.opp.ship_list.pop()
    else:
      self.print_shot_result("H")

  def miss(self, coord):
    self.mark_shot(self.opps_board, coord, "M") # Missed your opponent's ship. Tracking it for yourself.
    self.mark_shot(self.opp.board, coord, "M") # Missed your opponent's ship. Update their board
    self.print_shot_result("M")

  def mark_shot(self, board, coord, result):
    row, col = self.coord_translator(coord)
    board[row][col].symbol = result

    #if board == self.opps_board:
     # self.print_shot_result(result)

  def print_shot_result(self, result):
    self.br()
    self.br(result, gap = 5)

  def sunk_ship_opps(self, coord):
    row, col = self.coord_translator(coord)
    if self.opp.board[row][col].hp == 0:
      for i in self.opp.board[row][col].coords:
        ship_row = int(i[0])
        ship_col = int(i[1])
        self.opps_board[ship_row][ship_col].symbol = "S"
        self.opp.board[ship_row][ship_col].symbol = "S"

  def sunk_ship_player(self, coord):
    row, col = self.coord_translator(coord)
    if self.board[row][col].hp == 0:
      for i in self.board[row][col].coords:
        ship_row = int(i[1])
        ship_col = self.letter_to_col_index[coord[0].upper()]
        self.board[ship_row][ship_col].symbol = "S"
        self.opp.opps_board[row][col].symbol = "S"

  def __orient_ship(self, row, col):
    # If the selected ship length is > 1, orient the ship on the board while hiding it.
    # u: up
    # d: down
    # l: left
    # r: right
    # ---------------------------------------------------------- #

    direction = "" # Init for while loop
    while direction not in ["u","d","l","r"]:
      if self.selected_ship_length() > 1:
        print("u = Up\nd = Down\nl = Left\nr = Right")
        direction = input("Which direction do you want your ship to be oriented?: ").lower()
      else:
        # Default for 1x1 ships to orient themselves
        direction = "u"

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

  def print_ship_list(self):
    # Print the ship list
    # ---------------------------------------------------------- #
    for ship in self.ship_list:
      print(f"{ship.name} ({ship.size})")

  def print_remaining_ships_to_hide(self):
    if self.ship_list != []:
      print("Remaining ships:")
      self.print_ship_list()