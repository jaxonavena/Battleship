class Ship:
  def __init__(self, name, size, symbol):
    self.name = name
    self.size = size
    self.symbol = symbol
    self.coords = []
    self.has_valid_coords = False
    self.hidden = False
    self.hp = int(self.size[-1]) # A 1x3 ship will init with hp = 3
    self.sunk = self.hp == 0

  def __str__(self):
      return self.symbol

  def __repr__(self):
      return self.symbol

  def valid_coords(self):
    flag = True
    for coord in self.coords:
      if coord[0] > 9 or coord[0] < 0 or coord[1] > 9 or coord[1] < 0:
        self.coords = []
        flag = False
    return flag
