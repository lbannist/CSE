This tutorial video should give you a head start on how to make a simple game in Pygame.

You'll need to copy 

[![Watch the video](https://img.youtube.com/vi/IL_PMGVxEUY/maxresdefault.jpg)](https://youtu.be/IL_PMGVxEUY)

### [Watch this video on YouTube](https://youtu.be/IL_PMGVxEUY)


# Starter Assets
You wil need to create your own pictures for this challenge.  
Start by creating an **assets** folder in the same place as your .py game file will exist.

It would be best to match their name with the following:
- Board.png
- O.png
- X.png
- Winning O.png
- Winning X.png

And choose a **font** of your choice.  Make sure it is in a .tff file format and place it in the assets folder.

# Starter Code
Use this code to give you a headstart

```python
import pygame, sys
 
pygame.init()
 
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]

to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

def render_board(board, ximg, oimg):



def add_XO(board, graphical_board, to_move):



def check_win(board):

```
