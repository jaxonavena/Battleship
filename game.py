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
["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",]
]
    self.turn_count = 1

  def switch_turns(self):
    for player in self.player_bank:
      if player.active == False:
        player.active = True
      elif player.active == True:
        player.active = False

  def start(self):
    self.take_turn(1)

  def take_turn(self, turn_num):
    print(f"Turn #{turn_num}")
    self.print_board()

    move = input("Enter a coordinate: ")
    print(move)

    self.turn_count += 1
    self.take_turn(self.turn_count)

  def print_board(self):
    print("  A B C D E F G H I J")
    for i, row in enumerate(self.board, start=1):
      print(f"{i} " + " ".join(row))