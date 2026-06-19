# Unit 2 — The Ledger and the Treasury 📜
### Lists · Tuples · Dictionaries · *the kingdom's record-keeping system*

**Topics Covered:** lists, 2D lists, tuples (immutability), dictionaries, `enumerate()`, list comprehensions, nested data, when to use each structure  
**Instructions:** Complete all checkpoints in order. Each one builds directly onto your Unit 1 files — you are not starting from scratch, you are upgrading what you already built.

> *"The kingdom's scribe must record everything — the coordinates of every district, the stats of every knight, the layout of every tile. Without proper records, rebuilding descends into chaos. The question is not whether to keep records — it is which kind of record to keep."*

---

## Why Are We Doing This?

In Unit 1 you gave your `Entity` class a `stats` dictionary — but you may not have thought carefully about *why* a dictionary and not a list. This unit answers that question directly.

Python gives you three core ways to store collections of data:

- **Lists** — ordered, changeable, accessed by position number
- **Tuples** — ordered, *unchangeable*, accessed by position number
- **Dictionaries** — unordered, changeable, accessed by a meaningful **name** (key)

Choosing the right one for each job makes your code cleaner, safer, and much easier to read. By the end of this unit your game will have:

- A `settings.py` full of named constants in tuples
- A tile map stored as a 2D list, loaded into the game world
- Every character's stats in a dictionary, with a working shop that upgrades them

> ⚠️ **These structures connect directly to Unit 3.** When you save your game to a file using JSON, Python converts your dictionaries and lists automatically. The cleaner your data structures are now, the simpler saving and loading will be later.

---

## Key Vocabulary

| Term | Plain English meaning |
|---|---|
| `list` | An ordered, changeable collection. Items accessed by index: `my_list[0]` |
| `tuple` | An ordered, *fixed* collection. Cannot be changed after creation: `(1280, 720)` |
| `dictionary` | A collection of key-value pairs. Access by name: `stats["HP"]` not `stats[0]` |
| `index` | The position number of an item in a list or tuple. Always starts at `0`. |
| `key` | The name used to look up a value in a dictionary. Usually a string. |
| `value` | The data stored under a key in a dictionary. |
| `mutable` | Can be changed after creation. Lists and dicts are mutable. |
| `immutable` | Cannot be changed after creation. Tuples are immutable. |
| `enumerate()` | A built-in that gives you both the index and the value while looping. |
| `2D list` | A list where every item is also a list — a grid of rows and columns. |
| `list comprehension` | A compact way to build a list using a one-line loop: `[x*2 for x in nums]` |

---

## The Big Question: List, Tuple, or Dictionary?

Before writing any code, read this table. Come back to it whenever you are not sure which to use.

| Question | Answer | Use this |
|---|---|---|
| Will this value ever change? No — it is a constant. | Immutable is safer | **tuple** |
| Is the order important and will it change? | Ordered + mutable | **list** |
| Do I need to look things up by a meaningful name? | Named access | **dictionary** |
| Am I storing a grid of rows and columns? | Ordered + nested | **2D list** |
| Am I storing related properties of one thing? | Named + grouped | **dictionary** |

---

---

## Checkpoint 1 — The Problem With Lists of Lists 🧩

### 📋 Your Task

Before we introduce dictionaries and tuples, we are going to look at what happens when you *only* use lists. This checkpoint shows you a real limitation — so that when you reach Checkpoint 2 and 3, you understand exactly what problem the other structures solve.

You will store player stats as a list, write code that uses them, and then discover why this approach breaks down.

### 🧠 Understand It First

Imagine you want to track a player's stats. A list seems obvious:

```python
# Storing stats as a list
player_stats = [100, 100, 15, 5, 4, 0, 1]
```

This works — until you try to read it back six weeks later. What is index `[2]`? Is it Attack? Defence? Speed? You have to remember the position of every value. Now imagine you need to add a new stat — you have to update every piece of code that uses position numbers.

Compare that to a dictionary:

```python
# Storing stats as a dictionary
player_stats = {
    "HP":      100,
    "max_HP":  100,
    "Attack":   15,
    "Defence":   5,
    "Speed":     4,
    "Gold":      0,
    "Level":     1,
}
```

`player_stats["Attack"]` tells you exactly what you are reading. Adding `"Luck": 3` doesn't break any existing code. Saving to JSON in Unit 3 becomes one line.

This checkpoint makes you feel the pain of the list approach — so you appreciate the dictionary solution.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `player_stats` as a list | `[100, 100, 15, 5, 4, 0, 1]` — HP, max_HP, Attack, Defence, Speed, Gold, Level |
| `print_stats(stats)` | A function that prints every stat with its label, using *position numbers only* (no names) |
| `apply_upgrade(stats, index, amount)` | A function that adds `amount` to `stats[index]` |
| `simulate_purchase()` | Call `apply_upgrade` to add 10 to Attack and 5 to Defence. Print before and after. |
| Written reflection | Answer the question at the bottom before moving to Checkpoint 2 |

### 💡 Hints

- `stats[0]` is HP, `stats[2]` is Attack, `stats[3]` is Defence — you have to track this yourself
- You are not expected to like this approach. That is the point.
- Keep this file — you will rewrite it in Checkpoint 2 and compare the two versions

### 🖊️ Your Code

```python
# checkpoint1_lists.py
# Name:
# Date:

# Step 1: Store player stats as a plain list
# Order: HP, max_HP, Attack, Defence, Speed, Gold, Level
player_stats = [100, 100, 15, 5, 4, 0, 1]


def print_stats(stats):
    # Step 2: Print each stat with a label
    # You must use index numbers — stats[0], stats[1], etc.
    # Example output:
    #   HP:      100 / 100
    #   Attack:   15
    #   Defence:   5
    #   Speed:     4
    #   Gold:      0
    #   Level:     1
    pass


def apply_upgrade(stats, index, amount):
    # Step 3: Add amount to stats[index]
    # Print a confirmation — but what do you print as the stat name?
    # You only have the index number...
    pass


# Step 4: Print stats, buy two upgrades, print stats again
print("=== Before upgrades ===")
print_stats(player_stats)

# Apply +10 to Attack (index 2) and +5 to Defence (index 3)

print("\n=== After upgrades ===")
print_stats(player_stats)


# Step 5: Now try to add a new stat — "Magic" — to the list
# Where does it go? What index does it get?
# What existing code breaks when you add it?
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Print stats before upgrades | All 7 values display with correct labels | |
| 2 | Apply +10 to Attack | Attack shows 25 after upgrade | |
| 3 | Apply +5 to Defence | Defence shows 10 after upgrade | |
| 4 | Try adding "Magic" as a new stat | Identify which existing code now has the wrong index | |

> **Answer this question before moving on — this is the whole point of the checkpoint:**
>
> What are two specific problems with using a list to store player stats? What would break if another developer added a new stat to position 2 in the list without telling you?
>
> *(your answer here)*

---

---

## Checkpoint 2 — Tuples: The Kingdom's Law 📌

### 📋 Your Task

Now we introduce **tuples**. A tuple looks like a list but uses round brackets `()` instead of square brackets `[]`. The key difference: **a tuple cannot be changed after it is created**. That is not a limitation — it is a feature.

You will create `settings.py`, which becomes the single source of truth for every constant in your game. When TILE_SIZE or the screen resolution needs to change, you change it in one place and it updates everywhere.

### 🧠 Understand It First

**Why use a tuple instead of a list for constants?**

```python
# As a list — looks fine, but nothing stops accidental changes
SCREEN = [1280, 720]
SCREEN[0] = 999      # oops — someone changed the screen width mid-game

# As a tuple — Python enforces that it cannot change
SCREEN = (1280, 720)
SCREEN[0] = 999      # TypeError: 'tuple' object does not support item assignment
```

When you mark something as a tuple, you are making a contract: *this value is a law of the kingdom, and it does not change at runtime.* Any code that accidentally tries to modify it gets an immediate error instead of a silent bug that is hard to track down.

Tuples are also used for Pygame **colours** — every `(R, G, B)` colour value is naturally a tuple.

**Tuple unpacking** is a convenient shortcut:

```python
SCREEN = (1280, 720)
width, height = SCREEN   # width = 1280, height = 720 — two assignments in one line
```

**When a tuple holds more than two values**, give each position a name using a comment or a named constant:

```python
# Position 0 = width, position 1 = height
SCREEN = (1280, 720)

# Better for colour — use a dictionary of tuples (covered in Checkpoint 3)
COLORS = {
    "gold":  (201, 168, 76),
    "red":   (220, 80, 80),
}
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| Create `settings.py` | This file holds ALL constants for the game |
| `SCREEN` | Tuple `(1280, 720)` |
| `TILE_SIZE` | Integer `64` |
| `FPS` | Integer `60` |
| `COLORS` | Dictionary of tuples — at least: `"black"`, `"white"`, `"gold"`, `"red"`, `"blue"`, `"bg"` |
| Import in `main.py` | Replace any hard-coded values with imports from `settings` |
| Demonstrate immutability | Try to change `SCREEN[0]` in a test, catch the `TypeError`, and print an explanation |

### 💡 Hints

- `from settings import SCREEN, TILE_SIZE, FPS, COLORS` at the top of any file that needs them
- `pygame.display.set_mode(SCREEN)` — the tuple passes directly to Pygame
- `COLORS["bg"]` gives you the background colour tuple
- To demonstrate immutability safely: wrap the assignment in a `try/except TypeError` block

### 🖊️ Your Code

```python
# settings.py
# Name:
# Date:
# This file is imported by every other file in the project.
# Change a value here and it updates everywhere — never hard-code these elsewhere.

# ── Screen ────────────────────────────────────────────────────────────────────
SCREEN    = (1280, 720)    # tuple — width and height are fixed laws of the kingdom
TILE_SIZE = 64             # pixels per tile
FPS       = 60

# ── Colours — a dictionary of (R, G, B) tuples ───────────────────────────────
COLORS = {
    # Step 1: Add at least 6 colours
    # Each value is a tuple: (red, green, blue)
}

# ── Demonstrate that tuples are immutable ────────────────────────────────────
# Step 2: In a try/except block, attempt to change SCREEN[0] to 800
# Catch the TypeError and print: "Tuples are immutable — SCREEN cannot be changed at runtime"
```

```python
# Update main.py — replace hard-coded values with imports

# Step 3: Add this import at the top of main.py
from settings import SCREEN, FPS, COLORS

# Step 4: Change pygame.display.set_mode((1280, 720))   →  pygame.display.set_mode(SCREEN)
# Step 5: Change self.clock.tick(60)                    →  self.clock.tick(FPS)
# Step 6: Change self.screen.fill((30, 30, 46))         →  self.screen.fill(COLORS["bg"])
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Game still launches after importing settings | No crash — same window as before | |
| 2 | Change `SCREEN` to `(800, 600)` in settings.py, rerun | Game opens at 800×600 — one change, one file | |
| 3 | Change it back to `(1280, 720)` | Game returns to original size | |
| 4 | Try `SCREEN[0] = 999` in a `try/except` | Prints the immutability message | |

> **Answer this question before moving on:**
>
> A list would technically work for SCREEN — `[1280, 720]` behaves the same in most cases. Give one concrete reason why using a tuple is *safer* for a value that should never change. Think about what happens in a large project with many developers.
>
> *(your answer here)*

---

---

## Checkpoint 3 — Dictionaries: The Knight's Dossier ⚔️

### 📋 Your Task

Now we fix the problem from Checkpoint 1. You will rewrite your player stats as a **dictionary** and build a complete shop system around it. Every stat has a name instead of an index number. Upgrades, healing, and levelling up become readable one-liners.

This is also the point where you update your Unit 1 `Entity` class to use a proper stats dictionary — and feel how much cleaner everything becomes.

### 🧠 Understand It First

**Dictionary vs List — a direct comparison:**

```python
# LIST — you must memorise what each index means
stats = [100, 100, 15, 5, 4, 0, 1]
stats[2] += 10          # what is index 2? You have to check your notes
stats[0] = min(stats[0] + 25, stats[1])   # HP capped at max_HP — but which index is which?

# DICTIONARY — the key tells you exactly what you are reading
stats = {"HP": 100, "max_HP": 100, "Attack": 15, "Defence": 5, "Speed": 4, "Gold": 0, "Level": 1}
stats["Attack"] += 10   # perfectly clear — no notes needed
stats["HP"] = min(stats["HP"] + 25, stats["max_HP"])   # reads like English
```

**Dictionary rules to know:**

```python
d = {"HP": 100, "Attack": 15}

# Reading a value
d["HP"]              # 100

# Changing a value
d["HP"] -= 20        # HP is now 80

# Adding a new key
d["Magic"] = 5       # no index to track — just add the key

# Safe reading with a default (won't crash if key is missing)
d.get("Luck", 0)     # returns 0 if "Luck" doesn't exist

# Looping over all key-value pairs
for stat, value in d.items():
    print(f"{stat}: {value}")

# Check if a key exists
"Attack" in d        # True
"Flying" in d        # False
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| Update `Entity.__init__` | Replace the simple stats dict with the full version: HP, max_HP, Attack, Defence, Speed, Gold, Level, XP, XP_next |
| `take_damage(amount)` | Uses `self.stats["HP"]` — already done in Unit 1, confirm it still works |
| `heal(amount)` | `self.stats["HP"] = min(self.stats["HP"] + amount, self.stats["max_HP"])` |
| `check_level_up()` | New method on `Player`. If `XP >= XP_next`: increment Level, raise max_HP by 20, restore HP to full, raise XP_next by 50%, reset XP to 0, print a summary |
| `SHOP_ITEMS` in `settings.py` | A list of dictionaries — at least 4 items. Each has `"name"`, `"type"`, `"cost"`, and `"bonus"` keys |
| `buy_item(player, item_name)` | Function in a new file `shop.py`. Checks gold, deducts cost, applies bonus dict to player stats, prints receipt or "Not enough gold." |

### 💡 Hints

- `self.stats["XP_next"] = int(self.stats["XP_next"] * 1.5)` — multiply then convert to int so it stays a whole number
- The `"bonus"` value in each shop item is itself a dictionary: `{"Attack": 10}`. Loop over it with `.items()` to apply each bonus to the player's stats
- `player.stats.get(stat, 0)` is safer than `player.stats[stat]` if a bonus key might not exist yet in stats
- Add `from settings import SHOP_ITEMS` at the top of `shop.py`

### 🖊️ Your Code

```python
# Update entity.py — replace the old stats dict in __init__

self.stats = {
    "HP":      100,
    "max_HP":  100,
    "Attack":   10,
    "Defence":   0,
    "Speed":     3,
    "Gold":      0,
    "Level":     1,
    "XP":        0,
    "XP_next":  100,
}
```

```python
# Add to player.py — inside the Player class

def check_level_up(self):
    # Step 1: Check if self.stats["XP"] >= self.stats["XP_next"]
    # Step 2: If yes:
    #         → Increment Level by 1
    #         → Increase max_HP by 20
    #         → Restore HP to max_HP (full heal)
    #         → Multiply XP_next by 1.5, convert to int
    #         → Set XP back to 0
    #         → Print a level-up summary showing all changed stats
    pass
```

```python
# Add to settings.py

SHOP_ITEMS = [
    # Step 1: Define at least 4 items
    # Each item is a dictionary with these keys:
    #   "name"  : string  — display name
    #   "type"  : string  — "weapon", "armour", or "consumable"
    #   "cost"  : int     — gold price
    #   "bonus" : dict    — stats to improve, e.g. {"Attack": 10}
    #
    # Example structure (fill in the values yourself):
    {"name": "Iron Sword",    "type": "weapon",     "cost": 80,  "bonus": {"Attack": 10}},
    {"name": "Leather Tunic", "type": "armour",     "cost": 50,  "bonus": {"Defence": 5}},
    # Add two more items of your choice
]
```

```python
# shop.py — new file
# Name:
# Date:

from settings import SHOP_ITEMS

def buy_item(player, item_name):
    # Step 1: Find the item in SHOP_ITEMS where item["name"] == item_name
    #         If not found, print "Item not found." and return

    # Step 2: Check if player.stats["Gold"] >= item["cost"]
    #         If not, print "Not enough gold." and return

    # Step 3: Deduct the cost from player.stats["Gold"]

    # Step 4: Apply the bonus — loop over item["bonus"].items()
    #         For each (stat, value), add value to player.stats[stat]
    #         Use player.stats.get(stat, 0) in case the stat doesn't exist yet

    # Step 5: Print a receipt:
    #         "Purchased Iron Sword for 80 gold. Attack is now 25."
    pass


def show_shop(player):
    # Step 6: Print a formatted shop menu
    # Show each item's name, type, cost, and whether the player can afford it
    # Example:
    #   Iron Sword    (weapon)  .............. 80 gold   [affordable]
    #   Dragon Plate  (armour)  ............. 300 gold   [too expensive]
    pass
```

### 🧪 Test Your Program

```python
# test_shop.py — run this to verify your shop works (no Pygame needed)
# Add this as a temporary test file, not part of the final game

import sys
sys.path.append("../unit1_oop")   # so we can import Entity/Player

from player import Player
from shop   import buy_item, show_shop

# Create a mock player — just need the stats dict for this test
class MockPlayer:
    def __init__(self):
        self.stats = {
            "HP": 100, "max_HP": 100, "Attack": 15,
            "Defence": 0, "Speed": 4, "Gold": 150, "Level": 1,
            "XP": 0, "XP_next": 100,
        }

player = MockPlayer()
show_shop(player)
buy_item(player, "Iron Sword")
buy_item(player, "Dragon Plate")   # should fail — too expensive
print(f"\nGold remaining: {player.stats['Gold']}")
print(f"Attack is now:  {player.stats['Attack']}")
```

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | `show_shop()` | All 4+ items display with cost and affordability | |
| 2 | `buy_item(player, "Iron Sword")` with 150 gold | Deducts 80 gold, Attack increases by 10 | |
| 3 | `buy_item(player, "Dragon Plate")` | Prints "Not enough gold." — gold unchanged | |
| 4 | `buy_item(player, "Magic Carpet")` | Prints "Item not found." | |
| 5 | Give player 0 XP\_next worth of XP, call `check_level_up()` | Level increases, HP restored, XP\_next rises | |

> **Answer these questions before moving on:**
>
> 1. Rewrite this list-based stat access as a dictionary access:  
>    `stats[2] += 10`  — what does this become, and why is it better?
>
>    *(your answer here)*
>
> 2. The `"bonus"` key in each shop item holds a dictionary inside a dictionary. What is the advantage of this design versus giving every item a separate `"attack_bonus"`, `"defence_bonus"`, `"speed_bonus"` key?
>
>    *(your answer here)*

---

---

## Checkpoint 4 — 2D Lists: The District Map 🗺️

### 📋 Your Task

A **2D list** (list of lists) is how we represent a tile map before you move to Tiled CSV files in Unit 5. Each inner list is one row of tiles. Each character in that row is a tile type. You loop through the whole grid with nested `enumerate()` calls to turn characters into actual sprite positions.

This is one of the most important patterns in game development. Learn it here; it scales directly to your Unit 5 Tiled workflow.

### 🧠 Understand It First

```python
# A 2D list — a list where each item is also a list
WORLD_MAP = [
    ["W", "W", "W", "W", "W"],    # row 0
    ["W", ".", "P", ".", "W"],    # row 1
    ["W", ".", "W", "E", "W"],    # row 2
    ["W", "W", "W", "W", "W"],   # row 3
]

# Accessing a single tile:
WORLD_MAP[1][2]   # row 1, column 2 → "P"  (player spawn)
WORLD_MAP[2][3]   # row 2, column 3 → "E"  (enemy spawn)

# Looping with enumerate() to get BOTH the index AND the value:
for row_idx, row in enumerate(WORLD_MAP):
    for col_idx, tile in enumerate(row):
        x = col_idx * TILE_SIZE     # pixel X position
        y = row_idx * TILE_SIZE     # pixel Y position
        print(f"Tile '{tile}' at pixel ({x}, {y})")
```

**Why `enumerate()` and not `range(len(...))`?**

```python
# The old way — works, but harder to read
for row_idx in range(len(WORLD_MAP)):
    for col_idx in range(len(WORLD_MAP[row_idx])):
        tile = WORLD_MAP[row_idx][col_idx]

# With enumerate() — cleaner, and you can't accidentally get the index wrong
for row_idx, row in enumerate(WORLD_MAP):
    for col_idx, tile in enumerate(row):
        ...    # tile and both indices are right here, no extra lookup needed
```

**Why a 2D list and not a dictionary?** 

Because the *position* of the tile in the grid is what matters. `WORLD_MAP[2][3]` means "row 2, column 3" — the row and column numbers are the address. You wouldn't name every tile like `tiles["row2_col3"]`. For spatial/grid data where position is the key, a 2D list is the right tool.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `WORLD_MAP` in `settings.py` | At least 10 columns × 8 rows. Use `"W"` (wall), `"."` (floor), `"P"` (player spawn — exactly one), `"E"` (enemy), `"C"` (chest), `"N"` (NPC) |
| Surrounded by walls | Entire border should be `"W"` tiles |
| At least one of each | `"P"`, 2× `"E"`, 1× `"C"`, 1× `"N"` inside the walls |
| `_create_map()` in `Level` | Replace the hard-coded spawn positions from Unit 1 with a loop over `WORLD_MAP` using `enumerate()`. Spawn the correct sprite for each character. |
| Wall sprite | Create a simple `Tile` class in `tile.py` that inherits from `pygame.sprite.Sprite` and fills its image with a colour |

### 💡 Hints

- Import `WORLD_MAP` and `TILE_SIZE` from `settings`: `from settings import WORLD_MAP, TILE_SIZE`
- `x = col_idx * TILE_SIZE` and `y = row_idx * TILE_SIZE` gives the pixel position of each tile
- Your `Tile` class should be added to both `self.visible_sprites` and `self.obstacle_sprites` for walls, and only `self.visible_sprites` for decorative floor tiles
- `"P"` should spawn the player — save the result as `self.player` so enemies can reference it

### 🖊️ Your Code

```python
# tile.py — new file
# Name:
# Date:

import pygame
from settings import TILE_SIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, colour=(80, 60, 50)):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(colour)
        # Add a slightly lighter border so tiles are visually distinct
        pygame.draw.rect(self.image, (colour[0]+20, colour[1]+20, colour[2]+20),
                         self.image.get_rect(), 1)
        self.rect  = self.image.get_rect(topleft=pos)
```

```python
# Add to settings.py

from settings import TILE_SIZE   # already there — just making sure

WORLD_MAP = [
    # Step 1: Design a 10×8 map (or larger) using:
    #   "W" = wall      "." = floor
    #   "P" = player    "E" = enemy
    #   "C" = chest     "N" = NPC
    # Every edge tile should be "W"
    # Example — replace with your own design:
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","P",".",".",".",".","E",".","C","W"],
    ["W",".","W","W",".","W","W",".",".",  "W"],
    # ... add your remaining rows here
]
```

```python
# Update level.py — replace _setup_map() entirely

from settings import WORLD_MAP, TILE_SIZE, COLORS
from tile    import Tile
from player  import Player
from enemy   import Enemy
from chest   import Chest
from npc     import NPC

def _create_map(self):
    for row_idx, row in enumerate(WORLD_MAP):
        for col_idx, tile in enumerate(row):

            # Step 1: Calculate pixel position from grid position
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE

            # Step 2: Match the tile character and spawn the right object
            if tile == "W":
                # Wall — goes in BOTH visible and obstacle groups
                pass

            elif tile == ".":
                # Floor — goes in visible only, light colour
                pass

            elif tile == "P":
                # Player spawn — save as self.player
                pass

            elif tile == "E":
                # Enemy — needs a reference to self.player
                # But what if "P" hasn't been read yet?
                # Solution hint: do a first pass for "P" only, then a second pass for everything else
                pass

            elif tile == "C":
                pass   # Chest

            elif tile == "N":
                pass   # NPC — pick a dialogue string
```

> **Two-pass tip:** The map might have enemies placed *before* the player tile when the loop runs. One clean solution is to loop the map twice — first pass finds and spawns only the player, second pass spawns everything else. Give it a try.

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Game launches with your map | Coloured tiles fill the screen in the correct layout | |
| 2 | Walk into a wall tile | Player stops — wall collision works | |
| 3 | Enemy spawns at correct map position | Red square appears where you put `"E"` | |
| 4 | Change a `"."` to `"E"` in WORLD_MAP, rerun | New enemy appears at that new position — no other code changed | |
| 5 | Print the map dimensions | Rows and columns match your WORLD_MAP definition | |

> **Answer these questions before moving on:**
>
> 1. You changed a character in `WORLD_MAP` and a new enemy appeared without touching any other file. What does this tell you about keeping data separate from logic?
>
>    *(your answer here)*
>
> 2. Why is a 2D list the right structure for a tile map, rather than a dictionary? What would a dictionary version look like, and why is it worse for this use case?
>
>    *(your answer here)*

---

---

## Checkpoint 5 — Lists of Dictionaries: The Market and Enemy Roster 🏪

### 📋 Your Task

The most powerful real-world data pattern is **a list of dictionaries**. Each dictionary describes one item, and the list holds all of them. This is how almost every game stores its item tables, enemy configurations, dialogue trees, and quest logs.

In this checkpoint you will:
1. Add an `ENEMY_DATA` dictionary to `settings.py` so different enemy *types* can have different stats without separate classes
2. Build a `show_shop()` and `buy_item()` system that uses the `SHOP_ITEMS` list from Checkpoint 3
3. Run the shop from inside the game by pressing a key

This checkpoint also directly shows the contrast between the three structures and when each one earns its place.

### 🧠 Understand It First

**A list of dictionaries — the item table pattern:**

```python
SHOP_ITEMS = [
    {"name": "Iron Sword",    "type": "weapon",     "cost": 80,  "bonus": {"Attack": 10}},
    {"name": "Leather Tunic", "type": "armour",     "cost": 50,  "bonus": {"Defence": 5}},
    {"name": "Speed Boots",   "type": "armour",     "cost": 120, "bonus": {"Speed": 2}},
    {"name": "Health Potion", "type": "consumable", "cost": 30,  "bonus": {"HP": 25}},
]
```

- The **list** holds all items in order — you can loop through them, sort them, filter them
- Each **dictionary** describes one item — you access its properties by name, not by position
- The `"bonus"` value is itself a **dictionary** — so one item can grant multiple stat bonuses

**Why not just use a 2D list?**

```python
# As a 2D list — position-based, fragile
SHOP_ITEMS = [
    ["Iron Sword", "weapon", 80, 10, 0, 0],
    #              index 0    1   2   3  4  5
    #              name  type cost atk def spd
]
# To read attack bonus: SHOP_ITEMS[0][3]   ← what is index 3? You must remember.

# As a list of dicts — name-based, self-documenting
SHOP_ITEMS[0]["bonus"]["Attack"]   # immediately readable
```

**The `ENEMY_DATA` dictionary — one class, many enemy types:**

```python
ENEMY_DATA = {
    "goblin":   {"HP": 50,  "Attack": 8,  "Speed": 3, "XP": 40,  "colour": (100, 200, 80)},
    "skeleton": {"HP": 80,  "Attack": 12, "Speed": 2, "XP": 70,  "colour": (200, 200, 180)},
    "troll":    {"HP": 200, "Attack": 20, "Speed": 1, "XP": 150, "colour": (80,  140, 80)},
}
```

Instead of three separate `Goblin`, `Skeleton`, `Troll` classes, one `Enemy` class reads from this dictionary at creation time. Spawning a new enemy type means adding one entry to the data table — not writing a whole new class.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `ENEMY_DATA` in `settings.py` | At least 3 enemy types, each with HP, Attack, Speed, XP reward, and colour tuple |
| Update `Enemy.__init__` | Accept an `enemy_type` string. Look up `ENEMY_DATA[enemy_type]`, copy the stats into `self.stats`, set the image colour from the data |
| Update `WORLD_MAP` | Use different characters for different enemy types: `"g"` = goblin, `"s"` = skeleton, `"t"` = troll |
| Update `_create_map()` | Spawn `Enemy("goblin", ...)`, `Enemy("skeleton", ...)` etc. for each character |
| `show_shop()` in `shop.py` | Prints a formatted list of all items with cost and `[affordable]` / `[too expensive]` tag |
| Wire shop into game | Press `B` to print the shop to the console. Press `1`/`2`/`3`/`4` to buy the corresponding item (console-based for now) |

### 💡 Hints

- `data = ENEMY_DATA[enemy_type].copy()` — use `.copy()` so each enemy instance gets independent stats (without this, all goblins share one dictionary and damaging one damages all of them)
- `self.stats.update(data)` copies all keys from `data` into `self.stats` at once
- For the shop key press, handle `pygame.KEYDOWN` events in `Level.handle_events()`. `event.key == pygame.K_b` is the `B` key.
- `sorted(SHOP_ITEMS, key=lambda item: item["cost"])` — sorts items by cost for display

### 🖊️ Your Code

```python
# Add to settings.py

ENEMY_DATA = {
    # Step 1: Define at least 3 enemy types
    # Each entry is a dictionary with: HP, max_HP, Attack, Speed, XP, colour
    # colour should be an (R, G, B) tuple
    "goblin": {
        "HP":     50,
        "max_HP": 50,
        "Attack":  8,
        "Speed":   3,
        "XP":     40,
        "colour": (100, 200, 80),
    },
    # Add skeleton and troll here
}
```

```python
# Update enemy.py

from settings import ENEMY_DATA

class Enemy(Entity):
    def __init__(self, enemy_type, pos, groups, player):
        super().__init__(pos, groups)

        # Step 2: Look up the enemy type in ENEMY_DATA
        #         Copy the data — do NOT assign directly or all enemies share one dict
        data = ENEMY_DATA[enemy_type].copy()

        # Step 3: Update self.stats with the data from ENEMY_DATA
        self.stats.update(data)

        # Step 4: Set image colour from data["colour"]
        self.image.fill(data["colour"])

        self.player        = player
        self.notice_radius = 200
        self.attack_radius = 50

    # _distance_to_player, _chase_player, update — unchanged from Unit 1
```

```python
# Update settings.py WORLD_MAP to use different enemy characters
# "g" = goblin, "s" = skeleton, "t" = troll
# Example:
WORLD_MAP = [
    ["W","W","W","W","W","W","W","W","W","W","W","W"],
    ["W","P",".",".","g",".",".","s",".",".","C","W"],
    # ... rest of your map using g, s, t instead of just "E"
]
```

```python
# Update _create_map() in level.py to handle the new enemy characters

elif tile == "g":
    Enemy("goblin",   (x, y), self.visible_sprites, self.player)
elif tile == "s":
    Enemy("skeleton", (x, y), self.visible_sprites, self.player)
elif tile == "t":
    Enemy("troll",    (x, y), self.visible_sprites, self.player)
```

```python
# Update shop.py — complete show_shop() and add key handling

def show_shop(player):
    print("\n╔══ THE KINGDOM MARKET ══════════════════╗")
    # Step 5: Sort items by cost using sorted() and a lambda
    sorted_items = sorted(SHOP_ITEMS, key=lambda item: item["cost"])

    for i, item in enumerate(sorted_items, 1):
        # Step 6: Check if player can afford it
        affordable = "✓ affordable" if player.stats["Gold"] >= item["cost"] else "✗ too expensive"
        # Print: "1. Iron Sword (weapon) .......... 80 gold   ✓ affordable"
        print(f"  {i}. {item['name']:<20} {item['cost']:>4} gold   {affordable}")

    print(f"  Your gold: {player.stats['Gold']}")
    print("╚════════════════════════════════════════╝\n")
```

```python
# Add to Level — new handle_events() method

def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Step 7: If event.key == pygame.K_b → call show_shop(self.player)
            # Step 8: If event.key is K_1 through K_4 → call buy_item for that item
            pass

# Update Level.run() to call self.handle_events() instead of handling events in Game.run()
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Goblins, skeletons, trolls all spawn | Three different colours on screen at their map positions | |
| 2 | Troll has 200 HP, goblin has 50 HP | Troll survives many more hits — check by printing HP in take_damage | |
| 3 | Press `B` in-game | Shop menu prints to console with all items and affordability | |
| 4 | Press `1` to buy the first item | Gold decreases, stat increases, receipt prints | |
| 5 | Add a new enemy type `"archer"` to ENEMY_DATA only | Add `"a"` to map and `elif tile == "a"` in _create_map — no other changes needed | |

> **Answer these questions before moving on:**
>
> 1. You added a brand new enemy type (`"archer"`) by editing only two things — `ENEMY_DATA` and the map parser. If you had used three separate classes (`Goblin`, `Skeleton`, `Troll`) instead, how many files would you have needed to change?
>
>    *(your answer here)*
>
> 2. Each enemy does `ENEMY_DATA[enemy_type].copy()` instead of directly assigning the dictionary. Run this experiment and describe what you see:
>    ```python
>    # Without .copy()
>    data = {"HP": 50}
>    enemy1_stats = data
>    enemy2_stats = data
>    enemy1_stats["HP"] -= 30
>    print(enemy2_stats["HP"])  # what do you expect? what actually happens?
>    ```
>
>    *(your answer here)*

---

---

## 🏁 Reflection Questions

Answer in your own words.

1. A classmate says "I'll just use lists for everything — they can hold anything." Give them two specific examples from this unit where a list would be the wrong choice and explain what to use instead.

   > *(your answer here)*

2. A tuple raises a `TypeError` if you try to change it. Why is getting an error *better* than silently changing a value that was supposed to be constant?

   > *(your answer here)*

3. Look at your `ENEMY_DATA` dictionary. If you had used a 2D list instead (`[[50, 8, 3, 40, (100,200,80)], ...]`), what would `enemy_data[0][3]` mean? What does `ENEMY_DATA["goblin"]["XP"]` mean? Which one would you rather read in six months?

   > *(your answer here)*

4. You used `enumerate()` to loop over `WORLD_MAP`. Write the same loop using `range(len(...))` — then explain which version you prefer and why.

   > *(your answer here)*

5. The `"bonus"` value inside each `SHOP_ITEMS` entry is itself a dictionary. Why is this better than giving each item individual keys like `"attack_bonus"`, `"defence_bonus"`, `"speed_bonus"`? Think about what happens when you want to apply the bonus in code.

   > *(your answer here)*

6. You now have three ways to store a collection of data. Complete this sentence for each one:
   - I would use a **list** when...
   - I would use a **tuple** when...
   - I would use a **dictionary** when...

   > *(your answer here)*

---

## What Changed From Unit 1

Here is every file you touched and why:

| File | What changed | Why |
|---|---|---|
| `settings.py` | Created. Added SCREEN, TILE_SIZE, FPS, COLORS, WORLD_MAP, SHOP_ITEMS, ENEMY_DATA | Single source of truth for all constants and data |
| `entity.py` | Expanded `self.stats` dict with Defence, Gold, Level, XP, XP_next | More stats, all named — no position numbers |
| `player.py` | Added `check_level_up()` | Levelling logic reads from the stats dict |
| `enemy.py` | `__init__` now takes an `enemy_type` string and reads from `ENEMY_DATA` | One class, many enemy types — data drives behaviour |
| `level.py` | `_setup_map()` replaced with `_create_map()` using WORLD_MAP loop | Map is now data, not hard-coded positions |
| `tile.py` | Created | Wall and floor tiles need a sprite class |
| `shop.py` | Created | Shop logic is separate from game logic |

---

## How This Connects to the Rest of the Year

```
Unit 2 — Data Structures  (this unit)
    settings.py: SCREEN tuple, COLORS dict, WORLD_MAP 2D list, ENEMY_DATA dict, SHOP_ITEMS list
         ↓
Unit 3 — File I/O
    self.stats dict → json.dump() → savegame.json → json.load() → back into self.stats
    (Because it is already a dict, saving takes three lines)
         ↓
Unit 4 — Libraries
    import_folder() returns a list of Surfaces (animation frames)
    random.choice(LOOT_TABLE) picks from a list of dicts
         ↓
Unit 5 — End-of-Term Project
    Tiled exports CSV files → import_csv_layout() returns a 2D list — same pattern as WORLD_MAP
    ENEMY_DATA and SHOP_ITEMS scale to a full game without rewriting any logic
```

---

*Previous → [Unit 1 — The Blueprints of the Kingdom](./unit1_oop.md)*  
*Next → [Unit 3 — The Great Archives](./unit3_file_io.md)*
