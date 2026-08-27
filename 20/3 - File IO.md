# 📖 Lesson — File I/O in Python
### *Starfleet Academy — Royal Archives Division*

> **Course:** Grade 11 · Python  
> **Before this lesson:** You should have completed the Classes lesson, Unit 1, the Data Structures lesson, and Unit 2.  
> **After this lesson:** You will be ready to tackle Unit 3 — The Great Archives.

---

> *"The computer's memory is vast, but it is temporary. When power is lost, everything in RAM is gone. Starfleet's survival across centuries depends not on what officers remember — but on what is written down. The ship's log. The crew manifest. The mission database. All of it committed to permanent storage, retrievable long after the voyage ends."*
> — Inspired by the Starfleet Archives, Earth, 2364

---

## 🎯 Learning Goals

By the end of this lesson you will be able to:

- [ ] Explain the difference between **RAM** (temporary) and **file storage** (permanent)
- [ ] Open a file safely using the `with` statement
- [ ] Read a file using `read()`, `readlines()`, and line-by-line loops
- [ ] Write to a file using `"w"` mode and append using `"a"` mode
- [ ] Explain what each file mode does and when to use it
- [ ] Save a Python dictionary to a `.json` file using `json.dump()`
- [ ] Load a `.json` file back into Python using `json.load()`
- [ ] Handle missing or corrupted files safely using `try/except`

---

## 🎬 Watch First

> ⚠️ **A note on videos:** Data with Baraa's Python course is excellent for data concepts, but his File I/O content is embedded in longer data engineering tutorials that go beyond what you need right now. The videos below are the clearest targeted explanations available for each concept in this lesson. You will come back to Data with Baraa when we reach data analysis topics later in the course.

---

### 📺 Group 1 — Text Files: Reading and Writing *(watch before Section 1)*

| # | Topic | Video |
|---|---|---|
| 1 | **Python File I/O** — `open()`, modes, `read()`, `write()`, the `with` statement | 🎥 [Corey Schafer — File Objects](https://www.youtube.com/watch?v=Uh2ebFW8OYM) |
| 2 | **Reading Files** — `read()`, `readline()`, `readlines()`, looping | 🎥 [Tech With Tim — Reading Files](https://www.youtube.com/watch?v=4mX0uPQFLDU) |

**Write down while watching:**
- What is the difference between `"r"`, `"w"`, and `"a"` modes?
- What does the `with` statement do that `open()` alone does not?
- What is the difference between `read()` and `readlines()`?

---

### 📺 Group 2 — JSON: Structured Data Storage *(watch before Section 2)*

| # | Topic | Video |
|---|---|---|
| 3 | **JSON in Python** — `json.dump()`, `json.load()`, `json.dumps()`, `json.loads()` | 🎥 [Corey Schafer — JSON](https://www.youtube.com/watch?v=9N6a-VLBa2I) |

**Write down while watching:**
- What is the difference between `json.dump()` and `json.dumps()`?
- What is the difference between `json.load()` and `json.loads()`?
- What does `indent=4` do?

---

### 📺 Group 3 — Error Handling for Files *(watch before Section 3)*

| # | Topic | Video |
|---|---|---|
| 4 | **try/except in Python** — catching errors gracefully | 🎥 [Corey Schafer — Exceptions](https://www.youtube.com/watch?v=NIWwJbo-9_8) |

**Write down while watching:**
- What is a `FileNotFoundError` and when does it occur?
- What does `except Exception as e:` give you?
- Why is it better to let some errors crash than to catch all of them?

---

---

## Section 1 — Text Files: Reading and Writing 📄

### The Problem — RAM Is Temporary

Right now your game forgets everything when you close it. Every run starts fresh. The player's gold, their level, the enemies they defeated — all of it lives in RAM, and RAM is wiped the moment Python stops running.

**File I/O** (Input/Output) is how programs talk to the hard drive. Data written to a file survives after the program ends. Data read from a file can restore exactly where things left off.

```
Your Python program                    Your hard drive (permanent)
──────────────────                     ───────────────────────────
                    open("log.txt")
         ───────────────────────────►  finds or creates the file
                    file object
         ◄───────────────────────────  returns a connection
                    f.write("...")
         ───────────────────────────►  bytes flow to disk
                    with block ends
         ───────────────────────────►  file closed automatically
```

---

### The `open()` Function and File Modes

```python
# Syntax:  open(filename, mode)
# mode tells Python what you want to do with the file

open("log.txt", "r")    # Read   — file must exist or you get FileNotFoundError
open("log.txt", "w")    # Write  — creates the file if missing, ERASES if it exists
open("log.txt", "a")    # Append — creates if missing, adds to the END, never erases
open("log.txt", "r+")   # Read + Write — file must exist, does NOT erase
```

| Mode | File must exist? | Erases existing content? | Use when... |
|---|---|---|---|
| `"r"` | ✅ Yes — crashes if missing | No | Reading a file you know is there |
| `"w"` | No — creates it | ✅ **Yes** | Writing a fresh file each time |
| `"a"` | No — creates it | No | Adding to a log or history |
| `"r+"` | ✅ Yes — crashes if missing | No | Reading AND updating the same file |

> ⚠️ **The most dangerous mode is `"w"`.** It silently erases everything in the file before writing. If you mean to add to an existing file, use `"a"`. Using `"w"` by mistake has lost many programmers hours of work.

---

### The `with` Statement — Always Use It

You can open a file with just `open()`, but you must then remember to call `f.close()` yourself. If your program crashes before `close()`, the file can be left in a broken state.

The `with` statement solves this automatically:

```python
# WITHOUT with — you must remember to close, and crashes leave files open
f = open("log.txt", "r")
content = f.read()
f.close()        # easy to forget; crash before this = broken file

# WITH with — closes automatically when the block ends, even if an error occurs
with open("log.txt", "r") as f:
    content = f.read()
# file is closed here — automatically, always, even if an error occurred inside
```

> 💡 **Rule:** Always use `with open(...) as f:` — never bare `open()`. It is safer, cleaner, and shorter.

---

### Writing a File

```python
# Writing Starfleet's mission log to a text file
# "w" mode: creates the file if it does not exist, erases it if it does

with open("mission_log.txt", "w") as f:
    f.write("Stardate 47634.44\n")        # \n is the newline character
    f.write("USS Enterprise — NCC-1701-D\n")
    f.write("Departing Earth spacedock.\n")
    f.write("All systems nominal.\n")

# After this block, mission_log.txt exists on your hard drive
# Open it in VS Code and you will see exactly what was written
```

```python
# Writing multiple lines at once with a loop
log_entries = [
    "Stardate 47634.44 — Departing Earth spacedock.\n",
    "Stardate 47640.10 — Arrived at Veridian III.\n",
    "Stardate 47650.22 — Anomaly detected. Investigating.\n",
    "Stardate 47658.77 — Returning to base. Mission complete.\n",
]

with open("mission_log.txt", "w") as f:
    for entry in log_entries:
        f.write(entry)
```

---

### Appending to a File

```python
# "a" mode: adds to the END without erasing anything already there

with open("mission_log.txt", "a") as f:
    f.write("Stardate 47665.11 — Received distress signal from Klingon vessel.\n")
    f.write("Stardate 47670.00 — Responding. Warp 7 engaged.\n")

# The original entries are still there — these two were added to the bottom
```

---

### Reading a File

Three ways to read — each suits a different situation:

```python
# Method 1: read() — entire file as ONE big string
with open("mission_log.txt", "r") as f:
    content = f.read()
print(content)              # prints everything at once
print(type(content))        # <class 'str'>
```

```python
# Method 2: readlines() — entire file as a LIST of strings, one per line
with open("mission_log.txt", "r") as f:
    lines = f.readlines()   # ["Stardate 47634.44 — ...\n", "Stardate 47640.10 ...\n", ...]

print(lines[0])             # first line including the \n
print(lines[0].strip())     # first line WITHOUT the \n — strip() removes whitespace

# Count the log entries
print(f"Total log entries: {len(lines)}")
```

```python
# Method 3: Loop line by line — most memory-efficient for large files
with open("mission_log.txt", "r") as f:
    for line in f:
        clean = line.strip()     # remove the \n at the end
        if clean:                # skip blank lines
            print(f"  LOG: {clean}")
```

---

### The `\n` Newline Character

This trips up almost every beginner. When you write `"Picard\n"` to a file, the `\n` creates a new line. When you read it back, `\n` is still part of the string. Use `.strip()` to remove it:

```python
# In the file:          "USS Enterprise\n"
# After readlines():    "USS Enterprise\n"   ← \n is still there
# After .strip():       "USS Enterprise"     ← clean string

lines = ["USS Enterprise\n", "USS Defiant\n", "USS Voyager\n"]
clean_lines = [line.strip() for line in lines]
print(clean_lines)   # ['USS Enterprise', 'USS Defiant', 'USS Voyager']
```

---

### 🧪 Practice Block 1 — The Ship's Log

Create `lesson_fileio_practice.py` and type this out:

```python
# lesson_fileio_practice.py — Practice Block 1: Text Files

import os

# MISSION 1: Write a mission log
print("=== WRITING THE MISSION LOG ===")

log_entries = [
    "Stardate 47634.44 — USS Enterprise departing Earth spacedock.",
    "Stardate 47640.10 — Arrived at the Veridian system. All quiet.",
    "Stardate 47650.22 — Temporal anomaly detected near the star.",
    "Stardate 47658.77 — Anomaly dissipated. Crew unaffected.",
    "Stardate 47665.11 — Distress signal from IKS Rotarran received.",
    "Stardate 47670.00 — Rendezvous with Klingon vessel. Crew rescued.",
]

with open("mission_log.txt", "w") as f:
    for entry in log_entries:
        f.write(entry + "\n")

print(f"Mission log written: {len(log_entries)} entries.")
print("Open mission_log.txt in VS Code to verify.")

# MISSION 2: Append a new entry
print("\n=== APPENDING NEW ENTRY ===")
with open("mission_log.txt", "a") as f:
    f.write("Stardate 47680.33 — Returning to Earth. Mission complete.\n")
print("New entry appended.")

# MISSION 3: Read the whole log
print("\n=== READING THE FULL LOG ===")
with open("mission_log.txt", "r") as f:
    for line in f:
        print(f"  {line.strip()}")

# MISSION 4: Read into a list and analyse it
print("\n=== LOG ANALYSIS ===")
with open("mission_log.txt", "r") as f:
    lines = f.readlines()

total = len(lines)
clean = [l.strip() for l in lines if l.strip()]
print(f"Total entries: {total}")
print(f"First entry: {clean[0]}")
print(f"Last entry:  {clean[-1]}")

# MISSION 5: Search the log
print("\n=== SEARCHING FOR ANOMALY ENTRIES ===")
with open("mission_log.txt", "r") as f:
    for i, line in enumerate(f, 1):
        if "anomaly" in line.lower():
            print(f"  Line {i}: {line.strip()}")
```

**Answer these in a comment before moving on:**
```python
# Q1: You wrote the log with "w" mode. Run the script a second time.
#     How many entries does the log have? Why is it not doubling?
# A1:

# Q2: Change the append line to use "w" instead of "a". Run it.
#     What happened to the original 6 entries? Why?
# A2:

# Q3: What does line.strip() remove, and why do you need it?
# A3:
```

---

---

## Section 2 — JSON: Structured Data That Survives 🖥️

### Why JSON and Not Plain Text?

Plain text files work for human-readable logs. But your player's stats are a Python dictionary. Writing them as text and reading them back would require you to parse every line manually — splitting strings, converting types, handling errors. It would be fragile and tedious.

**JSON (JavaScript Object Notation)** solves this. It converts Python dictionaries and lists directly into structured text, and reads them straight back. Because you already store your game data as dictionaries and lists, saving becomes almost no extra work.

```
Python dictionary                JSON file on disk
─────────────────                ─────────────────
{                                {
  "shields": 85,      ──────►        "shields": 85,
  "crew": 1012,       json.dump      "crew": 1012,
  "warp": 7,                         "warp": 7,
  "cloaked": False                   "cloaked": false
}                                }

{                                {
  "shields": 85,      ◄──────        "shields": 85,
  "crew": 1012,       json.load      "crew": 1012,
  "warp": 7,                         "warp": 7,
  "cloaked": False                   "cloaked": false
}                                }
```

---

### `json.dump()` and `json.load()` — Saving and Loading

```python
import json

# The current status of the USS Voyager — a Python dictionary
voyager_status = {
    "name":       "USS Voyager",
    "registry":   "NCC-74656",
    "shields":    72,
    "hull":       91,
    "crew":       141,
    "warp":       9,
    "cloaked":    False,
    "sector":     [1, 4],          # a list inside the dictionary — fine!
    "log":        ["Entered Delta Quadrant", "First contact: Ocampa"],
}

# ── SAVING ───────────────────────────────────────────────────────────────────
# json.dump(data, file_object)  — writes Python → JSON to a file
# indent=4 makes the file human-readable (you can open it in VS Code)

with open("voyager_status.json", "w") as f:
    json.dump(voyager_status, f, indent=4)

print("Saved. Open voyager_status.json in VS Code — it should be readable.")
```

After running this, open `voyager_status.json` in VS Code. You will see:

```json
{
    "name": "USS Voyager",
    "registry": "NCC-74656",
    "shields": 72,
    "hull": 91,
    "crew": 141,
    "warp": 9,
    "cloaked": false,
    "sector": [1, 4],
    "log": [
        "Entered Delta Quadrant",
        "First contact: Ocampa"
    ]
}
```

Notice: Python's `False` becomes JSON's `false` (lowercase). Python's `True` becomes `true`. Python's `None` becomes `null`. These are automatically converted back when you load.

```python
# ── LOADING ───────────────────────────────────────────────────────────────────
# json.load(file_object)  — reads JSON from a file → Python dictionary

with open("voyager_status.json", "r") as f:
    loaded = json.load(f)

print(type(loaded))             # <class 'dict'>  — it came back as a dict
print(loaded["name"])           # USS Voyager
print(loaded["shields"])        # 72
print(loaded["log"])            # ['Entered Delta Quadrant', 'First contact: Ocampa']
print(loaded["cloaked"])        # False  — JSON false became Python False again
```

---

### `json.dumps()` and `json.loads()` — Working With Strings

Sometimes you don't need a file — you want JSON as a string (for printing, sending over a network, or debugging):

```python
import json

data = {"ship": "Voyager", "shields": 72}

# dumps (dump to String) — converts Python → JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
print(type(json_string))    # <class 'str'>

# loads (load from String) — converts JSON string → Python
back_to_dict = json.loads(json_string)
print(back_to_dict["ship"])    # Voyager
print(type(back_to_dict))      # <class 'dict'>
```

**Easy way to remember:**
- `dump` / `load` → **file** (no `s`)
- `dumps` / `loads` → **string** (the `s` stands for string)

---

### What Python Types Become in JSON

| Python | JSON | Notes |
|---|---|---|
| `dict` | `object {}` | Keys must be strings in JSON |
| `list` | `array []` | |
| `str` | `string ""` | |
| `int` / `float` | `number` | |
| `True` / `False` | `true` / `false` | JSON uses lowercase |
| `None` | `null` | |
| `tuple` | `array []` | Tuples become lists — they load back as lists |

> ⚠️ **Tuples become lists in JSON.** If you save `(1, 4)` (a tuple), it loads back as `[1, 4]` (a list). If you need a tuple after loading, convert it: `tuple(loaded["sector"])`.

---

### 🧪 Practice Block 2 — The Ship's Computer Database

Add this below Practice Block 1:

```python
# Practice Block 2: JSON

import json

# The fleet database — dictionary of ship status dictionaries
fleet_database = {
    "enterprise": {
        "name":     "USS Enterprise",
        "registry": "NCC-1701-D",
        "shields":  85,
        "hull":     100,
        "crew":     1012,
        "warp":     0,
        "missions": ["Veridian III", "Wolf 359", "First Contact"],
    },
    "defiant": {
        "name":     "USS Defiant",
        "registry": "NX-74205",
        "shields":  60,
        "hull":     88,
        "crew":     50,
        "warp":     9,
        "missions": ["Dominion War patrol", "Deep Space Nine defence"],
    },
    "voyager": {
        "name":     "USS Voyager",
        "registry": "NCC-74656",
        "shields":  72,
        "hull":     91,
        "crew":     141,
        "warp":     9,
        "missions": ["Delta Quadrant transit"],
    },
}

# MISSION 1: Save the fleet database to JSON
print("=== SAVING FLEET DATABASE ===")
with open("fleet_database.json", "w") as f:
    json.dump(fleet_database, f, indent=4)
print("fleet_database.json saved. Open it in VS Code.")

# MISSION 2: Load it back and verify
print("\n=== LOADING AND VERIFYING ===")
with open("fleet_database.json", "r") as f:
    loaded_fleet = json.load(f)

print(f"Ships in database: {len(loaded_fleet)}")
for key, ship in loaded_fleet.items():
    print(f"  {ship['name']}: shields {ship['shields']}%  hull {ship['hull']}%")

# MISSION 3: Modify the loaded data and save again
print("\n=== BATTLE DAMAGE UPDATE ===")
loaded_fleet["enterprise"]["shields"] -= 40
loaded_fleet["defiant"]["hull"]       -= 15
loaded_fleet["enterprise"]["missions"].append("Borg encounter")

with open("fleet_database.json", "w") as f:
    json.dump(loaded_fleet, f, indent=4)
print("Updated fleet database saved.")

# MISSION 4: Demonstrate dumps/loads for quick display
print("\n=== QUICK JSON STRING DISPLAY ===")
voyager_only = loaded_fleet["voyager"]
as_string    = json.dumps(voyager_only, indent=2)
print(as_string)
print(f"Type of as_string: {type(as_string)}")

back = json.loads(as_string)
print(f"Missions loaded back as: {type(back['missions'])}")   # should be list
```

**Answer in a comment:**
```python
# Q1: Open fleet_database.json in VS Code after running.
#     Python's True becomes ___ in JSON.
#     Python's None would become ___ in JSON.
# A1:

# Q2: You saved a list of missions. After json.load(), is it still a list?
#     What type is it? How did you verify this?
# A2:

# Q3: What is the difference between json.dump() and json.dumps()?
#     Give one situation where you would use each one.
# A3:
```

---

---

## Section 3 — Handling Missing and Broken Files 🛡️

### Why Files Can Go Wrong

Files fail in predictable ways:

| Error | What causes it | Python exception |
|---|---|---|
| File does not exist | Player deleted the save file, first run ever | `FileNotFoundError` |
| File is corrupted | Save was interrupted mid-write, manual edits broke the JSON | `json.JSONDecodeError` |
| Expected key is missing | Old save format, someone manually edited the JSON | `KeyError` |
| Permission denied | File is locked by another process | `PermissionError` |

A program that crashes on a missing save file is a bad program. These are predictable, recoverable situations — your code should handle them gracefully.

---

### `try/except` — Catching Errors Without Crashing

```python
# Without try/except — any error crashes the program
with open("save.json", "r") as f:    # FileNotFoundError if file missing
    data = json.load(f)              # JSONDecodeError if file is corrupted

# With try/except — specific errors are caught and handled
try:
    with open("save.json", "r") as f:
        data = json.load(f)
    print("Save loaded successfully.")
except FileNotFoundError:
    print("No save file found — starting fresh.")
    data = {}
except json.JSONDecodeError:
    print("Save file is corrupted — starting fresh.")
    data = {}
```

---

### `os.path.exists()` — Check Before Opening

Sometimes you want to check whether a file exists *before* trying to open it — for example, to grey out a "Load Game" button in a menu:

```python
import os

save_file = "voyager_save.json"

if os.path.exists(save_file):
    print("Save file found — Load Game is available.")
else:
    print("No save file — Load Game is greyed out.")
```

---

### A Complete Save and Load System

Here is the full pattern you will use in Unit 3. Read every comment:

```python
import json
import os

SAVE_FILE = "voyager_save.json"

def save_ship(ship_data):
    """
    Save the ship's status dictionary to a JSON file.
    Called when the player presses S.
    """
    with open(SAVE_FILE, "w") as f:
        json.dump(ship_data, f, indent=4)
    print(f"💾 Saved: {ship_data['name']}  Shields: {ship_data['shields']}%")


def load_ship():
    """
    Load ship status from JSON.
    Returns the dictionary if successful.
    Returns None if file is missing or corrupted — caller decides what to do.
    """
    if not os.path.exists(SAVE_FILE):
        print("📂 No save file found.")
        return None                         # caller can start fresh

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        print(f"📖 Loaded: {data['name']}  Shields: {data['shields']}%")
        return data

    except json.JSONDecodeError:
        print("⚠️  Save file is corrupted — starting fresh.")
        return None

    except KeyError as e:
        print(f"⚠️  Save file missing field '{e}' — starting fresh.")
        return None


def delete_save():
    """Remove the save file. Called when starting a New Game."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("🗑️  Save file deleted.")
    else:
        print("Nothing to delete.")
```

> 💡 **Why return `None` instead of an empty dict `{}`?** Returning `None` lets the caller decide what to do. An empty dict `{}` looks like a valid (but empty) save, which could cause confusing downstream bugs. `None` is unambiguous: "there is no save data."

---

### Deliberately Breaking Files (Learning Tool)

The best way to understand how errors occur is to cause them yourself:

```python
# Test 1 — FileNotFoundError
# Delete voyager_save.json in VS Code, then call load_ship()
# It should print "No save file found." — not crash

# Test 2 — JSONDecodeError
# Open voyager_save.json in VS Code
# Delete the closing } from the last line
# Save the file, then call load_ship()
# It should print "Save file is corrupted." — not crash

# Test 3 — KeyError
# Open voyager_save.json in VS Code
# Delete the "name" line entirely
# Save, then call load_ship()
# It should print "Save file missing field 'name'." — not crash
```

---

### 🧪 Practice Block 3 — The Complete Archive System

Add this below Practice Block 2:

```python
# Practice Block 3: Save, Load, and Error Handling

import json, os

ARCHIVE_FILE = "starfleet_archive.json"

def save_archive(data):
    with open(ARCHIVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Archive saved: {len(data)} records.")

def load_archive():
    if not os.path.exists(ARCHIVE_FILE):
        print("Archive not found — starting with empty records.")
        return {}
    try:
        with open(ARCHIVE_FILE, "r") as f:
            data = json.load(f)
        print(f"Archive loaded: {len(data)} records found.")
        return data
    except json.JSONDecodeError:
        print("Archive corrupted — starting with empty records.")
        return {}
    except KeyError as e:
        print(f"Archive missing field {e} — starting with empty records.")
        return {}

def add_mission_record(archive, ship_name, mission):
    if ship_name not in archive:
        archive[ship_name] = {"missions": [], "commendations": 0}
    archive[ship_name]["missions"].append(mission)
    print(f"  Added: {ship_name} — {mission}")


# MISSION 1: Build and save the archive
print("=== BUILDING THE ARCHIVE ===")
archive = {}
add_mission_record(archive, "USS Enterprise", "Veridian III rescue operation")
add_mission_record(archive, "USS Enterprise", "First contact with the Borg")
add_mission_record(archive, "USS Voyager",    "Transit of the Nekrit Expanse")
add_mission_record(archive, "USS Defiant",    "Dominion War — Cardassian border")
archive["USS Enterprise"]["commendations"] = 3
archive["USS Voyager"]["commendations"]    = 1

save_archive(archive)

# MISSION 2: Load it back
print("\n=== LOADING THE ARCHIVE ===")
loaded = load_archive()
for ship, record in loaded.items():
    print(f"  {ship}: {len(record['missions'])} missions, "
          f"{record['commendations']} commendations")

# MISSION 3: Test missing file
print("\n=== TESTING MISSING FILE ===")
os.remove(ARCHIVE_FILE)           # delete it on purpose
result = load_archive()           # should handle gracefully
print(f"Returned: {result}")      # should be {}

# MISSION 4: Test corrupted file — write deliberately broken JSON
print("\n=== TESTING CORRUPTED FILE ===")
with open(ARCHIVE_FILE, "w") as f:
    f.write('{"USS Enterprise": {"missions": ["Veridian III"')   # deliberately incomplete
result = load_archive()           # should catch JSONDecodeError
print(f"Returned: {result}")      # should be {}

# MISSION 5: Clean up and rebuild properly
print("\n=== REBUILDING ARCHIVE ===")
os.remove(ARCHIVE_FILE)
save_archive(archive)
final = load_archive()
print(f"Archive restored: {len(final)} ships")
```

---

## Section 4 — Putting It All Together 🖖

### Text Files vs JSON — When to Use Each

| Use a **text file** when... | Use a **JSON file** when... |
|---|---|
| The content is meant for humans to read | The content is structured Python data |
| You are storing a log or a plain document | You are saving dictionaries or lists |
| Format is simple — one thing per line | Multiple related values belong together |
| `mission_log.txt` — dated log entries | `save_game.json` — player stats and position |
| `monster_manual.txt` — lore text | `fleet_database.json` — nested ship records |

---

### The Complete File I/O Toolkit

```python
# Everything you need for Unit 3 — in one place

import json
import os

# ── Text files ────────────────────────────────────────────────────────────────
with open("log.txt", "w") as f:         # write (erases first)
    f.write("Line one\n")

with open("log.txt", "a") as f:         # append (preserves content)
    f.write("Line two\n")

with open("log.txt", "r") as f:         # read
    content   = f.read()                # whole file as one string
    # OR
with open("log.txt", "r") as f:
    lines     = f.readlines()           # list of lines (each has \n)
    # OR
with open("log.txt", "r") as f:
    for line in f:                      # line by line — best for large files
        clean = line.strip()

# ── JSON files ────────────────────────────────────────────────────────────────
data = {"ship": "Voyager", "shields": 85}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)        # Python dict → JSON file

with open("data.json", "r") as f:
    loaded = json.load(f)              # JSON file → Python dict

# ── Checking file existence ───────────────────────────────────────────────────
if os.path.exists("data.json"):
    print("File is there.")
else:
    print("File is missing.")

os.remove("data.json")                  # delete a file

# ── Error handling ────────────────────────────────────────────────────────────
try:
    with open("data.json", "r") as f:
        loaded = json.load(f)
except FileNotFoundError:
    loaded = {}                          # no file — start fresh
except json.JSONDecodeError:
    loaded = {}                          # corrupted — start fresh
except KeyError as e:
    print(f"Missing key: {e}")
    loaded = {}
```

---

## 🔑 Key Takeaways

Cover the right column and answer from memory:

| Question | Answer |
|---|---|
| What is the difference between RAM and file storage? | RAM is temporary — wiped when the program stops. Files persist on the hard drive. |
| What does `"w"` mode do that makes it dangerous? | It erases all existing content before writing |
| What does `"a"` mode do differently from `"w"`? | Appends to the end without erasing anything |
| Why use `with open() as f:` instead of just `open()`? | Closes the file automatically — even if an error occurs |
| What does `line.strip()` remove? | Leading and trailing whitespace, including the `\n` newline character |
| What does `json.dump()` do? | Converts a Python dict/list → writes JSON text to a file |
| What does `json.load()` do? | Reads JSON text from a file → converts to a Python dict/list |
| `dump` vs `dumps` — what does the `s` mean? | `s` = string. `dumps` converts to a string; `dump` writes to a file |
| What exception does a missing file raise? | `FileNotFoundError` |
| What exception does broken JSON raise? | `json.JSONDecodeError` |

---

## 🚫 Common Mistakes — Red Alert

**Mistake 1 — Using `"w"` when you meant `"a"`:**
```python
# WRONG — erases your log on every run
with open("mission_log.txt", "w") as f:
    f.write("New entry\n")              # original entries are GONE

# CORRECT — adds to the log without destroying history
with open("mission_log.txt", "a") as f:
    f.write("New entry\n")
```

---

**Mistake 2 — Forgetting `\n` between lines:**
```python
# WRONG — all entries run together on one line
with open("log.txt", "w") as f:
    f.write("Entry one")
    f.write("Entry two")               # no \n = same line as Entry one

# CORRECT — each write ends with a newline
with open("log.txt", "w") as f:
    f.write("Entry one\n")
    f.write("Entry two\n")
```

---

**Mistake 3 — Not stripping `\n` when reading:**
```python
with open("log.txt", "r") as f:
    lines = f.readlines()

# WRONG — lines still have \n attached
print(lines[0])               # "Entry one\n"   ← the \n is there
print(lines[0] == "Entry one") # False!

# CORRECT — strip the newline before using the string
print(lines[0].strip())         # "Entry one"
print(lines[0].strip() == "Entry one")  # True
```

---

**Mistake 4 — Not using `try/except` for file operations:**
```python
# WRONG — crashes if file is missing
with open("save.json", "r") as f:
    data = json.load(f)

# CORRECT — handles the error gracefully
try:
    with open("save.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
    print("No save found — starting fresh.")
```

---

**Mistake 5 — Using `json.load()` on a string instead of a file:**
```python
json_string = '{"ship": "Voyager"}'

# WRONG — json.load() expects a FILE OBJECT, not a string
data = json.load(json_string)       # TypeError

# CORRECT — use json.loads() for strings
data = json.loads(json_string)      # loads = load from String
print(data["ship"])                 # Voyager
```

---

## ✅ Ready to Move On?

Before opening Unit 3, tick every box:

- [ ] I watched all four videos and wrote down answers to the guided questions
- [ ] I typed out and ran all three practice blocks — no copy-pasting
- [ ] I can explain what `"r"`, `"w"`, and `"a"` do without looking at my notes
- [ ] I can explain why `with open(...) as f:` is always better than bare `open()`
- [ ] I can explain the difference between `json.dump()` and `json.dumps()`
- [ ] I deliberately broke a JSON file and confirmed my `try/except` handled it gracefully
- [ ] `lesson_fileio_practice.py` runs without errors

If every box is ticked → **you are ready for Unit 3 — The Great Archives.**

---

## 🤔 Still Confused? — Don't Panic

1. **Open the files in VS Code** — every time you write a file, open it and look at it. Seeing the actual content on disk is the fastest way to verify your code is doing what you think.
2. **Use `print(type(x))`** everywhere — after loading from JSON, print the type of every variable. `dict`? `list`? `str`? Knowing the type prevents almost all confusion.
3. **Break it deliberately** — manually edit a JSON file in VS Code to introduce errors; run your code and confirm the `try/except` catches it cleanly.
4. **Re-watch the Corey Schafer file video** at 0.75× speed — his explanation of the `with` statement is exceptionally clear.
5. **Search** `"python json.load vs json.loads difference"` — this is the most commonly googled File I/O question for a reason.

---

## 📚 Further Study — The Holodeck Library

| Resource | What it covers | Link |
|---|---|---|
| **Corey Schafer — File Objects** | `open()`, modes, `with`, `read()`, `readlines()` | [YouTube](https://www.youtube.com/watch?v=Uh2ebFW8OYM) |
| **Corey Schafer — JSON** | `json.dump`, `load`, `dumps`, `loads`, `indent` | [YouTube](https://www.youtube.com/watch?v=9N6a-VLBa2I) |
| **Corey Schafer — Exceptions** | `try/except`, common exception types | [YouTube](https://www.youtube.com/watch?v=NIWwJbo-9_8) |
| **Real Python — File I/O** | Comprehensive written guide with examples | [realpython.com](https://realpython.com/read-write-files-python/) |
| **Python Docs — json module** | Official reference for every json function | [docs.python.org](https://docs.python.org/3/library/json.html) |
| **Python Docs — os.path** | `exists()`, `remove()`, and other file system tools | [docs.python.org](https://docs.python.org/3/library/os.path.html) |

---

*Lesson — File I/O · Grade 11 Python*  
*Starfleet Academy — Royal Archives Division*  
*"The record is the only thing that outlasts the mission." 🖖*
