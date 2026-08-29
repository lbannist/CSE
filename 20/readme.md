# Rebuilding the Kingdom
### Grade 11 Python — Course Overview

Last year the hero was born (**Grade 10 — Hero's Journey**). The fundamentals were mastered: functions, loops, conditionals, strings — enough to defeat the boss and end the story. But the kingdom lies in ruins. This year the real work begins: proper object-oriented architecture, structured data, persistent files, a library of reusable tools, and a complete self-directed game built in a professional map editor.

Five units. One continuous kingdom. Every unit's code becomes the next unit's foundation — nothing built this year is ever thrown away.

---

## Unit 1 — The Blueprints of the Kingdom 🏗️
**Object-Oriented Programming · Inheritance · Sprite Groups**

Introduces classes from the ground up, starting in plain Python before touching Pygame. A base `Entity` class becomes the blueprint for everything in the world: `Player` adds keyboard input and two-step collision, `Enemy` adds detection radius and chase AI, `NPC` speaks on approach, `Chest` drops loot. A `Level` class wraps the entire world so `main.py` never needs to know how any of it works. OOP is not a topic that gets left behind here — it is the architecture every later unit builds inside.

**Builds:** `Entity` → `Player`, `Enemy`, `NPC`, `Chest`, `Boss` · `Level` with sprite groups · `main.py` under 25 lines

---

## Unit 2 — The Ledger and the Treasury 📜
**Lists · Tuples · Dictionaries · Data Structures**

Replaces every hard-coded value with the right data structure for the job. A `settings.py` file becomes the single source of truth: screen constants as tuples (immutable by design), a `WORLD_MAP` 2D list that spawns tiles and enemies by character, a `self.stats` dictionary on every entity so upgrades are one readable line, and an `ENEMY_DATA` dictionary that lets one `Enemy` class produce every enemy type in the game. A working shop system — `SHOP_ITEMS` as a list of dictionaries — completes the unit by showing how all three structures work together.

**Builds:** `settings.py` · `WORLD_MAP` map parser · `self.stats` dict on `Entity` · `ENEMY_DATA` · `SHOP_ITEMS` and `buy_item()` · `Tile` class

---

## Unit 3 — The Great Archives 📚
**File I/O · JSON · Save Systems · Main Menu**

Gives the kingdom memory. The game opens with a proper main menu — New Game, Load Game, Monster Manual, Spellbook, Quit — built in Pygame with dynamic state: Load Game greys out when no save exists. A `monster_manual.txt` and `spellbook.txt` that students write themselves are read from disk and displayed as a scrollable in-game overlay mid-session, with `[DEFEATED]` tags that update as enemies are killed. A `save_load.py` module commits the player's full state to `savegame.json` and restores it exactly, with `try/except` catching every realistic failure mode so a corrupted file never crashes the game.

**Builds:** `menu.py` with five options · `monster_manual.txt` and `spellbook.txt` · `save_load.py` with `save_game()`, `load_game()`, `delete_save()` · `ReferenceOverlay` with paging and `[DEFEATED]` tags

---

## Unit 4 — The Guild Contracts ⚗️
**Built-in Libraries · Custom Modules · Spritesheets · Timers**

Two kinds of work happen here: learning which tools already exist, and building a reusable toolkit of your own. The `random` module drives procedural loot drops with daily seeds. `pygame.math.Vector2` replaces raw arithmetic so enemy movement is smooth, directional, and consistent-speed regardless of angle. A complete `support.py` module is designed, built, and tested in isolation — `import_folder()`, `import_spritesheet()`, `clamp()`, `draw_bar()`, `draw_text()`, `distance()` — and then everything imports from it. Spritesheets are drawn in Piskel or downloaded from opengameart.org, sliced by `import_spritesheet()`, and cycled by a float frame counter. `pygame.time.get_ticks()` drives the attack cooldown bar in the HUD and a timed speed buff triggered by potions.

**Builds:** `support.py` (the project's utility module) · spritesheet animation system · projectile class · HUD with `draw_bar()` and `draw_text()` · attack cooldown · speed buff · autosave timer

---

## Unit 5 — The Kingdom Fully Realized 🎮
**Tiled Maps · Camera · Combat · Sound · Self-Directed Game**

Everything converges. Students choose their game style — Zelda-style top-down or side-scrolling platformer — design three zones and a final boss arena in Tiled, export each layer as CSV, and load them using the `import_csv_layout()` already sitting in `support.py`. A `CameraGroup` replaces the basic sprite group so the world scrolls. Real sprite art replaces every coloured placeholder. A `Weapon` sprite creates attack hitboxes; enemy health bars float above enemies in world space; XP and loot drop on kill. A `SoundManager` adds background music and effects. A `Boss` class enters a second phase at 50% HP. Zone transitions auto-save. A victory screen fires when the boss dies. The completed project is pushed to a public GitHub repository with a `README.md`, `requirements.txt`, and `.gitignore`.

**Builds:** three Tiled zones + boss arena · `CameraGroup` · `Weapon` hitbox · `UI` class · `SoundManager` · `Boss` with second phase · zone transitions · victory screen · GitHub repo

---

## What Carries Through All Five Units

| From Unit | Reused In |
|---|---|
| `Entity` class hierarchy (U1) | Every sprite in the game — Player, Enemy, NPC, Chest, Boss, Tile, Weapon all descend from it |
| `self.stats` dictionary (U1+U2) | `json.dump()` saves it in one line (U3); `draw_bar()` reads it for the HUD (U4) |
| `ENEMY_DATA` and `WORLD_MAP` (U2) | `_create_map()` reads WORLD_MAP; Tiled CSV replaces it in U5 with the same loop |
| `save_load.py` (U3) | Auto-saves on every zone transition; `current_zone` field added without rewriting the module |
| `support.py` (U4) | `import_csv_layout()` reads Tiled exports; `draw_bar()` and `draw_text()` power the HUD; `distance()` drives enemy AI |

By the end of Grade 11, the final game running in Tiled's zone was never rewritten from scratch — each unit's output was upgraded, extended, and connected to the next. That's the throughline of the whole year: not five separate topics, but one kingdom whose code never had to start over to go somewhere new.
