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

    for player in self.player_bank:
      if player.active == True:
        active_player_id = player.id

    coord = input(f"Player {active_player_id}'s turn: ")

    if self.valid_coord(coord):
      print(coord) # TODO: Replace with actual stuff.

      self.turn_count += 1
      self.__switch_turns()

    self.__take_turn(self.turn_count)

  def print_board(self):
    print("  A B C D E F G H I J")
    for i, row in enumerate(self.board, start=0): # This just prepends the numbers to the rows
      print(f"{i} " + " ".join(row))

  def valid_coord(self, coord):
    row, col = self.__set_row_and_col_from_coord(coord)
    if self.__handle_invalid_coordinates(row, col): # row, col valid?
      return True
    else:
      return False


  def __set_row_and_col_from_coord(self, coord):
    try:
      col = coord[0].upper() # Assume it's a letter
      row = int(coord[1]) # Assume it's a number
    except ValueError as e:
      print(f"An error occurred: {e}. Your coordinate must be a letter-number pair (e.g. A8)")
      return False

    return row, col

  def __handle_invalid_coordinates(self, row, col):
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