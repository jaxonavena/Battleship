from game_object import GameObject
class Game(GameObject):
  def __init__(self, player_bank):
    super().__init__()
    self.player_bank = player_bank
    self.player1 = player_bank[0]
    self.player2 = player_bank[1]
    self.turn_count = 1
    self.active_player = self.get_active_player()
    self.num_ships = 0

  def __switch_turns(self): # Switch who is activated
    for player in self.player_bank:
      player.active = not player.active

  def start(self):
    self.__set_ship_lists() # Determine the number of ships each player will have and set the list
    self.__setup_boards() # Hide the ships
    self.__take_turn(1) # Start shootin

  def __take_turn(self, turn_count):
    print(f"Turn #{turn_count}")
    self.print_board(self.active_player.opps)

    coord = self.get_input(f"Player {self.active_player.id}'s turn: ")

    if self.valid_coord_with_error_messages(coord):
      self.active_player.attack_ship(coord)
      self.turn_count += 1
      self.__switch_turns()

    self.__take_turn(self.turn_count) # This will replay the turn if the input was invalid otherwise it will start the next turn

  def get_active_player(self):
    for player in self.player_bank:
      if player.active == True:
        return player
      
  def __setup_boards(self):
    for player in self.player_bank:
      player.hide_ships()
      print(f"Player {player.id} - All ships are hidden...")
      self.print_board(player.board) # Show their board after they're finished hiding their ships
      print("----------------------------------\n")

  def __set_ship_lists(self):
    while 0 >= self.num_ships or self.num_ships > 5: # Until num ships is a number 1-5
      print("Please enter a number between 1 and 5.")
      try:
        self.num_ships = int(input("How many ships per team?: "))
      except:
        self.num_ships = 0

    self.player1.set_ship_list(self.num_ships)
    self.player2.set_ship_list(self.num_ships)