import numpy as np
from helpers import check_for_win 
from config import spots, turn, colticker

def get_next_open_row(spots, col):
    for row in range(0, len(spots[0])):
        if spots[col][row] == "-":
            return row

MAX_DEPTH = 5
def bestMove():
    bestScore = -np.Infinity
    move = -1
    for col in range(len(spots)):
         if (spots[col][5] == "-"):
            row = get_next_open_row(spots, col)
            spots[col][row] = "O"
            score = miniMax(spots, turn - 1, False)
            spots[col][row] = "-"
            if (score > bestScore):
                bestScore = score
                move = col
    if move != -1:
      row = get_next_open_row(spots, move)
      spots[move][row] = "O"
      colticker[move] += 1
    else:
    # Handle the case where no valid move was found
      raise ValueError("No valid move found")
  
  
def evaluate_board(spots, depth):
    score = 0
    if (depth % 2 == 1):
     for i in range(len(spots[0])):
        row_array = []
        for j in range(len(spots)):
            row_array.append(spots[j][i])
        for c in range(len(spots) - 3):
            window = row_array[c:c+4]
            if window.count("O") == 4:
                score -= 10
            elif window.count("O") == 3 and window.count("-") == 1:
                score -= 1
            elif window.count("X") == 4:
                score += 10
            elif window.count("X") == 3 and window.count("-") == 1:
                score += 1
     for i in range(len(spots)):
        col_array = []
        for j in range(len(spots[0])):
            col_array.append(spots[i][j])
        for c in range(len(spots[0]) - 3):
            window = col_array[c:c+4]
            if window.count("O") == 4:
                score -= 10
            elif window.count("O") == 3 and window.count("-") == 1:
                score -= 1
            elif window.count("X") == 4:
                score += 10
            elif window.count("X") == 3 and window.count("-") == 1:
                score += 1
     result = -(score / 1000)
     return result
    elif (depth % 2 == 0):
     for i in range(len(spots[0])):
        row_array = []
        for j in range(len(spots)):
            row_array.append(spots[j][i])
        for c in range(len(spots) - 3):
            window = row_array[c:c+4]
            if window.count("O") == 4:
                score += 10
            elif window.count("O") == 3 and window.count("-") == 1:
                score += 1
            elif window.count("X") == 4:
                score -= 10
            elif window.count("X") == 3 and window.count("-") == 1:
                score -= 1
     for i in range(len(spots)):
        col_array = []
        for j in range(len(spots[0])):
            col_array.append(spots[i][j])
        for c in range(len(spots[0]) - 3):
            window = col_array[c:c+4]
            if window.count("O") == 4:
                score += 10
            elif window.count("O") == 3 and window.count("-") == 1:
                score += 1
            elif window.count("X") == 4:
                score -= 10
            elif window.count("X") == 3 and window.count("-") == 1:
                score -= 1
     result = (score / 100)
     return result
            
            
  
  
   
def miniMax(spots, depth, isMaximizing):
    result = check_for_win(spots, depth)
    if (result == "win"):
        return -10
    if (result == "draw"):
        return 0
    if (result == "lose"):
        return 10
    if depth >= MAX_DEPTH:
        return evaluate_board(spots, depth)
    if (isMaximizing):
        bestScore = -np.Infinity
        for col in range(len(spots)):
            if spots[col][5] == "-":
                row = get_next_open_row(spots, col)
                spots[col][row] = "O"
                score = miniMax(spots, depth + 1, False)
                spots[col][row] = "-"
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = np.Infinity
        for col in range(len(spots)):
            if spots[col][5] == "-":
                row = get_next_open_row(spots, col)
                spots[col][row] = "X"
                score = miniMax(spots, depth + 1, True)
                spots[col][row] = "-"
                bestScore = min(score, bestScore)
        return bestScore
    