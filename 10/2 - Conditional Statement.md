
# Boolean Functions
[![Watch the video](https://img.youtube.com/vi/v8tuWg_rvjE/maxresdefault.jpg)](https://youtu.be/v8tuWg_rvjE)

### [Watch this video on YouTube](https://youtu.be/v8tuWg_rvjE)


# Comparitors
[![Watch the video](https://img.youtube.com/vi/OZ7AinsDYVo/maxresdefault.jpg)](https://youtu.be/OZ7AinsDYVo)

### [Watch this video on YouTube](https://youtu.be/OZ7AinsDYVo)


# Logicl Operators
[![Watch the video](https://img.youtube.com/vi/yFaYylK1yCE/maxresdefault.jpg)](https://youtu.be/yFaYylK1yCE)

### [Watch this video on YouTube](https://youtu.be/yFaYylK1yCE)


# If Statements
[![Watch the video](https://img.youtube.com/vi/7s-zyoaaBOY/maxresdefault.jpg)](https://youtu.be/7s-zyoaaBOY)

### [Watch this video on YouTube](https://youtu.be/7s-zyoaaBOY)


# Python Conditionals — Coding Challenges

**Topics Covered:** `if`, `elif`, `else`, booleans, comparators, logic operators  
**Instructions:** Complete both challenges below. Write your code in the spaces provided. Test your program with multiple inputs to make sure all conditions work correctly.

---

## Challenge A: The Weather Advisor

### 📋 Your Task
Write a program that asks the user for the current temperature and whether it is raining. Based on their input, print outfit advice and a reminder about an umbrella if needed.

### ✅ Requirements

| Condition | Output |
|---|---|
| Temperature below 0 | `"Wear a heavy winter coat."` |
| Temperature 0–10 | `"Wear a jacket."` |
| Temperature 11–20 | `"A sweater should do."` |
| Temperature above 20 | `"T-shirt weather!"` |
| If raining (any temp) | Also print `"Don't forget your umbrella!"` |

### 💡 Hints
- Use `int(input())` to get the temperature as a number
- Use `and` to check ranges (e.g. `temp >= 0 and temp <= 10`)
- Ask the user if it is raining and check if their answer equals `"yes"`

### 🖊️ Your Code

```python
# Challenge 1: The Weather Advisor
# Your Name:
# Date:

# Step 1: Ask the user for the temperature


# Step 2: Ask the user if it is raining (yes or no)


# Step 3: Print outfit advice using if / elif / else


# Step 4 (Bonus): Check if it is raining and print umbrella reminder

```

### 🧪 Test Your Program
Run your program at least **3 times** using the inputs below and record what it printed:

| Test | Temperature | Raining? | Expected Output |
|---|---|---|---|
| 1 | -5 | no | Wear a heavy winter coat. |
| 2 | 15 | yes | A sweater should do. + umbrella reminder |
| 3 | 25 | no | T-shirt weather! |

> **What did your program actually print for each test?**
>
> Test 1:
>
> Test 2:
>
> Test 3:

---

## Challenge B: The Login Checker

### 📋 Your Task
Write a program that stores a correct username and password, asks the user to enter both, and prints a message depending on whether they got them right.

### ✅ Requirements

| Condition | Output |
|---|---|
| Both username and password are correct | `"Access granted. Welcome!"` |
| Username correct, password wrong | `"Wrong password."` |
| Username is wrong | `"Username not found."` |
| **Bonus:** | Store `True` or `False` in a variable called `is_logged_in` and print it |

### 💡 Hints
- Set your username and password as variables at the top of your code (e.g. `correct_username = "student"`)
- Use `==` to compare what the user typed to the correct values
- Use nested `if` statements or `and` to check both conditions
- A boolean stores either `True` or `False` — no quotes!

### 🖊️ Your Code

```python
# Challenge 2: The Login Checker
# Your Name:
# Date:

# Step 1: Set the correct username and password
correct_username = "student"
correct_password = "python123"

# Step 2: Ask the user to enter a username and password


# Step 3: Use if / elif / else to check the login


# Step 4 (Bonus): Create an is_logged_in boolean and print it

```

### 🧪 Test Your Program
Run your program at least **3 times** using the inputs below and record what it printed:

| Test | Username | Password | Expected Output |
|---|---|---|---|
| 1 | student | python123 | Access granted. Welcome! |
| 2 | student | wrongpass | Wrong password. |
| 3 | wronguser | python123 | Username not found. |

> **What did your program actually print for each test?**
>
> Test 1:
>
> Test 2:
>
> Test 3:

---

## 🏁 Reflection Questions

Answer the following questions in your own words:

1. What is the difference between `if`, `elif`, and `else`?

> *Your answer:*

2. What does a boolean store? Give an example from one of your programs.

> *Your answer:*

3. What comparator did you use the most? What does it do?

> *Your answer:*

4. What part was the trickiest and how did you figure it out?

> *Your answer:*
