def draw_board(spots):
    board = (f"|{spots[0][5]}|{spots[1][5]}|{spots[2][5]}|{spots[3][5]}|{spots[4][5]}|{spots[5][5]}|{spots[6][5]}|\n"
             f"|{spots[0][4]}|{spots[1][4]}|{spots[2][4]}|{spots[3][4]}|{spots[4][4]}|{spots[5][4]}|{spots[6][4]}|\n"
             f"|{spots[0][3]}|{spots[1][3]}|{spots[2][3]}|{spots[3][3]}|{spots[4][3]}|{spots[5][3]}|{spots[6][3]}|\n"
             f"|{spots[0][2]}|{spots[1][2]}|{spots[2][2]}|{spots[3][2]}|{spots[4][2]}|{spots[5][2]}|{spots[6][2]}|\n"
             f"|{spots[0][1]}|{spots[1][1]}|{spots[2][1]}|{spots[3][1]}|{spots[4][1]}|{spots[5][1]}|{spots[6][1]}|\n"
             f"|{spots[0][0]}|{spots[1][0]}|{spots[2][0]}|{spots[3][0]}|{spots[4][0]}|{spots[5][0]}|{spots[6][0]}|\n"
             )
    print(board)
    

def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'

def check_for_win(spots, depth):
  # Handle Horizontal Cases
  draw = False
  count = 0
  for i in range(0, len(spots)):
      for j in range(0, len(spots[0])):
        if (spots[i][j] != "X" and spots[i][j] !="O"):
          count = count + 1 
  if (count == 0):
      draw = True
  if check_turn(depth) == "X":
      #horizontal check
    for i in range (0, len(spots) - 3): 
        for j in range (0, len(spots[0])):
           if (spots[i][j] == spots[i+1][j] == spots[i+2][j] == spots[i+3][j] and (spots[i][j] in {"X", "O"})):
               return "win"
       #vertical check
    for j in range (0, len(spots[0]) - 3): 
        for i in range (0, len(spots)):
           if (spots[i][j] == spots[i][j+1] == spots[i][j+2] == spots[i][j+3] and (spots[i][j] in {"X", "O"})):
               return "win"
        #diag check 1
    for j in range (0, len(spots[0]) - 3): 
        for i in range (0, len(spots) - 3):
           if (spots[i][j] == spots[i+1][j+1] == spots[i+2][j+2] == spots[i+3][j+3] and (spots[i][j] in {"X", "O"})):
               return "win"
        #diag check 2
    for j in range (3, len(spots[0])): 
        for i in range (0, len(spots) - 3):
           if (spots[i][j] == spots[i+1][j-1] == spots[i+2][j-2] == spots[i+3][j-3] and (spots[i][j] in {"X", "O"})):
               return "win"
  
  elif check_turn(depth) == "O":
     for i in range (0, len(spots) - 3): 
        for j in range (0, len(spots[0])):
           if (spots[i][j] == spots[i+1][j] == spots[i+2][j] == spots[i+3][j] and (spots[i][j] in {"X", "O"})):
               return "lose"
       #vertical check
     for j in range (0, len(spots[0]) - 3): 
        for i in range (0, len(spots)):
           if (spots[i][j] == spots[i][j+1] == spots[i][j+2] == spots[i][j+3] and (spots[i][j] in {"X", "O"})):
               return "lose"
        #diag check 1
     for j in range (0, len(spots[0]) - 3): 
        for i in range (0, len(spots) - 3):
           if (spots[i][j] == spots[i+1][j+1] == spots[i+2][j+2] == spots[i+3][j+3] and (spots[i][j] in {"X", "O"})):
               return "lose"
        #diag check 2
     for j in range (3, len(spots[0])): 
        for i in range (0, len(spots) - 3):
           if (spots[i][j] == spots[i+1][j-1] == spots[i+2][j-2] == spots[i+3][j-3] and (spots[i][j] in {"X", "O"})):
               return "lose"
  if (draw):
      return "draw"
    