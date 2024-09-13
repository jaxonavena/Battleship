from player import Player
from game import Game
# Pete dumb
p1 = Player(1, True)
p2 = Player(2, False)
p1.set_opponent(p2)
p2.set_opponent(p1)
player_bank = [p1,p2]
game = Game(player_bank)
game.start()