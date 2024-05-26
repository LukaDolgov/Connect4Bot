import os, time
from config import spots, turn, colticker
from bot import bestMove
from helpers import draw_board, check_turn, check_for_win
playing = True
complete = False
prev_turn = 0
while playing:
    os.system('cls' if os.name == 'nt' else 'cls')
    draw_board(spots)

    if check_turn(turn) == "X":
        # If an invalid turn occurred, let the player know
        if prev_turn == turn:
            print("Invalid spot selected, please pick another.")
        prev_turn = turn
        print("Player's turn: Pick your collumn (+x direction is increasing col number) or press q to quit")
        choiceRow = int(input()) - 1
        if choiceRow == 'q':
            playing = False
        elif ((choiceRow) <= len(spots) - 1 and colticker[choiceRow] < 6):
           if not spots[choiceRow][colticker[choiceRow]] in {"X", "O"}:
                  spots[(choiceRow)][colticker[choiceRow]] = check_turn(turn)
                  colticker[choiceRow] += 1
                  if check_for_win(spots, turn) == "win" or check_for_win(spots, turn) == "lose":
                    playing, complete = False, True
                    turn = turn - 1
                  elif check_for_win(spots, turn) == "draw":
                       playing, complete = False, False
                  turn += 1
         
    elif check_turn(turn) == "O":
        print("Bot is Calculating...")
        time.sleep(.3)
        bestMove()
        if check_for_win(spots, turn) == "win" or check_for_win(spots, turn) == "lose":
            playing, complete = False, True
            turn = turn - 1
        elif check_for_win(spots, turn) == "draw":
            playing, complete = False, True
        turn += 1


# Update the board one last time. 

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# If there was a winner, say who won
if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("BOT Wins! You really need to sharpen your skills.")
else: 
  # Tie Game
  print("No winner, which is expected unless you are really dumb and lose")
  
print("Thanks for playing!") 