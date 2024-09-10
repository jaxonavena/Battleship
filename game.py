class Game:
  def __init__(self, player_bank):
    self.player_bank = player_bank
    self.player1 = player_bank[0]
    self.player2 = player_bank[1]
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
    self.turn_count = 1
    self.list_of_synonyms_for_quit_lol = ["exit", "q", "quit", "EXIT", "Q", "QUIT"]

  def __switch_turns(self): # Switch who is activated
    for player in self.player_bank:
      if player.active == False:
        player.active = True
      elif player.active == True:
        player.active = False

  def start(self):
    self.__take_turn(1)

  def __take_turn(self, turn_count):
    print(f"Turn #{turn_count}")
    self.print_board()
    active_player_id = self.get_active_player_id()

    coord = input(f"Player {active_player_id}'s turn: ")
    if coord in self.list_of_synonyms_for_quit_lol: # QUIT GAME
      exit()

    if self.valid_coord(coord):
      print(coord) # TODO: Replace with actual stuff.
      self.turn_count += 1
      self.__switch_turns()

    self.__take_turn(self.turn_count) # This will replay the turn if the input was invalid otherwise it will start the next turn

  def print_board(self):
    print("  A B C D E F G H I J")
    for i, row in enumerate(self.board, start=0): # This just prepends the numbers to the rows
      print(f"{i} " + " ".join(row))

  def valid_coord(self, coord):
    valid = self.__handle_coordinates(coord) # (valid? (bool), row, col) tuple being returned
    return True if valid else False

  def __handle_coordinates(self, coord):
    row, col = coord[0], coord[1]

    try:
      col = coord[0].upper() # Assume it's a letter
      row = int(coord[1:]) # Assume it's a number, grab everything after the column letter
    except ValueError as _e:
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

  def get_active_player_id(self):
    for player in self.player_bank:
      if player.active == True:
        return player.id