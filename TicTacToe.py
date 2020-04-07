import sys
import math
import pygame
import numpy as np

SIDE_COUNT = 3


def create_board():
    board = np.zeros((SIDE_COUNT, SIDE_COUNT))
    return board


def print_board(board):
    print(board[0][0] , " | ", board[0][1], " | ", board[0][2])
    print("______________________")
    print(board[1][0] , " | ", board[1][1], " | ", board[0][2])
    print("______________________")
    print(board[2][0] , " | ", board[2][1], " | ", board[2][2])
    
def winning_check(board, piece):
    for i in range(SIDE_COUNT):
            if board[i][0] == piece and board[i][1] == piece and board[i][2] == piece:
                return True
            if board[0][i] == piece and board[1][i] == piece and board[2][i] == piece:
                return True     
    if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
        return True     
    if board[2][0] == piece and board[1][1] == piece and board[0][2] == piece:
        return True
 

def main():
    board = create_board()
    print_board(board)
    
    turn = 0
    game_over = False

    while not game_over:
        #Player 1
        if turn%2 == 0:
            row = int(input("Player 1 choose row (0-2) : "))
            col = int(input("Player 1 choose column (0-2) : "))
            board[row][col] = 1

            if winning_check(board, 1):
                print("player 1 wins")
                game_over = True

        if turn%2 == 1:
            row = int(input("Player 2 choose row (0-2) : "))
            col = int(input("Player 2 choose column (0-2) : "))
            board[row][col] = 2
            

            if winning_check(board, 2):
                print("player 2 wins")
                game_over = True
        
        if game_over:
            sys.exit(0
            )

        print_board(board)
        turn +=1



main()