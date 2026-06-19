# Unit 3 — The Great Archives 📚
### File I/O · Reading & Writing · JSON Save Systems · Menus

**Topics Covered:** `open()`, file modes, `read()` / `write()` / `readlines()`, `json.dump()`, `json.load()`, `os.path`, `try/except`, main menu, Monster Manual, Spellbook  
**Instructions:** Complete all checkpoints in order. You are building on your Unit 1 and Unit 2 files — do not start from scratch. Each checkpoint adds one new layer to the same project.

> *"When the hero rests, the Royal Scribe must commit every detail to the royal archives — the player's position, their gold, the districts restored — so nothing is lost to time. A kingdom with no memory of its past cannot rebuild its future."*

---

## Why Are We Doing This?

Right now your game forgets everything the moment you close it. Every run starts over. The player's hard-earned gold, their upgraded stats, the enemies they defeated — gone.

**File I/O** (Input/Output) is how programs talk to the hard drive. When you write to a file, the data survives after Python stops running. When you read it back, your program picks up exactly where it left off.

By the end of this unit your game will:
- Open with a **main menu** (New Game, Load Game, Monster Manual, Spellbook, Quit)
- **Save** the player's stats, position, inventory, and progress to a file when they press `S`
- **Load** that save automatically when they choose "Load Game"
- Let players browse a **Monster Manual** and **Spellbook** stored as readable text files
- Handle broken or missing save files without crashing

> 💡 **Why does this matter beyond games?** Every application that stores data uses File I/O — websites write log files, apps save your settings, banks record transactions. The pattern you learn here is the same one used in professional software.

---

## What Happens When Python Reads a File?

Before writing any code, picture what is actually happening:

```
Your Python program                    Your hard drive
──────────────────                    ──────────────
                    open("data.txt")
         ───────────────────────────► finds the file
                    file object
         ◄─────────────────────────── returns a connection
                    f.read()
         ───────────────────────────► reads the bytes
                    "hello world"
         ◄─────────────────────────── sends the text back
                    f.close() / with block ends
         ───────────────────────────► closes the connection
```

The `with` statement handles the open and close automatically — even if an error occurs halfway through reading. **Always use `with` when working with files.**

---

## Key Vocabulary

| Term | Plain English meaning |
|---|---|
| `open(path, mode)` | Creates a connection to a file on disk. Returns a file object. |
| file mode | How you want to use the file: read, write, or append |
| `"r"` | Read mode — file must already exist |
| `"w"` | Write mode — creates the file if missing, **erases** existing content |
| `"a"` | Append mode — adds to the end, never erases |
| `f.read()` | Returns the entire file as one big string |
| `f.readlines()` | Returns a list of strings, one per line (each includes `\n`) |
| `f.write(text)` | Writes a string to the file |
| `\n` | The newline character — what makes text go to the next line |
| `.strip()` | Removes whitespace and `\n` from the start and end of a string |
| `JSON` | A text format that stores Python dicts and lists as structured text |
| `json.dump()` | Converts a Python dict/list → writes it as JSON text to a file |
| `json.load()` | Reads JSON text from a file → converts back to a Python dict/list |
| `os.path.exists()` | Returns `True` if a file or folder exists on disk |
| `try/except` | Attempt something that might fail; catch the error if it does |

---

## File Modes at a Glance

```python
open("file.txt", "r")   # Read    — crashes if file doesn't exist
open("file.txt", "w")   # Write   — creates if missing, ERASES if it exists
open("file.txt", "a")   # Append  — creates if missing, adds to the END
open("file.txt", "r+")  # Read+Write — file must exist, does NOT erase
```

| Mode | File must exist? | Erases content? | Use when... |
|---|---|---|---|
| `"r"` | Yes — crashes if missing | No | Reading a file you know is there |
| `"w"` | No — creates it | **Yes** | Writing a brand-new file each time |
| `"a"` | No — creates it | No | Adding to a log or score list |
| `"r+"` | Yes — crashes if missing | No | Reading and updating the same file |

---

---

## Checkpoint 1 — Reading and Writing Text Files 📄

### 📋 Your Task

Before JSON or save systems, let's understand the basics of file reading and writing using plain text files. You will create a **Hall of Records** — a high-score leaderboard stored in a `.txt` file that persists between game sessions.

This checkpoint uses no Pygame at all. Run it from the terminal so you can see exactly what the file contains.

### 🧠 Understand It First

**Writing a file:**

```python
with open("scores.txt", "w") as f:
    f.write("Arthur,1500\n")
    f.write("Lancelot,1200\n")
```

- `open("scores.txt", "w")` creates (or overwrites) a file called `scores.txt`
- `as f` gives the file object the name `f` inside the `with` block
- `f.write("Arthur,1500\n")` writes that text to the file — `\n` is the newline character
- When the `with` block ends, Python closes the file automatically

After running this, open `scores.txt` in VS Code. You will see:
```
Arthur,1500
Lancelot,1200
```

**Reading a file — whole file at once:**

```python
with open("scores.txt", "r") as f:
    content = f.read()          # one big string — all lines joined together
print(content)
```

**Reading a file — line by line:**

```python
with open("scores.txt", "r") as f:
    for line in f:              # Python treats the file like a list of lines
        print(line.strip())     # .strip() removes the \n at the end
```

**Reading into a list:**

```python
with open("scores.txt", "r") as f:
    lines = f.readlines()       # returns ["Arthur,1500\n", "Lancelot,1200\n"]

# Clean up the \n from each line
lines = [line.strip() for line in lines]
```

**Appending (adding without erasing):**

```python
with open("scores.txt", "a") as f:
    f.write("Galahad,2100\n")   # adds to the END — does not erase Arthur or Lancelot
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| `write_scores(scores)` | Takes a list of `(name, score)` tuples. Writes each as `"name,score\n"` to `scores.txt` using `"w"` mode |
| `read_scores()` | Reads `scores.txt`, splits each line on `","`, returns a list of `(name, int(score))` tuples |
| `add_score(name, score)` | Appends one new entry to `scores.txt` using `"a"` mode |
| `top_scores(n=3)` | Calls `read_scores()`, sorts by score descending, returns the top `n` entries |
| `display_leaderboard()` | Calls `top_scores()` and prints a formatted ranked list |
| Test all functions | Run a sequence that writes, appends, reads, and displays |

### 💡 Hints

- `"Arthur,1500".split(",")` returns `["Arthur", "1500"]` — use `[0]` for name and `int([1])` for score
- `sorted(entries, key=lambda e: e[1], reverse=True)` sorts by the second item (score) highest first
- `f"#{rank}  {name:<15} {score:>6} pts"` — `:<15` left-aligns in 15 characters, `:>6` right-aligns in 6

### 🖊️ Your Code

```python
# checkpoint1_scores.py
# Name:
# Date:
# Run with: python checkpoint1_scores.py
# After running, open scores.txt in VS Code to see what was written

SCORES_FILE = "scores.txt"


def write_scores(scores):
    # Step 1: Open SCORES_FILE in "w" mode
    # Step 2: Loop over scores — each item is a (name, score) tuple
    # Step 3: Write each as "name,score\n"
    pass


def read_scores():
    # Step 4: Open SCORES_FILE in "r" mode
    # Step 5: Read all lines with f.readlines()
    # Step 6: Strip each line, split on ",", return list of (name, int(score)) tuples
    # Remember: the score comes in as a string — convert it with int()
    pass


def add_score(name, score):
    # Step 7: Open SCORES_FILE in "a" mode (append — does not erase!)
    # Step 8: Write "name,score\n"
    pass


def top_scores(n=3):
    # Step 9: Call read_scores() to get all entries
    # Step 10: Sort by score descending
    # Step 11: Return only the first n entries using a slice [:n]
    pass


def display_leaderboard():
    print("\n╔══ HALL OF RECORDS ═══════════════╗")
    entries = top_scores(5)
    # Step 12: Print each entry with rank, name, and score
    # Format: "#1  Arthur          1500 pts"
    print("╚══════════════════════════════════╝\n")


# ── Test sequence ─────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Write initial scores
    write_scores([
        ("Arthur",   1500),
        ("Lancelot", 1200),
        ("Percival",  980),
    ])

    # Add a new entry
    add_score("Galahad", 2100)

    # Display the leaderboard
    display_leaderboard()

    # Verify independence — read raw and print
    print("Raw file contents:")
    with open(SCORES_FILE, "r") as f:
        print(f.read())
```

### 🧪 Test Your Program

Run `python checkpoint1_scores.py` — **no Pygame needed.**

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Open `scores.txt` in VS Code after running | Four lines, one per knight, comma-separated | |
| 2 | Leaderboard prints top 5 | Galahad first with 2100 pts | |
| 3 | Run the script a second time | `scores.txt` has 4 lines (not 8) — `"w"` mode erased and rewrote | |
| 4 | Change `write_scores` to use `"a"` instead of `"w"`, run again | File now has 8 lines — append does NOT erase | |
| 5 | Delete `scores.txt`, run again | Script recreates the file from scratch | |

> **Answer this question before moving on:**
>
> You ran the script twice. With `"w"` mode the file had 4 lines both times. With `"a"` mode it had 8 lines the second time. Explain in your own words what the difference is, and give one real-world situation where you would want `"a"` instead of `"w"`.
>
> *(your answer here)*

---

---

## Checkpoint 2 — The Monster Manual and Spellbook 📖

### 📋 Your Task

Your game now has lore. The **Monster Manual** and **Spellbook** are reference documents stored as plain text files. Players can open them from the main menu (built in Checkpoint 3) to look up enemy weaknesses or available spells.

This checkpoint teaches you to read structured text files that you design yourself, and to display multi-line content cleanly.

### 🧠 Understand It First

A plain text file can hold any structure you design — as long as you are consistent. Here is one approach using section separators:

```
--- GOBLIN ---
HP: 50
Attack: 8
Speed: 3
Weakness: Fire
Description: A small, wiry creature that travels in packs. Cowardly alone, dangerous in groups.

--- SKELETON ---
HP: 80
Attack: 12
...
```

When you read this back, you can split on `"--- "` to separate each entry, then split each entry on `"\n"` to get individual lines. This is exactly what early game engines did before databases existed.

**Reading the whole file at once:**

```python
with open("data/monster_manual.txt", "r") as f:
    content = f.read()      # one big string

# Split into sections at every "---" separator
sections = content.split("---")
# sections[0] is everything before the first ---
# sections[1] is "GOBLIN ---\nHP: 50\n..."
# sections[2] is "SKELETON ---\n..."
```

**Reading line by line — good for simple formats:**

```python
with open("data/monster_manual.txt", "r") as f:
    for line in f:
        line = line.strip()     # remove \n and spaces
        if line == "":
            continue            # skip blank lines
        if line.startswith("---"):
            print(f"\n{line}")  # print headers differently
        else:
            print(f"  {line}")  # indent body text
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| `data/` folder | Create this folder inside your project. All data files go here. |
| `monster_manual.txt` | At least 3 monsters, each with: name header, HP, Attack, Speed, Weakness, and Description |
| `spellbook.txt` | At least 3 spells, each with: name header, Cost (MP), Effect, and Flavour text |
| `read_monster_manual()` | Opens and returns the full content as a string |
| `read_spellbook()` | Opens and returns the full content as a string |
| `display_file(content, title)` | Prints a bordered title then the content, page by page if it's long |
| Test both | Run from the terminal and confirm the files display cleanly |

### 💡 Hints

- Create the `data/` folder by right-clicking in VS Code's file explorer → New Folder
- Use a relative path: `"data/monster_manual.txt"` — this works as long as you run the script from your project folder
- `content.split("\n\n")` splits on blank lines — each section becomes one chunk
- For now, print all content at once. In Checkpoint 3 you will add this to the main menu.

### 🖊️ Your Code

First, create the data files. Open VS Code, create `data/monster_manual.txt`, and write your content:

```
# data/monster_manual.txt
# Create this file manually in VS Code — it is NOT Python

--- GOBLIN ---
HP: 50
Attack: 8
Speed: 3 (Fast)
Weakness: Fire
Description: A small wiry creature that travels in packs.
  Cowardly alone but dangerous in groups. Will flee if
  the pack is reduced below half strength.

--- SKELETON ---
HP: 80
Attack: 12
Speed: 2 (Slow)
Weakness: Holy
Description: Animated by dark magic. Does not tire and
  feels no pain. Destroy the ribcage to end it quickly.

--- TROLL ---
HP: 200
Attack: 20
Speed: 1 (Very slow)
Weakness: Acid
Description: Ancient stone-skinned guardian of the mountain
  passes. Regenerates HP each turn unless acid is applied.
  Target the legs to slow it first.
```

```
# data/spellbook.txt
# Create this file manually in VS Code

--- HEAL ---
MP Cost: 10
Effect: Restore 30 HP instantly. Cannot exceed max HP.
Flavour: The golden light of restoration fills the wound.

--- FIREBALL ---
MP Cost: 25
Effect: Deal 40 damage to all enemies within 150px.
Flavour: A sphere of pure heat, hurled from the palm.

--- GHOST STEP ---
MP Cost: 15
Effect: Move through walls for 3 seconds.
Flavour: Your body becomes briefly insubstantial. The
  stones of the wall pass through you like cold smoke.
```

Now write the Python:

```python
# file_reader.py
# Name:
# Date:

import os

MANUAL_PATH   = "data/monster_manual.txt"
SPELLBOOK_PATH = "data/spellbook.txt"


def read_monster_manual():
    # Step 1: Check if MANUAL_PATH exists using os.path.exists()
    #         If it doesn't, return "Monster Manual not found."
    # Step 2: Open the file in "r" mode and return f.read()
    pass


def read_spellbook():
    # Step 3: Same pattern — check exists, open, return f.read()
    pass


def display_file(content, title):
    # Step 4: Print a decorated title bar
    width = 50
    print("\n" + "═" * width)
    print(f"  {title.upper()}")
    print("═" * width)

    # Step 5: Split content on blank lines ("\n\n") to get sections
    # Step 6: Loop over sections, print each one, then print a divider line
    pass


# ── Test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    display_file(read_monster_manual(), "Monster Manual")
    print()
    display_file(read_spellbook(), "Spellbook")
```

### 🧪 Test Your Program

Run `python file_reader.py` from your project folder.

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Monster Manual displays | All 3 monsters print with their stats and descriptions | |
| 2 | Spellbook displays | All 3 spells print with cost, effect, and flavour | |
| 3 | Rename `monster_manual.txt` temporarily | Returns "Monster Manual not found." — no crash | |
| 4 | Add a 4th monster to the text file, rerun | New monster appears — no Python code changed | |
| 5 | Open the `.txt` files in VS Code | They are human-readable without any Python | |

> **Answer this question before moving on:**
>
> You added a 4th monster by editing only the `.txt` file — no Python changes. What principle does this demonstrate? Why is keeping data in a separate file better than hard-coding it as a Python list?
>
> *(your answer here)*

---

---

## Checkpoint 3 — The Main Menu 🏰

### 📋 Your Task

Every game needs a front door. Before the player enters the world, they should see a menu that gives them control. You will build a fully functional Pygame main menu with five options:

1. **New Game** — start fresh, clear any existing save
2. **Load Game** — resume from save (greyed out if no save exists)
3. **Monster Manual** — read from file and display on screen
4. **Spellbook** — read from file and display on screen
5. **Quit** — exit cleanly

This menu will become the first thing players see when `main.py` runs.

### 🧠 Understand It First

A Pygame menu is a loop just like the game loop — except instead of updating sprites, you draw text and wait for mouse clicks or key presses.

**The core pattern:**

```python
# A menu is a state — the game is either in "menu" state or "playing" state
class Game:
    def __init__(self):
        self.state = "menu"    # start in menu, switch to "playing" after selection

    def run(self):
        while True:
            if self.state == "menu":
                self.main_menu()
            elif self.state == "playing":
                self.level.run()
```

**Drawing text in Pygame:**

```python
font  = pygame.font.SysFont("monospace", 36, bold=True)
label = font.render("New Game", True, (255, 255, 255))   # True = anti-aliased
screen.blit(label, (100, 200))                           # blit at (x, y)
```

**Detecting mouse clicks on text:**

```python
# Get the rectangle of the label so we can check if the mouse is inside it
label_rect = label.get_rect(center=(640, 360))
screen.blit(label, label_rect)

for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if label_rect.collidepoint(event.pos):
            print("New Game clicked!")
```

**Hover highlighting** — check if the mouse is over the rect each frame:

```python
mouse_pos = pygame.mouse.get_pos()
color = (255, 215, 0) if label_rect.collidepoint(mouse_pos) else (200, 200, 200)
label = font.render("New Game", True, color)
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| `Menu` class in `menu.py` | Handles all menu drawing and click detection |
| Five menu items | New Game, Load Game, Monster Manual, Spellbook, Quit — each on its own line |
| Hover highlight | Hovered item turns gold; others stay white/grey |
| "Load Game" greyed out | If `savegame.json` does not exist, Load Game is grey and unclickable |
| Monster Manual screen | Clicking Monster Manual reads the file and displays it on screen; any key returns to menu |
| Spellbook screen | Same pattern as Monster Manual |
| State in `Game` | `self.state` is `"menu"` at start; transitions to `"playing"` on New Game or Load Game |
| Title and crown | Display the game title and a decorative subtitle on the menu background |

### 💡 Hints

- Store menu items as a list of dicts: `{"label": "New Game", "action": "new_game"}` — loop over them to draw and check clicks
- `os.path.exists("savegame.json")` tells you if a save exists — check this each frame so the menu updates if a save is created mid-session
- For the text display screens (Monster Manual, Spellbook), split the content into lines and blit each one at increasing Y positions: `y += line_height`
- A simple "press any key to return" loop: `waiting = True; while waiting: for event in ...: if event.type == KEYDOWN: waiting = False`
- `pygame.font.SysFont("monospace", size)` uses a system font — no font file needed

### 🖊️ Your Code

```python
# menu.py
# Name:
# Date:

import pygame
import os
import sys
from file_reader import read_monster_manual, read_spellbook

SAVE_FILE = "savegame.json"


class Menu:
    def __init__(self, screen):
        self.screen       = screen
        self.width        = screen.get_width()
        self.height       = screen.get_height()

        # Fonts
        self.font_title   = pygame.font.SysFont("monospace", 56, bold=True)
        self.font_item    = pygame.font.SysFont("monospace", 32)
        self.font_sub     = pygame.font.SysFont("monospace", 18)
        self.font_content = pygame.font.SysFont("monospace", 16)

        # Colours
        self.COLOR_BG      = (20,  20,  35)
        self.COLOR_TITLE   = (201, 168, 76)   # gold
        self.COLOR_ITEM    = (220, 220, 220)  # light grey
        self.COLOR_HOVER   = (255, 215, 0)    # bright gold
        self.COLOR_DISABLED= (90,  90,  90)   # dark grey — unclickable
        self.COLOR_RULE    = (60,  60,  90)   # divider lines

        # Menu items — label, action string, and whether they can be disabled
        self.items = [
            {"label": "New Game",       "action": "new_game"},
            {"label": "Load Game",      "action": "load_game"},
            {"label": "Monster Manual", "action": "monster_manual"},
            {"label": "Spellbook",      "action": "spellbook"},
            {"label": "Quit",           "action": "quit"},
        ]

    def _save_exists(self):
        return os.path.exists(SAVE_FILE)

    def _draw_title(self):
        # Step 1: Render the game title in gold, centred near the top
        title = self.font_title.render("REBUILDING THE KINGDOM", True, self.COLOR_TITLE)
        rect  = title.get_rect(center=(self.width // 2, 140))
        self.screen.blit(title, rect)

        # Step 2: Render a decorative subtitle below it
        sub = self.font_sub.render("~ The kingdom fell. Rise and reclaim it. ~", True, (150, 130, 80))
        sub_rect = sub.get_rect(center=(self.width // 2, 200))
        self.screen.blit(sub, sub_rect)

        # Step 3: Draw a horizontal rule below the subtitle
        pygame.draw.line(self.screen, self.COLOR_RULE,
                         (self.width // 4, 225), (3 * self.width // 4, 225), 1)

    def _draw_items(self, mouse_pos):
        # Step 4: Loop over self.items with enumerate
        #         Calculate Y position: start at 290, add i * 65 each item
        #         For each item:
        #           - Determine if it is disabled (Load Game when no save exists)
        #           - Choose colour: DISABLED, HOVER (if mouse over), or ITEM
        #           - Render the label text
        #           - Get rect centred horizontally at the correct Y
        #           - Blit to screen
        #           - Return a list of (rect, action) tuples so run() can detect clicks
        rects = []
        for i, item in enumerate(self.items):
            y = 290 + i * 65

            # Determine colour
            disabled = (item["action"] == "load_game" and not self._save_exists())
            rect = None   # replace with actual rect after rendering

            rects.append((rect, item["action"], disabled))
        return rects

    def _show_text_screen(self, content, title):
        # Step 5: Fill the screen with a dark background
        # Step 6: Draw the title at the top using font_title
        # Step 7: Split content into lines using content.split("\n")
        # Step 8: Loop over lines, blit each with font_content at increasing Y
        #         Start Y at 120, add 20 each line
        #         Skip lines that would go off the bottom of the screen
        # Step 9: Draw "Press any key to return..." at the bottom
        # Step 10: Update the display
        # Step 11: Wait for a KEYDOWN event, then return
        pass

    def run(self):
        # Step 12: Main menu loop
        # Each iteration:
        #   - Fill background
        #   - Draw title
        #   - Get mouse position
        #   - Draw items, get list of (rect, action, disabled) back
        #   - Loop over pygame events:
        #       QUIT → pygame.quit() and sys.exit()
        #       MOUSEBUTTONDOWN → check each rect for collidepoint
        #           if disabled → do nothing
        #           "new_game"       → return "new_game"
        #           "load_game"      → return "load_game"
        #           "monster_manual" → call _show_text_screen(read_monster_manual(), "Monster Manual")
        #           "spellbook"      → call _show_text_screen(read_spellbook(), "Spellbook")
        #           "quit"           → pygame.quit(); sys.exit()
        #   - pygame.display.update()
        pass
```

```python
# Update main.py — add menu state management

import pygame
import sys
from settings    import SCREEN, FPS, COLORS
from level       import Level
from menu        import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption("Rebuilding the Kingdom")
        self.clock  = pygame.time.Clock()
        self.state  = "menu"        # start in the menu
        self.level  = None          # Level created only when game starts

    def start_new_game(self):
        # Remove any existing save file so New Game is truly fresh
        import os
        if os.path.exists("savegame.json"):
            os.remove("savegame.json")
        self.level = Level()
        self.state = "playing"

    def start_load_game(self):
        self.level = Level()        # Level.__init__ will auto-load the save (Checkpoint 4)
        self.state = "playing"

    def run(self):
        menu = Menu(self.screen)

        while True:
            if self.state == "menu":
                choice = menu.run()         # blocks until a choice is made
                if choice == "new_game":
                    self.start_new_game()
                elif choice == "load_game":
                    self.start_load_game()

            elif self.state == "playing":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.state = "menu"     # press Escape to return to menu
                self.screen.fill(COLORS["bg"])
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == "__main__":
    Game().run()
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Game launches | Main menu appears — dark background, gold title, five items | |
| 2 | Hover over menu items | Hovered item turns gold | |
| 3 | No `savegame.json` exists | "Load Game" is grey and does not respond to clicks | |
| 4 | Click "Monster Manual" | Text screen appears with all monsters; any key returns to menu | |
| 5 | Click "Spellbook" | Spellbook content displays; any key returns | |
| 6 | Click "New Game" | Game world appears with player and enemies | |
| 7 | Press Escape in-game | Returns to main menu | |
| 8 | Click "Quit" | Game closes cleanly | |

> **Answer this question before moving on:**
>
> `self.state` is just a string — `"menu"` or `"playing"`. In your own words, explain why using a state variable is better than having one giant function that tries to handle menus and gameplay at the same time.
>
> *(your answer here)*

---

---

## Checkpoint 4 — JSON: The Royal Save System 💾

### 📋 Your Task

Plain text files work for human-readable documents like the Monster Manual. But your player's stats are a Python dictionary. Writing it as text and reading it back manually would require parsing code for every key. **JSON** solves this — it converts Python dictionaries and lists to text automatically, and reads them back just as easily.

You will build a complete save and load system: pressing `S` saves the game, the Level auto-loads on startup if a save exists, and corrupted saves are handled gracefully.

### 🧠 Understand It First

**What is JSON?**

JSON is a text format that looks almost exactly like Python dictionaries and lists:

```
Python dict                     JSON file (savegame.json)
──────────────────────          ──────────────────────────────────────
{"HP": 85, "Gold": 340}    →   {
                                    "HP": 85,
                                    "Gold": 340
                                }
```

The two main functions you need:

```python
import json

# SAVING — write Python data to a JSON file
data = {"HP": 85, "Gold": 340, "Level": 3}
with open("savegame.json", "w") as f:
    json.dump(data, f, indent=4)    # indent=4 makes it human-readable
# savegame.json now exists on disk

# LOADING — read JSON file back into Python
with open("savegame.json", "r") as f:
    loaded = json.load(f)           # loaded is now a Python dict
print(loaded["HP"])   # 85
```

**Why not just use `f.write(str(data))`?**

```python
# DON'T do this:
f.write(str({"HP": 85, "Gold": 340}))
# Reads back as a STRING — you'd have to use eval() to convert it back
# eval() is dangerous and fragile — never use it for save files

# DO this instead:
json.dump(data, f)
# json.load() converts it back perfectly, safely, every time
```

**One gotcha — Vector2 is not JSON-serialisable:**

```python
# pygame.math.Vector2 cannot be saved directly as JSON
# Convert it to a list first:
"position": list(self.player.pos)    # [416.0, 288.0]

# Load it back like this:
self.player.pos = pygame.math.Vector2(data["position"])
```

**What if the file is corrupted or missing a key?**

```python
try:
    with open("savegame.json", "r") as f:
        data = json.load(f)
    player.stats = data["stats"]          # KeyError if "stats" is missing
except FileNotFoundError:
    print("No save file found — starting fresh.")
except json.JSONDecodeError:
    print("Save file is corrupted — starting fresh.")
except KeyError as e:
    print(f"Save file is missing key {e} — starting fresh.")
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| `save_load.py` — new file | Contains `save_game()`, `load_game()`, `delete_save()` |
| `save_game(player, defeated_bosses, play_time)` | Writes stats, position, inventory, defeated_bosses, play_time to `savegame.json` |
| `load_game(player)` | Reads JSON, restores all fields. Returns `(defeated_bosses, play_time)` tuple. If file missing or corrupted → returns `([], 0)` |
| `delete_save()` | Removes `savegame.json` if it exists |
| Auto-load in `Level.__init__` | After `_create_map()`, call `load_game(self.player)` — saves load transparently |
| `S` key saves | Handle `pygame.K_s` in Level events |
| `"Load Game"` now works | Because auto-load runs on Level creation, "Load Game" from menu just creates the Level |
| `try/except` for 3 error types | FileNotFoundError, json.JSONDecodeError, KeyError |

### 💡 Hints

- `import time` — `self.session_start = time.time()` stores when this session began; add it to `self.play_time` when saving to get the total
- `data.get("inventory", [])` — use `.get()` with a default when loading optional fields, in case older saves don't have that key yet
- Add `play_time` to `self.level` as `self.play_time = 0`; update it on save; display it in the HUD later
- After deleting the save with `start_new_game()`, the menu's "Load Game" option will automatically grey out (because `_save_exists()` checks in real time)

### 🖊️ Your Code

```python
# save_load.py
# Name:
# Date:

import json
import os
import pygame

SAVE_FILE = "savegame.json"


def save_game(player, defeated_bosses, play_time):
    """
    Serialise the complete game state to savegame.json.
    Called when the player presses S.
    """
    # Step 1: Build the save data dictionary
    #         Include: stats, position (as a list), inventory, defeated_bosses, play_time
    data = {
        "stats":           player.stats,
        "position":        list(player.pos),    # Vector2 → [x, y]
        "inventory":       player.inventory,
        "defeated_bosses": defeated_bosses,
        "play_time":       play_time,
    }

    # Step 2: Write to SAVE_FILE using "w" mode and json.dump()
    #         Use indent=4 so humans can read the file in VS Code


    # Step 3: Print a confirmation message with the player's level


def load_game(player):
    """
    Load game state from savegame.json into the player object.
    Returns (defeated_bosses, play_time) so Level can store them.
    Returns ([], 0) if file is missing, corrupted, or has wrong keys.
    """
    # Step 4: Wrap everything in try/except for three error types:
    #         FileNotFoundError, json.JSONDecodeError, KeyError
    try:
        # Step 5: Open SAVE_FILE in "r" mode, call json.load(f)

        # Step 6: Restore player.stats from data["stats"]

        # Step 7: Restore player.pos as a Vector2 from data["position"]
        #         player.pos = pygame.math.Vector2(data["position"])
        #         Also sync: player.rect.topleft = (int(player.pos.x), int(player.pos.y))

        # Step 8: Restore player.inventory using data.get("inventory", [])

        # Step 9: Print a load confirmation showing Level and play time

        # Step 10: Return (data.get("defeated_bosses", []), data.get("play_time", 0))
        pass

    except FileNotFoundError:
        print("No save file found — starting fresh.")
        return [], 0

    except json.JSONDecodeError:
        print("Save file is corrupted — starting fresh.")
        return [], 0

    except KeyError as e:
        print(f"Save file is missing a field ({e}) — starting fresh.")
        return [], 0


def delete_save():
    """Remove the save file. Called when starting a New Game."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("Save file deleted — starting fresh.")
    else:
        print("No save file to delete.")
```

```python
# Update level.py — add save/load wiring

import time
import sys
import pygame
from save_load import save_game, load_game

class Level:
    def __init__(self):
        self.display_surface  = pygame.display.get_surface()
        self.visible_sprites  = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.defeated_bosses = []
        self.play_time       = 0
        self.session_start   = time.time()

        self._create_map()

        # Auto-load — if savegame.json exists, restore state immediately
        self.defeated_bosses, self.play_time = load_game(self.player)

    def _get_total_play_time(self):
        # Returns total play time: saved time + time since this session started
        return self.play_time + int(time.time() - self.session_start)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    save_game(self.player, self.defeated_bosses, self._get_total_play_time())
                    # Step 11: Add any other key handlers here (B for shop, etc.)

    def run(self):
        self.handle_events()
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)   # or .draw() if no camera yet
```

### 🧪 Test Your Program

After running the game, open `savegame.json` in VS Code. You should be able to read it clearly.

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Click New Game, move, collect gold, press `S` | `savegame.json` appears in your project folder | |
| 2 | Open `savegame.json` in VS Code | Readable JSON with all stats, position, inventory | |
| 3 | Close game, reopen, click Load Game | Player appears at the exact saved position with correct stats | |
| 4 | Load Game is now clickable in the menu | Because `savegame.json` exists and `_save_exists()` returns `True` | |
| 5 | Click New Game | `savegame.json` is deleted; Load Game greys out again | |
| 6 | Manually corrupt `savegame.json` (delete a `}`) | Game starts fresh and prints corruption warning — no crash | |
| 7 | Delete `savegame.json` entirely, try Load Game | Should be greyed out — this case should be impossible by design | |

> **Answer these questions before moving on:**
>
> 1. Your player's stats are already a dictionary. Why does that make saving with `json.dump()` almost effortless compared to writing each stat as a separate line in a text file?
>
>    *(your answer here)*
>
> 2. You have `try/except` catching three different errors. What specific scenario causes each one? (FileNotFoundError, json.JSONDecodeError, KeyError)
>
>    *(your answer here)*

---

---

## Checkpoint 5 — The In-Game Reference Screens 📜

### 📋 Your Task

The Monster Manual and Spellbook are already readable from the main menu. Now bring them into the game world — a player should be able to press `M` mid-game to open the Monster Manual and `P` to open the Spellbook, displayed as a semi-transparent overlay without leaving the game. The world pauses while the overlay is open.

This checkpoint also adds **enemy entries to the Monster Manual** that update dynamically — enemies the player has defeated show a `[DEFEATED]` tag.

### 🧠 Understand It First

**A pause overlay** is drawn over the top of the game world but under the HUD. The trick is to draw everything in the right order:

```
Draw order (bottom to top):
1. Background fill
2. Game world (sprites)
3. Overlay surface (semi-transparent)  ← new
4. Text on the overlay
5. HUD
```

**Semi-transparent surfaces in Pygame:**

```python
# Create a dark translucent panel
overlay = pygame.Surface((800, 500), pygame.SRCALPHA)
overlay.fill((20, 20, 35, 200))    # RGBA — 200 is alpha (0=invisible, 255=opaque)
screen.blit(overlay, (240, 110))   # blit at position (x, y)
```

**Splitting long text across multiple lines:**

```python
content = read_monster_manual()
lines   = content.split("\n")

y = start_y
for line in lines:
    if y > max_y:
        break                          # stop before going off screen
    label = font.render(line, True, color)
    screen.blit(label, (start_x, y))
    y += line_height
```

### ✅ Requirements

| Requirement | Details |
|---|---|
| `ReferenceOverlay` class in `overlay.py` | Handles drawing and paging for both Manual and Spellbook |
| `show(content, title)` method | Draws the overlay, renders the text page by page, waits for key input |
| Page through content | If content is more than ~20 lines, pressing any key advances to the next page; `Q` or `Escape` exits |
| `[DEFEATED]` tags | Pass `defeated_bosses` into `show()`. If a monster name appears in the list, add `[DEFEATED]` |
| `M` key in game | Opens Monster Manual overlay — game loop continues drawing behind it |
| `P` key in game | Opens Spellbook overlay |
| Returns to game | After closing the overlay, the game resumes exactly where it was |

### 💡 Hints

- `overlay.py` imports `read_monster_manual` and `read_spellbook` from `file_reader.py` — no duplication
- Pass `defeated_bosses` as a parameter: `overlay.show(content, "Monster Manual", defeated_bosses)`
- To add `[DEFEATED]` tags: loop over lines, and if `"--- " in line`, extract the name and check if it's in `defeated_bosses`
- For paging: collect lines into pages of 20, track `current_page`, advance on key press
- Handle `M` and `P` key presses in `Level.handle_events()` alongside `S` for save

### 🖊️ Your Code

```python
# overlay.py
# Name:
# Date:

import pygame
from file_reader import read_monster_manual, read_spellbook


class ReferenceOverlay:
    def __init__(self, screen):
        self.screen      = screen
        self.width       = screen.get_width()
        self.height      = screen.get_height()
        self.font_title  = pygame.font.SysFont("monospace", 28, bold=True)
        self.font_body   = pygame.font.SysFont("monospace", 15)
        self.font_footer = pygame.font.SysFont("monospace", 13)

        # Overlay panel dimensions
        self.panel_x   = 80
        self.panel_y   = 60
        self.panel_w   = self.width  - 160
        self.panel_h   = self.height - 120
        self.lines_per_page = 24

    def _build_pages(self, content, defeated_bosses):
        # Step 1: Split content on "\n" into a list of lines
        # Step 2: Loop over lines — if "---" is in the line, extract the monster/spell name
        #         Check if that name (lowercase) appears in defeated_bosses (also lowercase)
        #         If yes, append "  [DEFEATED]" to the line
        # Step 3: Split the list of lines into pages of self.lines_per_page
        #         pages = [lines[0:24], lines[24:48], ...]
        #         Use a list comprehension with range(0, len(lines), self.lines_per_page)
        pass

    def show(self, source, title, defeated_bosses=None):
        """
        Display content as a full-screen overlay.
        source: either "manual" or "spellbook"
        """
        if defeated_bosses is None:
            defeated_bosses = []

        content = read_monster_manual() if source == "manual" else read_spellbook()
        pages   = self._build_pages(content, defeated_bosses)

        if not pages:
            return

        current_page = 0
        showing      = True

        while showing:
            # Step 4: Draw the overlay panel
            panel = pygame.Surface((self.panel_w, self.panel_h), pygame.SRCALPHA)
            panel.fill((15, 15, 30, 220))
            self.screen.blit(panel, (self.panel_x, self.panel_y))

            # Step 5: Draw title
            title_surf = self.font_title.render(title.upper(), True, (201, 168, 76))
            self.screen.blit(title_surf, (self.panel_x + 20, self.panel_y + 15))

            # Step 6: Draw the current page's lines
            y = self.panel_y + 60
            for line in pages[current_page]:
                color = (201, 168, 76) if "---" in line else (200, 200, 200)
                if "[DEFEATED]" in line:
                    color = (100, 200, 100)    # green for defeated
                surf = self.font_body.render(line, True, color)
                self.screen.blit(surf, (self.panel_x + 20, y))
                y += 22

            # Step 7: Draw footer
            page_info = f"Page {current_page + 1} of {len(pages)}"
            nav_hint  = "[ Any key: next page   Q / Esc: close ]"
            footer    = self.font_footer.render(f"{page_info}   {nav_hint}", True, (120, 120, 120))
            self.screen.blit(footer, (self.panel_x + 20, self.panel_y + self.panel_h - 30))

            pygame.display.update()

            # Step 8: Wait for a key press
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); import sys; sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_q, pygame.K_ESCAPE):
                        showing = False
                    elif current_page < len(pages) - 1:
                        current_page += 1
                    else:
                        showing = False   # last page — any key closes
```

```python
# Update level.py — add overlay and new key bindings

from overlay import ReferenceOverlay

class Level:
    def __init__(self):
        # ... existing init code ...
        self.overlay = ReferenceOverlay(self.display_surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    save_game(self.player, self.defeated_bosses, self._get_total_play_time())
                if event.key == pygame.K_m:
                    # Show Monster Manual — pass defeated_bosses so [DEFEATED] tags appear
                    self.overlay.show("manual", "Monster Manual", self.defeated_bosses)
                if event.key == pygame.K_p:
                    # Show Spellbook
                    self.overlay.show("spellbook", "Spellbook")
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Press `M` in-game | Monster Manual overlay appears over the game world | |
| 2 | Page through content | Next key advances page; Q or Escape closes | |
| 3 | Press `P` in-game | Spellbook appears | |
| 4 | Defeat an enemy (add it to `defeated_bosses`), press `M` | That monster shows `[DEFEATED]` in green | |
| 5 | Close overlay | Game resumes exactly as left — player has not moved | |
| 6 | Manual also accessible from main menu | Both entry points use the same `read_monster_manual()` function | |

> **Answer this question before moving on:**
>
> The Monster Manual text file is read by both the main menu and the in-game overlay, but you only wrote `read_monster_manual()` once. What software principle does this follow, and why does it matter when you want to add a new monster?
>
> *(your answer here)*

---

---

## 🏁 Reflection Questions

Answer in your own words.

1. What is the difference between `"r"`, `"w"`, and `"a"` file modes? Give a game-specific example of when you would use each one.

   > *(your answer here)*

2. You stored the Monster Manual as a plain `.txt` file rather than in a Python list. What is the advantage of this — especially for a non-programmer who wants to add monsters to the game?

   > *(your answer here)*

3. Why is `json.dump()` better than `f.write(str(my_dict))` for saving a Python dictionary? What would go wrong trying to read the data back with the string approach?

   > *(your answer here)*

4. Your save system catches `FileNotFoundError`, `json.JSONDecodeError`, and `KeyError`. Write a one-sentence description of the real-world event that causes each one.

   > *(your answer here)*

5. The `with open(...) as f:` pattern closes the file automatically. What could go wrong if you forgot to close a file manually — and why is this especially important when writing?

   > *(your answer here)*

6. The `"Load Game"` menu option greys out when no save file exists. This is a design decision. What would happen to the user experience if you let them click it anyway?

   > *(your answer here)*

7. What was the most confusing part of this unit, and what helped you push through it?

   > *(your answer here)*

---

## What Changed From Unit 2

| File | What changed | Why |
|---|---|---|
| `main.py` | Added `self.state`, `start_new_game()`, `start_load_game()` | Game now has a menu phase and a playing phase |
| `menu.py` | Created | Main menu with five options and dynamic Load Game state |
| `save_load.py` | Created | All save/load logic isolated in one place |
| `file_reader.py` | Created | Reads Monster Manual and Spellbook from disk |
| `overlay.py` | Created | In-game reference overlay with paging and defeated tags |
| `level.py` | Added `handle_events()`, auto-load in `__init__`, `M`/`P`/`S` key handling | Level now owns its own event loop |
| `data/` folder | Created | Holds `monster_manual.txt` and `spellbook.txt` |

---

## How This Connects to the Rest of the Year

```
Unit 3 — File I/O  (this unit)
    save_load.py saves self.stats dict → json.dump() → savegame.json
    menu.py controls game state and reads lore files
         ↓
Unit 4 — Libraries
    support.py uses os.walk() — same os module you used here
    import_csv_layout() reads Tiled CSV files — same open() pattern
    random powers loot drops when chests are opened
         ↓
Unit 5 — End-of-Term Project
    Tiled map layers are read as CSV files using your import_csv_layout()
    Save system carries forward — your final game saves and loads automatically
    Monster Manual updates as players explore new zones
```

---

*Previous → [Unit 2 — The Ledger and the Treasury](./unit2_data_structures.md)*  
*Next → [Unit 4 — The Guild Contracts](./unit4_libraries.md)*
