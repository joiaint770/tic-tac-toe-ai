#%%
import random
import copy
from tic_tac_toe_board_and_judge import (IsBoardEmpty, IsSpaceFree, Judge)
#%%
def ComputerPlayer(Tag, Board, N=1):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, N is not used here
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
            0 <= row, col <= 2 
    Description:
        ComputerPlayer will think 1 step ahead
    Attention:
        Board is NOT modified in this function
    '''
    opponent_tag = 'O' if Tag == 'X' else 'X'
    
    # First, check for a winning move
    for i in range(3):
        for j in range(3):
            if IsSpaceFree(Board, i, j):
                Board_copy = copy.deepcopy(Board)
                Board_copy[i][j] = Tag
                if Judge(Board_copy) == (1 if Tag == 'X' else 2):
                    return (i, j)  # Take the winning move
    
    # Second, check for a blocking move
    for i in range(3):
        for j in range(3):
            if IsSpaceFree(Board, i, j):
                Board_copy = copy.deepcopy(Board)
                Board_copy[i][j] = opponent_tag
                if Judge(Board_copy) == (1 if opponent_tag == 'X' else 2):
                    return (i, j)  # Block the opponent

    # If no winning or blocking move, select a random empty space
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if IsSpaceFree(Board, row, col):
            return (row, col)
# %%
