<!-- Grade 12 Computer Science — Algorithm Challenges -->

# 🧠 Challenge 1: The Minimax Algorithm

> **Algorithm Challenges · Challenge 1 of 3**  
> Grade 12 Computer Science · Python 3 + Pygame · 1–2 Weeks · **100 Marks**

---

| **Field** | **Value** | **Field** | **Value** |
|-----------|-----------|-----------|----------|
| **Course** | Grade 12 Computer Science | **Estimated Time** | 1–2 Weeks |
| **Language** | Python 3 + Pygame | **Total Marks** | 100 marks |

> Assignment Overview
> You have already built your own 2-player game using Pygame — now it’s time to make it think. In this challenge, you will implement the Minimax algorithm — a classic artificial intelligence technique used in two-player strategy games like Chess, Checkers, and Tic-Tac-Toe. Your AI opponent will explore possible future game states and choose moves that maximize its own advantage while minimizing yours.
> By the end of this assignment, your game will have a fully functional AI opponent that never makes a random move — it reasons.


**1. Background: How Does Minimax Work?**

Before writing any code, you need to understand the algorithm conceptually. Minimax models a game as a tree of possible future moves. At each level of the tree, players alternate turns. One player is the “Maximizer” (trying to get the highest score) and the other is the “Minimizer” (trying to get the lowest score).

### The Core Idea

Imagine you’re the Maximizer. You look at all the moves you could make, and for each one, you imagine the Minimizer responding with their best move, and so on — all the way to the end of the game. You then work backwards, choosing the path that leads to the best outcome for you, assuming your opponent also plays perfectly.

> Example: Tic-Tac-Toe
> Suppose it’s X’s turn and there are 3 empty squares. X explores all 3 moves. For each, O then explores all remaining moves. At the deepest level (terminal states), the board is scored: +10 if X wins, -10 if O wins, 0 for a draw. X picks the move with the highest minimum score. O picks the move with the lowest maximum score.


### Pseudocode

```python
def minimax(board, is_maximizing):
    if terminal state:
    return score(board)
    if is_maximizing:
    best = -infinity
    for each move in available_moves:
    make move, recurse, undo move
    best = max(best, result)
    return best
    else: # minimizing
    best = +infinity
    for each move in available_moves:
    make move, recurse, undo move
    best = min(best, result)
    return best
```

### Key Vocabulary

| **Term**            | **Meaning**                                                    |
|---------------------|----------------------------------------------------------------|
| **Game Tree**       | A tree where each node is a game state and each edge is a move |
| **Terminal State**  | A board position where the game is over (win, loss, or draw)   |
| **Heuristic Score** | A numeric value representing how good a board position is      |
| **Depth**           | How many moves ahead the algorithm looks                       |
| **Maximizer**       | The player trying to achieve the highest score (your AI)       |
| **Minimizer**       | The player trying to achieve the lowest score (the opponent)   |
| **Backtracking**    | Undoing a move after exploring it so the board stays clean     |

**2. Learning Goals**

By completing this assignment, you will be able to:

- Explain how the Minimax algorithm works conceptually and trace it on a simple game tree

- Implement a recursive Minimax function in Python

- Define a heuristic evaluation function that scores any game state numerically

- Integrate your AI into your existing Pygame game so a human can play against it

- Observe and reflect on the algorithm’s performance and limitations

- Measure search depth’s effect on AI difficulty and response time

**3. Milestones & Timeline**

This assignment is broken into 5 milestones to keep you on track. Each milestone builds on the last. Check in with your teacher at the end of each milestone.

|        |                              |                                                                         |         |           |
|--------|------------------------------|-------------------------------------------------------------------------|---------|-----------|
| **\#** | **Milestone**                | **Key Deliverables**                                                    | **Due** | **Marks** |
| **1**  | **Conceptual Understanding** | Game tree diagram, written explanation of minimax, vocabulary quiz      | Day 2   | **15**    |
| **2**  | **Heuristic Function**       | Written score function, tested on at least 5 board positions            | Day 4   | **15**    |
| **3**  | **Core Minimax**             | Working recursive minimax() function with unit tests, no Pygame yet     | Day 7   | **25**    |
| **4**  | **Pygame Integration**       | AI plays against human in your game, difficulty levels, visual feedback | Day 9   | **30**    |
| **5**  | **Reflection & Demo**        | Written reflection, live demo to teacher, depth analysis chart          | Day 10  | **15**    |

**4. Detailed Task Requirements**


### 🔵 Milestone 1 — Conceptual Understanding (15 marks)

Before writing code, make sure you deeply understand what Minimax does.


#### Task 1.1 — Draw a Game Tree (5 marks)

Draw a complete Minimax game tree for a simplified version of your game (or Tic-Tac-Toe if your game is complex). Your diagram must show:

- At least 3 levels deep (root, two ply, terminal or near-terminal nodes)

- Scores at each terminal node

- Which player is Maximizer and which is Minimizer at each level

- The backed-up scores at each internal node, and the final chosen move

**Tip:** You can draw by hand and photograph it, or use a tool like draw.io.


#### Task 1.2 — Written Explanation (5 marks)

Write a short explanation (200–300 words) answering all of the following:

- What problem does Minimax solve?

- Why does the algorithm alternate between maximizing and minimizing?

- What happens if you make the depth very large? What are the tradeoffs?

- Why is it important to “undo” a move after exploring it?


#### Task 1.3 — Vocabulary Check (5 marks)

Define each term in your own words (2–3 sentences each): game tree, terminal state, heuristic, depth, backtracking.


### 🟣 Milestone 2 — Heuristic Evaluation Function (15 marks)

The heuristic function is the heart of your AI — it assigns a numeric score to any board position so the algorithm knows what’s “good” and what’s “bad”.

```python
    Requirements for your heuristic function:
    Must return a positive number when the AI (Maximizer) is winning
    Must return a negative number when the human (Minimizer) is winning
    Must return 0 for a draw or neutral position
    Must return a large value (e.g. +1000 or -1000) for an immediate win/loss
    Should award partial credit for “nearly winning” positions (e.g. 2-in-a-row in Tic-Tac-Toe)
```


#### Task 2.1 — Design Your Heuristic (10 marks)

Write the evaluate(board) function in Python. Then test it on at least 5 different board positions. For each test, show the board state, expected score, actual score, and whether they match.


#### Task 2.2 — Justify Your Scoring (5 marks)

Write a brief justification (100–150 words) explaining your scoring choices. Why did you pick those values? What happens if a score is too small or too large?


### 🟤 Milestone 3 — Core Minimax Algorithm (25 marks)

This is the main algorithmic challenge. Implement Minimax as a standalone Python module before integrating it into Pygame.


#### Task 3.1 — Implement minimax() (15 marks)

Your function must meet all of the following requirements:

- Accept the board state, current depth, and a boolean is_maximizing flag

- Correctly return the best score for the current player using recursion

- Stop recursing when the game is over (win/loss/draw) or depth reaches 0

- Never permanently modify the board — use make_move() and undo_move()

- Return both the best score AND the best move (as a tuple)

```python
    Suggested function signature:
def minimax(board, depth, is_maximizing) -&gt; tuple[int, move]:
```


#### Task 3.2 — Unit Tests (10 marks)

Write at least 6 unit tests using Python’s built-in unittest or pytest. You must test:

- Minimax returns a winning move when one is immediately available

- Minimax blocks an opponent’s winning move

- Minimax returns 0 score for a full board draw

- Minimax works correctly at depth 1, depth 3, and depth 5

- The heuristic returns correct values for known board states

- Your make_move() / undo_move() functions leave the board unchanged


### 🔴 Milestone 4 — Pygame Integration (30 marks)

Now bring your AI to life! Integrate your minimax() function into your existing Pygame game.


#### Task 4.1 — AI Opponent (15 marks)

- When it is the AI’s turn, call minimax() to determine the best move

- The AI should never make an illegal move

- Add a small visual delay (0.3–0.8 seconds) so the AI doesn’t feel instant

- Display whose turn it is on screen (Human / AI)


#### Task 4.2 — Difficulty Levels (10 marks)

Implement at least 3 difficulty levels by changing the search depth:

|           |            |          |
|-----------|------------|----------|
| **Easy**  | **Medium** | **Hard** |
| Depth 1–2 | Depth 3–4  | Depth 5+ |

Let the player select the difficulty from a menu screen before starting the game.


#### Task 4.3 — Polish & UX (5 marks)

- Show a “Game Over” screen indicating the winner

- Allow the player to restart without closing the window

- Show the AI’s thinking time on screen (use Python’s time module)


### 🟢 Milestone 5 — Reflection & Demo (15 marks)


#### Task 5.1 — Written Reflection (8 marks)

Write a reflection of 300–400 words addressing the following:

- Describe a specific moment where the AI surprised you. What did it do, and why did it work?

- What is the biggest limitation of your current AI? What kinds of situations does it handle poorly?

- How did changing the depth affect both the AI’s skill and the game’s speed? Include the data from your timing experiment.

- If you were to improve this AI further, what would you change first and why?


#### Task 5.2 — Depth Analysis Chart (4 marks)

Measure how long minimax() takes at depths 1 through 6 (or until it takes more than 5 seconds). Record the time for each depth and create a chart (hand-drawn or digital). Describe the pattern you see. What does this tell you about the algorithm’s time complexity?


#### Task 5.3 — Live Demo (3 marks)

Demo your game to your teacher. You will be asked to play one round at each difficulty level and explain one part of your minimax code in your own words.

**5. Evaluation Rubric**

|                                                            |                                                                                            |            |            |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------|------------|
| **Task**                                                   | **Marking Criteria — What to look for**                                                    | **Out of** | **Score**  |
| **MILESTONE 1 — Conceptual Understanding (15 marks)**      |                                                                                            |            |            |
| **Task 1.1**                                               | Game Tree Diagram                                                                          | **5**      | \_\_\_     |
| →                                                          | Tree has at least 3 levels; root, intermediate, and terminal nodes all present             | **2**      | \_\_\_     |
| →                                                          | Terminal node scores are correct; backed-up values shown at internal nodes                 | **2**      | \_\_\_     |
| →                                                          | Maximizer / Minimizer labeled per level; final chosen move is indicated                    | **1**      | \_\_\_     |
| **Task 1.2**                                               | Written Explanation (200–300 words)                                                        | **5**      | \_\_\_     |
| →                                                          | Accurately explains the core problem Minimax solves (adversarial game search)              | **1**      | \_\_\_     |
| →                                                          | Correctly explains why players alternate between maximizing and minimizing                 | **1**      | \_\_\_     |
| →                                                          | Discusses tradeoffs of depth (stronger but slower); shows clear understanding              | **2**      | \_\_\_     |
| →                                                          | Explains why undoing moves is essential (board must stay clean between calls)              | **1**      | \_\_\_     |
| **Task 1.3**                                               | Vocabulary (5 terms × 1 mark each)                                                         | **5**      | \_\_\_     |
| →                                                          | game tree — accurate, in own words                                                         | **1**      | \_\_\_     |
| →                                                          | terminal state — accurate, in own words                                                    | **1**      | \_\_\_     |
| →                                                          | heuristic — accurate, in own words                                                         | **1**      | \_\_\_     |
| →                                                          | depth — accurate, in own words                                                             | **1**      | \_\_\_     |
| →                                                          | backtracking — accurate, in own words                                                      | **1**      | \_\_\_     |
| ***Milestone Subtotal***                                   |                                                                                            | **/ 15**   | **\_\_\_** |
| **MILESTONE 2 — Heuristic Evaluation Function (15 marks)** |                                                                                            |            |            |
| **Task 2.1**                                               | evaluate(board) Function + Test Cases                                                      | **10**     | \_\_\_     |
| →                                                          | Returns a large positive value (+500 or more) for an immediate AI win                      | **2**      | \_\_\_     |
| →                                                          | Returns a large negative value (−500 or less) for an immediate human win                   | **2**      | \_\_\_     |
| →                                                          | Returns 0 (or near-0) for a draw or neutral board state                                    | **1**      | \_\_\_     |
| →                                                          | Awards partial scores for intermediate positions (e.g. 2-in-a-row)                         | **2**      | \_\_\_     |
| →                                                          | At least 5 test cases shown: board state, expected score, actual score                     | **2**      | \_\_\_     |
| →                                                          | All 5 test cases pass — expected matches actual; output shown or runnable                  | **1**      | \_\_\_     |
| **Task 2.2**                                               | Heuristic Justification (100–150 words)                                                    | **5**      | \_\_\_     |
| →                                                          | Explains the reasoning behind chosen score magnitudes (why +1000, why +5, etc.)            | **2**      | \_\_\_     |
| →                                                          | Discusses effect of scores being too small or large (e.g. AI plays erratically)            | **2**      | \_\_\_     |
| →                                                          | Writing is clear, within word count, and uses correct CS vocabulary                        | **1**      | \_\_\_     |
| ***Milestone Subtotal***                                   |                                                                                            | **/ 15**   | **\_\_\_** |
| **MILESTONE 3 — Core Minimax Algorithm (25 marks)**        |                                                                                            |            |            |
| **Task 3.1**                                               | minimax() Function Implementation                                                          | **15**     | \_\_\_     |
| →                                                          | Function accepts board, depth, and is_maximizing parameters correctly                      | **1**      | \_\_\_     |
| →                                                          | Base case: returns heuristic score when is_terminal() is True                              | **3**      | \_\_\_     |
| →                                                          | Base case: returns heuristic score when depth reaches 0                                    | **2**      | \_\_\_     |
| →                                                          | Correctly maximizes score when is_maximizing is True                                       | **2**      | \_\_\_     |
| →                                                          | Correctly minimizes score when is_maximizing is False                                      | **2**      | \_\_\_     |
| →                                                          | make_move() and undo_move() used correctly; board fully restored after each call           | **3**      | \_\_\_     |
| →                                                          | Function returns a tuple of (best_score, best_move), not just a score                      | **2**      | \_\_\_     |
| **Task 3.2**                                               | Unit Tests (6 required)                                                                    | **10**     | \_\_\_     |
| →                                                          | Test: returns a winning move when one is immediately available                             | **2**      | \_\_\_     |
| →                                                          | Test: blocks the opponent’s winning move                                                   | **2**      | \_\_\_     |
| →                                                          | Test: returns 0 score for a full-board draw                                                | **1**      | \_\_\_     |
| →                                                          | Test: correct results at depth 1, depth 3, and depth 5 (1 mark per depth level)            | **3**      | \_\_\_     |
| →                                                          | Test: evaluate() returns correct values for at least 2 known board states                  | **1**      | \_\_\_     |
| →                                                          | Test: make_move() + undo_move() leaves board byte-for-byte identical                       | **1**      | \_\_\_     |
| ***Milestone Subtotal***                                   |                                                                                            | **/ 25**   | **\_\_\_** |
| **MILESTONE 4 — Pygame Integration (30 marks)**            |                                                                                            |            |            |
| **Task 4.1**                                               | AI Opponent in Game                                                                        | **15**     | \_\_\_     |
| →                                                          | AI calls minimax() on its turn and applies the returned best move                          | **4**      | \_\_\_     |
| →                                                          | AI never produces an illegal move (occupied square, off-board, etc.)                       | **3**      | \_\_\_     |
| →                                                          | Visual or timed delay of 0.3–0.8 s prevents the AI from moving instantly                   | **2**      | \_\_\_     |
| →                                                          | Turn indicator shown on screen (“Your Turn” / “AI Thinking…”)                              | **2**      | \_\_\_     |
| →                                                          | AI thinking time displayed using time.perf_counter() or equivalent                         | **2**      | \_\_\_     |
| →                                                          | Human input is blocked while the AI is calculating                                         | **2**      | \_\_\_     |
| **Task 4.2**                                               | Difficulty Levels                                                                          | **10**     | \_\_\_     |
| →                                                          | Easy mode uses depth 1–2; AI is beatable by a careful player                               | **2**      | \_\_\_     |
| →                                                          | Medium mode uses depth 3–4; AI plays reasonably well                                       | **2**      | \_\_\_     |
| →                                                          | Hard mode uses depth 5+; AI plays strongly                                                 | **2**      | \_\_\_     |
| →                                                          | Pre-game menu lets player select difficulty before starting                                | **2**      | \_\_\_     |
| →                                                          | Selected difficulty visible on screen during gameplay                                      | **2**      | \_\_\_     |
| **Task 4.3**                                               | Polish & UX                                                                                | **5**      | \_\_\_     |
| →                                                          | Game Over screen correctly identifies winner (or draw) and is clearly visible              | **2**      | \_\_\_     |
| →                                                          | Player can restart without closing and relaunching the program                             | **2**      | \_\_\_     |
| →                                                          | No crashes or unhandled exceptions during a full game, start to Game Over                  | **1**      | \_\_\_     |
| ***Milestone Subtotal***                                   |                                                                                            | **/ 30**   | **\_\_\_** |
| **MILESTONE 5 — Reflection & Demo (15 marks)**             |                                                                                            |            |            |
| **Task 5.1**                                               | Written Reflection (300–400 words)                                                         | **8**      | \_\_\_     |
| →                                                          | Describes a specific moment where AI surprised the student; explains why the move was good | **2**      | \_\_\_     |
| →                                                          | Identifies a genuine AI limitation with a specific example or scenario                     | **2**      | \_\_\_     |
| →                                                          | Analyzes effect of depth on skill and speed; references actual timing data from Task 5.2   | **2**      | \_\_\_     |
| →                                                          | Proposes a meaningful improvement (e.g. alpha-beta, better heuristic) and explains why     | **2**      | \_\_\_     |
| **Task 5.2**                                               | Depth Analysis Chart                                                                       | **4**      | \_\_\_     |
| →                                                          | Timing data collected for depths 1 through at least 5 (or until timeout ≥5 s)              | **2**      | \_\_\_     |
| →                                                          | Chart is clearly labeled (axes, title); exponential growth pattern is visible              | **1**      | \_\_\_     |
| →                                                          | Student describes the pattern and connects it to Big-O / time complexity in writing        | **1**      | \_\_\_     |
| **Task 5.3**                                               | Live Demo                                                                                  | **3**      | \_\_\_     |
| →                                                          | Game runs without errors at all three difficulty levels during demo                        | **1**      | \_\_\_     |
| →                                                          | Student can explain in plain language what minimax() does and why it works                 | **1**      | \_\_\_     |
| →                                                          | Student can point to specific lines for base case, maximizing branch, and undo logic       | **1**      | \_\_\_     |
| ***Milestone Subtotal***                                   |                                                                                            | **/ 15**   | **\_\_\_** |
| **FINAL TOTAL**                                            |                                                                                            | **/ 100**  | **\_\_\_** |

**6. Helpful Resources & Tips**

> Recommended Resources
> Sebastian Lague — “Minimax and Alpha-Beta Pruning” (YouTube) — excellent visual walkthrough
> CS50 AI — Free course covering Minimax with Python (cs50.harvard.edu/ai)
> Pygame docs: pygame.org/docs — especially the event and time modules
> Python docs: time.perf_counter() for accurate timing measurements
> realpython.com — search “Minimax Python” for step-by-step tutorials


### Common Mistakes to Avoid

- Forgetting to undo moves — always restore the board after recursing

- Using the wrong sign — make sure Maximizer maximizes and Minimizer minimizes

- No base case — always check for terminal state BEFORE recursing

- Modifying a list directly — use copy.deepcopy() if needed, or track changes manually

- Huge depth on a complex game — start with depth 2–3 and increase slowly

### Starter Code Structure

Here is a suggested file structure for your project:

> your_game/
> ├── main.py # Pygame loop, event handling, rendering
> ├── game.py # Board state, make_move(), undo_move(), is_terminal()
> ├── ai.py # minimax(), evaluate(), get_best_move()
> ├── test_ai.py # Unit tests for ai.py and game.py
> └── reflection.pdf # Written reflection and depth chart


**7. Submission Checklist**

Before submitting, make sure you can check off every item below:

|        |                                                                        |
|--------|------------------------------------------------------------------------|
| **M1** | ☐ Game tree diagram with at least 3 levels and backed-up scores        |
| **M1** | ☐ Written explanation of Minimax (200–300 words)                       |
| **M1** | ☐ Vocabulary definitions for all 5 terms                               |
| **M2** | ☐ evaluate(board) function with 5 documented test cases                |
| **M2** | ☐ Written justification of heuristic scoring (100–150 words)           |
| **M3** | ☐ minimax(board, depth, is_maximizing) function, returns (score, move) |
| **M3** | ☐ At least 6 passing unit tests                                        |
| **M4** | ☐ AI opponent works correctly in Pygame game                           |
| **M4** | ☐ Three difficulty levels selectable from a menu                       |
| **M4** | ☐ Game over screen, restart function, and AI thinking time display     |
| **M5** | ☐ Written reflection (300–400 words) addressing all 4 prompts          |
| **M5** | ☐ Depth analysis chart with timing data from depths 1–6                |
| **M5** | ☐ Ready for live demo — can explain minimax code out loud              |

---

*Grade 12 Computer Science · Algorithm Challenges · Challenge 1 of 3*
