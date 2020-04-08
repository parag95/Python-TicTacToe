import sys
import math
import pygame
import numpy as np

SIDE_COUNT = 3
SCREEN_SIZE = 600
LINE_COLOR = (255, 255, 255)
YELLOW = (255, 255, 0)

def create_board():
    board = np.zeros((SIDE_COUNT, SIDE_COUNT))
    return board


def draw_board(screen, board):
    print("draw_board()")
    
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (int(SCREEN_SIZE/3), 0), (int(SCREEN_SIZE/3), SCREEN_SIZE), 7 )
    pygame.draw.line(screen, LINE_COLOR, (int(SCREEN_SIZE/3 * 2), 0), (int(SCREEN_SIZE/3 * 2), SCREEN_SIZE), 7 )
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, int(SCREEN_SIZE/3)), (SCREEN_SIZE, int(SCREEN_SIZE/3)), 7 )
    pygame.draw.line(screen, LINE_COLOR, (0, int(SCREEN_SIZE/3 * 2)), (SCREEN_SIZE, int(SCREEN_SIZE/3 * 2)), 7 )

    pygame.display.update()


def update_board(screen, board):

    # screen.blit(cross, (0 , 0))
    # screen.blit(cross, (0 , 200))

    for i in range(SIDE_COUNT):
        l = 0
        for j in range(SIDE_COUNT):
            k = 0
            if board[i][j] == 1:
                screen.blit(cross, (j * 2 * 100 + 10 , i * 2 * 100 + 10))
                print("X drawn at ", i, "  ", j)
            elif board[i][j] == 2:
                screen.blit(circle, (j * 2 * 100 + 10 , i * 2 * 100 + 10))
                print("O drawn at ",i, "  ",j )
            k += 2
        l += 2
                

def print_board(board):
    print(board[0][0] , " | ", board[0][1], " | ", board[0][2])
    print("______________________")
    print(board[1][0] , " | ", board[1][1], " | ", board[1][2])
    print("______________________")
    print(board[2][0] , " | ", board[2][1], " | ", board[2][2])


def getMousePos(pos):
    if pos[0] <= 200:
        col = 0
    elif pos[0] <= 400:
        col = 1
    else:
        col = 2
    
    if pos[1] <= 200:
        row = 0
    elif pos[1] <= 400:
        row = 1
    else:
        row = 2 

    print ("row: ", row)
    print("col: ", col)
    return (row, col)




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
    pygame.init()

    global cross
    global circle

    cross = pygame.image.load('cross.png')
    cross = pygame.transform.scale(cross, (180,180))
    circle = pygame.image.load('circle.png')
    circle = pygame.transform.scale(circle, (180,180))

    myfont = pygame.font.SysFont("monospace", 50)

    board = create_board()
    print_board(board)

    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
   
    draw_board(screen, board)
    pygame.display.update()


    turn = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                position = getMousePos(event.pos)

                if turn%2 == 0:
                    board[ position[0] ][ position[1] ] = 1
                    if winning_check(board, 1):
                        label = myfont.render("Player 1 wins!", 1, YELLOW) # 1 is the axis
                        screen.blit(label, (40, 10))
                        game_over = True
                
                if turn%2 == 1:
                    board[position[0]][position[1]] = 2
                    if winning_check(board, 2):
                        label = myfont.render("Player 2 wins!", 1, YELLOW) # 1 is the axis
                        screen.blit(label, (40, 40))
                        game_over = True
            
                print_board(board)
                update_board(screen, board)
                pygame.display.update()
                
                if game_over:
                    pygame.time.wait(3000)
                    sys.exit()
          
                turn +=1


 
main()