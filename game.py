from game_object import GameObject
class Game(GameObject):
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
    self.__setup_boards()
    # TODO: Need to have an initial period where players submit their boards with their ships laid out
    # We'll need to have some vars tracking their real boards, but display a different board for the shooter with the ships hidden.
    self.__take_turn(1) # Start shootin

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
    return self.handle_coordinates(coord) # bool

  def get_active_player_id(self):
    for player in self.player_bank:
      if player.active == True:
        return player.id

  def __setup_boards(self):
    self.player1.hide_ships()
    self.player2.hide_ships()


