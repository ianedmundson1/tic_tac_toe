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

def make_a_turn(board, symbol):

  check = True

  check_board = [[0 if element == " " else 1 for element in row] for row in board]

  while check == True:
    # Have computer choose spot randomly
      pick1 = random.randint(0, 2)
      pick2 = random.randint(0, 2)
  
      
        # check if spot has been used before
      if check_board[pick1][pick2] == 0:

        board[pick1][pick2] = symbol

        check = False
      else:

        pass
        
  
  return board


def check_board_new(board, symbol):
  
  check_tie, winList = check_for_tie(board)
  if check_for_tie(board) == True:
    print(' ')
    print('Its a tie')
    return True, winList
 
  if check_for_win(board, symbol) == True:
    print('')
    print('its a win')
    return True, winList
  
  return False, winList



def opposite_symbol(symbol):
  
  if symbol == 'x':
    return 'o'
  else:
    return 'x'

def check_for_tie(board):

  board = [[0 if element == " " else 1 for element in row] for row in board]
  
  winList = get_win_check(board)

  if sum(winList) == 3*8:
    return True, winList
  
  else:
    return False, winList
  #if all winlist == 3 return True else false



def check_for_win(board, symbol):

  board = [[0 if element == " " or element == opposite_symbol(symbol) else 1 for element in row] for row in board]

  winList = get_win_check(board)

  for spot in range(8):

    #check for win
    if winList[spot] == 3:
      return True, winList

  return False, winList

def get_win_check(board):

  col_1 = [item[0] for item in board]
  col_2 = [item[1] for item in board]
  col_3 = [item[2] for item in board]
  col1 = sum(col_1)
  col2 = sum(col_2)
  col3 = sum(col_3)
  row1 = sum(board[0])
  row2 = sum(board[1])
  row3 = sum(board[2])
  diag1 = board[0][0] + board[1][1] + board[2][2]
  diag2 = board[0][2] + board[1][1] + board[2][0]
  winList = [diag1, diag2, row1, row2, row3, col1, col2, col3]

  return winList
