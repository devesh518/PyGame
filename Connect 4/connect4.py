#Purpose: Create a 2 player connect 4 game
#Author: Devesh Patel
#Date: 16th November 2021

import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 250, 0)
WHITE = (255, 255, 255)
ROW_COUNT = 6
COLUMN_COUNT = 7

#Creating a board for the connect 4 game
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


#Creating a function to drop a piece at given row and column in our board. 
def drop_piece(board, row, column, piece):
    board[row][column] = piece


#Checking whether the location is valid or not
def is_valid_location(board, column):
    return board[ROW_COUNT - 1][column] == 0

#Creating a function to get the index of open row when the location is valid
def get_next_open_row(board, column):
    for i in range(ROW_COUNT):
        if board[i][column] == 0:
            return i

#Creating a function that prints the reverse of the board so that we can drop the pieces at the bottom
def print_reverse_board(board):
    print(np.flip(board, 0))

#Defining a winning move
def winning_move(board, piece):
    #Checking horizontal locations for winning move
    for i in range(COLUMN_COUNT - 3):
        for j in range(ROW_COUNT):
            if board[j][i] == piece and board[j][i + 1] == piece and board[j][i + 2] == piece and board[j][i + 3] == piece:
                return True

    #Checking Vertical locations for winning move
    for j in range(ROW_COUNT - 3):
        for i in range(COLUMN_COUNT):
            if board[j][i] == piece and board[j + 1][i] == piece and board[j + 2][i] == piece and board[j + 3][i] == piece:
                return True

    #Checking Positive Diagonals
    for j in range(ROW_COUNT - 3):
        for i in range(COLUMN_COUNT - 3):
            if board[j][i] == piece and board[j + 1][i + 1] == piece and board[j + 2][i + 2] == piece and board[j + 3][i + 3] == piece:
                return True

    #Checking Negative Diagonals
    for j in range(3, ROW_COUNT):
        for i in range(COLUMN_COUNT - 3):
            if board[j][i] == piece and board[j - 1][i + 1] == piece and board[j - 2][i + 2] == piece and board[j - 3][i + 3] == piece:
                return True

def draw_board(board):
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (i*SQUARESIZE, j*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))    
            pygame.draw.circle(screen, BLACK, (int(i*SQUARESIZE + SQUARESIZE/2), int(j*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), radius)

    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):        
            if board[j][i] == 1:
                pygame.draw.circle(screen, RED, (int(i*SQUARESIZE + SQUARESIZE/2), height - int(j*SQUARESIZE + SQUARESIZE/2)), radius)

            elif board[j][i] == 2:
                pygame.draw.circle(screen, GREEN, (int(i*SQUARESIZE + SQUARESIZE/2), height - int(j*SQUARESIZE + SQUARESIZE/2)), radius)
    pygame.display.update()    

board = create_board()
print_reverse_board(board)
game_over = False
turn = 0

#Initiating pygame for graphics
pygame.init()
SQUARESIZE = 100  #in pixels
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)
radius = int(SQUARESIZE/2 - 5)

#Creating a screen in pygame
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

#Initializing a font in pygame
font = pygame.font.SysFont('timesnewroman.ttf', 60)

#Writing the main game loop
while not game_over:             #This means that the game will keep running until someone gets 4 connected

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), radius)
            
            else:
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE / 2)), radius)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

            #print(event.pos)

            #Ask for input from Player 1
            if turn == 0:      #turn = 0 so take input from Player 1
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        print("Player 1 is the winner")
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        text = font.render("Player 1 wins!", 1, WHITE)
                        screen.blit(text, (40, 10))
                        game_over = True


            #Ask for input from Player 2
            else:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))

                
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

                    if winning_move(board, 2):
                        print("Player 2 is the winner") 
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        text = font.render("Player 2 wins!", 1, WHITE)
                        screen.blit(text, (40, 10))
                        game_over = True

            draw_board(board)
            print_reverse_board(board)

            if game_over:
                pygame.time.wait(3000) 

            turn += 1
            turn = turn % 2