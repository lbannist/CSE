# 🎯 Introduction: Tic Tac Toe

Welcome to your Tic Tac Toe assignment! This is your biggest project yet — a fully playable two-player game that runs in the terminal. It brings together *everything* you've learned: `print()`, `input()`, variables, `int()`, `str()`, `if` statements, **strings**, and now **loops**.  

This challenge assumed you have not learned about functions or lists.

## The Problem It Solves

Tic Tac Toe needs to do a lot of things: display a board, accept moves, check for a winner, and keep going until the game ends. Without loops, you'd have to copy the same "take a turn" code nine times and hope nobody needed more. Without strings, you couldn't store or update the board at all.

With loops and strings, you can write code that keeps the game going *automatically* until there's a winner or a draw:

```python
game_over = False

while not game_over:
    move = input("Player X — choose a square (1-9): ")
    # update board, check for winner...
```

One loop. Handles every turn. That's the power of combining what you know.

## Understanding the Key Ideas

| Concept | What It Does | Example |
|---|---|---|
| `list` | Stores multiple values in one variable | `board = ["1","2","3","4","5","6","7","8","9"]` |
| `list[index]` | Accesses or changes one item in a list | `board[0] = "X"` |
| `while` loop | Keeps running while a condition is true | `while not game_over:` |
| `for` loop | Repeats for each item in a sequence | `for row in rows:` |
| `and` / `or` | Combines conditions in an `if` statement | `if a == "X" and b == "X":` |
| `break` | Exits a loop immediately | `break` |

Think of it this way:
- The **board** is a list of 9 strings — either a number `"1"`–`"9"`, `"X"`, or `"O"`
- Each **turn** is one pass through the `while` loop
- **Checking for a winner** means checking every possible line with `if` statements and `and`

---

## 📋 Assignment Overview

Build a fully playable two-player Tic Tac Toe game in the terminal. Players take turns entering a square number (1–9). The game displays the board after every turn and announces the winner — or a draw — when the game ends.

**File name:** `[YourName]_TicTacToe.py`

---

## 📚 Key Learning Objectives

By completing this assignment you will:

- Store and update a game board using a **list**
- Access and change individual list items using **index notation**
- Use a `while` loop to keep the game running until it ends
- Use `if`, `elif`, and `else` to handle different outcomes each turn
- Combine multiple conditions using `and` and `or`
- Use a `for` loop to print the board in rows
- Swap between players each turn using string variables
- Write a win-checking block that covers all 8 winning lines

---

## ✅ Requirements Checklist

Your program **must** include all of the following:

- [ ] A welcome banner displayed with `print()`
- [ ] A board stored as a **list** of 9 strings (`"1"` through `"9"`)
- [ ] A function that **displays the board** in a 3×3 grid after every turn
- [ ] A `while` loop that keeps the game running until it is over
- [ ] Players alternating between `"X"` and `"O"` each turn
- [ ] An `input()` asking the current player to choose a square (1–9)
- [ ] Validation that the chosen square **hasn't already been taken**
- [ ] The board **updated** with the player's symbol after a valid move
- [ ] A win check covering **all 8 winning lines** (3 rows, 3 columns, 2 diagonals)
- [ ] A **draw** detected when all 9 squares are filled and nobody has won
- [ ] A message announcing the **winner** or a **draw** at the end
- [ ] The game **stops** after a win or draw
- [ ] Added four ⭐ Extensions (any combination)

---

## 🗺️ How to Structure Your Board

If you were to create a board using just variables, the board would be quite messy and easily mixed up.  At this point, you have not learned about lists, use the given code in this section to make your program a bit more structured.

Store the board as a list with 9 items. Index `0` is the top-left square, index `8` is the bottom-right:

```
Square numbers the player sees:    List indexes used in code:

 1 | 2 | 3                          [0] | [1] | [2]
-----------                        -------------------
 4 | 5 | 6                          [3] | [4] | [5]
-----------                        -------------------
 7 | 8 | 9                          [6] | [7] | [8]
```

So if the player types `5`, you update `board[4]` (because lists start at index 0, so square number minus 1).

```python
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
```

To display the board in rows, slice three items at a time:

```python
print(board[0] + " | " + board[1] + " | " + board[2])
print("---------")
print(board[3] + " | " + board[4] + " | " + board[5])
print("---------")
print(board[6] + " | " + board[7] + " | " + board[8])
```

---

## 📤 Expected Output Example

Here is what a complete game should look like:

```
================================
     Welcome to Tic Tac Toe!
================================
Player 1 is X  |  Player 2 is O
Take turns choosing a square (1-9).

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Player X — choose a square (1-9): 5

1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9

Player O — choose a square (1-9): 1

O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9

Player X — choose a square (1-9): 9

O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X

... (game continues) ...

Player X — choose a square (1-9): 7

O | 2 | 3
---------
4 | X | 6
---------
X | 8 | X

Player X — choose a square (1-9): 3

O | 2 | X
---------
4 | X | 6
---------
X | 8 | X

🎉 Player X wins!
Thanks for playing!
```

---

## 🧪 Testing Your Program

Play your game several times to check every outcome. Use this checklist:

| Test | How to Do It | Expected Result |
|---|---|---|
| Row win | Fill any complete row with one symbol | Winner announced |
| Column win | Fill any complete column with one symbol | Winner announced |
| Diagonal win | Fill either diagonal with one symbol | Winner announced |
| Draw | Fill all 9 squares with no winner | Draw announced |
| Already taken | Try to play a square that's already used | Error message, same player tries again |
| Board displays | Make a move | Board updates and reprints correctly |

**Before submitting, ask yourself:**
- Does the board display correctly after every single move?
- Does the game correctly detect all 8 winning lines?
- Does the game end immediately when someone wins — not continue for more turns?
- If a player picks an already-used square, do they get another chance?

---

## ⚠️ Common Mistakes to Avoid

**Forgetting that list indexes start at 0**
```python
# ❌ Player types "5" but you update the wrong square
move = int(input("Choose a square: "))
board[move] = current_player   # This updates square 6, not 5!

# ✅ Subtract 1 to convert from square number to list index
board[move - 1] = current_player
```

**Not checking if a square is already taken**
```python
# ❌ Lets players overwrite each other's moves silently
move = int(input("Choose a square: "))
board[move - 1] = current_player

# ✅ Check the square still holds its original number
if board[move - 1] == "X" or board[move - 1] == "O":
    print("That square is already taken! Try again.")
else:
    board[move - 1] = current_player
```

**Swapping players at the wrong time**
```python
# ❌ Swapping before checking for a win means the wrong player gets credit
current_player = "O" if current_player == "X" else "X"
if ... win condition ...:
    print("Player " + current_player + " wins!")  # Wrong player announced!

# ✅ Check for a win BEFORE swapping to the next player
if ... win condition ...:
    print("Player " + current_player + " wins!")
    game_over = True
else:
    current_player = "O" if current_player == "X" else "X"
```

**Checking the board display but forgetting to reprint after every move**
```python
# ❌ Only prints the board at the start — players can't see what's changed
print(board[0] + " | " + board[1] + " | " + board[2])
# ... rest of game loop with no board display

# ✅ Print the board inside the loop, after every valid move
board[move - 1] = current_player
print()
print(board[0] + " | " + board[1] + " | " + board[2])
print("---------")
print(board[3] + " | " + board[4] + " | " + board[5])
print("---------")
print(board[6] + " | " + board[7] + " | " + board[8])
```

**Missing a winning line in your win check**
There are exactly 8 winning lines. Make sure you check all of them:
```python
# Rows:      [0,1,2]  [3,4,5]  [6,7,8]
# Columns:   [0,3,6]  [1,4,7]  [2,5,8]
# Diagonals: [0,4,8]  [2,4,6]
```

---

## 🚀 Extension Challenges

Now that the main program is done and working, choose a few extension challenges. Choose enough that you have gained 4 stars.

---

### ⭐ Challenge 1 — Personalised Players
Ask for both players' names at the start and use them throughout the game instead of just "Player X" and "Player O".

*Skills used: input(), variables, string concatenation*

---

### ⭐ Challenge 2 — Input Validation
Currently, if a player types something that isn't a number (like `"hello"`), the program will crash. Use a `while` loop to keep asking until they enter a valid number between 1 and 9.

*Skills used: while loops, if statements, string comparison*

---

### ⭐⭐ Challenge 3 — Move Counter
Track how many moves have been made. Display the move count after each turn and use it to detect a draw more simply — if 9 moves have been made and nobody has won, it's a draw.

*Skills used: variables, arithmetic, str(), if statements*

---

### ⭐⭐ Challenge 4 — Play Again
After the game ends, ask both players if they want to play again. If yes, reset the board and start a new game — all inside an outer `while` loop.

*Skills used: while loops, nested loops, list, if statements*

---

### ⭐⭐⭐ Challenge 5 — Win/Draw Score Tracker
Keep a running score across multiple games. Track how many times each player has won and how many draws there have been. Print the scoreboard at the end of each game.

*Skills used: variables, str(), if statements, while loops*

---

### ⭐⭐⭐ Challenge 6 — Highlight the Winning Line
When a player wins, print the board one final time but mark the three winning squares differently — for example, with lowercase `x` and `o` — so the winning line stands out visually.

*Skills used: string methods (.lower()), list indexing, if statements*

---

## 📬 Submission Checklist

Before handing in, tick every box:

- [ ] File is named `[YourName]_TicTacToe.py`
- [ ] Program runs without any errors
- [ ] Board displays correctly in a 3×3 grid after every move
- [ ] Players alternate turns correctly between X and O
- [ ] All 8 winning lines are checked
- [ ] A draw is detected when the board is full with no winner
- [ ] Playing an already-taken square shows an error and asks again
- [ ] Game ends immediately after a win or draw
- [ ] Code is neat and readable with consistent indentation
- [ ] *(Optional)* At least one extension challenge attempted
- [ ] *(Optional)* Extension challenge is clearly labelled with a comment `# Extension: ...`
