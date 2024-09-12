class Tile:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.symbol = " "

  def str(self):
    return self.symbol

  def __repr__(self):
    return self.symbol