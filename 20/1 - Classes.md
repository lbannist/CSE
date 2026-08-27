# 📖 Lesson — Classes and Objects in Python
### *Starfleet Academy — Programming Division*

> **Course:** Grade 11 · Python  
> **Before this lesson:** You should be comfortable with functions, loops, and if/else from Grade 10.  
> **After this lesson:** You will apply what you learned here in your first unit assignment.

---

> *"The human brain — and the Vulcan brain — is an object. It has properties: intelligence, memory capacity, emotional control. It has behaviours: learning, reasoning, deciding. When Starfleet designs a computer system, it models the universe the same way. Everything is an object."*
> — Inspired by Commander Data, USS Enterprise NCC-1701-D

---

## 🎯 Learning Goals

By the end of this lesson you will be able to:

- [ ] Explain the difference between a **class** and an **instance** in your own words
- [ ] Write a class with `__init__`, attributes, and methods from scratch
- [ ] Explain what `self` means and why every method needs it
- [ ] Create multiple independent instances from one class and prove they are separate
- [ ] Recognise when a class is the right tool for a problem

---

## 🎬 Watch First

Watch these two videos **before** reading the notes below. Pause frequently and try the code yourself — do not just watch passively.

---

### Video 1 — Python OOP Tutorial: Classes and Instances *(~26 min)*

**Corey Schafer** is one of the clearest Python educators on YouTube. This video starts from zero and builds up everything you need.

[![Watch the video](https://img.youtube.com/vi/ZDa-Z5JzLYM/maxresdefault.jpg)](https://youtu.be/ZDa-Z5JzLYM)

**Write down answers to these while you watch:**
- What is the difference between a class and an instance?
- What does `__init__` do, and when does it run?
- What is `self`, and why is it always the first parameter?

---

### Video 2 — Python Classes for Beginners *(~15 min)*

**Tech With Tim** uses a different example and a slightly different explanation style. Hearing the same concept explained differently is one of the fastest ways to make something stick.

[![Watch the video](https://img.youtube.com/vi/jQiUOV15IRI/maxresdefault.jpg)](https://youtu.be/jQiUOV15IRI)

**Write down answers to these while you watch:**
- How do you create an instance from a class?
- How is `self.name` different from a regular variable called `name`?

---

## 📝 Lesson Notes

### The Problem That Classes Solve

Starfleet Command needs to track every ship in the fleet. Each ship has a name, a registry number, a crew count, and shield strength. In the style of programming you used in Grade 10, a junior programmer might write this:

```python
# Procedural approach — loose variables for every ship
ship1_name     = "USS Enterprise"
ship1_registry = "NCC-1701-D"
ship1_crew     = 1012
ship1_shields  = 100

ship2_name     = "USS Defiant"
ship2_registry = "NX-74205"
ship2_crew     = 50
ship2_shields  = 100

# Fire phasers at ship1
ship1_shields -= 40
print(f"{ship1_name} shields at {ship1_shields}%")

# What about ship3? ship4? The entire Klingon fleet?
# You would need three new variables per ship.
# And what if you want to check if a ship is destroyed?
# You would have to write that check everywhere, by hand, every time.
```

This approach falls apart the moment Starfleet has more than a handful of ships. There is no clean way to say *"do this to ship 7"* and the logic for what counts as a destroyed ship has to be copied everywhere it's needed.

**Classes** solve this by bundling the data (name, shields, crew) and the behaviour (take damage, hail, self-destruct) into one reusable blueprint. You write the blueprint once and stamp out as many ships as the fleet needs:

```python
# With a class — one blueprint, infinite ships
enterprise = Starship("USS Enterprise", "NCC-1701-D", crew=1012)
defiant    = Starship("USS Defiant",    "NX-74205",   crew=50)
voyager    = Starship("USS Voyager",    "NCC-74656",  crew=141)

enterprise.take_damage(40)
defiant.hail("USS Enterprise")
print(voyager.status_report())
```

The rest of this lesson teaches you how to write that `Starship` class.

---

### Anatomy of a Class

Every class follows the same structure. Read every comment — they are part of the lesson.

```python
# ── The class keyword defines the blueprint ───────────────────────────────────
# Class names use CapitalLetters (called PascalCase — it is a Python convention)

class Starship:

    # ── __init__ is the CONSTRUCTOR ───────────────────────────────────────────
    # Python calls __init__ automatically the instant you create a Starship.
    # You never call it yourself — Python does it for you.
    #
    # self  = the specific ship being created right now
    # name  = whatever name you pass in when creating the ship
    # ...and so on for each parameter

    def __init__(self, name, registry, crew):

        # ── Attributes — data stored ON this specific instance ────────────────
        # self.name means "THIS ship's name" — not a global variable.
        # Every Starship gets its own completely separate copy of these.

        self.name     = name
        self.registry = registry
        self.crew     = crew
        self.shields  = 100     # all ships start at full shields
        self.hull     = 100     # and full hull integrity
        self.is_cloaked = False # Starfleet ships don't cloak... usually

    # ── Methods — functions that belong to this class ─────────────────────────
    # Every method takes self as its FIRST parameter — no exceptions.
    # self lets the method access and update THIS ship's attributes.

    def take_damage(self, amount):
        """Distribute incoming damage to shields first, then hull."""
        if self.shields >= amount:
            self.shields -= amount
            print(f"{self.name}: Shields at {self.shields}%. Hull intact.")
        else:
            # Shields absorb what they can, hull takes the rest
            remainder    = amount - self.shields
            self.shields = 0
            self.hull   -= remainder
            print(f"{self.name}: SHIELDS DOWN! Hull at {self.hull}%.")
            if self.hull <= 0:
                print(f"{self.name}: Hull breach. Ship destroyed.")

    def hail(self, target_name):
        """Open a communication channel."""
        print(f"{self.name} to {target_name}: Hailing frequencies open.")

    def engage_cloak(self):
        """Engage the cloaking device (if installed)."""
        self.is_cloaked = True
        print(f"{self.name} has cloaked.")

    def status_report(self):
        """Return a formatted status string."""
        cloak_status = "CLOAKED" if self.is_cloaked else "visible"
        return (
            f"=== {self.name} ({self.registry}) ===\n"
            f"  Crew:    {self.crew}\n"
            f"  Shields: {self.shields}%\n"
            f"  Hull:    {self.hull}%\n"
            f"  Status:  {cloak_status}"
        )
```

---

### Creating Instances

The class is the blueprint. An **instance** is one specific ship built from that blueprint.

```python
# Create three completely separate Starship instances
enterprise = Starship("USS Enterprise", "NCC-1701-D", crew=1012)
defiant    = Starship("USS Defiant",    "NX-74205",   crew=50)
voyager    = Starship("USS Voyager",    "NCC-74656",  crew=141)

# Each ship has its OWN shields, hull, and crew — they share nothing
enterprise.take_damage(60)    # Enterprise takes a hit
defiant.take_damage(30)       # Defiant takes a separate hit
voyager.engage_cloak()        # Voyager cloaks — doesn't affect the others

print(enterprise.status_report())
print()
print(defiant.status_report())
print()
print(voyager.status_report())
```

Output:
```
USS Enterprise: Shields at 40%. Hull intact.
USS Defiant: Shields at 70%. Hull intact.
USS Voyager has cloaked.

=== USS Enterprise (NCC-1701-D) ===
  Crew:    1012
  Shields: 40%
  Hull:    100%
  Status:  visible

=== USS Defiant (NX-74205) ===
  Crew:    50
  Shields: 70%
  Hull:    100%
  Status:  visible

=== USS Voyager (NCC-74656) ===
  Crew:    141
  Shields: 100%
  Hull:    100%
  Status:  CLOAKED
```

> **This is the most important thing to understand about instances:** `enterprise`, `defiant`, and `voyager` are all `Starship` objects, but each one owns a completely separate copy of every attribute. Damaging the Enterprise does not change Defiant's shields. Cloaking Voyager does not cloak anyone else.

---

### What Is `self`?

`self` trips up almost everyone the first time they see it. Here is the clearest way to think about it:

> **`self` is the ship talking about itself.**

When you call `enterprise.take_damage(60)`, Python secretly rewrites it like this:

```python
# What you write:
enterprise.take_damage(60)

# What Python actually does behind the scenes:
Starship.take_damage(enterprise, 60)
#                    ^^^^^^^^^^
#                    self = enterprise — Python passes this automatically
```

Python passes the instance as `self` automatically. You **never** type `self` when calling a method. You **always** write it as the first parameter when defining one.

```python
# CALLING — do NOT write self
enterprise.take_damage(60)
defiant.hail("USS Enterprise")

# DEFINING — ALWAYS write self as the first parameter
def take_damage(self, amount):
    self.shields -= amount

def hail(self, target_name):
    print(f"{self.name} to {target_name}: hailing...")
```

Without `self`, the `take_damage` method would have no way to know *which ship* it is dealing damage to. It could be Enterprise, Defiant, Voyager, or a Klingon Bird-of-Prey. `self` is the answer to: *"which specific ship are we talking about right now?"*

---

### The `__init__` Method in Detail

`__init__` is the **constructor**. Python calls it automatically the moment you create an instance — you never call it yourself.

```python
enterprise = Starship("USS Enterprise", "NCC-1701-D", crew=1012)
# ↑ Python immediately calls:
# Starship.__init__(enterprise, "USS Enterprise", "NCC-1701-D", 1012)
# self = enterprise
# name = "USS Enterprise"
# registry = "NCC-1701-D"
# crew = 1012
```

Whatever you assign with `self.` inside `__init__` becomes a permanent attribute — data the ship carries throughout its lifetime.

```python
def __init__(self, name, registry, crew):
    self.name     = name       # stored permanently on the instance
    self.registry = registry
    self.crew     = crew
    self.shields  = 100        # you can add attributes that don't come from parameters
    self.hull     = 100        # every ship starts at full hull
    self.is_cloaked = False    # every ship starts visible
```

The attributes that do not come from parameters (`shields`, `hull`, `is_cloaked`) give every new ship sensible defaults. You do not have to pass in `shields=100` every time — the class handles that for you.

---

### `__repr__` — The Captain's Log Entry

By default, `print(enterprise)` shows something useless:

```
<__main__.Starship object at 0x10f3a2c10>
```

Fix this by defining `__repr__` — Python calls it automatically when you `print()` an instance:

```python
class Starship:
    # ... all existing code ...

    def __repr__(self):
        return f"Starship('{self.name}', shields={self.shields}%, hull={self.hull}%)"

print(enterprise)   # Starship('USS Enterprise', shields=40%, hull=100%)
print(defiant)      # Starship('USS Defiant', shields=70%, hull=100%)
```

`__repr__` is one of Python's **dunder methods** (double underscore on both sides — short for "double-underscore", sometimes called "magic methods"). You will encounter more of them throughout the year.

---

### Classes vs Functions — When to Use Each

| Use a **function** when... | Use a **class** when... |
|---|---|
| You have one specific task to perform | You need data AND behaviour bundled together |
| No state needs to be remembered | The thing needs to remember and update its own state |
| You do it once and you are done | You need many independent copies of the same thing |
| `distance = calculate_warp_distance(speed, time)` | `ship = Starship("USS Enterprise", "NCC-1701-D", 1012)` |

**A useful rule of thumb:** If you find yourself creating multiple variables that all belong to the same *thing* (`ship1_name`, `ship1_shields`, `ship1_hull`), that thing probably wants to be a class.

---

## 🧪 Try It Yourself — Four Practice Missions

Open VS Code and create `lesson_practice.py`. Work through each mission in order. **Type the code — do not copy and paste it.** Typing it yourself forces your brain to process every character.

---

### 🖖 Mission 1 — Commission the Fleet

```python
# lesson_practice.py — Mission 1

class Starship:
    def __init__(self, name, registry, crew):
        self.name       = name
        self.registry   = registry
        self.crew       = crew
        self.shields    = 100
        self.hull       = 100
        self.is_cloaked = False

    def take_damage(self, amount):
        if self.shields >= amount:
            self.shields -= amount
            print(f"{self.name}: Shields at {self.shields}%. Hull intact.")
        else:
            remainder    = amount - self.shields
            self.shields = 0
            self.hull   -= remainder
            print(f"{self.name}: SHIELDS DOWN! Hull at {self.hull}%.")

    def hail(self, target_name):
        print(f"{self.name} to {target_name}: Hailing frequencies open.")

    def status_report(self):
        return (
            f"=== {self.name} ({self.registry}) ===\n"
            f"  Crew: {self.crew}  |  Shields: {self.shields}%  |  Hull: {self.hull}%"
        )


# Commission three ships
enterprise = Starship("USS Enterprise", "NCC-1701-D", crew=1012)
defiant    = Starship("USS Defiant",    "NX-74205",   crew=50)
voyager    = Starship("USS Voyager",    "NCC-74656",  crew=141)

# Simulate a battle — each ship takes different damage
enterprise.take_damage(60)
defiant.take_damage(30)
enterprise.take_damage(20)    # Enterprise takes a second hit

# Print status of all three
print(enterprise.status_report())
print(defiant.status_report())
print(voyager.status_report())   # Voyager was not in the battle
```

Run it. Then answer this in a comment:

```python
# Q: After enterprise.take_damage(60), what is defiant.shields?
#    Why hasn't it changed?
# A: (write your answer here)
```

---

### 🖖 Mission 2 — Prove Independence

```python
# Add below Mission 1 — commission the Klingon fleet too

bird_of_prey = Starship("IKS Rotarran",  "IKC-9764", crew=36)
neghvar      = Starship("IKS Negh'Var",  "IKC-1108", crew=2500)
vorcha       = Starship("IKS Kronos One","IKC-7100",  crew=1800)

# Klingons don't dodge
bird_of_prey.take_damage(150)   # shields are gone — hull takes damage
neghvar.take_damage(40)
# vorcha hasn't been hit yet

print("\n--- Klingon Fleet Status ---")
print(bird_of_prey.status_report())
print(neghvar.status_report())
print(vorcha.status_report())    # vorcha should still be at 100% shields and hull
```

Six ships. One class definition. Each ship completely independent.

---

### 🖖 Mission 3 — Add Warp Drive and a Crew Report

Add these two methods **inside** the `Starship` class (indented to match the others):

```python
    def set_warp(self, factor):
        """Set warp speed. Warp 10 is impossible — Voyager learned that the hard way."""
        if factor >= 10:
            print(f"{self.name}: Warp 10 is theoretically impossible, Captain.")
        elif self.hull < 30:
            print(f"{self.name}: Hull integrity too low for warp, Captain.")
        else:
            print(f"{self.name}: Engaging warp {factor}. Make it so.")

    def crew_report(self):
        """Report crew status based on ship condition."""
        if self.hull <= 0:
            print(f"{self.name}: Ship destroyed. No survivors.")
        elif self.shields == 0:
            print(f"{self.name}: Shields down — crew of {self.crew} at risk.")
        else:
            print(f"{self.name}: All {self.crew} crew members accounted for.")
```

Test them:

```python
enterprise.set_warp(9)          # should work — hull is above 30%
bird_of_prey.set_warp(6)        # hull took damage — check if it is below 30%
enterprise.set_warp(10)         # should print the Warp 10 warning
enterprise.crew_report()
bird_of_prey.crew_report()
```

---

### 🖖 Mission 4 — Add `__repr__` and a Cloak System

Add `__repr__` and the cloak methods to the class:

```python
    def __repr__(self):
        cloak = " [CLOAKED]" if self.is_cloaked else ""
        return (f"Starship('{self.name}'{cloak}, "
                f"shields={self.shields}%, hull={self.hull}%)")

    def engage_cloak(self):
        if self.shields > 0:
            print(f"{self.name}: You cannot cloak while shields are up, Captain.")
        else:
            self.is_cloaked = True
            print(f"{self.name} has cloaked. They could be anywhere.")

    def disengage_cloak(self):
        self.is_cloaked = False
        print(f"{self.name} has decloaked.")
```

Test it:

```python
# Enterprise can't cloak — shields are still up
enterprise.engage_cloak()

# Defiant's shields were hit — try to cloak it
# (you may need to damage it more first — check its shield level)
defiant.take_damage(defiant.shields)   # drain remaining shields to 0
defiant.engage_cloak()

print(enterprise)    # Starship('USS Enterprise', shields=20%, hull=100%)
print(defiant)       # Starship('USS Defiant' [CLOAKED], shields=0%, hull=100%)
```

> **Notice:** You added two new methods and a `__repr__` without touching any code outside the class. Everything the ship knows about itself stays inside the class. That is **encapsulation** — one of the four pillars of OOP.

---

## 🔑 Key Takeaways

Cover the right column and answer each question from memory:

| Question | Answer |
|---|---|
| What is a **class**? | A blueprint — defines what data and behaviour instances will have |
| What is an **instance**? | One specific object created from a class |
| What does `__init__` do? | Runs automatically when an instance is created; sets up its attributes |
| What is `self`? | A reference to the specific instance currently being worked with |
| Why does `self` appear in definitions but not calls? | Python passes the instance as `self` automatically |
| What does `__repr__` control? | What `print(instance)` displays |
| Can two instances share attribute data accidentally? | No — each instance owns its own completely separate copy |

---

## 🚫 Common Mistakes — Red Alert

**Mistake 1 — Forgetting `self.` when storing an attribute:**

```python
# WRONG — name disappears when __init__ ends
def __init__(self, name):
    name = name      # this is a local variable, not an attribute

# CORRECT — self.name is stored on the instance permanently
def __init__(self, name):
    self.name = name
```

---

**Mistake 2 — Forgetting `self` in the method definition:**

```python
# WRONG — Python raises: "takes 0 positional arguments but 1 was given"
def take_damage(amount):
    self.shields -= amount

# CORRECT — self is always first, no exceptions
def take_damage(self, amount):
    self.shields -= amount
```

---

**Mistake 3 — Arguments in the wrong order:**

```python
class Starship:
    def __init__(self, name, registry, crew):
        ...

# WRONG — name gets 1012, registry gets "USS Enterprise", crew gets "NCC-1701-D"
wrong = Starship(1012, "USS Enterprise", "NCC-1701-D")

# CORRECT — match the order in __init__
right = Starship("USS Enterprise", "NCC-1701-D", 1012)

# ALSO CORRECT — keyword arguments; order does not matter
also_right = Starship(crew=1012, name="USS Enterprise", registry="NCC-1701-D")
```

---

**Mistake 4 — Calling `__init__` manually:**

```python
# WRONG — never call __init__ yourself
ship = Starship()
ship.__init__("USS Enterprise", "NCC-1701-D", 1012)

# CORRECT — Python calls __init__ automatically
ship = Starship("USS Enterprise", "NCC-1701-D", 1012)
```

---

**Mistake 5 — Running logic in `__init__` that belongs in a method:**

```python
# WRONG — __init__ should only SET UP the instance
def __init__(self, name, registry, crew):
    self.name = name
    ...
    self.take_damage(10)    # do not call methods inside __init__

# CORRECT — set up first, then use the instance
ship = Starship("USS Enterprise", "NCC-1701-D", 1012)
ship.take_damage(10)        # call methods after creating the instance
```

---

## 📚 Further Study — The Holodeck Library

| Resource | What it covers | Link |
|---|---|---|
| **Corey Schafer — Full OOP Series** | 6 videos: classes, inheritance, dunder methods, properties — the best OOP playlist on YouTube | [YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) |
| **Tech With Tim — OOP in Python** | Classes, inheritance, and a mini project | [YouTube](https://www.youtube.com/watch?v=jQiUOV15IRI) |
| **Real Python — OOP Guide** | Long written tutorial with many examples | [realpython.com](https://realpython.com/python3-object-oriented-programming/) |
| **Python Docs — Classes** | The official reference — worth reading once you have the basics | [docs.python.org](https://docs.python.org/3/tutorial/classes.html) |

---

## ✅ Ready to Move On?

Before opening your first unit assignment, tick all of these:

- [ ] I watched both videos and wrote down answers to the guided questions
- [ ] I typed out and ran all four missions in VS Code (no copy-pasting)
- [ ] I can explain `self` out loud without looking at any notes
- [ ] I can explain the difference between a class and an instance without looking at any notes
- [ ] `lesson_practice.py` runs without errors and produces sensible output

If every box is ticked → **you are ready for Unit 1.**

---

## 🤔 Still Confused? — Don't Panic

If something is not clicking, work through this list before asking for help:

1. **Re-watch** the Corey Schafer video at 0.75× speed — pause after every code block and type it yourself in VS Code before continuing
2. **Delete your code** and type it again from scratch — re-reading is not the same as re-doing
3. **Change the values** — give your Starship a different name or starting shields; see what changes and what stays the same
4. **Break it on purpose** — remove `self.` from one attribute in `__init__` and read the error message carefully; it tells you exactly what went wrong
5. **Try a third explanation** — search YouTube for `"python class self explained beginner"` — hearing the same concept a third different way often makes it click

---

*Lesson — Classes and Objects · Grade 11 Python*  
*Starfleet Academy — Programming Division*  
*"To boldly code what no one has coded before."* 🖖
