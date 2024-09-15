class Ship:
  def __init__(self, name, size, symbol):
    self.name = name
    self.size = size
    self.symbol = symbol
    self.coords = []
    self.tiles = []
    self.hidden = False
    self.hp = int(self.size[-1]) # A 1x3 ship will init with hp = 3

  def is_sunk(self):
    return self.hp == 0

  def sink(self):
    for tile in self.tiles:
      tile.symbol = "S"

  def __str__(self):
    return self.symbol

  def __repr__(self):
    return self.symbol
