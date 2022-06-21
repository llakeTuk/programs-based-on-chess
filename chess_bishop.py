coordinate = ''
def draw(coordinate):
  coordinate = input("enter coordinate(in format 'b3'): ")
  letter = 'abcdefgh'
  y = letter.find(coordinate[0])
  x = 8 - int(coordinate[1])
  chessboard = [['.'] * 8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      if (abs(y - j) == abs(x - i)):
        chessboard[i][j] = '*'
  chessboard[x][y] = 'B'
  for i in range(8):
    print((8 - i), *chessboard[i])
  print('  a b c d e f g h')
y = 'y'
while y == 'y':
  draw(coordinate)
  y = input("Do you want to restart?(y/n): ", )
print('Goodbye')
