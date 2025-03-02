import random
import copy
from tic_tac_toe_board_and_judge import (IsBoardEmpty, IsSpaceFree, Judge)
#%%
def ComputerPlayer(Tag, Board, N):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, N >= 2
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
            0 <= row, col <= 2 
    Description:
        ComputerPlayer will think N step ahead
    Attention:
        Board is NOT modified in this function
    '''
    def minimax(board, depth, is_maximizing):
        score = Judge(board)
        if Tag == 'X':

            if score == 1:  # X wins
                return 1, None
            elif score == 2:  # O wins
                return -1, None
        else:  # Tie
            if score == 2:
                return 1, None
            elif score == 1:
                return -1, None
        if score == 3:
            return 0, None
        if depth == 0:
            return 0, None
        
        
        if is_maximizing:
            best_score = -float('inf') 
            best_move = None
            for i in range(3):
                for j in range(3):
                    if IsSpaceFree(board, i, j):
                        board[i][j] = Tag
                        score, _ = minimax(board, depth - 1, not is_maximizing)
                        board[i][j] = ' '
                        if score == 1:
                            return score, (i,j)
                        
                        if score> best_score:
                            best_score = score
                            best_move = (i,j)
            return best_score, best_move
        else:

            best_move = None
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if IsSpaceFree(Board, i, j):
                        Board[i][j] = 'O' if Tag == 'X' else 'X'
                        score, _ = minimax(Board, depth - 1, True)
                        Board[i][j] = ' '
                        if score == -1 :
                            return score, (i, j)
                        
                        if score < best_score:
                            best_score = score
                            best_move = (i,j)
            return best_score, best_move
        
    score,ComputerPlayerChoice = minimax(Board, N, True)
    return ComputerPlayerChoice
# %%
