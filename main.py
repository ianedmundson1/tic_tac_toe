import random
from function_tik import *

# empty matrix for board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

win = False
# Game starts
print("Welcome to Tic Tac Toe!")

while win == False:

  for symbol in ['x','o']:
    
    win, winList = check_board_new(board, symbol)

    if win == False:

      Board = make_a_turn(board, symbol)

    else: 

      dic = {'diag1':winList[0], 
              'diag2':winList[1],
              'row1':winList[2], 
              'row2':winList[3],
              'row3':winList[4],
              'col1':winList[5],
              'col2':winList[6],
              'col3':winList[7]}
      
      print(dic)
      break
    
    print_Board(board)
    
    
print("game is over")