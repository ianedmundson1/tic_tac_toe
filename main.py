import random
from function_tik import *

# empty matrix for board
Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
check = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

n = 0
s = 5
a = 0
# Game starts
print("Welcome to Tic Tac Toe!")
while n == 0:
    # check for winners
  n, s = check_board(check, n)
  # have computer take turn
  if n == 0:
    print('Computers turn to move')

    Board, check, s = computers_turn(Board, check,s)
    
    print_Board(Board)
  
    a = a + 1
    if a == 5:
      print("It's a Draw!!!")
      n += 1
      break
  
    # start useres turn
    while s < 0:
        # Take user input
        Board, check, s = players_turn(Board, check,s)