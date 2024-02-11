import random
def print_Board(Board):
  # dividing lines
  # dividing lines
  print('---------')
  # loop meant for finishing board
  for point in range(3):
      print(" |{:s}|{:s}|{:s}|".format(Board[point][0], Board[point][1], Board[point][2]))
      print('---------')
  return 0

def check_board(check, n):
  col_1 = [item[0] for item in check]
  col_2 = [item[1] for item in check]
  col_3 = [item[2] for item in check]
  col1 = sum(col_1)
  col2 = sum(col_2)
  col3 = sum(col_3)
  row1 = sum(check[0])
  row2 = sum(check[1])
  row3 = sum(check[2])
  diag1 = check[0][0] + check[1][1] + check[2][2]
  diag2 = check[0][2] + check[1][1] + check[2][0]
  WinList = [diag1, diag2, row1, row2, row3, col1, col2, col3]
  s = 5
  for spot in range(8):
    if WinList[spot] == 30:
      print('Congratulation!!! You Won!!!')
      return 1, -1
    elif WinList[spot] == 0:
      print('Sorry, You Lose')
      return 1, -1
  return n, s

def players_turn(Board, check, s):

  try:
    row, column = input('Enter row and column values: ').split()
  
    row = int(row) - 1
    column = int(column) - 1
      # check if available then place if so
    if check[row][column] == 1:
      Board[row][column] = 'X'
      check[row][column] = 10
      print_Board(Board)
      s = s + 10
    elif check[pick1][pick2] == 0 or 10:
      print('  ')
      print('invalid move try different spot')
      print('  ')
      pass
  except (ValueError):
    print('  ')
    print('invalid move try again')
    print('Remember to put spaces between answers  ')
    print('  ')
  
  return Board, check, s

def computers_turn(Board, check, s):
  while s > 0:
    # Have computer choose spot randomly
      pick1 = random.randint(0, 2)
      pick2 = random.randint(0, 2)
  
        # check if spot has been used before
      if check[pick1][pick2] == 1:
        Board[pick1][pick2] = 'O'
        check[pick1][pick2] = 0
        s = s - 10
      elif check[pick1][pick2] == 0 or 10:
        s = 5
  
  return Board, check, s