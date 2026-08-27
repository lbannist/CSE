# 📖 Lesson — Classes and Objects in Python

> **Course:** Grade 11 · Python  
> **Before this lesson:** You should be comfortable with functions, loops, and if/else from Grade 10.  
> **After this lesson:** You will apply what you learned here in your first unit assignment.

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

Watch these two videos **before** reading the notes below. Pause frequently and try the code in VS Code as you go — do not just watch passively.

---

### Video 1 — Python OOP Tutorial: Classes and Instances *(~26 min)*

**Corey Schafer** is one of the clearest Python educators on YouTube. This video starts from zero and covers exactly what you need.

[![Watch the video](https://img.youtube.com/vi/ZDa-Z5JzLYM/maxresdefault.jpg)](https://youtu.be/ZDa-Z5JzLYM)

**Write down answers to these while you watch:**
- What is the difference between a class and an instance?
- What does `__init__` do, and when does it run?
- What is `self`, and why is it always the first parameter in every method?

---

### Video 2 — Python Classes for Beginners *(~15 min)*

**Tech With Tim** uses a different example and a slightly different explanation style. Hearing the same concept twice, explained differently, is one of the fastest ways to make it stick.

[![Watch the video](https://img.youtube.com/vi/jQiUOV15IRI/maxresdefault.jpg)](https://youtu.be/jQiUOV15IRI)

**Write down answers to these while you watch:**
- How do you create an instance from a class?
- How is `self.name` different from a regular variable called `name`?

---

## 📝 Lesson Notes

### The Problem That Classes Solve

Imagine you are writing software to manage a bank. You need to track accounts — each one has an owner name, a balance, and an account number. In the style of programming you used in Grade 10, you might start like this:

```python
# Procedural approach — separate variables for every account
account1_owner   = "Alice"
account1_balance = 500.00
account1_number  = "ACC-001"

account2_owner   = "Bob"
account2_balance = 1200.00
account2_number  = "ACC-002"

# To deposit into Alice's account:
account1_balance += 200

# To check Bob's balance:
print(f"{account2_owner}: ${account2_balance}")
```

This works for two accounts. What about two thousand? What if each account also needs a transaction history, an interest rate, and an overdraft limit? The number of variables explodes. There is no clean way to say *"do this to account 3"* without writing it all out manually.

**Classes** solve this by bundling related data and behaviour together into one reusable blueprint:

```python
# With a class — create as many accounts as you need from one blueprint
alice = BankAccount("Alice", 500.00, "ACC-001")
bob   = BankAccount("Bob",  1200.00, "ACC-002")

alice.deposit(200)
print(bob.balance_summary())
```

The rest of this lesson teaches you how to write that `BankAccount` class from scratch.

---

### Anatomy of a Class

Every class follows the same structure. Read every comment — they are part of the lesson.

```python
# ── The class keyword names the blueprint ──────────────────────────────────
# Class names use CapitalLetters (called PascalCase — it is a convention)

class BankAccount:

    # ── __init__ is the CONSTRUCTOR ────────────────────────────────────────
    # Python calls this automatically the instant you create an instance.
    # self = the specific instance being set up right now.
    # Every parameter after self becomes data you pass in at creation time.

    def __init__(self, owner, balance, account_number):

        # ── Attributes — data stored ON this instance ──────────────────────
        # self.owner means "THIS account's owner" — not a shared global variable.
        # Every instance gets its own separate copy of these.

        self.owner          = owner
        self.balance        = balance
        self.account_number = account_number
        self.transactions   = []    # start with an empty history
                                    # (you can add attributes beyond the parameters)

    # ── Methods — functions that belong to this class ──────────────────────
    # Every method takes self as its FIRST parameter.
    # self lets the method access and change THIS instance's attributes.

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"+${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"-${amount:.2f}")

    def balance_summary(self):
        return f"{self.owner} ({self.account_number}): ${self.balance:.2f}"
```

---

### Creating Instances

The class is the blueprint. An **instance** is one specific object stamped out from that blueprint.

```python
# Create two completely separate BankAccount instances
alice = BankAccount("Alice", 500.00, "ACC-001")
bob   = BankAccount("Bob",  1200.00, "ACC-002")

# Each instance has its OWN data — they do not share anything
alice.deposit(200)       # alice's balance goes to 700
bob.withdraw(50)         # bob's balance goes to 1150

print(alice.balance_summary())  # Alice (ACC-001): $700.00
print(bob.balance_summary())    # Bob   (ACC-002): $1150.00

# Proof they are independent — alice's deposit did NOT change bob
print(alice.balance)    # 700.00
print(bob.balance)      # 1150.00   ← completely unchanged by alice's deposit
```

> **This is the most important thing to understand about instances:** `alice` and `bob` are both `BankAccount` objects, but they each own a completely separate copy of `owner`, `balance`, `account_number`, and `transactions`. Changing one never affects the other.

---

### What Is `self`?

`self` confuses almost everyone the first time. Here is the clearest way to think about it:

> **`self` is the instance talking about itself.**

When you call `alice.deposit(200)`, Python secretly rewrites it like this:

```python
# What you write:
alice.deposit(200)

# What Python actually does:
BankAccount.deposit(alice, 200)
#                   ^^^^^
#                   self = alice  — Python passes this automatically
```

Python passes the instance as `self` automatically. You never type `self` when **calling** a method — only when **defining** one.

```python
# Calling — do NOT write self
alice.deposit(200)
bob.withdraw(50)

# Defining — ALWAYS write self first
def deposit(self, amount):
    self.balance += amount
```

Without `self`, a method has no way to know *which* account to deposit into. It could be `alice`, `bob`, or any account you ever create. `self` is the answer to the question: *"which one are we talking about right now?"*

---

### The `__init__` Method in Detail

`__init__` is called the **constructor**. Python calls it automatically the instant you create an instance:

```python
alice = BankAccount("Alice", 500.00, "ACC-001")
#      ↑ Python calls BankAccount.__init__(alice, "Alice", 500.00, "ACC-001") here
#        You never call __init__ yourself — Python does it for you
```

Whatever you assign with `self.` inside `__init__` becomes a permanent attribute of that instance — data it carries with it for its entire lifetime.

```python
def __init__(self, owner, balance, account_number):
    self.owner          = owner           # stored permanently on the instance
    self.balance        = balance
    self.account_number = account_number
    self.transactions   = []              # you can add extra attributes too —
    self.is_frozen      = False           # they do not have to come from parameters
```

---

### `__repr__` — Making `print()` Useful

By default, `print(alice)` shows something unhelpful like `<__main__.BankAccount object at 0x10f3a2c10>`. Fix this by defining `__repr__`:

```python
class BankAccount:
    # ... all existing code ...

    def __repr__(self):
        return f"BankAccount('{self.owner}', ${self.balance:.2f})"

print(alice)    # BankAccount('Alice', $700.00)  ← much more useful
print(bob)      # BankAccount('Bob', $1150.00)
```

`__repr__` is one of Python's **dunder methods** (double underscore on both sides). You will meet more of them as the year goes on. For now, just know that defining it controls what `print()` shows for your objects.

---

### Classes vs Functions — When to Use Each

| Use a **function** when... | Use a **class** when... |
|---|---|
| You have one specific task to do | You need data AND behaviour bundled together |
| No memory needed between calls | The thing needs to remember its state over time |
| You produce one result and you're done | You need multiple independent copies of the same thing |
| `total = calculate_tax(income, rate)` | `account = BankAccount("Alice", 500)` |

A useful rule of thumb: if you find yourself creating multiple variables that all belong to the same *thing* (account1_owner, account1_balance, account1_number), that is a signal the thing should be a class.

---

## 🧪 Try It Yourself — Four Practice Blocks

Open VS Code and create a new file called `lesson_practice.py`. Work through each block in order. **Type the code — do not copy and paste.**

---

### Block 1 — Write the class and create instances

```python
# lesson_practice.py — Block 1

class BankAccount:
    def __init__(self, owner, balance, account_number):
        self.owner          = owner
        self.balance        = balance
        self.account_number = account_number
        self.transactions   = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"+${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Declined: {self.owner} has insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"-${amount:.2f}")

    def balance_summary(self):
        return f"{self.owner} ({self.account_number}): ${self.balance:.2f}"


# Create two accounts and test them
alice = BankAccount("Alice", 500.00, "ACC-001")
bob   = BankAccount("Bob",  1200.00, "ACC-002")

alice.deposit(200)
bob.withdraw(300)

print(alice.balance_summary())
print(bob.balance_summary())
```

Run it. Confirm the output looks right. Then answer:

> After `alice.deposit(200)`, what is `bob.balance`? Why has it not changed?

*(write your answer as a comment in the file)*

---

### Block 2 — Prove instances are independent

```python
# Add below Block 1 — still in lesson_practice.py

# Create three more accounts — notice you are reusing the class each time
carol = BankAccount("Carol",    0.00, "ACC-003")
dave  = BankAccount("Dave",  9999.00, "ACC-004")
eve   = BankAccount("Eve",    100.00, "ACC-005")

# Do different things to each one
carol.deposit(50)
dave.withdraw(10000)    # should fail — insufficient funds
eve.deposit(25)
eve.withdraw(10)

print(carol.balance_summary())   # Carol (ACC-003): $50.00
print(dave.balance_summary())    # Dave  (ACC-004): $9999.00  (unchanged — declined)
print(eve.balance_summary())     # Eve   (ACC-005): $115.00
```

You created five completely separate accounts from one class definition. That is the power of instances.

---

### Block 3 — Add a transaction history method

```python
# Add this method INSIDE the BankAccount class (indented to match the others)

def print_history(self):
    print(f"\n--- {self.owner}'s transaction history ---")
    if not self.transactions:
        print("  No transactions yet.")
    else:
        for t in self.transactions:
            print(f"  {t}")
    print(f"  Current balance: ${self.balance:.2f}")
```

```python
# Test it — add below your Block 2 code
alice.print_history()
eve.print_history()
carol.print_history()   # should show only one deposit
```

---

### Block 4 — Add `__repr__` and a freeze feature

```python
# Add __repr__ to the class

def __repr__(self):
    status = "FROZEN" if self.is_frozen else "active"
    return f"BankAccount('{self.owner}', ${self.balance:.2f}, {status})"
```

```python
# Add is_frozen to __init__ (inside __init__, with the other attributes)
self.is_frozen = False
```

```python
# Add a freeze method to the class

def freeze(self):
    self.is_frozen = True
    print(f"{self.owner}'s account has been frozen.")

def deposit(self, amount):       # UPDATE the existing deposit method
    if self.is_frozen:
        print(f"Deposit declined: {self.owner}'s account is frozen.")
        return
    if amount > 0:
        self.balance += amount
        self.transactions.append(f"+${amount:.2f}")
```

```python
# Test it
carol.freeze()
carol.deposit(100)      # should be declined
print(carol)            # BankAccount('Carol', $50.00, FROZEN)
print(alice)            # BankAccount('Alice', $700.00, active)
```

> **Reflect:** You added the `freeze` feature without changing any of the other methods or any code outside the class. This is **encapsulation** — the account manages its own rules internally.

---

## 🔑 Key Takeaways

Test yourself — cover the right column and answer from memory:

| Question | Answer |
|---|---|
| What is a **class**? | A blueprint that defines what data and behaviour objects will have |
| What is an **instance**? | One specific object created from a class |
| What does `__init__` do? | Runs automatically when an instance is created; sets up attributes |
| What is `self`? | A reference to the specific instance currently being worked with |
| Why does `self` appear in definitions but not calls? | Python passes the instance as `self` automatically |
| What does `__repr__` control? | What `print(instance)` displays |
| Can two instances accidentally share attribute data? | No — each owns its own separate copy |

---

## 🚫 Common Mistakes

**Mistake 1 — Forgetting `self.` when storing an attribute:**

```python
# WRONG — balance is a local variable; it disappears when __init__ ends
def __init__(self, owner, balance):
    owner   = owner       # this is a local variable — NOT stored on the instance
    balance = balance

# CORRECT — self.balance is stored ON the instance permanently
def __init__(self, owner, balance):
    self.owner   = owner
    self.balance = balance
```

---

**Mistake 2 — Forgetting `self` in the method signature:**

```python
# WRONG — Python will raise: "takes 0 positional arguments but 1 was given"
def deposit(amount):
    self.balance += amount

# CORRECT — self is always first, always there
def deposit(self, amount):
    self.balance += amount
```

---

**Mistake 3 — Passing arguments in the wrong order:**

```python
class BankAccount:
    def __init__(self, owner, balance):
        ...

# WRONG — owner gets 500, balance gets "Alice"
wrong = BankAccount(500, "Alice")

# CORRECT — match the parameter order
right = BankAccount("Alice", 500)

# ALSO CORRECT — keyword arguments; order does not matter
also_right = BankAccount(balance=500, owner="Alice")
```

---

**Mistake 4 — Calling `__init__` manually:**

```python
# WRONG — you never call __init__ yourself
alice = BankAccount()
alice.__init__("Alice", 500)   # do not do this

# CORRECT — Python calls __init__ automatically when you create the instance
alice = BankAccount("Alice", 500)
```

---

**Mistake 5 — Putting logic in `__init__` that belongs in a method:**

```python
# WRONG — __init__ should only SET UP the instance
def __init__(self, owner, balance):
    self.owner   = owner
    self.balance = balance
    self.deposit(100)    # do not call methods inside __init__

# CORRECT — set up first, then call methods separately
account = BankAccount("Alice", 500)
account.deposit(100)
```

---

## 📚 Want to Go Deeper?

| Resource | What it covers | Link |
|---|---|---|
| Corey Schafer — Full OOP Series | 6 videos: classes, inheritance, dunder methods, properties | [YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) |
| Tech With Tim — OOP in Python | Classes, inheritance, and a mini project | [YouTube](https://www.youtube.com/watch?v=jQiUOV15IRI) |
| Real Python — OOP Guide | Long written tutorial with many examples | [realpython.com](https://realpython.com/python3-object-oriented-programming/) |
| Python Docs — Classes | The official reference | [docs.python.org](https://docs.python.org/3/tutorial/classes.html) |

---

## ✅ Ready to Move On?

Before opening your unit assignment, tick all of these:

- [ ] I watched both videos and wrote down answers to the questions
- [ ] I typed out and ran all four practice blocks in VS Code
- [ ] I can explain `self` without looking at my notes
- [ ] I can explain the difference between a class and an instance without looking at my notes
- [ ] `lesson_practice.py` runs without any errors and the output looks correct

---

## 🤔 Still Confused?

If something is not clicking, try these steps before asking for help:

1. **Re-watch** the Corey Schafer video at 0.75× speed — pause after every code block and type it yourself
2. **Delete your code** and retype it from scratch — re-reading is not the same as re-doing
3. **Change the values** — give your BankAccount a different owner or balance; notice what changes and what stays the same
4. **Break it on purpose** — remove `self.` from one attribute and read the error message; it will tell you what went wrong
5. **Search YouTube** for `"python class self explained beginner"` — hearing the concept explained a third way often makes it click

---

*Lesson — Classes and Objects · Grade 11 Python*
