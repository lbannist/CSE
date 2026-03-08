# 🧠 Algorithm Challenges — Challenge 2 of 3
## Alpha-Beta Pruning
### *Making your AI smarter — and faster*

---

| | |
|---|---|
| **Course** | Grade 12 Computer Science |
| **Language** | Python 3 + Pygame |
| **Estimated Time** | 1–2 Weeks |
| **Total Marks** | 100 marks |

---

## 📋 Assignment Overview

You have already built a Minimax AI that plays your game from scratch. It reasons — but it is slow. In this challenge, you will supercharge it by implementing **Alpha-Beta Pruning**: a technique that cuts away entire branches of the game tree without ever looking at them, making your AI dramatically faster without losing a single point of intelligence.

Alpha-Beta pruning can reduce the number of nodes your AI evaluates from **O(b<sup>d</sup>)** all the way down to **O(b<sup>d/2</sup>)** in ideal conditions — meaning your AI can look **twice as deep** in the same time. By the end of this assignment, you will be able to measure that speedup yourself and explain exactly why it works.

---

## 1. Background: How Does Alpha-Beta Pruning Work?

Alpha-Beta pruning is an optimization layered on top of Minimax. It keeps track of two running values during the search:

> **Alpha (α)** — The best score the Maximizer is guaranteed to achieve so far. Starts at −∞.
>
> **Beta (β)** — The best score the Minimizer is guaranteed to achieve so far. Starts at +∞.

As the algorithm explores the tree, it updates α and β. Whenever **β ≤ α**, the current branch can never affect the final decision — it is **pruned**. The algorithm immediately stops searching that subtree and moves on.

### The Core Idea

Imagine you are the Maximizer, evaluating a move that gives you a score of +7. While checking the Minimizer's responses to a different earlier move, the Minimizer already found a path that gives you only +3. There is no reason to look further — the Minimizer will never let you get to +7 from that branch. **Prune it.**

### 💡 Worked Example

> Suppose Minimax without pruning evaluates **27 leaf nodes** in a depth-3 tree. With Alpha-Beta pruning and good move ordering, the same tree might evaluate only **9 leaf nodes** — the same best move is returned, but with 67% less work. The AI did not get dumber; it just stopped wasting effort on provably irrelevant branches.

### Pseudocode

```python
def alpha_beta(board, depth, alpha, beta, is_maximizing):

    if terminal state or depth == 0:
        return evaluate(board), None

    if is_maximizing:
        best_score = -infinity
        for each move in available_moves:
            make_move(board, move)
            score, _ = alpha_beta(board, depth-1, alpha, beta, False)
            undo_move(board, move)
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
            if beta <= alpha:          # Beta cut-off
                break                  # Prune remaining siblings
        return best_score, best_move

    else:   # minimizing
        best_score = +infinity
        for each move in available_moves:
            make_move(board, move)
            score, _ = alpha_beta(board, depth-1, alpha, beta, True)
            undo_move(board, move)
            if score < best_score:
                best_score, best_move = score, move
            beta = min(beta, best_score)
            if beta <= alpha:          # Alpha cut-off
                break                  # Prune remaining siblings
        return best_score, best_move
```

### Key Vocabulary

| Term | Meaning |
|------|---------|
| **Alpha (α)** | The highest score the Maximizer can guarantee from the current path; initialised to −∞ |
| **Beta (β)** | The lowest score the Minimizer can guarantee from the current path; initialised to +∞ |
| **Cut-off / Prune** | Stopping the search of a subtree because its result cannot influence the parent node's decision |
| **Beta Cut-off** | A cut that occurs in the Maximizer's node because the score exceeds the Minimizer's upper bound |
| **Alpha Cut-off** | A cut that occurs in the Minimizer's node because the score falls below the Maximizer's lower bound |
| **Move Ordering** | Sorting available moves so the best moves are explored first, maximising the number of pruned nodes |
| **Branching Factor** | The average number of legal moves available at each node; lower effective branching factor = faster search |
| **Nodes Evaluated** | The count of board positions scored during a search; the primary measure of pruning effectiveness |

---

## 2. Learning Goals

By completing this assignment, you will be able to:

- Explain how Alpha-Beta pruning works and trace it on a game tree, identifying which nodes are cut
- Implement `alpha_beta()` in Python by extending your existing Minimax module
- Count nodes evaluated during a search and measure the pruning speedup at various depths
- Explain how move ordering affects pruning efficiency and implement at least one ordering strategy
- Integrate your optimized AI into your Pygame game and compare performance against pure Minimax
- Analyse the time complexity improvement and present your findings clearly

---

## 3. Milestones & Timeline

> Your Challenge 1 code is the starting point — **do not discard it**. Check in with your teacher at the end of each milestone.

| # | Milestone | Key Deliverables | Due | Marks |
|---|-----------|-----------------|-----|-------|
| **1** | **Conceptual Understanding** | Pruning diagram, written comparison of Minimax vs Alpha-Beta, vocabulary quiz | Day 2 | **15** |
| **2** | **Pruning Logic** | Working `alpha_beta()` function with pruning counters, tested standalone | Day 5 | **25** |
| **3** | **Performance Analysis** | Speed comparison experiment, branching factor write-up, timing charts | Day 7 | **20** |
| **4** | **Pygame Integration** | Alpha-Beta AI in full game, move-ordering toggle, pruning stats overlay | Day 9 | **25** |
| **5** | **Reflection & Demo** | Written reflection, optimization report, live demo | Day 10 | **15** |

---

## 4. Detailed Task Requirements

### Milestone 1 — Conceptual Understanding *(15 marks)*

Before modifying any code, you need a clear mental model of where and why pruning occurs.

#### Task 1.1 — Annotated Pruning Diagram *(6 marks)*

Take the same game tree you drew in Challenge 1 (or draw a new one for a 3-ply search with branching factor 3). Trace the Alpha-Beta algorithm through the tree by hand and annotate the following:

- Current values of α and β at every node that is evaluated
- Every edge or subtree that is pruned — mark it clearly with an **X** and label it as an *alpha cut-off* or *beta cut-off*
- The total node count **with** pruning vs. **without** pruning, written below the diagram

> **Tip:** Draw the full Minimax tree first, then replay Alpha-Beta on it, crossing out pruned branches as you go.

#### Task 1.2 — Written Comparison *(5 marks)*

Write a comparison of **200–300 words** addressing all of the following questions:

- What does Alpha-Beta pruning *add* to Minimax? What does it change, and what stays exactly the same?
- Why does the order in which moves are explored matter so much for pruning efficiency?
- What is the best-case and worst-case number of nodes Alpha-Beta evaluates compared to Minimax? What causes each extreme?
- Could Alpha-Beta ever return a *different* move than Minimax for the same position? Why or why not?

#### Task 1.3 — Vocabulary Check *(4 marks)*

Define each term in your own words (2–3 sentences each): **alpha cut-off**, **beta cut-off**, **move ordering**, **nodes evaluated**.

---

### Milestone 2 — Implementing Alpha-Beta Pruning *(25 marks)*

This is the core technical challenge. You will extend your existing `ai.py` module from Challenge 1.

#### Task 2.1 — Implement `alpha_beta()` *(15 marks)*

Create a new function `alpha_beta()` in your `ai.py`. Your function must meet **all** of the following requirements:

> **Function Requirements**
> - Accept parameters: `board`, `depth`, `alpha`, `beta`, `is_maximizing`
> - Return a tuple of `(best_score, best_move)`
> - Stop recursing at terminal states or `depth == 0`
> - Correctly update `alpha` in the Maximizer branch
> - Correctly update `beta` in the Minimizer branch
> - Prune (`break`) when `beta <= alpha` in both branches
> - Never permanently modify the board — use `make_move()` and `undo_move()` as in Challenge 1
> - Include a `node_count` parameter (default `[0]`) or use a mutable counter so you can track nodes evaluated

**Suggested function signature:**

```python
def alpha_beta(board, depth, alpha, beta, is_maximizing, node_count=[0]) -> tuple[int, move]:
```

> ⚠️ **Important:** Your original `minimax()` function must still work unchanged. Do not replace it — you will need both functions for the comparison experiment in Milestone 3.

#### Task 2.2 — Move Ordering *(6 marks)*

Implement a move ordering strategy to improve pruning efficiency. You must do **at least one** of the following:

- **Basic ordering (3 marks):** Sort available moves so that winning or capturing moves are explored first. Even a simple sort improves pruning significantly.
- **Advanced ordering (6 marks):** Implement a full killer move table or iterative deepening move-ordering scheme. Explain your approach in a comment block at the top of the function.

Add a boolean parameter `use_ordering=True` to `alpha_beta()` so you can turn move ordering on and off for the experiment in Milestone 3.

#### Task 2.3 — Unit Tests *(4 marks)*

Add at least **4 new tests** to your existing `test_ai.py`. You must test:

- `alpha_beta()` returns the same best move as `minimax()` for the same board and depth
- `alpha_beta()` evaluates fewer nodes than `minimax()` for the same board and depth
- Alpha cut-off is triggered: a specific board state where a beta cut-off is provably correct
- Move ordering reduces `nodes_evaluated` compared to unordered search (same board, same depth)

---

### Milestone 3 — Performance Analysis *(20 marks)*

Now that both functions exist, it is time to measure the speedup scientifically.

#### Task 3.1 — Nodes Evaluated Experiment *(10 marks)*

Run both `minimax()` and `alpha_beta()` on the same starting board position at depths 1 through 6 (or until one takes more than 10 seconds). For each depth and each function, record:

- Number of nodes evaluated
- Wall-clock time (use `time.perf_counter()`)
- The best move returned

**Required output format:**

```
Depth | Minimax Nodes | AB Nodes | Minimax Time | AB Time  | Same Move?
------+---------------+----------+--------------+----------+-----------
  1   |             9 |        9 |      0.0001s | 0.0001s  |    Yes
  2   |            81 |       17 |      0.0009s | 0.0002s  |    Yes
  3   |           729 |       42 |      0.008s  | 0.0009s  |    Yes
  ...
```

#### Task 3.2 — Timing and Nodes Charts *(6 marks)*

Create **two charts** (hand-drawn or digital) using your experiment data:

- **Chart A — Nodes Evaluated:** Plot depth on the x-axis and nodes evaluated on the y-axis for both Minimax and Alpha-Beta on the same graph. Use different colours or markers for each.
- **Chart B — Wall-Clock Time:** Same axes, but y-axis is time in seconds. Both functions on the same chart.

Both charts must have labelled axes, a title, and a legend.

#### Task 3.3 — Written Analysis *(4 marks)*

Write a short analysis of **150–200 words** interpreting your results:

- How large was the speedup at depth 4? At depth 6? Was it what you expected?
- Did your move ordering make a measurable difference? By how much did it change `nodes_evaluated`?
- If Alpha-Beta is O(b<sup>d/2</sup>) in the best case, does your data support that? Show your reasoning.
- At what depth does Alpha-Beta become impractically slow for your game? What does this suggest about a reasonable hard-mode depth?

---

### Milestone 4 — Pygame Integration *(25 marks)*

Replace your Minimax AI with Alpha-Beta in your Pygame game, and add a new developer overlay to visualize the pruning in action.

#### Task 4.1 — Replace the AI Core *(10 marks)*

- Replace all calls to `minimax()` in your game with `alpha_beta()`
- Pass initial values of `alpha = float('-inf')` and `beta = float('inf')` at the root call
- The AI must still never make an illegal move
- Add a toggle key (e.g. press **`M`**) that switches between Minimax and Alpha-Beta during gameplay so you can observe the speed difference live
- Display the name of the currently active algorithm on screen (e.g. `"AI: Alpha-Beta"`)

#### Task 4.2 — Pruning Stats Overlay *(10 marks)*

Add an on-screen stats panel that updates after every AI move. It must display:

- Number of nodes evaluated in the last move (both Minimax and Alpha-Beta side-by-side if the toggle is active)
- Time taken to compute the last move (in milliseconds)
- Current search depth
- Estimated pruning efficiency as a percentage: `(1 - ab_nodes / mm_nodes) × 100%`

**Example overlay:**

```
┌─────────────────────────┐
│  Last Move Stats        │
│  Algorithm:  Alpha-Beta │
│  Nodes:      42 (vs 729)│
│  Time:       0.9 ms     │
│  Depth:      3          │
│  Pruned:     94.2% ✓    │
└─────────────────────────┘
```

#### Task 4.3 — Difficulty Levels *(5 marks)*

Update your difficulty system from Challenge 1 to use Alpha-Beta depths. Because Alpha-Beta is faster, you can now offer a deeper Hard level:

| Easy | Medium | Hard |
|------|--------|------|
| Depth 2–3 | Depth 4–5 | Depth 6–7 |

---

### Milestone 5 — Reflection & Demo *(15 marks)*

#### Task 5.1 — Written Reflection *(8 marks)*

Write a reflection of **300–400 words** addressing all four of the following:

- Describe the biggest real-world speedup you observed. At which depth was the difference most dramatic, and why?
- Alpha-Beta always returns the same move as Minimax — but is it *guaranteed* to evaluate the same nodes? Under what conditions might two identical implementations evaluate different nodes?
- What was the most challenging part of implementing the pruning logic? Describe a bug you introduced and how you identified and fixed it.
- If your game tree was *perfectly ordered* (best moves always first), how would that change the number of nodes evaluated? What would the worst-case ordering look like?

#### Task 5.2 — Optimization Report *(4 marks)*

Write a **100–150 word** report on your move ordering implementation:

- What strategy did you implement and why?
- How much did it reduce `nodes_evaluated` at depth 4? Provide the specific numbers.
- What further ordering strategies could improve it? Name at least one and describe how it works.

#### Task 5.3 — Live Demo *(3 marks)*

Demo your game to your teacher. You will be asked to:

- Play one round with Alpha-Beta active at Hard difficulty
- Toggle to Minimax and let the AI make one move — the class will observe the stats overlay
- Explain in your own words exactly where and why a beta cut-off fires during the search

---

## 5. Evaluation Rubric

### Milestone 1 — Conceptual Understanding *(15 marks)*

| Task | Marking Criteria | Out of | Score |
|------|-----------------|--------|-------|
| **Task 1.1** | **Annotated Pruning Diagram** | **6** | ___ |
| → | Tree is at least 3 levels deep with branching factor ≥ 3; all evaluated nodes shown | 2 | ___ |
| → | Alpha and beta values correctly annotated at every visited node | 2 | ___ |
| → | Pruned subtrees clearly marked as alpha or beta cut-offs; total node counts correct | 2 | ___ |
| **Task 1.2** | **Written Comparison (200–300 words)** | **5** | ___ |
| → | Accurately explains what Alpha-Beta adds to Minimax and what is unchanged | 1 | ___ |
| → | Correctly explains why move ordering affects pruning efficiency | 1 | ___ |
| → | States the O(b^(d/2)) best case and O(b^d) worst case with explanation of each | 2 | ___ |
| → | Correctly answers whether Alpha-Beta can ever return a different move than Minimax | 1 | ___ |
| **Task 1.3** | **Vocabulary (4 terms × 1 mark)** | **4** | ___ |
| → | alpha cut-off — accurate, in own words | 1 | ___ |
| → | beta cut-off — accurate, in own words | 1 | ___ |
| → | move ordering — accurate, in own words | 1 | ___ |
| → | nodes evaluated — accurate, in own words | 1 | ___ |
| | ***Milestone Subtotal*** | **/ 15** | ___ |

### Milestone 2 — Implementing Alpha-Beta Pruning *(25 marks)*

| Task | Marking Criteria | Out of | Score |
|------|-----------------|--------|-------|
| **Task 2.1** | **`alpha_beta()` Function Implementation** | **15** | ___ |
| → | Function signature accepts `board`, `depth`, `alpha`, `beta`, `is_maximizing` | 1 | ___ |
| → | Base case: returns `evaluate(board)` and `None` at terminal state or depth 0 | 2 | ___ |
| → | Maximizer branch correctly updates `alpha` and uses `max()` | 3 | ___ |
| → | Minimizer branch correctly updates `beta` and uses `min()` | 3 | ___ |
| → | Beta cut-off (`break` when `beta <= alpha`) fires correctly in Maximizer branch | 2 | ___ |
| → | Alpha cut-off (`break` when `beta <= alpha`) fires correctly in Minimizer branch | 2 | ___ |
| → | `make_move()` and `undo_move()` used correctly; board fully restored; `minimax()` still works unchanged | 2 | ___ |
| **Task 2.2** | **Move Ordering** | **6** | ___ |
| → | Basic ordering implemented: winning/capturing moves sorted first (3 marks) OR advanced strategy with explanation (6 marks) | 3–6 | ___ |
| → | `use_ordering` toggle parameter functions correctly | — | ___ |
| **Task 2.3** | **Unit Tests (4 required)** | **4** | ___ |
| → | Test: `alpha_beta()` returns same best move as `minimax()` for identical inputs | 1 | ___ |
| → | Test: `alpha_beta()` evaluates fewer nodes than `minimax()` | 1 | ___ |
| → | Test: a specific alpha or beta cut-off is triggered and verified | 1 | ___ |
| → | Test: move ordering reduces `nodes_evaluated` vs. unordered | 1 | ___ |
| | ***Milestone Subtotal*** | **/ 25** | ___ |

### Milestone 3 — Performance Analysis *(20 marks)*

| Task | Marking Criteria | Out of | Score |
|------|-----------------|--------|-------|
| **Task 3.1** | **Nodes Evaluated Experiment** | **10** | ___ |
| → | Data collected for both functions at depths 1 through at least 5 | 3 | ___ |
| → | Nodes evaluated and wall-clock time recorded for each depth and function | 3 | ___ |
| → | Both functions return the same best move at every depth tested | 2 | ___ |
| → | Results presented in the required table format, clearly readable | 2 | ___ |
| **Task 3.2** | **Charts (2 required)** | **6** | ___ |
| → | Chart A (nodes): both functions plotted, axes labelled, legend present, exponential difference visible | 3 | ___ |
| → | Chart B (time): same standards; correct scaling; time in seconds with adequate precision | 3 | ___ |
| **Task 3.3** | **Written Analysis (150–200 words)** | **4** | ___ |
| → | Quantifies speedup at depth 4 and depth 6 using actual experimental numbers | 1 | ___ |
| → | Assesses move ordering impact with specific node-count data | 1 | ___ |
| → | Evaluates whether data supports the O(b^(d/2)) best-case claim with reasoning | 1 | ___ |
| → | Identifies a practical maximum depth for Hard mode based on timing data | 1 | ___ |
| | ***Milestone Subtotal*** | **/ 20** | ___ |

### Milestone 4 — Pygame Integration *(25 marks)*

| Task | Marking Criteria | Out of | Score |
|------|-----------------|--------|-------|
| **Task 4.1** | **Replace the AI Core** | **10** | ___ |
| → | All AI calls use `alpha_beta()` with correct initial α/β values (−∞ / +∞) | 3 | ___ |
| → | `M` key toggle switches between Minimax and Alpha-Beta; active algorithm displayed on screen | 3 | ___ |
| → | AI still never produces an illegal move at any depth or difficulty setting | 2 | ___ |
| → | Human input blocked during AI calculation; no input-lag or race conditions | 2 | ___ |
| **Task 4.2** | **Pruning Stats Overlay** | **10** | ___ |
| → | Nodes evaluated displayed correctly after each AI move | 2 | ___ |
| → | Time taken displayed in milliseconds, accurate to at least one decimal | 2 | ___ |
| → | Current depth displayed | 1 | ___ |
| → | Pruning efficiency percentage computed and displayed correctly | 3 | ___ |
| → | Overlay is readable and does not obstruct gameplay | 2 | ___ |
| **Task 4.3** | **Difficulty Levels** | **5** | ___ |
| → | Easy (depth 2–3), Medium (depth 4–5), Hard (depth 6–7) selectable from pre-game menu | 3 | ___ |
| → | Selected difficulty displayed during gameplay; no crashes at any setting | 2 | ___ |
| | ***Milestone Subtotal*** | **/ 25** | ___ |

### Milestone 5 — Reflection & Demo *(15 marks)*

| Task | Marking Criteria | Out of | Score |
|------|-----------------|--------|-------|
| **Task 5.1** | **Written Reflection (300–400 words)** | **8** | ___ |
| → | Identifies the specific depth with the most dramatic speedup and explains why | 2 | ___ |
| → | Correctly reasons about whether identical Alpha-Beta implementations must evaluate the same nodes | 2 | ___ |
| → | Describes a real implementation bug: what it was, how it manifested, and how it was fixed | 2 | ___ |
| → | Accurately describes the perfectly-ordered and worst-ordered tree node counts | 2 | ___ |
| **Task 5.2** | **Optimization Report (100–150 words)** | **4** | ___ |
| → | Identifies and justifies the move ordering strategy used | 1 | ___ |
| → | Provides specific node-count numbers showing ordering impact at depth 4 | 2 | ___ |
| → | Names and briefly describes a further improvement strategy | 1 | ___ |
| **Task 5.3** | **Live Demo** | **3** | ___ |
| → | Game runs without errors; toggle works live; stats overlay visible during demo | 1 | ___ |
| → | Student explains in plain English where a beta cut-off fires and why it is safe to prune | 1 | ___ |
| → | Student can identify the alpha update line, the beta update line, and the prune condition in their code | 1 | ___ |
| | ***Milestone Subtotal*** | **/ 15** | ___ |
| | **FINAL TOTAL** | **/ 100** | ___ |

---

## 6. Helpful Resources & Tips

### 📚 Recommended Resources

- **Sebastian Lague** — "Minimax and Alpha-Beta Pruning" (YouTube) — watch the second half for pruning visuals
- **CS50 AI** — Free course at [cs50.harvard.edu/ai](https://cs50.harvard.edu/ai) — Lecture 0 covers both Minimax and Alpha-Beta
- **Wikipedia** — [Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) — clear diagrams of alpha and beta cut-off examples
- **Python docs** — `time.perf_counter()` for high-resolution timing across all platforms
- **Pygame docs** — [pygame.org/docs](https://www.pygame.org/docs) — event and font modules for the stats overlay
- **Real Python** — search "minimax alpha beta python" for step-by-step walk-throughs

### ⚠️ Common Mistakes to Avoid

- **Wrong initial values:** Always start the root call with `alpha = float('-inf')` and `beta = float('inf')`, not `0`.
- **Passing α/β by value vs. reference:** Each recursive call should receive the current alpha and beta values but only update them locally — never modify the parent's copies directly. Python's default passing handles this correctly.
- **Pruning at the wrong level:** The cut-off check (`beta <= alpha`) must happen *inside* the loop, after updating `alpha` or `beta`, not before recursing.
- **Breaking out of the loop too early:** Make sure you record `best_move` before the `break`, otherwise you might return `None` as the best move.
- **Forgetting to pass alpha and beta down:** Both values must be passed to every recursive call. Forgetting one eliminates all pruning.
- **Not testing move ordering separately:** Always verify that your ordering is actually reducing `nodes_evaluated` before claiming it works.

### 🗂️ Suggested File Structure

```
your_game/
    ├── main.py          # Pygame loop, event handling, rendering, stats overlay
    ├── game.py          # Board state, make_move(), undo_move(), is_terminal()
    ├── ai.py            # minimax(), alpha_beta(), evaluate(), get_best_move()
    ├── test_ai.py       # All unit tests (Challenge 1 + new Challenge 2 tests)
    ├── experiment.py    # Standalone script that runs the M3 experiment and prints table
    └── reflection.pdf   # Written reflection, optimization report, and charts
```

---

## 7. Submission Checklist

Before submitting, check off every item:

**Milestone 1**
- [ ] Annotated pruning diagram with alpha/beta values and labelled cut-offs
- [ ] Written comparison (200–300 words) answering all four questions
- [ ] Vocabulary definitions for all 4 terms in own words

**Milestone 2**
- [ ] `alpha_beta()` function implemented correctly in `ai.py`
- [ ] Move ordering implemented with `use_ordering` toggle parameter
- [ ] Original `minimax()` function still works unchanged
- [ ] At least 4 new passing unit tests in `test_ai.py`

**Milestone 3**
- [ ] Nodes-evaluated experiment table populated for depths 1 through at least 5
- [ ] Chart A (nodes evaluated) and Chart B (wall-clock time) created and labelled
- [ ] Written analysis (150–200 words) interpreting results

**Milestone 4**
- [ ] All AI calls replaced with `alpha_beta()`; correct initial α/β at root
- [ ] `M`-key toggle switches between Minimax and Alpha-Beta during gameplay
- [ ] Pruning stats overlay shows nodes, time, depth, and efficiency after every AI move
- [ ] Difficulty levels updated to Easy / Medium / Hard with deeper Hard depth

**Milestone 5**
- [ ] Written reflection (300–400 words) addressing all four prompts
- [ ] Optimization report (100–150 words) with specific node-count numbers
- [ ] Ready for live demo — can explain alpha/beta update lines and prune condition in code

---

> *Remember: Alpha-Beta pruning does not make your AI smarter — it makes it faster. And a faster AI can think deeper. A deeper AI is smarter. The optimization is real.*
