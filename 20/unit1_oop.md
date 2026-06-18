# Unit 1 — The Blueprints of the Kingdom 🏗️
### Object-Oriented Programming · *the backbone of all 5 units*

**Topics Covered:** `class`, `__init__`, `self`, `super()`, inheritance, encapsulation, polymorphism, `pygame.sprite.Sprite`, sprite groups  
**Instructions:** Complete all checkpoints in order. Each one builds directly on the previous one. Do not skip ahead — the concepts stack.

> *"The architects have arrived. To rebuild the kingdom we need more than raw stone — we need blueprints. Every hero, enemy, building, and creature must be designed as a class before a single pixel appears on screen."*

---

## Why Are We Doing This?

In Grade 10 you wrote standalone functions. That worked well for a single hero fighting a single boss — but now the kingdom needs rebuilding. That means:

- Many heroes and enemies, each with their own HP, speed, and behaviour
- Objects that update themselves every frame without you calling them one by one
- A structure that grows cleanly across the whole year

**Object-Oriented Programming (OOP)** solves all of this. Instead of writing separate variables and functions for each character, you write a **class** — a blueprint — and stamp out as many copies as you need. Each copy is called an **instance**, and it owns its own data.

> ⚠️ **OOP is not just a Unit 1 topic.** The classes you write today will be expanded in Units 2, 3, 4, and 5. You are not writing throwaway practice code — you are building the engine of your game.

---

## Key Vocabulary

Study these before you write a single line of code. You will see every one of them today.

| Term | Plain English meaning |
|---|---|
| `class` | The blueprint. Defines what data and behaviour an object has. |
| `instance` | One specific object made from a class. `arthur = Knight("Arthur")` creates an instance. |
| `__init__` | The **constructor**. Runs automatically the moment you create an instance. |
| `self` | Inside a class, `self` means "this specific instance." It is always the first parameter. |
| `attribute` | A variable that belongs to an instance. Written as `self.hp`, `self.name`, etc. |
| `method` | A function that belongs to a class. Always has `self` as the first parameter. |
| `inherit` | When one class gets all the features of another class automatically. |
| `super()` | Calls the parent class's version of a method so you don't have to rewrite it. |
| `override` | When a child class replaces a parent method with its own version. |

---

## The Four Pillars of OOP

You don't need to memorise these today, but you will see them come up naturally as you build.

| Pillar | What it means | You will see it when... |
|---|---|---|
| **Encapsulation** | Data lives inside the class that owns it | `self.hp` lives in `Knight`, not floating in `main.py` |
| **Inheritance** | A child class gets the parent's features for free | `Player` and `Enemy` both get `take_damage()` from `Entity` |
| **Abstraction** | Hide complicated logic behind a simple method name | `enemy.update()` hides all the AI — the caller doesn't need to know how |
| **Polymorphism** | Same method name, completely different behaviour | `player.update()` reads keys; `enemy.update()` chases the player |

---

## How to Read the Code Examples

Throughout this guide, code examples include inline comments explaining *why* — not just *what*:

```python
class Knight:                    # defines the blueprint
    def __init__(self, name):    # constructor — runs at creation
        self.name = name         # self.name is an attribute belonging to this instance
```

Read every comment. They are there to build your understanding, not to be skipped.

---

---

## Checkpoint 1 — Your First Class (No Pygame) 🧱

### 📋 Your Task

Before we touch Pygame at all, you are going to prove that you understand what a class is, what `self` means, and what `__init__` does — using nothing but plain Python in the terminal.

We will build a `Knight` class from scratch. A Knight has a name and HP, and can take damage or heal. You will create two independent Knights and show that changing one does **not** affect the other — that is the whole point of instances.

### 🧠 Understand It First

A class is like a cookie cutter. The cutter is the class. Each cookie it cuts is an instance.

```
Knight class (the cutter)
│
├── __init__(self, name, hp)    ← runs when a new Knight is created
├── take_damage(self, amount)   ← something every Knight can do
├── heal(self, amount)          ← something every Knight can do
└── status(self)                ← something every Knight can report
```

When you write `arthur = Knight("Arthur", 100)`, Python:
1. Creates a brand new empty object
2. Calls `__init__` automatically, passing `"Arthur"` and `100`
3. Inside `__init__`, `self` points to that new object
4. `self.name = "Arthur"` stores the name *on that object*
5. `self.hp = 100` stores the HP *on that same object*

When you then write `lancelot = Knight("Lancelot", 80)`, Python creates a *completely separate* object. `arthur` and `lancelot` each have their own `name` and `hp`. They do not share anything.

**This is the most important concept in the unit.** Read it twice before continuing.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `class Knight` | Define a class with `__init__(self, name, hp)` |
| `self.name`, `self.hp`, `self.max_hp` | Store all three in `__init__`. Set `max_hp = hp` right away. |
| `take_damage(self, amount)` | Subtract amount from `self.hp`. If HP hits 0 or below, set it to 0 and print `"{name} has fallen!"` |
| `heal(self, amount)` | Add amount to `self.hp` but never let it exceed `self.max_hp`. Use `min()`. |
| `status(self)` | Return a formatted string: `"Arthur | HP: 70/100"` |
| Two instances | Create `arthur` (100 HP) and `lancelot` (80 HP) |
| Show independence | Damage one, heal the other, print both statuses to prove they are independent |

### 💡 Hints

- `def __init__(self, name, hp):` — `self` is always the first parameter, Python passes it automatically
- `self.max_hp = hp` — save the starting HP as the max right away in `__init__`, before anything changes
- `self.hp = min(self.hp + amount, self.max_hp)` — `min()` picks the smaller of two values, which caps healing at the maximum
- `return f"{self.name} | HP: {self.hp}/{self.max_hp}"` — f-strings work inside methods using `self` attributes
- You do **not** need to import anything for this checkpoint. No Pygame. Just Python.

### 🖊️ Your Code

```python
# Checkpoint 1: Your First Class
# Name:
# Date:

# Step 1: Define the Knight class
class Knight:

    # Step 2: Write __init__
    #         Parameters: self, name, hp
    #         Store: self.name, self.hp, self.max_hp


    # Step 3: Write take_damage(self, amount)
    #         Subtract amount from self.hp
    #         If self.hp drops to 0 or below: set to 0, print that they have fallen


    # Step 4: Write heal(self, amount)
    #         Add amount to self.hp
    #         Use min() to make sure it never exceeds self.max_hp


    # Step 5: Write status(self)
    #         Return a formatted string: "Name | HP: current/max"


# Step 6: Create two Knight instances — different names, different HP values


# Step 7: Deal damage to one, heal the other
#         Print both statuses to prove they are independent
```

### 🧪 Test Your Program

Run `python checkpoint1.py` and fill in the table:

| Test | Action | Expected output | ✓ |
|---|---|---|---|
| 1 | `arthur.take_damage(30)` then `print(arthur.status())` | `Arthur \| HP: 70/100` | |
| 2 | `lancelot.take_damage(90)` | Prints `"Lancelot has fallen!"` | |
| 3 | `arthur.heal(999)` | HP stays at `max_hp`, not above | |
| 4 | Check `lancelot.hp` after only damaging arthur | Should still be 80 — instances are independent | |

> **Answer this question before moving on:**
>
> After you call `arthur.take_damage(30)`, what is `lancelot.hp`? Why does damaging Arthur not affect Lancelot?
>
> *(your answer here)*

---

---

## Checkpoint 2 — Inheritance: One Blueprint, Many Specialisations 🧬

### 📋 Your Task

Now we introduce **inheritance**. Instead of writing a completely separate class for Player and Enemy, we create a shared **parent class** called `Entity` that holds everything they have in common. Each child class only defines what makes it different.

This is the exact structure you will use for your entire game.

### 🧠 Understand It First

Picture the relationship as a family tree:

```
Entity  (parent — shared features)
│   name, hp, max_hp, alive
│   take_damage(), heal()
│
├── Player  (child — gets Entity's features for free, adds its own)
│       gold, level
│       collect_gold(), level_up()
│
└── Enemy   (child — gets Entity's features for free, adds its own)
        damage
        attack()
```

The key line in any child class is `super().__init__(...)`. It calls the **parent's** `__init__` so all the shared setup happens automatically. Without it, `self.hp`, `self.name`, and everything else from Entity would never get created, and your child class would crash immediately.

```python
class Player(Entity):               # Player inherits FROM Entity
    def __init__(self, name, hp):
        super().__init__(name, hp)  # run Entity's __init__ first — sets up hp, name, etc.
        self.gold = 0               # then add Player-specific attributes
```

Another important concept here is `__repr__`. This is a special method Python calls automatically when you `print()` an object. If you write it in `Entity` using `self.__class__.__name__`, it will print the actual subclass name — `"Player"` or `"Enemy"` — not `"Entity"`. That is polymorphism quietly at work.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `class Entity` | `__init__(self, name, hp)` storing `self.name`, `self.hp`, `self.max_hp`, `self.alive = True` |
| Move methods | Move `take_damage()` and `heal()` from Checkpoint 1 into `Entity`. Set `self.alive = False` when HP hits 0. |
| `__repr__` on Entity | Returns `"ClassName(name, HP:current)"` using `self.__class__.__name__` |
| `class Player(Entity)` | Calls `super().__init__()`. Adds `self.gold = 0` and `self.level = 1`. Has `collect_gold()` and `level_up()`. |
| `class Enemy(Entity)` | Calls `super().__init__()`. Adds `self.damage`. Has `attack(self, target)` that calls `target.take_damage()`. |
| Test all three | Show Player and Enemy both use `take_damage()` without you rewriting it. |

### 💡 Hints

- `class Player(Entity):` — put the parent class name in the brackets
- `self.__class__.__name__` inside `Entity.__repr__` prints `"Player"` when called on a Player instance, and `"Enemy"` when called on an Enemy — even though the method lives in Entity. This is polymorphism.
- `level_up()` should: increase `self.level` by 1, increase `self.max_hp` by 20, and restore `self.hp` to full
- `attack(self, target)` should call `target.take_damage(self.damage)` — Enemy doesn't need to know anything about Player's internals, just that it has a `take_damage` method

### 🖊️ Your Code

```python
# Checkpoint 2: Inheritance
# Name:
# Date:

# Step 1: Define Entity — the parent class
#         Move take_damage and heal here from Checkpoint 1
#         Add self.alive = True in __init__
#         Add __repr__ using self.__class__.__name__

class Entity:
    pass  # replace with your code


# Step 2: Define Player as a child of Entity
#         super().__init__(name, hp) calls the parent constructor
#         Add self.gold = 0 and self.level = 1
#         Add collect_gold(self, amount) and level_up(self)

class Player(Entity):
    pass  # replace with your code


# Step 3: Define Enemy as a child of Entity
#         super().__init__(name, hp) calls the parent constructor
#         Add self.damage in __init__
#         Add attack(self, target)

class Enemy(Entity):
    pass  # replace with your code


# Step 4: Create one Player and one Enemy
#         Have the enemy attack the player twice
#         Have the player collect gold and level up
#         Print both using print() — __repr__ handles the formatting
```

### 🧪 Test Your Program

| Test | Action | Expected result | ✓ |
|---|---|---|---|
| 1 | `print(player)` | `Player(Arthur, HP:100)` | |
| 2 | `goblin.attack(player)` twice | Player HP drops by `goblin.damage` each time | |
| 3 | `player.level_up()` | Level increases, max_hp increases, HP restores to new max | |
| 4 | `print(goblin)` | `Enemy(Goblin, HP:40)` — says Enemy, not Entity | |
| 5 | `goblin.collect_gold(10)` | Raises `AttributeError` — goblins don't have this method | |

> **Answer these questions before moving on:**
>
> 1. Why do we write `super().__init__(name, hp)` in Player's `__init__`? What goes wrong if you delete that line and test it?
>
>    *(your answer here)*
>
> 2. You only wrote `take_damage()` once — in `Entity`. But `player.take_damage(10)` and `goblin.take_damage(10)` both work. How?
>
>    *(your answer here)*

---

---

## Checkpoint 3 — Pygame Entities: Bringing It On Screen 🎮

### 📋 Your Task

Now we bring OOP into Pygame. The structure mirrors Checkpoint 2 exactly — we have a parent `Entity` and child `Player` / `Enemy` classes — but now `Entity` inherits from `pygame.sprite.Sprite`. This unlocks Pygame's group system, which handles drawing and updating automatically.

Build this file structure and get a moving blue square being chased by red squares.

```
unit1_oop/
├── entity.py    ← write this first
├── player.py
├── enemy.py
├── level.py
└── main.py
```

### 🧠 Understand It First

**Why inherit from `pygame.sprite.Sprite`?**

Pygame's draw system expects every drawable object to have:
- `self.image` — the Surface (pixels) to draw
- `self.rect` — the Rect (position and size) saying where to draw it

When you call `group.draw(screen)`, Pygame reads those two attributes from every sprite in the group and blits them all automatically. You never write `screen.blit()` in a loop yourself.

`super().__init__(groups)` in your Entity's `__init__` registers the sprite with every group you pass in. After that, the group tracks it.

**Why use `pygame.math.Vector2` instead of integers?**

If you store position as integers and press two arrow keys at once (diagonal), you move roughly 1.41× faster than pressing one key (because √2 ≈ 1.41). `Vector2` lets you store position as floats, then **normalize** the direction vector so it always has length 1 before multiplying by speed. Diagonal and cardinal movement end up identical speed.

**What does `group.update()` actually do?**

It calls `sprite.update()` on every sprite in the group — nothing more. Which means if `Player.update()` reads keys and `Enemy.update()` runs AI, then one call to `group.update()` runs all of it. That is the payoff for overriding `update()` in each class.

### ✅ Requirements

| File | Must contain |
|---|---|
| `entity.py` | `Entity(pygame.sprite.Sprite)` — `__init__`, `take_damage`, `heal`, `update` (pass) |
| `player.py` | `Player(Entity)` — `get_input()`, `move()`, `_collide()`, `update()` |
| `enemy.py` | `Enemy(Entity)` — `_distance_to_player()`, `_chase_player()`, `update()` |
| `level.py` | `Level` class — two sprite groups, `_setup_map()`, `run()` |
| `main.py` | `Game` class — pygame init, game loop. Under 25 lines, zero game logic. |

### 💡 Hints

- `super().__init__(groups)` must come **before** you set `self.image` and `self.rect` — Pygame needs to initialise the Sprite internals first
- Reset `self.direction` to `(0, 0)` at the start of every `get_input()` call — otherwise the player keeps moving in the last direction even after releasing the key
- **Two-step collision:** move X → check horizontal collisions → move Y → check vertical collisions. This lets the player slide along walls instead of stopping completely at corners
- `(self.player.pos - self.pos).length()` gives the distance between enemy and player as a single float
- `self.kill()` removes the sprite from all groups with one call — use it inside `take_damage` when HP hits 0

### 🖊️ Your Code

**`entity.py`**
```python
# entity.py
# Name:
# Date:

import pygame

class Entity(pygame.sprite.Sprite):
    """Base class for every living thing in the kingdom."""

    def __init__(self, pos, groups):
        super().__init__(groups)          # registers with every group passed in — must be first

        self.image = pygame.Surface((64, 64), pygame.SRCALPHA)
        self.rect  = self.image.get_rect(topleft=pos)

        # Float position — more precise than storing integers directly in rect
        self.pos       = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2(0, 0)

        self.stats = {
            "HP":     100,
            "max_HP": 100,
            "Attack": 10,
            "Speed":  3,
        }
        self.is_alive = True

    def take_damage(self, amount):
        # Subtract amount, clamp HP to 0, call self.kill() and set is_alive False if HP gone


    def heal(self, amount):
        # Add amount, cap at max_HP using min()


    def update(self):
        pass    # child classes override this
```

**`player.py`**
```python
# player.py
# Name:
# Date:

import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(pos, groups)
        self.image.fill((100, 180, 255))    # blue placeholder
        self.obstacle_sprites = obstacle_sprites
        self.stats["Speed"]   = 5
        self.stats["Gold"]    = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0              # reset every frame
        self.direction.y = 0
        # Set direction.x and direction.y based on WASD and arrow keys


    def move(self):
        # Normalise direction if it has length > 0
        # Move X by direction.x * speed, sync rect.x, call _collide("horizontal")
        # Move Y by direction.y * speed, sync rect.y, call _collide("vertical")


    def _collide(self, axis):
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == "horizontal":
                    # Push rect left or right depending on direction.x
                    # Sync self.pos.x back to self.rect.x
                    pass
                else:
                    # Push rect up or down depending on direction.y
                    # Sync self.pos.y back to self.rect.y
                    pass

    def update(self):
        self.get_input()
        self.move()
```

**`enemy.py`**
```python
# enemy.py
# Name:
# Date:

import pygame
from entity import Entity

class Enemy(Entity):
    def __init__(self, pos, groups, player):
        super().__init__(pos, groups)
        self.image.fill((220, 80, 80))      # red placeholder
        self.player        = player
        self.notice_radius = 200
        self.attack_radius = 50
        self.stats["Attack"] = 8
        self.stats["Speed"]  = 2

    def _distance_to_player(self):
        # Return (self.player.pos - self.pos).length()


    def _chase_player(self):
        # Get the normalised direction toward the player
        # Add direction * speed to self.pos
        # Sync self.rect.topleft to (round(self.pos.x), round(self.pos.y))


    def update(self):
        dist = self._distance_to_player()
        # If within attack_radius  → deal damage to player (scale by 0.016 for ~60fps)
        # Elif within notice_radius → chase the player
        # Otherwise                → stand still
```

**`level.py`**
```python
# level.py
# Name:
# Date:

import pygame
from player import Player
from enemy  import Enemy

class Level:
    def __init__(self):
        self.display_surface  = pygame.display.get_surface()
        self.visible_sprites  = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self._setup_map()

    def _setup_map(self):
        # Create the player at (400, 300) — pass visible_sprites and obstacle_sprites
        self.player = Player(
            pos=(400, 300),
            groups=self.visible_sprites,
            obstacle_sprites=self.obstacle_sprites
        )
        # Spawn three enemies at different positions, each needing a reference to self.player
        for pos in [(100, 100), (600, 200), (300, 500)]:
            Enemy(pos, self.visible_sprites, self.player)

    def run(self):
        self.visible_sprites.update()                    # calls update() on every sprite
        self.visible_sprites.draw(self.display_surface)  # blits image at rect for every sprite
```

**`main.py`**
```python
# main.py
# Name:
# Date:

import pygame
import sys
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Rebuilding the Kingdom")
        self.clock  = pygame.time.Clock()
        self.level  = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((30, 30, 46))
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
```

### 🧪 Test Your Program

Run `python main.py` from inside the `unit1_oop/` folder.

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Game launches | Blue square on dark background, no crash | |
| 2 | Press WASD or arrow keys | Blue square moves smoothly in all 8 directions | |
| 3 | Press two keys diagonally | Same speed as pressing one key — not faster | |
| 4 | Walk within 200px of a red square | Red square starts moving toward you | |
| 5 | Let an enemy touch you | Print to console confirms HP is decreasing | |
| 6 | Count lines in `main.py` | 25 or fewer, zero game logic inside it | |

> **Answer these questions before moving on:**
>
> 1. Why do we call `_collide("horizontal")` *before* moving in Y? What visual bug would appear if you checked both axes at the same time?
>
>    *(your answer here)*
>
> 2. `self.visible_sprites.update()` runs your player input and all enemy AI in a single call. In your own words, explain how that is possible.
>
>    *(your answer here)*

---

---

## Checkpoint 4 — Adding New Classes: NPC and Chest 📦

### 📋 Your Task

Once `Entity` exists, adding new types of objects requires very little code. You only write what is *different*. This checkpoint proves the inheritance structure is working and flexible — and it is a preview of how game development actually works.

Add an **NPC** that speaks when the player gets close, and a **Chest** that gives gold when opened.

### 🧠 Understand It First

Notice how small each new class is:

```
Entity — written once, ~30 lines of shared setup
│
├── Player  — ~40 lines: just input and movement
├── Enemy   — ~30 lines: just AI
├── NPC     — ~15 lines: just dialogue     ← new today
└── Chest   — ~20 lines: just loot drop    ← new today
```

The distance check you used in `Enemy._distance_to_player()` appears again in both NPC and Chest. You already know the pattern — you are just applying it to a different reaction.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `class NPC(Entity)` | Yellow. Has `self.dialogue` (string) and `self.has_spoken` (bool, starts `False`). In `update()`: if player is within 80px and `has_spoken` is False → print dialogue and set `has_spoken = True`. Reset to `False` when player walks away again. |
| `class Chest(Entity)` | Brown. Has `self.gold` (int) and `self.opened` (bool, starts `False`). In `update()`: if player within 60px and not opened → add gold to `player.stats["Gold"]`, print a message, set `opened = True`, darken the image. |
| Add to Level | 2 NPCs with different dialogue and positions. 2 Chests with different gold values. |
| Import new classes | Add `from npc import NPC` and `from chest import Chest` at the top of `level.py` |

### 💡 Hints

- Distance pattern: `dist = (self.player.pos - self.pos).length()`
- `self.has_spoken = False` in NPC's `__init__`. Set `True` when they speak. Reset to `False` in the `else` branch when the player is far — this lets the NPC speak again on the next visit.
- `self.image.fill((100, 80, 40))` darkens the chest image after opening — a cheap visual cue
- You do **not** need to change `level.run()`, `entity.py`, `player.py`, or `main.py` at all

### 🖊️ Your Code

```python
# npc.py
# Name:
# Date:

from entity import Entity

class NPC(Entity):
    def __init__(self, pos, groups, player, dialogue):
        super().__init__(pos, groups)
        self.image.fill((255, 220, 100))   # yellow
        self.player     = player
        self.dialogue   = dialogue
        self.has_spoken = False

    def update(self):
        # Step 1: Calculate distance to player
        # Step 2: If within 80px and not has_spoken → print dialogue, set has_spoken = True
        # Step 3: Else → reset has_spoken to False so they speak again on next visit
```

```python
# chest.py
# Name:
# Date:

import random
from entity import Entity

LOOT_TABLE = ["Health Potion", "Iron Key", "Ancient Scroll", "Sharpening Stone"]

class Chest(Entity):
    def __init__(self, pos, groups, player, gold=50):
        super().__init__(pos, groups)
        self.image.fill((180, 130, 50))    # brown
        self.player = player
        self.gold   = gold
        self.opened = False

    def update(self):
        # Step 1: If already opened → return immediately (nothing more to do)
        # Step 2: Calculate distance to player
        # Step 3: If within 60px:
        #         → Add self.gold to player.stats["Gold"]
        #         → Pick a random item from LOOT_TABLE
        #         → Print what was found (gold amount and item name)
        #         → Set self.opened = True
        #         → Darken the image: self.image.fill((100, 80, 40))
```

```python
# Add these to level.py

# At the top with other imports:
from npc   import NPC
from chest import Chest

# Inside _setup_map(), after spawning enemies:

# Spawn 2 NPCs with different positions and dialogue strings

# Spawn 2 Chests with different positions and gold values
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Walk near an NPC | Dialogue prints in the console | |
| 2 | Walk away from the NPC, then return | Dialogue prints again | |
| 3 | Walk near a chest | Gold amount and item print; chest darkens | |
| 4 | Walk near the same chest again | Nothing happens — already opened | |
| 5 | Open both chests | Each gives a different gold amount | |

> **Answer this question before moving on:**
>
> You added two new objects (NPC and Chest) without changing `entity.py`, `player.py`, `enemy.py`, `level.run()`, or `main.py`. Why was that possible? What does this tell you about the advantage of having a base class?
>
> *(your answer here)*

---

---

## Checkpoint 5 — The Boss: Inheritance Three Levels Deep 🐉

### 📋 Your Task

A `Boss` inherits from `Enemy`, which inherits from `Entity`. This is a three-level inheritance chain. The Boss reuses all of Enemy's AI logic and only overrides what makes it special: a dramatic second phase when HP drops below 50%.

> ⚠️ This is a **stretch challenge**. Complete Checkpoints 1–4 first.

### 🧠 Understand It First

```
Entity
  └── Enemy          ← Boss gets all of this for free
        └── Boss     ← only defines what is different
```

`super().update()` inside `Boss.update()` runs Enemy's complete AI. Then you bolt the phase check on top. The Boss never repeats any code from Entity or Enemy — it only adds.

### ✅ Requirements

| Requirement | Details |
|---|---|
| `class Boss(Enemy)` | Calls `super().__init__(pos, groups, player)`. Starts purple `(150, 0, 150)`. HP: 300, Speed: 1, Attack: 25, notice radius: 300. |
| `self.in_second_phase` | Boolean, starts `False` |
| `second_phase(self)` | Triggers once only. Doubles speed. Sets notice radius to 400. Changes image to orange `(255, 100, 0)`. Prints a warning. |
| `_check_phase(self)` | If HP is below 50% of max_HP and `in_second_phase` is False → call `second_phase()` |
| `update(self)` | Call `super().update()` first, then `self._check_phase()` |
| Add to Level | One Boss at a position far from the player start |

### 💡 Hints

- `self.stats["max_HP"] * 0.5` — fifty percent of max HP
- `self.stats["Speed"] *= 2` — double the current speed in `second_phase()`
- Set `self.in_second_phase = True` **inside** `second_phase()` — if you forget this, the method runs every frame because the condition is always true
- In `level.py`, add `from boss import Boss` and spawn one Boss in `_setup_map()`

### 🖊️ Your Code

```python
# boss.py
# Name:
# Date:

from enemy import Enemy

class Boss(Enemy):
    def __init__(self, pos, groups, player):
        # Step 1: Call super().__init__ — this runs Enemy's full constructor
        # Step 2: Override image colour to purple
        # Step 3: Override stats — HP 300, max_HP 300, Speed 1, Attack 25
        # Step 4: Set self.in_second_phase = False
        # Step 5: Set self.notice_radius = 300

    def second_phase(self):
        # Step 6: Set in_second_phase to True (prevents this from running again)
        # Step 7: Double the speed
        # Step 8: Set notice_radius to 400
        # Step 9: Change image colour to orange
        # Step 10: Print a dramatic message

    def _check_phase(self):
        # Step 11: If HP < 50% of max_HP and not in_second_phase → call second_phase()

    def update(self):
        # Step 12: Call super().update() — runs Enemy's full AI
        # Step 13: Call self._check_phase()
```

### 🧪 Test Your Program

| Test | What to check | Expected result | ✓ |
|---|---|---|---|
| 1 | Boss appears | Purple square on screen | |
| 2 | Walk within 300px | Boss chases you | |
| 3 | Boss HP drops below 150 | Turns orange, moves faster, warning prints | |
| 4 | Stay near the Boss | Warning only prints once, not every frame | |

> **Stretch question — no code needed:**
>
> How would you design a `third_phase()` that triggers at 25% HP? What attributes would you add, and where would you call the method?
>
> *(your answer here)*

---

---

## 🏁 Reflection Questions

Answer in your own words. Think about the *why*, not just the *what*.

1. What is the difference between a **class** and an **instance**? Use an example from this unit.

   > *(your answer here)*

2. What does `self` mean inside a method? Why does Python require it as the first parameter on every method?

   > *(your answer here)*

3. Why do child classes call `super().__init__(...)` in their constructors? What breaks if you leave it out?

   > *(your answer here)*

4. You wrote `take_damage()` once in `Entity`, but Player, Enemy, NPC, and Chest can all use it without you copying the code. What is the name of the OOP feature that makes this possible?

   > *(your answer here)*

5. `player.update()` reads keyboard input. `enemy.update()` chases the player. Both methods have the same name. What OOP concept is this, and why does it make `group.update()` so powerful?

   > *(your answer here)*

6. You added NPC and Chest in Checkpoint 4 without touching `main.py`, `level.run()`, or `entity.py`. What does that tell you about a well-designed class hierarchy?

   > *(your answer here)*

7. What was the most confusing part of this unit, and what helped you push through it?

   > *(your answer here)*

---

## How This Connects to the Rest of the Year

```
Unit 1 — OOP
    You build: Entity → Player, Enemy, NPC, Chest, Boss, Level
         ↓
Unit 2 — Data Structures
    self.stats dict expands; map loads from a 2D list; shop uses a list of dicts
         ↓
Unit 3 — File I/O
    self.stats dict gets saved to JSON and reloaded — persistent save/load system
         ↓
Unit 4 — Libraries
    import_folder() loads animation frames into Player; random powers loot drops
         ↓
Unit 5 — End-of-Term Project
    All of the above — Tiled maps, real sprites, camera, sound, self-directed game
```

The files you wrote in this unit are not practice exercises. Keep every one of them. You will keep evolving `entity.py`, `player.py`, and `enemy.py` all year long.

---

*Next → [Unit 2 — The Ledger and the Treasury](./unit2_data_structures.md)*
