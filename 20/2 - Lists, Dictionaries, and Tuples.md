# 📖 Lesson — Lists, Tuples, and Dictionaries in Python
### *Starfleet Academy — Data Management Division*

> **Course:** Grade 11 · Python  
> **Before this lesson:** You should have completed the Classes lesson and Unit 1.  
> **After this lesson:** You will be ready to tackle Unit 2 — The Ledger and the Treasury.

---

> *"The computer's record is precise. The crew manifest, the weapons inventory, the coordinates of every star system in the sector — all of it stored, sorted, and retrievable in milliseconds. That is the power of organised data, Mr. Data."*
> — Inspired by Captain Jean-Luc Picard, USS Enterprise NCC-1701-D

---

## 🎯 Learning Goals

By the end of this lesson you will be able to:

- [ ] Create and access a **list** and explain when to use one
- [ ] Loop through a list, add and remove items, and sort it
- [ ] Create a **tuple** and explain why its immutability is a feature, not a limitation
- [ ] Create a **dictionary** and access, add, update, and remove entries by key
- [ ] Decide which structure — list, tuple, or dictionary — is the right tool for a given situation

---

## 🎬 Watch First — The Starfleet Video Library

There are many short videos for this lesson. They are organised into four groups. **Watch each group, then read the matching section of notes and complete the practice block before moving on.** Do not watch all eight and then try to read — the concepts build on each other.

---

### 📺 Group 1 — Lists *(watch all four before reading Section 1)*

Watch this introductory video to Lists.
[![Watch the video](https://img.youtube.com/vi/LWeS6R9IPf4/maxresdefault.jpg)](https://youtu.be/LWeS6R9IPf4)

Here are links to other Lists videos that explore the many ways lists can be used in a program.
| # | Topic | Video |
|---|---|---|
| 1 | **Accessing List Items** — indexes, slices, negative indexing | 🎥 [Watch](https://www.youtube.com/watch?v=oPZ5xoKZ6Og) |
| 2 | **Analyse a List** — `len()`, `min()`, `max()`, loops | 🎥 [Watch](https://www.youtube.com/watch?v=zVt7oaBUsHk) |
| 3 | **Add/Remove from a List** — `append()`, `insert()`, `remove()`, `pop()` | 🎥 [Watch](https://www.youtube.com/watch?v=qtANRuRxiEo) |
| 4 | **Sort Lists** — `sort()`, `sorted()`, reverse sorting | 🎥 [Watch](https://www.youtube.com/watch?v=BUsmwsk8Des) |

**Write down while watching:**
- What is the index of the *first* item in any Python list?
- What does a negative index like `[-1]` refer to?
- What is the difference between `sort()` and `sorted()`?

---

### 📺 Group 2 — Tuples *(watch before reading Section 2)*

[![Watch the video](https://img.youtube.com/vi/TTkifjHCPWo/maxresdefault.jpg)](https://youtu.be/TTkifjHCPWo)

**Write down while watching:**
- What is the ONE key difference between a tuple and a list?
- What happens if you try to change an item in a tuple?

---

### 📺 Group 3 — Dictionaries *(watch before reading Section 3)*

[![Watch the video](https://img.youtube.com/vi/rpsYzPv1HiQ/maxresdefault.jpg)](https://youtu.be/rpsYzPv1HiQ)

**Write down while watching:**
- How do you access a value in a dictionary?
- How do you add a new key-value pair?

---

### 📺 Group 4 — Choosing the Right Structure *(watch last)*

[![Watch the video](https://img.youtube.com/vi/h-zcj4DmqHk/maxresdefault.jpg)](https://youtu.be/h-zcj4DmqHk)

**Write down while watching:**
- Name one situation where a tuple is better than a list.
- Name one situation where a dictionary is better than a list.

---

---

## Section 1 — Lists: The Crew Manifest 📋

### What Is a List?

A **list** is an ordered, changeable collection of items. You can put anything in a list — strings, numbers, objects, even other lists. Items are stored in a specific order and accessed by their **index** (position number).

**Lists are ordered** — the item you add first stays in position 0 unless you move it.  
**Lists are mutable** — you can add, remove, or change items after the list is created.

```python
# The crew manifest of the USS Enterprise
crew_manifest = [
    "Jean-Luc Picard",
    "William Riker",
    "Data",
    "Deanna Troi",
    "Worf",
    "Geordi La Forge",
    "Beverly Crusher",
]

# Lists are zero-indexed — the FIRST item is at position 0
print(crew_manifest[0])    # Jean-Luc Picard
print(crew_manifest[2])    # Data
print(crew_manifest[-1])   # Beverly Crusher  ← -1 always means the last item
print(crew_manifest[-2])   # Geordi La Forge  ← -2 means second from the end
```

> ⚠️ **The most common beginner mistake:** forgetting that lists start at index `0`, not `1`. In a list of 7 crew members, the last item is at index `6`, not `7`. Using index `7` would cause an `IndexError`.

---

### Slicing — Grabbing a Section of the List

A **slice** extracts a portion of the list without modifying the original:

```python
# Syntax: list[start : stop]
# start is INCLUDED, stop is EXCLUDED

senior_staff = crew_manifest[0:4]     # positions 0, 1, 2, 3 (not 4)
print(senior_staff)
# ['Jean-Luc Picard', 'William Riker', 'Data', 'Deanna Troi']

# Leave start blank → begin from the start
first_three = crew_manifest[:3]
print(first_three)    # ['Jean-Luc Picard', 'William Riker', 'Data']

# Leave stop blank → go to the end
last_three = crew_manifest[-3:]
print(last_three)    # ['Worf', 'Geordi La Forge', 'Beverly Crusher']
```

---

### Analysing a List

```python
print(len(crew_manifest))          # 7 — how many crew members
print(min([100, 40, 75, 90]))      # 40 — lowest value (works on numbers)
print(max([100, 40, 75, 90]))      # 100 — highest value

# Loop through every item
for officer in crew_manifest:
    print(f"  Officer on duty: {officer}")

# Loop with enumerate() — gives you the index AND the value together
for i, officer in enumerate(crew_manifest):
    print(f"  Position {i}: {officer}")

# Check if someone is on the manifest
if "Worf" in crew_manifest:
    print("Lieutenant Worf is aboard.")

if "Khan" not in crew_manifest:
    print("Khan is NOT on the crew manifest. Thank goodness.")
```

---

### Adding and Removing Crew

```python
# append() — add to the END of the list
crew_manifest.append("Wesley Crusher")
print(crew_manifest[-1])    # Wesley Crusher

# insert(index, item) — add at a SPECIFIC position
crew_manifest.insert(1, "Guinan")    # insert at position 1
print(crew_manifest[0])    # Jean-Luc Picard  (captain stays first)
print(crew_manifest[1])    # Guinan           (inserted here)
print(crew_manifest[2])    # William Riker    (everyone shifted right by one)

# remove(value) — remove the FIRST occurrence of a specific value
crew_manifest.remove("Wesley Crusher")

# pop(index) — remove AND return the item at a given index
# If no index given, removes and returns the LAST item
departed = crew_manifest.pop()
print(f"{departed} has left the ship.")

# del — delete by index without returning the item
del crew_manifest[1]    # removes Guinan (position 1)
```

---

### Sorting the Manifest

```python
# sort() — sorts the list IN PLACE (changes the original)
crew_manifest.sort()
print(crew_manifest)    # sorted alphabetically

# sort() in reverse
crew_manifest.sort(reverse=True)
print(crew_manifest)    # reverse alphabetical

# sorted() — returns a NEW sorted list, leaves the original untouched
shield_levels = [45, 100, 23, 78, 60]
sorted_shields = sorted(shield_levels)
print(sorted_shields)     # [23, 45, 60, 78, 100]
print(shield_levels)      # [45, 100, 23, 78, 60]  ← UNCHANGED
```

> 💡 **`sort()` vs `sorted()`:** Use `sort()` when you want to permanently reorder the original list. Use `sorted()` when you want a sorted copy but need to keep the original order intact.

---

### 🧪 Practice Block 1 — The Crew Manifest

Create `lesson_data_practice.py` and type this out:

```python
# lesson_data_practice.py — Practice Block 1: Lists

# The bridge crew of the USS Voyager
bridge_crew = [
    "Kathryn Janeway",
    "Chakotay",
    "Tuvok",
    "B'Elanna Torres",
    "Tom Paris",
    "The Doctor",
    "Seven of Nine",
    "Harry Kim",
    "Neelix",
]

# MISSION 1: Access
print("=== ACCESS DRILLS ===")
print(bridge_crew[0])       # First officer — actually captain
print(bridge_crew[-1])      # Last on the list
print(bridge_crew[3])       # Chief engineer
print(bridge_crew[2:5])     # A slice — positions 2, 3, 4

# MISSION 2: Analyse
print("\n=== ANALYSIS ===")
print(f"Total crew on bridge: {len(bridge_crew)}")
for i, officer in enumerate(bridge_crew):
    print(f"  Seat {i}: {officer}")

# MISSION 3: Modify
print("\n=== MODIFICATIONS ===")
bridge_crew.append("Kes")           # Add Kes to the end
bridge_crew.insert(0, "Admiral")    # Insert at the front
bridge_crew.remove("Neelix")        # Remove Neelix (the Talaxian gets lost)
departed = bridge_crew.pop()        # Remove and capture the last person

print(f"Departed: {departed}")
print(f"Crew count now: {len(bridge_crew)}")

# MISSION 4: Sort
print("\n=== SORTED ROSTER ===")
sorted_crew = sorted(bridge_crew)   # sorted() — don't change the original
for name in sorted_crew:
    print(f"  {name}")

print("\nOriginal order preserved:", bridge_crew[0])  # Should still be "Admiral"
```

**Answer these in a comment before moving on:**
```python
# Q1: What is the index of "Seven of Nine" in the ORIGINAL bridge_crew list?
# A1:

# Q2: What is the difference between bridge_crew.sort() and sorted(bridge_crew)?
# A2:

# Q3: After bridge_crew.insert(0, "Admiral"), what is bridge_crew[1]?
# A3:
```

---

---

## Section 2 — Tuples: Starfleet's Fixed Records 📌

### What Is a Tuple?

A **tuple** is like a list — it is ordered and you access items by index — with one critical difference: **a tuple cannot be changed after it is created.** It is **immutable**.

This is not a flaw. It is a deliberate design choice that communicates something important to anyone reading your code:

> *"These values are fixed. They should not — and cannot — change."*

```python
# Tuples use round brackets ( ) instead of square brackets [ ]
# Everything else about access is the same as a list

# The coordinates of Deep Space Nine — they don't change
ds9_coordinates = (53.1, 24.7, -1.4)    # (x, y, z) in light years

# Access works the same as a list
print(ds9_coordinates[0])     # 53.1
print(ds9_coordinates[-1])    # -1.4
print(ds9_coordinates[1:3])   # (24.7, -1.4)  ← slice of a tuple returns a tuple

# But you CANNOT change a tuple — this is the whole point
# ds9_coordinates[0] = 99.0   ← TypeError: 'tuple' does not support item assignment

# You can loop over a tuple exactly like a list
for coord in ds9_coordinates:
    print(coord)
```

---

### When to Use a Tuple vs a List

The question to ask yourself is: **should this data ever change at runtime?**

| Use a **list** when... | Use a **tuple** when... |
|---|---|
| The collection will grow or shrink | The values are fixed and should never change |
| Items will be added, removed, or reordered | You want Python to *enforce* that nothing changes |
| `crew_manifest` — people join and leave | `warp_factor_limits = (1, 9.9)` — physics doesn't change |
| `shield_history = [100, 80, 55, 20]` | `screen_resolution = (1920, 1080)` |
| `defeated_enemies = []` — grows over time | `STARDATE = (47634, 44, 2364)` — this mission's date |

```python
# Common tuple uses in games and programs:

# Screen dimensions — should never change mid-program
SCREEN_SIZE    = (1280, 720)

# RGB colours — these are constants
COLOR_RED      = (220, 50, 50)
COLOR_GOLD     = (201, 168, 76)
COLOR_BLUE     = (50, 120, 220)

# Warp speed boundaries — defined by physics
WARP_LIMITS    = (1, 9.9)

# Tuple unpacking — assign multiple variables at once
width, height = SCREEN_SIZE
print(f"Screen: {width} x {height}")

min_warp, max_warp = WARP_LIMITS
print(f"Warp range: {min_warp} to {max_warp}")
```

> 💡 **Convention:** Many programmers write tuple constants in `ALL_CAPS` to signal that they are fixed values that should not be changed.

---

### 🧪 Practice Block 2 — Starfleet's Fixed Constants

Add this below Practice Block 1 in your file:

```python
# Practice Block 2: Tuples

# Fixed constants for Starfleet systems
ENTERPRISE_REGISTRY = ("USS Enterprise", "NCC-1701-D", 2364)  # name, registry, launch year
STANDARD_ORBIT      = (200, "km")          # altitude, unit
PHASER_FREQUENCIES  = (1.02, 4.57, 8.12)  # three preset frequencies

# MISSION 1: Access tuples like lists
print("\n=== STARFLEET CONSTANTS ===")
print(f"Ship name:   {ENTERPRISE_REGISTRY[0]}")
print(f"Registry:    {ENTERPRISE_REGISTRY[1]}")
print(f"Launch year: {ENTERPRISE_REGISTRY[2]}")

# MISSION 2: Unpacking
ship_name, registry, year = ENTERPRISE_REGISTRY
print(f"\n{ship_name} ({registry}) commissioned in {year}")

altitude, unit = STANDARD_ORBIT
print(f"Entering standard orbit at {altitude} {unit}")

# MISSION 3: Prove immutability
print("\n=== IMMUTABILITY TEST ===")
print("Attempting to change ENTERPRISE_REGISTRY[0]...")
try:
    ENTERPRISE_REGISTRY[0] = "USS Defiant"   # this will fail
except TypeError as e:
    print(f"Starfleet rejected the change: {e}")
    print("Tuples cannot be modified. This is working as intended.")

# MISSION 4: Loop over a tuple
print("\n=== PHASER FREQUENCIES ===")
for i, freq in enumerate(PHASER_FREQUENCIES):
    print(f"  Preset {i+1}: {freq} GHz")
```

**Answer in a comment:**
```python
# Q1: Try changing ENTERPRISE_REGISTRY to a list. Does the TypeError still occur?
#     What does this tell you about who is responsible for protecting the data?
# A1:

# Q2: Why would you use ALL_CAPS for a tuple like SCREEN_SIZE or PHASER_FREQUENCIES?
# A2:
```

---

---

## Section 3 — Dictionaries: The Ship's Computer Database 🖥️

### What Is a Dictionary?

A **dictionary** stores data as **key-value pairs**. Instead of accessing items by a position number (index), you access them by a meaningful **key** — usually a string.

Think of it like the ship's computer: you do not ask *"give me item number 3"* — you ask *"what is the shield strength?"*

```python
# A dictionary uses curly braces { } and the format  key: value
# Keys are almost always strings
# Values can be anything — numbers, strings, lists, even other dicts

enterprise_status = {
    "name":     "USS Enterprise",
    "registry": "NCC-1701-D",
    "shields":  100,
    "hull":     100,
    "crew":     1012,
    "warp":     0,
    "cloaked":  False,
}

# Access a value by its KEY — not by position
print(enterprise_status["name"])       # USS Enterprise
print(enterprise_status["shields"])    # 100
print(enterprise_status["crew"])       # 1012

# Change a value
enterprise_status["shields"] = 60
enterprise_status["warp"]    = 7
print(enterprise_status["shields"])    # 60

# Add a NEW key-value pair
enterprise_status["red_alert"] = True

# Delete a key-value pair
del enterprise_status["red_alert"]
```

---

### Useful Dictionary Operations

```python
# Check if a key exists (always check before accessing to avoid KeyError)
if "shields" in enterprise_status:
    print(f"Shields: {enterprise_status['shields']}%")

# .get() — safe access with a default if the key doesn't exist
# This will NOT crash even if "torpedoes" is not in the dictionary
torps = enterprise_status.get("torpedoes", 0)
print(f"Torpedoes: {torps}")    # 0 — the default

# Loop over all keys
for key in enterprise_status:
    print(key)

# Loop over all values
for value in enterprise_status.values():
    print(value)

# Loop over key-value pairs together — the most useful loop
for key, value in enterprise_status.items():
    print(f"  {key}: {value}")

# How many entries?
print(len(enterprise_status))
```

---

### Dictionaries vs Lists — A Direct Comparison

```python
# The same data stored two ways — feel the difference

# ── As a list ──────────────────────────────────────────────────────────────
# You must remember that index 0 = shields, index 1 = hull, etc.
ship_data_list = [100, 100, 1012, 0, False]
ship_data_list[0] -= 40    # what is index 0? Shields? Hull? You must check.

# ── As a dictionary ────────────────────────────────────────────────────────
# The key tells you exactly what you are reading — no notes required
ship_data_dict = {"shields": 100, "hull": 100, "crew": 1012, "warp": 0}
ship_data_dict["shields"] -= 40    # immediately readable — no ambiguity

# Adding a new field:
ship_data_list.append(150)         # what is 150? You must remember.
ship_data_dict["torpedoes"] = 150  # obvious — no guessing
```

> **Rule:** If you are naming the things you store (shield strength, crew count, warp factor), use a **dictionary**. If you are storing a sequence of identical things (a list of names, a list of shield readings over time), use a **list**.

---

### Nested Dictionaries — The Fleet Database

Dictionaries can contain other dictionaries, creating a structured database:

```python
# A fleet database — dictionary of dictionaries
fleet = {
    "enterprise": {
        "name":    "USS Enterprise",
        "class":   "Galaxy",
        "shields": 100,
        "crew":    1012,
    },
    "defiant": {
        "name":    "USS Defiant",
        "class":   "Defiant",
        "shields": 85,
        "crew":    50,
    },
    "voyager": {
        "name":    "USS Voyager",
        "class":   "Intrepid",
        "shields": 100,
        "crew":    141,
    },
}

# Access a ship by key, then a field by key
print(fleet["enterprise"]["name"])     # USS Enterprise
print(fleet["defiant"]["shields"])     # 85
print(fleet["voyager"]["crew"])        # 141

# Update a nested value
fleet["defiant"]["shields"] -= 30
print(fleet["defiant"]["shields"])     # 55

# Loop over the whole fleet
print("\n=== FLEET STATUS ===")
for ship_key, ship_data in fleet.items():
    print(f"{ship_data['name']} ({ship_data['class']}-class): "
          f"shields {ship_data['shields']}%")
```

---

### 🧪 Practice Block 3 — The Ship's Computer

Add this below Practice Block 2:

```python
# Practice Block 3: Dictionaries

# Full status report for the USS Defiant
defiant = {
    "name":       "USS Defiant",
    "registry":   "NX-74205",
    "class":      "Defiant",
    "crew":       50,
    "shields":    100,
    "hull":       100,
    "torpedoes":  48,
    "cloaked":    False,
    "warp":       0,
}

# MISSION 1: Read the computer
print("=== DEFIANT STATUS REPORT ===")
for system, reading in defiant.items():
    print(f"  {system:<12}: {reading}")

# MISSION 2: Battle simulation
print("\n=== BATTLE SIMULATION ===")
defiant["shields"] -= 55
defiant["warp"]     = 9
defiant["red_alert"] = True

print(f"Shields now at: {defiant['shields']}%")
print(f"Warp factor:    {defiant['warp']}")
print(f"Red alert:      {defiant['red_alert']}")

# MISSION 3: Safe access with .get()
print("\n=== SYSTEM CHECKS ===")
for system in ["shields", "cloaking_device", "holodeck", "torpedoes"]:
    status = defiant.get(system, "NOT INSTALLED")
    print(f"  {system}: {status}")

# MISSION 4: Build a fleet
print("\n=== FLEET DATABASE ===")
fleet = {
    "enterprise": {"name": "USS Enterprise", "shields": 80, "crew": 1012},
    "defiant":    defiant,
    "voyager":    {"name": "USS Voyager",    "shields": 100, "crew": 141},
}

for key, ship in fleet.items():
    status = "⚠️  DAMAGED" if ship["shields"] < 100 else "✅ OPERATIONAL"
    print(f"  {ship['name']}: {ship['shields']}% shields  {status}")
```

**Answer in a comment:**
```python
# Q1: Why is defiant["shields"] better than a list like ship_data[0]?
# A1:

# Q2: What does .get("cloaking_device", "NOT INSTALLED") do differently
#     from defiant["cloaking_device"]? When would you use each one?
# A2:

# Q3: How would you add a "phasers" key with value 12 to the defiant dictionary?
# A3:
```

---

---

## Section 4 — Choosing the Right Tool 🖖

After watching Video 8 and working through the practice blocks, this decision should feel more intuitive. Here is the complete guide:

### The Decision Chart

```
You need to store a collection of data.
│
├── Will the values EVER need to change?
│   │
│   ├── NO → Use a TUPLE  (immutable — fixed forever)
│   │         Examples: screen size, colours, coordinates, config constants
│   │         SCREEN = (1280, 720)
│   │         WARP_LIMITS = (1, 9.9)
│   │
│   └── YES → Will you look items up by a MEANINGFUL NAME?
│             │
│             ├── YES → Use a DICTIONARY  (key-value lookup)
│             │         Examples: character stats, ship status, item data
│             │         ship = {"shields": 100, "crew": 1012}
│             │
│             └── NO → Use a LIST  (ordered sequence, access by position)
│                       Examples: crew roster, history log, inventory
│                       crew = ["Picard", "Riker", "Data"]
```

### Side-by-Side Comparison

| Feature | List `[]` | Tuple `()` | Dictionary `{}` |
|---|---|---|---|
| Ordered? | ✅ Yes | ✅ Yes | ❌ No (keys are unordered) |
| Access by | Index number | Index number | Key name |
| Changeable? | ✅ Yes | ❌ No | ✅ Yes |
| Duplicates allowed? | ✅ Yes | ✅ Yes | ❌ Keys must be unique |
| Best for | Sequences of similar things | Fixed constants | Named properties of one thing |
| Example | `["Picard", "Riker", "Data"]` | `(1280, 720)` | `{"shields": 100, "crew": 1012}` |

### A Starfleet Example of All Three Together

```python
# All three structures working together — this is how real programs are written

# TUPLE — constants that never change
SCREEN_SIZE   = (1280, 720)
COLOR_BLUE    = (50, 120, 220)
WARP_LIMITS   = (1, 9.9)

# DICTIONARY — named properties of one specific ship
enterprise = {
    "name":    "USS Enterprise",
    "shields": 100,
    "crew":    1012,
    "warp":    0,
}

# LIST — a collection of similar things that changes over time
battle_log     = []   # will grow as events happen
crew_manifest  = ["Picard", "Riker", "Data", "Troi", "Worf"]

# They work together naturally
crew_manifest.append("Crusher")          # add to the list
enterprise["shields"] -= 40             # update the dictionary
battle_log.append("Shields hit: -40%")   # record in the log

width, height = SCREEN_SIZE              # unpack the tuple
```

---

### Tuples as Dictionary Keys — The Astrometrics Grid 🌌

This is one of the most powerful and least-taught patterns in Python. You already know that:
- Tuples are immutable
- Dictionary keys must be immutable

That means **a tuple can be used as a dictionary key**. A list cannot — Python will refuse it because lists can be changed, and a key that could change would break the lookup system.

This unlocks something remarkable: you can build a **spatial grid** where the key is a coordinate pair `(row, col)` and the value is whatever is at that location.

**Seven of Nine's Astrometrics Lab** on Voyager displays a spatial grid of the Delta Quadrant — every sector mapped by its grid coordinates. That is exactly the structure we are about to build.

```python
# In Astrometrics, the grid is addressed by (row, col) coordinates
# The value at each coordinate is what is in that sector

# A tuple is immutable — it can be used as a dictionary key
# A list is mutable — it CANNOT be used as a dictionary key

# ── Why lists fail as keys ────────────────────────────────────────────────
# Try this and read the error:
# broken = { [0, 0]: "Sector Alpha" }   # TypeError: unhashable type: 'list'

# ── Why tuples work ──────────────────────────────────────────────────────
sector_map = {}   # empty dictionary — we will fill it with (row, col) keys

# Populate the grid — each coordinate is a tuple key
sector_map[(0, 0)] = "Borg Cube detected"
sector_map[(0, 1)] = "Empty space"
sector_map[(0, 2)] = "Nebula — avoid"
sector_map[(1, 0)] = "Kazon patrol route"
sector_map[(1, 1)] = "Voyager current position"
sector_map[(1, 2)] = "Wormhole — unstable"
sector_map[(2, 0)] = "Empty space"
sector_map[(2, 1)] = "Planet — class M"
sector_map[(2, 2)] = "Subspace anomaly"

# Read a specific coordinate
print(sector_map[(1, 1)])    # Voyager current position
print(sector_map[(0, 0)])    # Borg Cube detected
print(sector_map[(2, 1)])    # Planet — class M
```

**Why is this better than a 2D list for this purpose?**

```python
# ── 2D list approach ──────────────────────────────────────────────────────
# Access by position — [row][col]
grid_list = [
    ["Borg Cube detected", "Empty space",    "Nebula — avoid"],
    ["Kazon patrol route", "Voyager pos",    "Wormhole — unstable"],
    ["Empty space",        "Planet class M", "Subspace anomaly"],
]
print(grid_list[1][1])    # Voyager pos — works, but...

# ── The tuple-key dictionary approach ─────────────────────────────────────
# Access by meaningful coordinate
print(sector_map[(1, 1)])  # Voyager current position

# The REAL advantage: sparse grids
# A 2D list must fill EVERY cell — even empty ones
# A dictionary only stores cells that HAVE something

# Imagine a map of the entire Delta Quadrant — mostly empty space
# A 2D list: 1000 × 1000 = 1,000,000 entries, mostly "Empty space"
# A dict:    only stores the coordinates that have something interesting

deep_space = {}
deep_space[(47, 231)] = "Borg transwarp hub"
deep_space[(12, 8)]   = "Ocampa homeworld"
deep_space[(503, 99)]  = "Hirogen hunting ground"
# Only 3 entries stored — not 1,000,000
print(f"Known locations: {len(deep_space)}")
```

**Checking and updating the grid:**

```python
# Check if a coordinate has anything at it
probe_location = (0, 0)
if probe_location in sector_map:
    print(f"Probe at {probe_location}: {sector_map[probe_location]}")
else:
    print(f"Sector {probe_location} — no data on record")

# Safe access with .get() — returns None if the coordinate is not mapped
reading = sector_map.get((5, 5), "Uncharted territory")
print(reading)    # Uncharted territory — (5,5) is not in our map

# Update a sector as new information arrives
sector_map[(0, 0)] = "Borg Cube — course: 270 mark 15"   # they moved
sector_map[(3, 3)] = "Species 8472 detected"              # new discovery

# Loop over the entire grid — sorted so coordinates print in order
print("\n=== ASTROMETRICS FULL GRID REPORT ===")
for coordinate in sorted(sector_map):
    print(f"  Sector {coordinate}: {sector_map[coordinate]}")
```

**Unpacking the coordinate key while looping:**

```python
# Because the key is a tuple, you can unpack it directly in the loop
print("\n=== SEVEN OF NINE'S ANNOTATED SCAN ===")
for (row, col), content in sorted(sector_map.items()):
    if "Borg" in content:
        priority = "⚠️  THREAT"
    elif "Voyager" in content:
        priority = "📍 HOME"
    elif "Planet" in content:
        priority = "🌍 RESOURCE"
    else:
        priority = "   —"
    print(f"  [{row},{col}]  {priority}  {content}")
```

> 💡 **Key rule:** Only **immutable** types can be dictionary keys. Strings ✅, numbers ✅, tuples ✅. Lists ❌, dictionaries ❌. A tuple works as a key precisely because it cannot be changed — Python can trust that the coordinate `(1, 1)` will always mean the same location.

> 🖖 **When to use this pattern:** Any time your data is naturally addressed by two or more coordinates — a game map, a seating chart, a spatial grid, a chess board, a Battleship grid. Instead of `grid[row][col]` through a 2D list, you use `grid[(row, col)]` through a dictionary. The dictionary version is more readable, handles sparse data efficiently, and lets you store richer metadata alongside each coordinate.

---

### 🧪 Practice Block 4 — The Final Simulation

Add this below Practice Block 3:

```python
# Practice Block 4: All Three Together — including Astrometrics

# ── MISSION 0: Build Seven of Nine's Astrometrics Grid ───────────────────────
print("=== ASTROMETRICS LAB — DELTA QUADRANT GRID ===")

# The grid is a dictionary — keys are (row, col) tuples, values are sector contents
# This is called a SPARSE GRID — only occupied sectors are stored
quadrant_grid = {}

# Populate the grid — Seven has been scanning for weeks
scan_data = [
    ((0, 0), "Empty space"),
    ((0, 3), "Nekrit Expanse — sensor interference"),
    ((1, 1), "Voyager current position"),
    ((1, 4), "Kazon Ogla territory"),
    ((2, 2), "Class-M planet — pre-warp civilisation"),
    ((3, 0), "Borg transwarp conduit"),
    ((3, 3), "Hirogen relay station"),
    ((4, 1), "Malon freighter — antimatter waste"),
    ((4, 4), "Subspace corridor — origin unknown"),
]

# Build the grid from the scan data
for coordinate, content in scan_data:
    quadrant_grid[coordinate] = content

# MISSION 0a — Look up specific sectors
print(f"\nVoyager position:   {quadrant_grid[(1, 1)]}")
print(f"Nearest threat:     {quadrant_grid.get((3, 0), 'clear')}")
print(f"Sector (2, 0):      {quadrant_grid.get((2, 0), 'no data — uncharted')}")

# MISSION 0b — Print the full grid, sorted by coordinate
print("\n--- Full Sector Scan ---")
for (row, col), content in sorted(quadrant_grid.items()):
    threat = " ⚠️" if any(w in content for w in ["Borg", "Kazon", "Hirogen"]) else ""
    print(f"  Sector ({row},{col}): {content}{threat}")

# MISSION 0c — Update the grid as new information arrives
quadrant_grid[(1, 1)] = "Voyager — new heading 220 mark 15"   # we moved
quadrant_grid[(0, 2)] = "Spatial anomaly — avoid"              # new discovery
del quadrant_grid[(0, 0)]   # confirmed empty — remove to keep map clean

print(f"\nKnown sectors logged: {len(quadrant_grid)}")

# MISSION 0d — Prove a list CANNOT be a key (uncomment to see the error)
# broken_grid = {}
# broken_grid[[1, 1]] = "This will crash"   # TypeError: unhashable type: 'list'

print("\n" + "="*50 + "\n")

# ── MISSIONS 1-4: The rest of the simulation ──────────────────────────────────

# TUPLES — fixed constants
SHIELD_WARNING_THRESHOLD = 30    # percent
TORPEDO_WARNING_THRESHOLD = 10
CREW_COMPLEMENT = (1012, 141, 50)   # Enterprise, Voyager, Defiant — never changes

# DICTIONARY — one ship's full status
voyager = {
    "name":       "USS Voyager",
    "registry":   "NCC-74656",
    "shields":    100,
    "hull":       100,
    "torpedoes":  38,
    "crew":       141,
    "warp":       0,
    "log":        [],    # a list INSIDE the dictionary — perfectly fine!
}

# LIST — the fleet
fleet_names = ["USS Enterprise", "USS Voyager", "USS Defiant"]

# SIMULATION — Voyager takes damage over several turns
print("=== VOYAGER COMBAT LOG ===")
incoming_attacks = [25, 40, 15, 60, 10]   # a list of damage values

for i, damage in enumerate(incoming_attacks, 1):
    voyager["shields"] -= damage

    if voyager["shields"] < 0:
        # Shields are gone — hull takes the overflow
        voyager["hull"]   += voyager["shields"]   # shields is negative here
        voyager["shields"] = 0

    entry = f"Turn {i}: -{damage} damage. Shields: {voyager['shields']}%  Hull: {voyager['hull']}%"
    voyager["log"].append(entry)
    print(f"  {entry}")

    # Check warning thresholds — using the TUPLE constant
    if voyager["shields"] <= SHIELD_WARNING_THRESHOLD:
        print(f"  ⚠️  WARNING: Shields below {SHIELD_WARNING_THRESHOLD}%!")

    if voyager["hull"] <= 0:
        print(f"  💥 {voyager['name']} has been destroyed!")
        break

# Final report
print("\n=== FINAL STATUS ===")
print(f"Ship:    {voyager['name']}")
print(f"Shields: {voyager['shields']}%")
print(f"Hull:    {voyager['hull']}%")
print(f"\nFull combat log ({len(voyager['log'])} entries):")
for entry in voyager["log"]:
    print(f"  {entry}")

# Fleet check
print("\n=== FLEET ROSTER ===")
print(f"{len(fleet_names)} ships in the fleet:")
for name in sorted(fleet_names):
    print(f"  {name}")

min_crew, max_crew = min(CREW_COMPLEMENT), max(CREW_COMPLEMENT)
print(f"\nSmallest crew: {min_crew}  |  Largest crew: {max_crew}")
```

---

**Answer these in a comment at the bottom of your file:**

```python
# Q1: Why can a tuple be used as a dictionary key, but a list cannot?
# A1:

# Q2: The quadrant_grid only stores 9 sectors out of a possible 25 (a 5×5 grid).
#     If you used a 2D list instead, how many entries would you need?
#     What is the advantage of the dictionary approach for a sparse grid?
# A2:

# Q3: In the loop:
#         for (row, col), content in sorted(quadrant_grid.items()):
#     What does sorted() use to determine the order?
#     Try adding ((0, 1), "Test sector") to the grid — where does it appear?
# A3:

# Q4: How would you adapt the quadrant_grid to store a Battleship game board?
#     What would the keys be? What would the values be?
# A4:
```

---

## 🔑 Key Takeaways

Cover the right column and answer each question from memory:

| Question | Answer |
|---|---|
| What index is the first item of a list? | `0` — Python lists are zero-indexed |
| What does `list[-1]` return? | The last item in the list |
| What is the difference between `sort()` and `sorted()`? | `sort()` changes the original; `sorted()` returns a new sorted copy |
| What makes a tuple different from a list? | A tuple is immutable — it cannot be changed after creation |
| When should you use a tuple instead of a list? | When the values should never change (constants, fixed configs) |
| How do you access a value in a dictionary? | By its key: `ship["shields"]` |
| What does `.get(key, default)` do? | Returns the value if the key exists, or the default if it doesn't — no crash |
| When is a dictionary better than a list? | When items have meaningful names rather than position numbers |
| Can a tuple be a dictionary key? | Yes — because tuples are immutable. Lists cannot be keys. |
| When would you use a tuple as a key? | Spatial grids, coordinates, game boards — anything addressed by two values |

---

## 🚫 Common Mistakes — Red Alert

**Mistake 1 — Off-by-one index:**
```python
crew = ["Picard", "Riker", "Data"]
#        index 0    index 1  index 2

print(crew[3])   # IndexError — there is no index 3 in a 3-item list
print(crew[2])   # Data — correct, the last item is at len(crew) - 1
```

---

**Mistake 2 — Using a list when you need a dictionary:**
```python
# CONFUSING — what is index 2?
ship = ["Enterprise", 100, 1012, 0]
ship[1] -= 40    # Which stat is this? You must check every time.

# CLEAR — key names explain themselves
ship = {"name": "Enterprise", "shields": 100, "crew": 1012, "warp": 0}
ship["shields"] -= 40   # Obviously the shields — no notes needed
```

---

**Mistake 3 — Trying to change a tuple:**
```python
coordinates = (53.1, 24.7, -1.4)
coordinates[0] = 99.0   # TypeError — tuples cannot be changed

# If you need to change it, you wanted a list:
coordinates = [53.1, 24.7, -1.4]
coordinates[0] = 99.0   # Works fine
```

---

**Mistake 4 — Accessing a missing dictionary key:**
```python
ship = {"shields": 100, "crew": 1012}

# WRONG — crashes with KeyError if "torpedoes" isn't there
print(ship["torpedoes"])

# SAFE — returns 0 as the default instead of crashing
print(ship.get("torpedoes", 0))
```

---

**Mistake 5 — Using a list as a dictionary key:**

```python
# WRONG — lists are mutable, so Python refuses to use them as keys
grid = {}
grid[[1, 1]] = "Voyager"   # TypeError: unhashable type: 'list'

# CORRECT — use a tuple instead
grid = {}
grid[(1, 1)] = "Voyager"   # Works — tuples are immutable and hashable
print(grid[(1, 1)])         # Voyager

# A quick way to remember: if Python can't guarantee the key will never change,
# it refuses to use it as a key. Tuples: guaranteed. Lists: not guaranteed.
```

---

**Mistake 6 — Confusing `sort()` and `sorted()`:**
```python
names = ["Worf", "Data", "Riker", "Troi"]

# sort() changes the original
names.sort()
print(names)   # ['Data', 'Riker', 'Troi', 'Worf'] — original is now sorted

# sorted() returns a NEW list — original unchanged
original = ["Worf", "Data", "Riker", "Troi"]
sorted_names = sorted(original)
print(original)      # ['Worf', 'Data', 'Riker', 'Troi']  ← unchanged
print(sorted_names)  # ['Data', 'Riker', 'Troi', 'Worf']  ← new list
```

---

## ✅ Ready to Move On?

Before opening Unit 2, tick every box:

- [ ] I watched all eight videos and wrote down answers to every guided question
- [ ] I typed out and ran all four practice blocks — no copy-pasting
- [ ] I can explain the difference between a list, a tuple, and a dictionary without notes
- [ ] I can explain why `ship["shields"]` is better than `ship[0]`
- [ ] I can explain why you would choose a tuple over a list for a screen resolution
- [ ] `lesson_data_practice.py` runs without any errors

If every box is ticked → **you are ready for Unit 2 — The Ledger and the Treasury.**

---

## 🤔 Still Confused? — Don't Panic

1. **Re-watch** the specific video for the part that is not clicking — the videos are short and targeted
2. **Print everything** — add `print()` calls around every line you don't understand; seeing the value always helps
3. **Change the data** — swap Voyager's crew for Picard's crew, change the shield values, add new keys; experimenting is learning
4. **Break it deliberately** — try accessing `crew[99]` or `ship["photon_cannons"]` and read the error message carefully
5. **Compare structures** — write the same data as a list AND a dictionary and feel the difference yourself

---

## 📚 Further Study — The Holodeck Library

| Resource | What it covers | Link |
|---|---|---|
| **Python Lists full tutorial** | Lists from zero | [YouTube](https://www.youtube.com/watch?v=LWeS6R9IPf4) |
| **Accessing List Items** | Indexes, slices, negative indexing | [YouTube](https://www.youtube.com/watch?v=oPZ5xoKZ6Og) |
| **Analyse a List** | `len()`, `min()`, `max()`, loops | [YouTube](https://www.youtube.com/watch?v=zVt7oaBUsHk) |
| **Add/Remove from a List** | `append()`, `insert()`, `remove()`, `pop()` | [YouTube](https://www.youtube.com/watch?v=qtANRuRxiEo) |
| **Sort Lists** | `sort()`, `sorted()`, reverse | [YouTube](https://www.youtube.com/watch?v=BUsmwsk8Des) |
| **Python Tuples** | Immutability and when to use tuples | [YouTube](https://www.youtube.com/watch?v=TTkifjHCPWo) |
| **Python Dictionaries** | Keys, values, methods | [YouTube](https://www.youtube.com/watch?v=rpsYzPv1HiQ) |
| **List vs Tuple vs Set vs Dict** | Choosing the right structure | [YouTube](https://www.youtube.com/watch?v=h-zcj4DmqHk) |

---

*Lesson — Lists, Tuples, and Dictionaries · Grade 11 Python*  
*Starfleet Academy — Data Management Division*  
*"Insufficient data cannot justify a conclusion, Counsellor."* 🖖
