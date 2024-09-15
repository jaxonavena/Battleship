class Tile:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.symbol = " "

  def is_sunk(self):
    return False

  def str(self):
    return self.symbol

  def __repr__(self):
    return self.symbol