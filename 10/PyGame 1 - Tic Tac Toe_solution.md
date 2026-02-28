# 🎯 Introduction: Pygame Tic Tac Toe

Welcome to your Pygame Tic Tac Toe challenge! This project takes the terminal game you've already built and transforms it into a **fully graphical, mouse-driven game** running in its own window. You'll be following along with a walkthrough video to guide you through the new concepts step by step.

This is your first experience with a **game library** — Pygame. You won't need to understand every line of code straight away. The goal is to follow along, get the game working, and start building an instinct for how graphical programs are structured differently from terminal ones.

## The Problem It Solves

Terminal games work, but they're text-only and clunky to interact with. Real games need:
- A **window** with graphics instead of printed text
- **Mouse clicks** instead of keyboard input
- **Images** that update visually on screen in real time

Pygame handles all of that for you — you just tell it *what* to draw and *when*.

## How a Pygame Program Is Different

In a terminal program, code runs top to bottom and stops. Pygame programs run in a **game loop** — a `while` loop that runs dozens of times per second, constantly checking for input and redrawing the screen:

```python
# Terminal program — runs once, then stops
print("Your move:")
move = input()

# Pygame program — runs forever until you quit
while True:
    for event in pygame.event.get():       # Check for mouse clicks, key presses, etc.
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()                # Redraw the screen
```

## Understanding the Key Ideas

| Concept | What It Does | Example |
|---|---|---|
| `pygame.init()` | Starts up all Pygame systems | Called once at the top |
| `SCREEN.blit(image, (x, y))` | Draws an image at a position on screen | `SCREEN.blit(X_IMG, (100, 100))` |
| `pygame.event.get()` | Gets a list of things that just happened | Mouse clicks, key presses, window closed |
| `pygame.mouse.get_pos()` | Returns the `(x, y)` position of the mouse cursor | `x, y = pygame.mouse.get_pos()` |
| `pygame.display.update()` | Pushes your drawings onto the actual screen | Called once per loop |
| `graphical_board` | A 3×3 nested list storing what image to draw where | Mirrors your logic `board` |

Think of it this way:
- Your **logic board** (`board`) tracks the game state with numbers, X, and O — just like before
- Your **graphical board** (`graphical_board`) stores the *image* and *position* for each piece so Pygame knows what to draw
- Every frame, Pygame reads the graphical board and draws everything in the right place

---

## 📋 Assignment Overview

Follow the walkthrough video to build a fully graphical Tic Tac Toe game using Pygame. You'll create your own assets, complete the starter functions, and build the game loop that ties everything together.

**File name:** `[YourName]_PygameTicTacToe.py`

---

## 📚 Key Learning Objectives

By completing this assignment you will:

- Set up a Pygame project with a window, background colour, and image assets
- Understand the structure of a **game loop** and why it exists
- Use `pygame.event.get()` to detect and respond to **mouse clicks**
- Use `SCREEN.blit()` to draw images at specific coordinates on screen
- Manage a **nested list** (a list of lists) to represent the 3×3 board
- Separate game **logic** (who has played where) from game **graphics** (what gets drawn)
- Complete pre-defined function stubs by working out what each one needs to do
- Load and display a custom **font** for on-screen text

---

## 🗂️ Project Structure

Before writing any code, make sure your project folder looks like this:

```
📁 Your Project Folder
│
├── 📄 [YourName]_PygameTicTacToe.py
│
└── 📁 assets
    ├── 🖼️ Board.png
    ├── 🖼️ X.png
    ├── 🖼️ O.png
    ├── 🖼️ Winning X.png
    ├── 🖼️ Winning O.png
    └── 🔤 YourFont.ttf
```

> ⚠️ **File names are case-sensitive.** If your code says `"assets/Board.png"` but your file is called `"board.png"`, it will crash. Double-check spelling and capitalisation.

---

## 💻 Starter Walkthough Video
Use this video to help you build your code.  Make sure you already have the starter code and assets made beforehand.

[![Watch the video](https://img.youtube.com/vi/IL_PMGVxEUY/maxresdefault.jpg)](https://youtu.be/IL_PMGVxEUY)

### [Watch this video on YouTube](https://youtu.be/IL_PMGVxEUY)

## 🎨 Starter Assets

You will need to create your own images for this project. Place all of them inside your `assets` folder.

**Images to create** (save as `.png`):

| File | What It Shows |
|---|---|
| `Board.png` | The empty 3×3 grid |
| `X.png` | The X piece |
| `O.png` | The O piece |
| `Winning X.png` | A highlighted X for the winning line |
| `Winning O.png` | A highlighted O for the winning line |

**Tips for your assets:**
- Keep all images the same size as each other for X and O (the board will be a different size)
- Use a transparent background (`.png` supports transparency) so pieces sit cleanly over the board
- Your font must be a `.ttf` file — find free fonts at [fonts.google.com](https://fonts.google.com) or [dafont.com](https://www.dafont.com)
- The starter code uses a window size of **900 × 900 pixels** — design your board image to fill most of that

---

## ⌨️ Starter Code

Use this as your starting point. **Do not change the parts that are already written** — your job is to complete the three function bodies and build the game loop below them.

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
    # Your code here

def add_XO(board, graphical_board, to_move):
    # Your code here

def check_win(board):
    # Your code here
```

### What Each Function Should Do

**`render_board(board, ximg, oimg)`**
Loop through the `graphical_board` and draw every X and O image that has been placed. This is called every frame so the screen always shows the current state of the game.

**`add_XO(board, graphical_board, to_move)`**
Called when the player clicks a square. Works out *which* square was clicked based on the mouse position, updates the logic `board` with `"X"` or `"O"`, and stores the image and position in `graphical_board` so `render_board` knows what to draw.

**`check_win(board)`**
Checks all 8 winning lines on the logic board. Returns `"X"` if X has won, `"O"` if O has won, or `None` if the game is still going.

---

## 📤 Expected Output Example

When your game is working correctly, you should see:

**At the start:**
```
A 900×900 window titled "Tic Tac Toe!" with your board image displayed
and a purple/lavender background (214, 201, 227) visible around the edges.
```

**During play:**
```
Clicking a square places an X or O image in that cell.
The board updates visually after every click.
Players alternate automatically.
```

**At the end:**
```
The winning line shows the highlighted Winning X.png or Winning O.png images.
A message is displayed on screen announcing the winner (or a draw).
The game stops accepting new moves.
```

---

## ✅ Requirements Checklist

Your program **must** include all of the following:

- [ ] Project folder contains an `assets` folder with all 5 images and a `.ttf` font file
- [ ] Window opens at 900×900 with the title "Tic Tac Toe!"
- [ ] Board image displays correctly on screen at the start
- [ ] `render_board()` is complete and draws all placed pieces each frame
- [ ] `add_XO()` is complete and correctly detects which square was clicked
- [ ] `check_win()` is complete and checks all 8 winning lines
- [ ] Players alternate between X and O after each valid move
- [ ] Clicking an already-occupied square does nothing
- [ ] Winning pieces display the highlighted winning image, not the regular one
- [ ] A winner or draw message is shown on screen using your chosen font
- [ ] The game stops accepting clicks after the game ends
- [ ] Closing the window exits the program cleanly

---

## 🧪 Testing Your Program

| Test | How to Do It | Expected Result |
|---|---|---|
| Window opens | Run the program | 900×900 window appears with board |
| Pieces place correctly | Click each of the 9 squares | X or O appears in the right cell |
| Players alternate | Click multiple squares in a row | X and O take turns correctly |
| Row win | Fill a complete row | Winning images shown, result displayed |
| Column win | Fill a complete column | Winning images shown, result displayed |
| Diagonal win | Fill either diagonal | Winning images shown, result displayed |
| Draw | Fill all 9 squares with no winner | Draw message displayed |
| Already taken | Click an occupied square | Nothing happens |
| Quit | Click the window's close button | Program exits without errors |

**Before submitting, ask yourself:**
- Does the board image display in the right place with the background colour visible at the edges?
- Do X and O images line up neatly inside the grid squares?
- Does the game fully stop (no more moves accepted) after a win or draw?
- Does the winning line show the special highlighted images, not the regular ones?

---

## ⚠️ Common Mistakes to Avoid

**Images not loading — wrong file path or name**
```python
# ❌ Wrong capitalisation or spelling — Python can't find the file
X_IMG = pygame.image.load("assets/x.png")

# ✅ Must exactly match the filename including capitalisation
X_IMG = pygame.image.load("assets/X.png")
```

**Forgetting to call `pygame.display.update()`**
```python
# ❌ You draw things but the screen never updates — nothing appears!
SCREEN.blit(X_IMG, (100, 100))

# ✅ Always call update() at the end of your game loop
SCREEN.blit(X_IMG, (100, 100))
pygame.display.update()
```

**Not handling the QUIT event — window freezes instead of closing**
```python
# ❌ The window becomes unresponsive because quit is never handled
while True:
    pygame.display.update()

# ✅ Always check for the QUIT event in your loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
```

**Confusing row/column order in the nested list**
```python
# ❌ board[column][row] — accessing the wrong cell
board[x][y]

# ✅ board[row][column] — row first, then column
board[y][x]
```

**Letting players click after the game has ended**
```python
# ❌ Moves still register after a winner is found
if event.type == pygame.MOUSEBUTTONDOWN:
    add_XO(board, graphical_board, to_move)

# ✅ Check if the game is still ongoing before accepting a click
if event.type == pygame.MOUSEBUTTONDOWN:
    if winner is None:
        add_XO(board, graphical_board, to_move)
```

---

## 🚀 Extension Challenges

Finished the core game? Try one or more of these to go further!

---

### ⭐ Challenge 1 — Custom Background Colour
Change `BG_COLOR` to a colour of your choice and update your assets to complement it. Try looking up **RGB colour codes** to find a combination you like.

```python
BG_COLOR = (255, 213, 128)   # warm yellow — try your own!
```

*Skills used: tuples, pygame colour values*

---

### ⭐ Challenge 2 — Display Whose Turn It Is
Use `pygame.font` to display a message like `"X's Turn"` or `"O's Turn"` at the top or bottom of the screen, updating after every move.

```python
FONT = pygame.font.Font("assets/YourFont.ttf", 48)
text = FONT.render(to_move + "'s Turn", True, (0, 0, 0))
SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
```

*Skills used: pygame.font, blit(), variables*

---

### ⭐⭐ Challenge 3 — Restart Button
After a win or draw, display a **"Play Again"** button on screen. If the player clicks it, reset the board and start a new game without restarting the program.

```python
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
to_move = "X"
winner = None
```

*Skills used: nested lists, variables, mouse position, if statements*

---

### ⭐⭐ Challenge 4 — Win/Draw Score Tracker
Keep a score across multiple rounds and display it on screen: how many times X has won, how many times O has won, and how many draws.

```python
x_wins = 0
o_wins = 0
draws = 0
```

*Skills used: variables, pygame.font, conditional logic*

---

### ⭐⭐⭐ Challenge 5 — Animated Winning Line
Instead of just swapping to the winning image, draw a line across the three winning squares that animates (grows) from one end to the other using `pygame.draw.line()`.

```python
pygame.draw.line(SCREEN, (255, 0, 0), start_pos, end_pos, 8)
```

*Skills used: pygame.draw, coordinates, loops*

---

### ⭐⭐⭐ Challenge 6 — Sound Effects
Add a sound effect when a piece is placed and a different one when the game ends. Pygame supports `.wav` and `.ogg` audio files.

```python
pygame.mixer.init()
place_sound = pygame.mixer.Sound("assets/place.wav")
place_sound.play()
```

*Skills used: pygame.mixer, file loading*

---

## 📬 Submission Checklist

Before handing in, tick every box:

- [ ] File is named `[YourName]_PygameTicTacToe.py`
- [ ] `assets` folder is included with all images and font file
- [ ] Program runs without any errors or missing file warnings
- [ ] All three functions (`render_board`, `add_XO`, `check_win`) are fully complete
- [ ] All 9 testing scenarios from the Testing section have been checked
- [ ] Winning line displays highlighted images correctly
- [ ] Winner or draw is announced on screen
- [ ] Game stops accepting moves after it ends
- [ ] Window closes cleanly using the close button
- [ ] Code is neat with comments explaining each major section
- [ ] *(Optional)* At least one extension challenge attempted
- [ ] *(Optional)* Extension challenge is clearly labelled with a comment `# Extension: ...`


Baraltech Solution - https://github.com/baraltech/Tic-Tac-Toe/tree/main
