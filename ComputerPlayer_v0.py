#%%
import random
from tic_tac_toe_board_and_judge import IsSpaceFree
#%%
def ComputerPlayer(Tag, Board, N=0):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, N is not used here
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
            0 <= row, col <= 2 
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if the spot is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if IsSpaceFree(Board, row, col):
            return (row, col)
        
# %%
