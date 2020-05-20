from IPython.display import clear_output
import random

game_ended = False

def choose_first():
    return random.randint(1, 2)

def display_board(board):
  print(board[6] + "  |  " + board[7] + "  |  " + board[8])
  print("-------------")
  print(board[3] + "  |  " + board[4] + "  |  " + board[5])
  print("-------------")
  print(board[0] + "  |  " + board[1] + "  |  " + board[2])

def player_input():
  valid = False
    
  while not valid:
    player1 = input("Player 1, please pick a marker 'X' or 'O'").upper()
    if (player1 == 'X' or player1 == 'O'):
      valid = True
            
    if player1 == 'X':
      player2 = 'O'
    else:
      player2 = 'X'

    return(player1, player2)    
    print(f"Player 1 is {player1}")
    print(f"Player 2 is {player2}")

def place_marker(board, marker, position):
  index = int(position) - 1
  board[index] = marker

def win_check(board, mark):

  #Indexes of the Possible ways and order to win
  winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8], [0,4,8],[2,4,6]]
    
  #Index values of the marks.
  positions = []
  print(len(board))
  #Find all the indexes where the mark matches

  index = 0

  for x in board:
    # print(mark == x)
    if mark == x:
      positions.append(index)
    index += 1
    # print(f"{x} was compared to {mark}")
            
  print(positions)
            
  #Compare those marks with the winning combinations
    
  #Checks if there are more than 2 values so that it matches with the possible winning combinations.
  if (len(positions) < 3):
    print(f"No winning combinations because, there are {len(positions)} instances, you need 3!")
    return
    
    #Compare each winning combination to the user's marks positions
    
    #Go through all the winning combinations
  winning_combo = []
  has_won = False
    
  for x in winning_combinations:
    count = 0
#         if positions[0] in x and positions[1] in x and positions[2] in x:
#             winning_combo = x

    for i in positions:
      if i in x:
#                 print(f"{i} was found in {x}")
        count += 1
        if count >= 3:
#                 print(f"There is a winning combination in {x} because there are 3 matches in the positions {positions}")
          has_won = True
          winning_combo = x
                
#         print(f"I counted {count} in the {x} winning combo")
#         print(f"{positions[0]}, {positions[1]}, and {positions[2]}, to the winning combo of {x}")
#         print(f"The Winning Combo is {winning_combo}")

  game_ended = False

  if has_won:
    print(f"The player with the {mark} has won! With the winning positions at {winning_combo}")
    game_ended = True

  if full_board_check(board) and not has_won:
    print("There are no more available spaces! It is a TIE!!!!")
    game_ended = True
  

  return game_ended

def choose_first():
  return random.randint(1, 2)

def space_check(board, position):
  pos = int(position)
  index = pos-1
  return not board[index] == 'X' and not board[index] == 'O'

def full_board_check(board):
  return not '$' in board

def player_choice(board, marker):
  complete = False
    
  while not complete:
    
    choice = input("Please enter the desired position.")
        
    if space_check(board, choice):
      complete = True
      print(f"The position {choice} is available!")
      place_marker(board, marker, choice)

def replay():
  choice = input("Would you like to play again? Yes or No").lower()
  return choice == "yes"

def clearBoard(x):
  print('\n'*x)

def play_game():
  #Creates a variable for both player 1 and player based on the input
  player_symbols = player_input()
  p1 = player_symbols[0]
  p2 = player_symbols[1]

  print(f"Player 1 is {p1} and Player 2 is {p2}")  
  print("Let's get started!!")

  game_board = ['$','$','$','$','$','$','$','$','$']

  game_loop = True

  p2_turn = False
  p1_turn = False

  if choose_first() == 1:
    p1_turn = True
  else:
    p2_turn = True

  z = False

  while game_loop:
    

    #Player 1 input 
    if p1_turn:
      clearBoard(1)
          
          
      display_board(game_board)
      print("Player 1!")
          
      player_choice(game_board, p1)
          
      p2_turn = True
      p1_turn = False
          
      win_check(game_board, p1)
        
    #Player 2 input
    if p2_turn:
      clearBoard(1)
          
      display_board(game_board)
      print("Player 2!")
          
      player_choice(game_board, p2)
          
      p2_turn = False
      p1_turn = True

      z = win_check(game_board, p2)  

    print(f"z is {z}")
    if z:
      display_board(game_board)
      break

    # print(f"{game_ended} and {game_loop}")
  
  x = replay()
  if x:
    play_game()
  else:
    print("Thank you for playing!")

play_game()
