from game_object import GameObject
class Game(GameObject):
  def __init__(self, player_bank):
    super().__init__()
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
    self.active_player = self.get_active_player()
    self.num_ships = 0

  def __switch_turns(self): # Switch who is activated
    for player in self.player_bank:
      if player.active == False:
        player.active = True
      elif player.active == True:
        player.active = False

  def start(self):
    self.__set_ship_lists() # Determine the number of ships each player will have and set the list
    self.__setup_boards() # Hide the ships
    self.__take_turn(1) # Start shootin

  def __take_turn(self, turn_count):
    print(f"Turn #{turn_count}")
    self.print_board() # TODO: Remove this and the var. We won't need it since players track their own boards
    coord = input(f"Player {self.active_player.id}'s turn: ")

    if coord in self.list_of_synonyms_for_quit_lol: # QUIT GAME?
      exit()

    if self.valid_coord(coord):
      self.active_player.attack_ships(coord)
      self.turn_count += 1
      self.__switch_turns()

    self.__take_turn(self.turn_count) # This will replay the turn if the input was invalid otherwise it will start the next turn

  def print_board(self):
    print("  A B C D E F G H I J")
    for i, row in enumerate(self.board, start=0): # This just prepends the numbers to the rows
      print(f"{i} " + " ".join(row))

  def get_active_player(self):
    for player in self.player_bank:
      if player.active == True:
        return player

  # def __setup_boards(self):
  #   self.player1.hide_ships()
  #   self.player2.hide_ships()

  def __setup_boards(self):
    # Ensure all ships are hidden before switching to the other player
    print("Player 1 hiding ships...")
    self.player1.hide_ships()  # Hide ships for Player 1
    if self.player1.ship_list:  # Check if all ships are hidden
        print(f"DEBUG: Player 1 has remaining ships: {self.player1.ship_list}")

    print("Player 2 hiding ships...")
    self.player2.hide_ships()  # Hide ships for Player 2
    if self.player2.ship_list:  # Check if all ships are hidden
        print(f"DEBUG: Player 2 has remaining ships: {self.player2.ship_list}")


  def __set_ship_lists(self):
    while 0 >= self.num_ships or self.num_ships > 5: # Until num ships is a number 1-5
      self.num_ships = int(input("How many ships per team?: ")) # TODO: Error handling?

    self.player1.set_ship_list(self.num_ships)
    self.player2.set_ship_list(self.num_ships)