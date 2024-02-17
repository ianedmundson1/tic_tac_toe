import random
from function_tik import *
import pandas as pd
import numpy as np
# empty matrix for board
#board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Game starts
print("Welcome to Tic Tac Toe!")
training_data = {}
count = 0

for i in range(0,30):

  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

  win = False
  
  count+=1
  
  while win == False:

    for symbol in ['x','o']:
      
      win, winList = check_board_new(board, symbol)

      if win == False:

        board, row, col = make_a_turn(board, symbol)
        dic = {'diag1':winList[0], 
                          'diag2':winList[1],
                          'row1':winList[2], 
                          'row2':winList[3],
                          'row3':winList[4],
                          'col1':winList[5],
                          'col2':winList[6],
                          'col3':winList[7],
                          'col': col,
                          'row': row,
                          'symbol': symbol,
                          'game': i,
                          'win': np.nan}  
              #print_Board(board)
        training_data[count] = dic
        
      else: 
        dic = {'diag1':winList[0], 
                  'diag2':winList[1],
                  'row1':winList[2], 
                  'row2':winList[3],
                  'row3':winList[4],
                  'col1':winList[5],
                  'col2':winList[6],
                  'col3':winList[7],
                  'col': col,
                  'row': row,
                  'symbol': symbol,
                  'game': i,
                  'win': 'win'} 
        
        training_data[count] = dic
        break
      
      
      count+=1
    
  print("game is over")
    
x = pd.DataFrame(training_data).T
x.to_csv('training_data.csv')
print(training_data)