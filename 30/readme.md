# The Ascension
### Grade 12 Python — Course Overview

Two years ago, the kingdom was built from nothing (**Grade 10 — Hero's Journey**). Last year, it was rebuilt properly, with objects, structure, and a real game (**Grade 11 — Rebuilding the Kingdom**). This year, it ascends: deeper object-oriented design, real algorithms, two very different kinds of AI, and a leap from text and 2D into a fully scripted 3D world.

Five units. One continuous kingdom. Every unit's code becomes the next unit's foundation — nothing built this year is ever thrown away.

---

## Unit 1 — The Architect's Guild 🏛️
**Advanced OOP · Encapsulation · Dunder Methods**

Refactors last year's classes into a real inheritance hierarchy. `Entity` becomes an abstract base class enforced by `abc`; stats get protected with `@property`; characters gain `__str__`, `__repr__`, `__eq__`, and `__lt__` so they print, compare, and sort like real Python objects.

**Builds:** `Entity` (abstract) → `Player`, `Enemy`, `Boss`, `NPC` · property-protected stats · a dunder-powered `Inventory`

---

## Unit 2 — The Royal Scribes 🖋️
**Args & Kwargs · Scope & Closures · Decorators**

Spellcasting becomes flexible with `*args`/`**kwargs`. Scope and closures are taught deliberately as the mechanism decorators are built from, then put to work: custom `@cooldown` and `@requires_mana` decorators guard abilities, stacked alongside `@staticmethod`/`@classmethod`.

**Builds:** flexible `cast_spell()` · `@cooldown`, `@requires_mana`, `@log_action` · `Entity.from_save_data()` and `calculate_damage_multiplier()`

---

## Unit 3 — The Labyrinth 🌀
**Iterative & Recursive Algorithms**

Base cases, the call stack, and recursive backtracking — culminating in a real maze solver. The Minotaur is introduced here as an `Enemy` subclass whose pathfinding *is* the recursion: `find_path()` is generalized to target any coordinate, not just a fixed exit, which is exactly what a monster chasing a moving player needs.

**Builds:** `find_path()`, `find_all_paths()`, `generate_rooms()` · `Minotaur(Enemy)` with `take_step()` · memoization via `@lru_cache`

---

## Unit 4 — The War Room ♟️
**MinMax · Alpha-Beta Pruning · Intro PyTorch**

Two kinds of intelligence, built side by side. `Strategist(NPC)` plays an unbeatable game of Siege Table using minimax and alpha-beta pruning, logged with `@log_action` from Unit 2. The Threat Oracle — a small PyTorch neural network — is trained not on invented numbers, but on real stats pulled directly from `Player`, `Enemy`, `Boss`, and `Minotaur` instances already built.

**Builds:** `Strategist(NPC)` with `choose_move()` · `minimax_ab()` · `ThreatClassifier(nn.Module)` trained on real `Entity` data

---

## Unit 5 — The Third Dimension 🧊
**Unreal Engine 5 · Python Editor Scripting**

The kingdom leaves the terminal. After learning to navigate the UE5 editor by hand, Python takes over: actors are spawned and batch-edited by script, and Unit 3's `generate_rooms()` — completely unmodified — becomes the blueprint for a real 3D labyrinth. A Blueprint player can walk it, and the Minotaur hunts them live, its every move computed by the exact same `find_path()` recursion from Unit 3, exposed to Blueprint via `@unreal.ufunction`. A `game_config.py` file makes the whole game's difficulty tunable from one place.

**Builds:** a scripted 3D labyrinth · `minotaur_ai.py` (Python-powered live pathfinding) · `game_config.py` · an escalating, level-generating game loop

---

## What Carries Through All Five Units

| From Unit | Reused In |
|---|---|
| `Entity` hierarchy (U1) | `Minotaur(Enemy)` (U3), `Strategist(NPC)` (U4), Threat Oracle training data (U4) |
| `@log_action` decorator (U2) | `Strategist.choose_move()` (U4) |
| `find_path()` recursion (U3) | The Minotaur's chase, in text (U3) and live in 3D (U5) |
| `generate_rooms()` (U3) | The 3D labyrinth layout and its level-up progression (U5) |

By the end of Grade 12, nothing in the final Unreal Engine scene was ever rewritten from scratch — it was exposed, scaled, and connected. That's the throughline of the whole year: not five separate topics, but one kingdom whose logic never had to be rebuilt to go somewhere new.
