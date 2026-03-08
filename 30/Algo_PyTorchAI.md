# 🤖 Algorithm Challenges — Challenge 3 of 3
## Teaching Your Game with PyTorch
### *From a game loop to a training loop*

---

| **Course** | **Language** | **Estimated Time** | **Total Marks** |
|---|---|---|---|
| Grade 12 Computer Science | Python 3 + Pygame + PyTorch | 1–2 Weeks | 100 marks |

---

> ### 📋 Assignment Overview
>
> You've already taught your game to **think** using Minimax (Challenge 1) and taught it to think **faster** using Alpha-Beta Pruning (Challenge 2). Now it's time to teach it to **learn**.
>
> In this challenge you will use **PyTorch** — the same library used by researchers at Google, Meta, and OpenAI — to train a neural network that learns to play your game through experience. Instead of hand-crafting rules, you will let the AI discover strategy on its own.
>
> By the end, you will have a working AI that **improves the more it plays**, and you will understand the core ideas behind modern machine learning.

---

## Table of Contents

1. [The Big Idea: Game Loop → Training Loop](#1-the-big-idea-game-loop--training-loop)
2. [Key Vocabulary](#2-key-vocabulary)
3. [Learning Goals](#3-learning-goals)
4. [Milestones & Timeline](#4-milestones--timeline)
5. [Detailed Task Requirements](#5-detailed-task-requirements)
   - [Milestone 1 — Concepts & Setup](#milestone-1--concepts--setup-15-marks)
   - [Milestone 2 — Tensors & Network Design](#milestone-2--tensors--network-design-15-marks)
   - [Milestone 3 — Training Loop](#milestone-3--training-loop-25-marks)
   - [Milestone 4 — Pygame Integration](#milestone-4--pygame-integration-30-marks)
   - [Milestone 5 — Reflection & Demo](#milestone-5--reflection--demo-15-marks)
6. [Suggested File Structure](#6-suggested-file-structure)
7. [Tips & Common Mistakes](#7-tips--common-mistakes)
8. [Evaluation Rubric](#8-evaluation-rubric)
9. [Submission Checklist](#9-submission-checklist)

---

## 1. The Big Idea: Game Loop → Training Loop

You already know the **Pygame game loop** — the heartbeat of every game you have built. A training loop works the same way: it runs over and over, each time making the AI a tiny bit better. The table below shows how the two loops map onto each other:

| 🎮 **Pygame Game Loop** | 🧠 **PyTorch Training Loop** |
|---|---|
| `while game_running:` | `for epoch in range(epochs):` |
| `handle_events()` | `forward_pass(batch)` |
| `update_game_state()` | `compute_loss()` |
| `draw_screen()` | `backward_pass()` |
| `clock.tick(60)` | `optimizer.step()` |
| `# repeats until player quits` | `# repeats until model converges` |
| `# each tick = one moment in time` | `# each epoch = one round of learning` |
| `# reacts to player input` | `# reacts to how wrong the prediction was` |

The key difference is **what happens each iteration**. In a game loop, each tick moves the game forward in time. In a training loop, each pass through the data makes the model's predictions slightly more accurate. Both loops repeat until something is **good enough** — the game ends, or the loss is low enough.

> 💡 **Think of it this way:** your Pygame game loop reacts to player input. Your training loop reacts to **how wrong the AI's prediction was**. Both loops are just "run → observe → adjust → repeat".

---

## 2. Key Vocabulary

Before writing any code, make sure you understand these ten terms. You will use them throughout the assignment.

| **Term** | **What it means** |
|---|---|
| **Tensor** | A container for numbers — like a Python list, but much faster and designed for math. A single number, a row of numbers, a grid of numbers — all tensors. |
| **Neural Network** | A chain of layers that transforms an input (e.g. the board) into an output (e.g. how good each move is). It starts random and improves through training. |
| **Forward Pass** | Feeding an input through the network to get a prediction. Like running game logic forward one step. |
| **Loss** | A number that measures how wrong the network's prediction was. Low loss = doing well. High loss = still learning. |
| **Backward Pass** | PyTorch automatically figures out how to adjust every weight in the network to reduce the loss. You just call `loss.backward()`. |
| **Optimizer** | The thing that actually updates the network's weights using the gradients computed in the backward pass. You will use Adam — a popular, reliable choice. |
| **Training Loop** | The loop that runs forward pass → compute loss → backward pass → update weights, over and over until the network learns. |
| **Episode** | One full game played from start to finish. Used to collect training data. |
| **Reward** | A score the agent receives for what it did (+1 win, −1 lose, 0 draw). The network learns to chase rewards. |
| **Model** | The neural network after training. You can save it to a file and load it back. |

---

## 3. Learning Goals

By completing this assignment, you will be able to:

- Explain what a tensor is and create one in PyTorch
- Convert a game board into a tensor that a neural network can read
- Build a simple neural network class using `torch.nn.Module`
- Write a training loop that includes forward pass, loss, backward pass, and optimizer step
- Train an AI to play your game using self-play data
- Integrate a trained PyTorch model into your Pygame game
- Compare a learning-based AI to your Minimax AI from Challenge 1

---

## 4. Milestones & Timeline

This assignment is broken into 5 milestones. Each one builds on the last. Check in with your teacher at the end of each milestone.

| **#** | **Milestone** | **Key Deliverables** | **Due** | **Marks** |
|---|---|---|---|---|
| **1** | **Concepts & Setup** | Vocab quiz, game-loop vs training-loop comparison, PyTorch install confirmed | Day 2 | **15** |
| **2** | **Tensors & Network Design** | Board-to-tensor function, neural network class, forward pass test | Day 4 | **15** |
| **3** | **Training Loop** | Working training loop, loss curve chart, model saves/loads correctly | Day 7 | **25** |
| **4** | **Pygame Integration** | Trained AI plays in your game, human vs AI mode, performance comparison | Day 9 | **30** |
| **5** | **Reflection & Demo** | Written reflection, experiment chart, live demo to teacher | Day 10 | **15** |

---

## 5. Detailed Task Requirements

---

### Milestone 1 — Concepts & Setup (15 marks)

#### Task 1.1 — Vocabulary Quiz (10 marks)

Write a definition for each of the 10 vocabulary terms from Section 2 **in your own words**. Each definition should be 2–3 sentences. Do not copy the definitions from this sheet.

---

#### Task 1.2 — Game Loop vs Training Loop (3 marks)

Create your own comparison table (you can hand-draw it or type it). List at least 5 pairs of matching concepts — one from the Pygame game loop and one from the PyTorch training loop. Then write a short paragraph (50–80 words) explaining the most important difference between the two loops in your own words.

---

#### Task 1.3 — Environment Setup (2 marks)

Install PyTorch on your machine. Then create a file called `hello_tensor.py` that does the following:

1. Creates a 1D tensor containing the numbers 1 through 5
2. Creates a 2D tensor (a 3×3 grid) filled with zeros — think of it as an empty game board
3. Prints both tensors and their shapes

Confirm PyTorch is working by running `import torch; print(torch.__version__)` and including a screenshot or copy of the output in your submission.

> 💡 **Install tip:** Run `pip install torch` in your terminal. If you have a GPU and want to use it, visit pytorch.org for the correct install command for your system. CPU-only is fine for this assignment.

---

### Milestone 2 — Tensors & Network Design (15 marks)

#### Task 2.1 — board_to_tensor() (6 marks)

A neural network cannot read your game board directly — it only understands numbers arranged in a tensor (think of it as a super-powered list). Your first job is to write a bridge function that translates whatever board object your game uses into a flat row of numbers that PyTorch can work with.

**Step 1 — Choose your encoding**

Decide what number represents each possible cell value in your game. A standard choice that works well is:

- **+1** — AI's piece is here
- **−1** — Opponent's piece is here
- **0** — Empty cell

**Step 2 — Write the function**

Here is a worked example using a 3×3 board stored as a 2D list (a list of 3 rows, each containing 3 values). Adapt this to match however your game stores its board:

```python
import torch

def board_to_tensor(board):
    # Step 1: build a flat list of numbers from the board
    flat = []
    for row in board:
        for cell in row:
            if cell == 'AI':      # replace with your game's value for the AI
                flat.append(1.0)
            elif cell == 'OPP':   # replace with your game's value for the opponent
                flat.append(-1.0)
            else:                  # empty cell
                flat.append(0.0)
    # Step 2: convert the flat list into a PyTorch tensor
    return torch.tensor(flat, dtype=torch.float32)
```

**Step 3 — Check your work: a worked example**

Suppose you have a Tic-Tac-Toe board mid-game. The board looks like this (X = AI, O = opponent, – = empty):

```python
board = [                     # visual:  X | O | –
    ['AI',  'OPP', None],    #          – | X | –
    [None,  'AI',  None],    #          O | – | –
    ['OPP', None,  None],
]

t = board_to_tensor(board)
print(t)        # expected: tensor([ 1., -1.,  0.,  0.,  1.,  0., -1.,  0.,  0.])
print(t.shape)  # expected: torch.Size([9])
```

Now adapt this to your own game. Run it on at least 3 board states — empty board, a mid-game board, and a nearly-finished board. For each one, print both the board and the resulting tensor and confirm the numbers match what you expect.

> ⚠️ **Watch out:** Your board might not be a 2D list of lists. It might be a dictionary, a 1D list, or a custom object. Look at how your existing game code reads the board, and use that same structure as your starting point. The goal is just to end up with a flat list of floats before calling `torch.tensor()`.

---

#### Task 2.2 — GameNet Neural Network Class (6 marks)

Now you will build the brain of your AI: a neural network class. If you have used OOP before (and you have — you built a game with classes!), this will feel familiar. A PyTorch network is just a class with two special parts: an `__init__` method that defines the layers, and a `forward` method that describes how data flows through them.

**Understanding the structure**

Think of the network as a pipeline. The board state (e.g. 9 numbers for Tic-Tac-Toe) goes in one end. At the other end you get one score per possible move (e.g. 9 scores — one per square). The hidden layers in between are where the "thinking" happens.

- **Input layer:** size = number of cells on your board (9 for a 3×3 grid)
- **Hidden layers:** 64 or 128 neurons each, with ReLU activation after each one
- **Output layer:** size = number of possible moves (9 for Tic-Tac-Toe). No activation here.

**Starter code to adapt**

Create a file called `model.py` and use this as your starting point. Fill in the two `???` values with the right numbers for your game:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

INPUT_SIZE  = ???   # number of cells on your board (e.g. 9 for 3x3)
OUTPUT_SIZE = ???   # number of possible moves (e.g. 9 for 3x3)

class GameNet(nn.Module):
    def __init__(self):
        super().__init__()    # always call this first when inheriting from nn.Module

        # Layer 1: takes the board and finds patterns in it
        self.fc1 = nn.Linear(INPUT_SIZE, 64)

        # Layer 2: refines those patterns further
        self.fc2 = nn.Linear(64, 64)

        # Output layer: one score per possible move — higher = better move
        self.fc3 = nn.Linear(64, OUTPUT_SIZE)

    def forward(self, x):
        # Pass the board through layer 1, then apply ReLU
        x = F.relu(self.fc1(x))

        # Pass through layer 2, then apply ReLU again
        x = F.relu(self.fc2(x))

        # Output layer — no activation, raw scores
        return self.fc3(x)
```

> 💡 **What is ReLU?** ReLU stands for Rectified Linear Unit. It is a simple rule: if the number coming in is negative, output 0; otherwise pass it through unchanged. Without ReLU (or a similar function), multiple layers would collapse into one and the network could not learn complex patterns. You do not need to understand the math — just know that you need it after every hidden layer.

**Your task**

Use the starter code above as your base. Set `INPUT_SIZE` and `OUTPUT_SIZE` to match your game. Add a comment above each layer in `__init__` explaining what it does. If your game board is larger than 3×3, consider increasing the hidden layer size to 128.

---

#### Task 2.3 — Forward Pass Test (3 marks)

Now connect the two pieces you just built: feed a board tensor through your network and check what comes out. This is called a **forward pass**. At this stage the weights are random, so the output scores will be random too — and that is completely fine. The point is just to confirm everything is wired up correctly before you start training.

**Add this test at the bottom of model.py**

```python
if __name__ == '__main__':
    # Create the network
    model = GameNet()
    print(model)   # prints a summary of all the layers

    # Make a fake empty board and convert it to a tensor
    empty_board = [[None, None, None],   # replace with your board's empty state
                   [None, None, None],
                   [None, None, None]]
    t = board_to_tensor(empty_board)

    # Run the forward pass
    output = model(t)
    print("Output scores:", output)    # e.g. tensor([ 0.23, -0.11,  0.47, ...])
    print("Output shape:", output.shape) # should be torch.Size([OUTPUT_SIZE])
```

**Confirm all three of the following before moving on:**

1. No errors occur when you run `python model.py`
2. Output shape is `torch.Size([OUTPUT_SIZE])` — one score per possible move
3. The output values are different from each other (random weights produce varied scores — this is expected)

> ⚠️ **Most common error:** If you get a shape mismatch error like "mat1 and mat2 shapes cannot be multiplied", it means your tensor size does not match `INPUT_SIZE`. Print `t.shape` before calling the model and make sure the number matches. You can reshape with `t.view(-1)` or `t.flatten()` if needed.

> ✅ **Milestone 2 complete when:** your `board_to_tensor()` correctly encodes 3 board states, your `GameNet` class is defined with 2+ hidden layers, and `python model.py` prints a valid output tensor of the correct shape with no errors.

---

### Milestone 3 — Training Loop (25 marks)

This is the core of the assignment. You will build a **training loop** that plays many games automatically, records what happened, and uses that experience to improve the network. Think of it as your AI playing thousands of practice games while you sleep.

---

#### Task 3.1 — Self-Play Data Collection (8 marks)

Before you can train the network, you need data. The strategy is simple: make the AI play many complete games and write down everything that happened. Each game is called an **episode**. For each step inside an episode you record three things: the board state before the move, which move was made, and the final reward (did the game end in a win, loss, or draw?).

**How the AI picks a move during data collection**

Early in training the network's weights are random, so its move scores are meaningless. If you always pick the highest-scoring move, the AI will get stuck repeating the same bad strategy. The fix is **epsilon-greedy exploration**: most of the time pick the network's best move, but occasionally pick a random one. This ensures the AI tries different strategies early on.

```python
import random

EPSILON = 0.2   # 20% chance of picking a random move instead of the best one

def play_episode(model, game):
    """Play one complete game. Returns a list of (board_tensor, move, reward)."""
    game.reset()          # start a fresh game — add this method to your game class
    history = []          # will hold (board_tensor, move, reward) for every AI move

    while not game.is_terminal():
        legal_moves = game.get_legal_moves()   # replace with your method name

        if game.current_player == 'AI':    # replace with how your game tracks turns
            board_t = board_to_tensor(game.board)

            # Epsilon-greedy: explore randomly EPSILON% of the time
            if random.random() < EPSILON:
                move = random.choice(legal_moves)   # random exploration
            else:
                scores = model(board_t)             # forward pass
                # Only consider legal moves — mask out illegal ones
                best_score, move = -float('inf'), None
                for m in legal_moves:
                    if scores[m].item() > best_score:  # m is an index into scores
                        best_score, move = scores[m].item(), m

            history.append((board_t, move, 0))    # reward filled in later

        else:
            move = random.choice(legal_moves)     # opponent always plays randomly

        game.make_move(move)    # apply the move — use your existing method

    # Game over — assign reward to every AI move in this episode
    reward = game.get_reward()   # return +1 win, -1 loss, 0 draw
    return [(b, m, reward) for (b, m, _) in history]
```

> 💡 **How to adapt this to your game:** You need four things from your game class: `reset()` to start a new game, `is_terminal()` to check if it's over, `get_legal_moves()` to get a list of valid move indices, and `get_reward()` to return +1/−1/0 at the end. You likely already have most of these from Challenge 1 — just rename them if needed.

---

#### Task 3.2 — Training Loop Implementation (10 marks)

Now that you can generate episodes, you need the training loop that learns from them. Every iteration of this loop is one step of the AI getting smarter. Create a file called `train.py` and use the following starter code as your base:

```python
import torch
import torch.nn as nn
from model import GameNet, board_to_tensor
from game import YourGame   # replace with your game class name

# ── Configurable settings ──────────────────────────────────────────────────
NUM_EPISODES  = 1000   # how many games to play during training
LOG_EVERY     = 50     # print progress every N episodes
LEARNING_RATE = 0.001

# ── Setup ──────────────────────────────────────────────────────────────────
model     = GameNet()
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
loss_fn   = nn.MSELoss()
game      = YourGame()   # replace with your class
loss_log  = []   # stores average loss every LOG_EVERY episodes for charting

# ── Training loop ──────────────────────────────────────────────────────────
running_loss = 0.0

for episode in range(NUM_EPISODES):
    # Step 1: play a game and collect experience
    episode_data = play_episode(model, game)

    # Step 2: learn from every move in the episode
    for board_t, move, reward in episode_data:
        optimizer.zero_grad()           # CRITICAL: reset gradients before each step
        scores    = model(board_t)      # forward pass: what did the model predict?
        predicted = scores[move]        # score given to the move that was actually played
        target    = torch.tensor([reward], dtype=torch.float32)  # what it should have been
        loss      = loss_fn(predicted, target)   # how wrong was the prediction?
        loss.backward()                 # backward pass: compute how to fix the weights
        optimizer.step()                # update the weights
        running_loss += loss.item()

    # Step 3: log progress every LOG_EVERY episodes
    if (episode + 1) % LOG_EVERY == 0:
        avg = running_loss / LOG_EVERY
        loss_log.append(avg)
        print(f"Episode {episode+1:4d} / {NUM_EPISODES}  |  avg loss: {avg:.4f}")
        running_loss = 0.0

# ── Save the model ─────────────────────────────────────────────────────────
torch.save(model.state_dict(), 'game_ai.pth')
print("Training complete. Model saved to game_ai.pth")
```

> 💡 **What does each line in the inner loop do?**
>
> **`optimizer.zero_grad()`** — clears leftover gradients from the previous step. Forgetting this is the most common training bug.
>
> **`scores[move]`** — extracts just the score for the move that was actually played. The network produced a score for every possible move; we only care about the one that happened.
>
> **`loss_fn(predicted, target)`** — MSELoss measures (predicted − target)². If the model predicted 0.8 and the reward was −1.0, the loss is (0.8−(−1.0))² = 3.24. High loss = the model was very wrong.
>
> **`loss.backward() + optimizer.step()`** — PyTorch figures out how to adjust every weight to reduce the loss, then applies those adjustments. You never need to do any of that math yourself.

**What good output looks like**

When you run `python train.py` you should see something like this in the terminal. The exact numbers will differ, but the trend should be downward:

```
Episode   50 / 1000  |  avg loss: 0.8812
Episode  100 / 1000  |  avg loss: 0.7341
Episode  150 / 1000  |  avg loss: 0.5908
Episode  200 / 1000  |  avg loss: 0.4217
...                                             <-- should keep decreasing
Training complete. Model saved to game_ai.pth
```

> ⚠️ **If your loss is not decreasing at all:** Check that (1) you are calling `optimizer.zero_grad()` before each `loss.backward()`, (2) your reward values are actually different (+1 vs −1), and (3) your `board_to_tensor()` is returning different tensors for different board states.

---

#### Task 3.3 — Loss Curve Chart (7 marks)

The `loss_log` list in your training code already has everything you need. After training finishes, add this block at the bottom of `train.py` to plot and save the chart automatically:

```python
import matplotlib.pyplot as plt

x = [i * LOG_EVERY for i in range(1, len(loss_log) + 1)]   # episode numbers
plt.figure(figsize=(8, 4))
plt.plot(x, loss_log, color='steelblue', linewidth=2)
plt.title('Training Loss Over Episodes')
plt.xlabel('Episode')
plt.ylabel('Average Loss')
plt.tight_layout()
plt.savefig('loss_curve.png')   # saves image to your project folder
plt.show()
```

Install matplotlib if needed: run `pip install matplotlib` in your terminal.

Below your chart, write 2–3 sentences answering: Does the loss go down? Is the decrease smooth or noisy? What do you think would happen if you trained for 2000 episodes instead of 1000?

> ✅ **Milestone 3 complete when:** running `python train.py` completes without errors, loss is visibly decreasing in the console output, `game_ai.pth` exists on disk, and your loss curve chart is saved and labelled.

---

### Milestone 4 — Pygame Integration (30 marks)

Your model is trained and saved. Now plug it into your Pygame game so a human can actually play against it. This milestone is about connecting the two worlds you already know: the Pygame game loop and the PyTorch network.

---

#### Task 4.1 — AI Plays in Your Game (15 marks)

**Step 1 — Load the model at startup**

At the very top of `main.py`, before the game loop starts, load the trained model once:

```python
from model import GameNet, board_to_tensor
import torch

ai_model = GameNet()
ai_model.load_state_dict(torch.load('game_ai.pth'))
ai_model.eval()   # disables dropout; makes the AI play consistently
```

**Step 2 — Write an ai_move() helper function**

Keep your game loop clean by putting all the AI decision logic in one function. This is the same logic you used during training, but now it always picks the best legal move (no random exploration):

```python
def ai_move(model, game):
    """Ask the trained model which move to make. Returns the best legal move."""
    board_t     = board_to_tensor(game.board)
    legal_moves = game.get_legal_moves()
    with torch.no_grad():                 # no need to track gradients during gameplay
        scores = model(board_t)
    # Pick the legal move with the highest score
    return max(legal_moves, key=lambda m: scores[m].item())
```

**Step 3 — Call ai_move() inside your game loop**

Find where your game loop handles turns and add the AI branch. Here is a worked example showing the key structure — adapt the variable names to match your own game:

```python
# ── Inside your main game loop ─────────────────────────────────────────────
if not game.is_terminal():
    if game.current_player == 'HUMAN':
        # Handle mouse clicks / keyboard input as before
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                move = get_move_from_click(event.pos)   # your existing click handler
                if move in game.get_legal_moves():
                    game.make_move(move)
    else:  # AI's turn
        pygame.time.wait(400)             # small delay so the AI doesn't feel instant
        move = ai_move(ai_model, game)    # ask the network
        game.make_move(move)
```

**Step 4 — Draw the turn indicator**

In your draw function, show whose turn it is. Add something like this near the top of the screen:

```python
font  = pygame.font.SysFont('Arial', 24)
label = 'Your Turn' if game.current_player == 'HUMAN' else 'AI Thinking...'
screen.blit(font.render(label, True, (30, 30, 30)), (10, 10))
```

> ⚠️ **Important: always use `torch.no_grad()` during gameplay.** Without it, PyTorch tracks gradients every time the AI moves, which wastes memory and slows down your game. Wrapping the forward pass in `with torch.no_grad():` fixes this. It is already included in the `ai_move()` function above.

---

#### Task 4.2 — Performance Comparison (10 marks)

How much better is your trained AI than pure random luck? Create a new file called `benchmark.py` and use this starter code to run 50 automated games of trained AI vs random:

```python
import random, torch
from model import GameNet, board_to_tensor
from game import YourGame

def benchmark(model, num_games=50):
    wins, losses, draws = 0, 0, 0
    game = YourGame()
    for _ in range(num_games):
        game.reset()
        while not game.is_terminal():
            if game.current_player == 'AI':
                move = ai_move(model, game)              # trained AI
            else:
                move = random.choice(game.get_legal_moves())   # random opponent
            game.make_move(move)
        r = game.get_reward()
        if   r ==  1: wins   += 1
        elif r == -1: losses += 1
        else:         draws  += 1
    print(f"Results over {num_games} games:  Wins: {wins}  Losses: {losses}  Draws: {draws}")
    print(f"Win rate: {wins / num_games * 100:.1f}%")

if __name__ == '__main__':
    model = GameNet()
    model.load_state_dict(torch.load('game_ai.pth'))
    model.eval()
    benchmark(model, num_games=50)
```

**Example output from benchmark.py**

```
Results over 50 games:  Wins: 38  Losses: 7  Draws: 5
Win rate: 76.0%
```

Once you have your results, write a short note (100–150 words) comparing your trained AI's win rate to how your Minimax AI from Challenge 1 would perform. Consider: which AI is easier to build? Which is stronger? Which makes more sense for a simple game vs a complex one?

---

#### Task 4.3 — Polish & UX (5 marks)

Before your demo, add these three finishing touches to `main.py`:

**1. AI difficulty toggle**

Add a boolean variable `use_trained_ai = True` at the top of your file. When `True` the AI uses the trained model; when `False` it picks a random move. Let the player toggle this by pressing the `T` key:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_t:
        use_trained_ai = not use_trained_ai   # flip between trained and random
```

**2. Game Over screen with restart**

When `game.is_terminal()` is True, draw a Game Over overlay showing the winner. Listen for the `R` key to restart:

```python
if game.is_terminal():
    result = game.get_reward()   # 1, -1, or 0
    msg = 'AI Wins!' if result == 1 else ('You Win!' if result == -1 else 'Draw!')
    screen.blit(big_font.render(msg, True, (200, 0, 0)), (WIDTH//2 - 80, HEIGHT//2))
    screen.blit(font.render('Press R to restart', True, (80,80,80)), (WIDTH//2-90, HEIGHT//2+40))
    if keys[pygame.K_r]:
        game.reset()
```

**3. End-to-end test**

Play at least one complete game yourself against the trained AI and one against the random AI. Make sure the game runs from launch all the way through to the Game Over screen without any crashes or error messages. Fix anything that breaks before your demo.

> ✅ **Milestone 4 complete when:** the trained AI plays in your Pygame game without errors, the Game Over screen appears correctly, the difficulty toggle works, and your benchmark results are printed and saved.

---

### Milestone 5 — Reflection & Demo (15 marks)

#### Task 5.1 — Written Reflection (8 marks)

Write a reflection of 300–400 words addressing all four of the following prompts:

- **What did the AI learn?** Describe a specific moment in testing where the AI made a move that surprised you. What did it do, and why was it a smart move?
- **Where does it fail?** Identify a specific type of situation where your trained AI plays poorly. Why do you think it struggles there?
- **Minimax vs Machine Learning:** In Challenge 1, you built an AI that reasons logically. In this challenge, you built an AI that learns from experience. What are the trade-offs? When would you prefer one over the other?
- **What would you improve?** Name one concrete change that would make your trained AI stronger. Explain why you think it would help.

---

#### Task 5.2 — Training Experiment Chart (4 marks)

Create a chart showing one of the following (your choice):

- Loss over training episodes (from your training loop in Milestone 3)
- Win rate against the random agent, measured every 100 episodes during training

Label your chart clearly and write 2–3 sentences describing the trend.

---

#### Task 5.3 — Live Demo (3 marks)

Demo your game to your teacher. You should be ready to:

- Run your game and play one full round against your trained AI
- Explain in plain language what happens during a forward pass
- Explain what the loss measures, and why it should decrease over training

---

## 6. Suggested File Structure

Keep your project organised using this layout:

```
your_game/
    ├── main.py          # Pygame loop, event handling, rendering
    ├── game.py          # Board state, make_move(), is_terminal()
    ├── model.py         # GameNet class, board_to_tensor()
    ├── train.py         # Training loop, self-play, save model
    ├── benchmark.py     # benchmark() function, win-rate stats
    ├── game_ai.pth      # Saved model weights (after training)
    ├── hello_tensor.py  # M1 setup script
    └── reflection.pdf   # Written reflection and charts
```

---

## 7. Tips & Common Mistakes

> ⚠️ **Common Mistakes to Avoid**
>
> - **Tensor shape mismatch:** The #1 beginner error. Always print `.shape` before passing tensors to your network. Input layer size must exactly match.
> - **Not calling `model.eval()`:** During gameplay (not training), call `model.eval()` after loading. This disables dropout layers and makes predictions deterministic.
> - **Choosing illegal moves:** The network scores all moves, including occupied ones. Always filter the output to only consider legal moves before picking the best.
> - **Training for too few episodes:** 500 is a minimum. If your loss is still high, try 1000 or 2000. More self-play data = better learning.
> - **Forgetting to zero gradients:** Call `optimizer.zero_grad()` before each `loss.backward()` — otherwise gradients from previous steps accumulate and corrupt training.
> - **Expecting instant improvement:** Early in training, the AI will play terribly. That's normal. Trust the loss curve — if it's going down, the AI is learning.

> 📚 **Recommended Resources**
>
> - PyTorch official tutorials — [pytorch.org/tutorials](https://pytorch.org/tutorials) — especially "60 Minute Blitz"
> - 3Blue1Brown — "Neural Networks" series (YouTube) — best visual explanation of how networks learn
> - Sentdex — "PyTorch" playlist (YouTube) — hands-on, beginner-friendly coding walkthroughs
> - PyTorch docs: `torch.nn.Module`, `torch.nn.Linear`, `torch.optim.Adam` — all at [pytorch.org/docs](https://pytorch.org/docs)
> - Matplotlib docs: [matplotlib.org](https://matplotlib.org) — for plotting your loss curve

---

## 8. Evaluation Rubric

| **Task** | **Marking Criteria** | **Out of** | **Score** |
|---|---|---|---|
| **MILESTONE 1 — Concepts & Setup (15 marks)** | | | |
| **1.1** — Vocabulary Quiz (10 terms × 1 mark) | | **10** | ___ |
| → | Each of the 10 terms defined in own words, clearly and accurately — 1 mark each | 10 | ___ |
| **1.2** — Game-Loop vs Training-Loop Comparison | | **3** | ___ |
| → | At least 5 paired comparisons identified (e.g. event vs loss, tick vs epoch) | 2 | ___ |
| → | Explanation is written in student's own words, not just copied code | 1 | ___ |
| **1.3** — Environment Setup | | **2** | ___ |
| → | PyTorch successfully installed; screenshot or output of version check shown | 1 | ___ |
| → | `hello_tensor.py` creates a tensor, prints its shape, and runs without error | 1 | ___ |
| **MILESTONE 2 — Tensors & Network Design (15 marks)** | | | |
| **2.1** — board_to_tensor() Function | | **6** | ___ |
| → | Function accepts a board state and returns a PyTorch tensor | 2 | ___ |
| → | Tensor correctly encodes player 1, player 2, and empty squares as distinct numbers | 2 | ___ |
| → | Tested on at least 3 different board states; output shape is correct and consistent | 2 | ___ |
| **2.2** — GameNet Neural Network Class | | **6** | ___ |
| → | Network defined as a class inheriting from `nn.Module` | 2 | ___ |
| → | Has at least 2 hidden layers with activation functions (e.g. ReLU) | 2 | ___ |
| → | Output layer size matches the number of possible moves in the game | 2 | ___ |
| **2.3** — Forward Pass Test | | **3** | ___ |
| → | Forward pass called with a sample board tensor; no errors | 1 | ___ |
| → | Output is a tensor of the correct shape (one value per possible move) | 1 | ___ |
| → | Student explains in a comment what each layer does | 1 | ___ |
| **MILESTONE 3 — Training Loop (25 marks)** | | | |
| **3.1** — Self-Play Data Collection | | **8** | ___ |
| → | Game plays out automatically (AI vs random or AI vs AI) to generate episodes | 3 | ___ |
| → | Each episode records (board_state, move_made, reward) for every step | 3 | ___ |
| → | Reward assigned correctly: +1 win, -1 loss, 0 draw (or equivalent) | 2 | ___ |
| **3.2** — Training Loop Implementation | | **10** | ___ |
| → | Loop runs for a configurable number of episodes (at least 500) | 2 | ___ |
| → | Forward pass → loss → backward pass → `optimizer.step()` all present and correct | 4 | ___ |
| → | Loss printed or logged every N episodes so progress is visible | 2 | ___ |
| → | Model saved to disk at the end of training using `torch.save()` | 2 | ___ |
| **3.3** — Loss Curve Chart | | **7** | ___ |
| → | Chart shows loss (y-axis) vs training episode or epoch (x-axis) | 2 | ___ |
| → | Chart title and both axes labelled clearly | 1 | ___ |
| → | Loss shows a general downward trend over training | 2 | ___ |
| → | Student writes 2–3 sentences explaining what the chart shows | 2 | ___ |
| **MILESTONE 4 — Pygame Integration (30 marks)** | | | |
| **4.1** — AI Plays in Your Game | | **15** | ___ |
| → | Trained model loaded from file with `torch.load()` at game startup | 2 | ___ |
| → | On AI's turn, board converted to tensor, fed to network, best legal move selected | 4 | ___ |
| → | AI never selects an illegal move (occupied square, off-board, etc.) | 3 | ___ |
| → | Human vs AI mode works end-to-end: game starts, plays, and ends correctly | 4 | ___ |
| → | Whose turn it is displayed on screen during gameplay | 2 | ___ |
| **4.2** — Performance Comparison | | **10** | ___ |
| → | Random agent implemented: picks a random legal move each turn | 2 | ___ |
| → | At least 50 automated games played: trained AI vs random agent | 3 | ___ |
| → | Win rate recorded and displayed (e.g. 'AI won 38/50 games') | 3 | ___ |
| → | Results compared to Minimax performance from Challenge 1 in a short written note | 2 | ___ |
| **4.3** — Polish & UX | | **5** | ___ |
| → | Difficulty toggle (trained model vs random) selectable before or during game | 2 | ___ |
| → | Game Over screen shows winner; player can restart without relaunching | 2 | ___ |
| → | No crashes or unhandled exceptions during a full game, start to finish | 1 | ___ |
| **MILESTONE 5 — Reflection & Demo (15 marks)** | | | |
| **5.1** — Written Reflection (300–400 words) | | **8** | ___ |
| → | Describes what the AI learned — with a specific in-game example | 2 | ___ |
| → | Identifies a genuine weakness: when does the trained AI fail? | 2 | ___ |
| → | Compares learning-based AI to Minimax: what are the trade-offs? | 2 | ___ |
| → | Suggests one concrete improvement and explains why it would help | 2 | ___ |
| **5.2** — Training Experiment Chart | | **4** | ___ |
| → | Chart shows either loss over time OR win rate over training episodes | 2 | ___ |
| → | Axes labelled; trend is visible and discussed in 2–3 sentences | 2 | ___ |
| **5.3** — Live Demo | | **3** | ___ |
| → | Game runs without errors; trained AI plays at least one full game | 1 | ___ |
| → | Student explains in plain language what a forward pass does | 1 | ___ |
| → | Student explains what the loss measures and why it should go down | 1 | ___ |
| **FINAL TOTAL** | | **/ 100** | ___ |

---

## 9. Submission Checklist

Before submitting, make sure you can check off every item below:

| | Item |
|---|---|
| **M1** | ☐ Vocabulary definitions for all 10 terms (in your own words) |
| **M1** | ☐ Game-loop vs training-loop comparison table completed |
| **M1** | ☐ PyTorch installed and `hello_tensor.py` running with no errors |
| **M2** | ☐ `board_to_tensor()` function working on at least 3 board states |
| **M2** | ☐ `GameNet` neural network class written with at least 2 hidden layers |
| **M2** | ☐ Forward pass test — network produces an output of the correct shape |
| **M3** | ☐ Training loop runs for at least 500 episodes without crashing |
| **M3** | ☐ Loss curve chart showing loss decreasing over time |
| **M3** | ☐ Model saved with `torch.save()` and loaded back with `torch.load()` |
| **M4** | ☐ Trained AI plays your game in Pygame (human vs AI mode) |
| **M4** | ☐ Win-rate comparison: random agent vs trained AI, at least 50 games |
| **M4** | ☐ AI difficulty toggle (trained model vs random) selectable in-game |
| **M5** | ☐ Written reflection (300–400 words) addressing all 4 prompts |
| **M5** | ☐ Training experiment chart (loss or win rate vs training episodes) |
| **M5** | ☐ Ready for live demo — can explain forward pass and training loop |

---

> *Good luck — and remember: you're not just writing code, you're*
>
> ***teaching a machine to learn.***
