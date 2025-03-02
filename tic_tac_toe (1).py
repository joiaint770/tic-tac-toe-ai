"""
Course: Python Programming
"""
#%%
def author():
    return None
#%%
import random
import copy
# %% import every function in that module
from tic_tac_toe_board_and_judge import *
from tic_tac_toe_board_and_judge import (DrawBoard, UpdateBoard, 
                                         IsSpaceFree, Judge)
#%%
def HumanPlayer(Tag, Board, N=0):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N is a dumpy input
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
            0 <= row, col <= 2 
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            # Ensure row and col are within valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Please choose a row and column between 0 and 2.")
            # Check if the chosen space is free
            elif not IsSpaceFree(Board, row, col):
                print("That space is already occupied. Please choose another.")
            else:
                return (row, col)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    #%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    if Outcome == 1:
        print(f"PlayerX ({NameX}, X) wins!")
    elif Outcome == 2:
        print(f"PlayerO ({NameO}, O) wins!")
    elif Outcome == 3:
        print("It's a tie!")
    else:
        print("The game is still in progress.")
    #%% read but do not modify this function
def Which_Player_goes_first(ComputerPlayer, HumanPlayer):
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")        
        PlayerX = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Wellcome to Tic Tac Toe Game")
    N=input("Set the steps for ComputerPlayer so that it could think N steps ahead: N=")
    try:
        N = int(N)
        if N < 0:
            print('N < 0, set it to 0')
            N=0
    except:
        print('invalid input, set N to 0')
        N = 0
    #select ComputerPlayer
    if N == 0:
        from ComputerPlayer_v0 import ComputerPlayer
    elif N == 1:
        from ComputerPlayer_v1 import ComputerPlayer    
    else:
        from ComputerPlayer_v2 import ComputerPlayer
    #an empty board
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first(ComputerPlayer, HumanPlayer)
    # get the name of each function object
    # NameX and NameO are two strings, which could be 
    #   (1) 'ComputerPlayer' and 'HumanPlayer'    
    #   (2) 'HumanPlayer' and 'ComputerPlayer'
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # while ???:
    # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board, N)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get a choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    while True:
        ChoiceX = PlayerX('X', Board, N)
        UpdateBoard(Board, 'X', ChoiceX)
        DrawBoard(Board)
        Outcome = Judge(Board)
        ShowOutcome(Outcome, NameX, NameO)
        if Outcome in [1, 2, 3]:  # win or tie
            break

        ChoiceO = PlayerO('O', Board, N)
        UpdateBoard(Board, 'O', ChoiceO)
        DrawBoard(Board)
        Outcome = Judge(Board)
        ShowOutcome(Outcome, NameX, NameO)
        if Outcome in [1, 2, 3]:  # win or tie
            break
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()

# %%
