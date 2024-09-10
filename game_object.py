class GameObject:
  def handle_coordinates(self, coord):
    row, col = coord[0], coord[1]

    try:
      col = coord[0].upper() # Assume it's a letter
      row = int(coord[1:]) # Assume it's a number, grab everything after the column letter
    except ValueError as _e:
      print("Your coordinate must be a letter-number pair (e.g. A8)")
      return False

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