coordinate = ''
def draw(coordinate):
  coordinate = input("enter coordinate(in format 'b3'): ")
  letter = 'abcdefgh'
  y = letter.find(coordinate[0])
  x = int(coordinate[1]) - 1
  chessboard = [['.'] * 8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      if  ((abs(y - j) == 1) or y == j) and ((abs(x - i) == 1) or x == i):
        chessboard[i][j] = '*'
  chessboard[x][y] = 'K'
  for i in range(8):
    print((i + 1), *chessboard[i])
  print('  a b c d e f g h')
y = 'y'
while y == 'y':
  draw(coordinate)
  y = input("Do you want to restart?(y/n): ", )
print('Goodbye')