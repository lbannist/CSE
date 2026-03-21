
Welcome to your introduction into the Python programming language.

# Print ()
[![Watch the video](https://img.youtube.com/vi/IdXTxbBfDbc/maxresdefault.jpg)](https://youtu.be/IdXTxbBfDbc)

### [Watch this video on YouTube](https://youtu.be/IdXTxbBfDbc)

## Challenge
Every time someone starts their journey into a new coding language, it is customary to have their first program say "Hello World!!"

using what you ahve learned from this video, create a quick program that when run, the program outputs the simple statements, "Hello World!!"

If you cannot get this to happen, check that you are in VS Code and are pressing the play button.  If so, but it still does not run, call over your teacher to ask for help.


# Comments
[![Watch the video](https://img.youtube.com/vi/GEOnKhm940k/maxresdefault.jpg)](https://youtu.be/GEOnKhm940k)

### [Watch this video on YouTube](https://youtu.be/GEOnKhm940k)


## Challenge
Using your previous .py, add a comment above the code explaining what the code does.   Add in two inline comments

Once you have finished this step.  Show your teacher.

# Variables
[![Watch the video](https://img.youtube.com/vi/YHgkADDCWJg/maxresdefault.jpg)](https://youtu.be/YHgkADDCWJg)

### [Watch this video on YouTube](https://youtu.be/YHgkADDCWJg)




# User Input ()
[![Watch the video](https://img.youtube.com/vi/we54H-T1AL0/maxresdefault.jpg)](https://youtu.be/we54H-T1AL0)

### [Watch this video on YouTube](https://youtu.be/we54H-T1AL0)

## Challenge
Now that your program has some life, lets modify the hello statement to be a little more personal.  Have the program ask what your name is and after entering your name, the message will say "Hello [your name]"

```python
name = input ("What is your name? ")
```


# Python Data Types

[![Watch the video](https://i.ytimg.com/vi/0uY2qNAsAWs/sddefault.jpg)](https://youtu.be/0uY2qNAsAWs)

### [Watch this video on YouTube](https://youtu.be/0uY2qNAsAWs)

# Python Fundamentals — Coding Challenge

**Topics Covered:** `print`, `input`, variables, data types, string concatenation  
**Instructions:** Complete the challenge below. Write your code in the space provided. Test your program with multiple inputs to make sure everything works correctly.

---

## Challenge: The Personal Info Card

### 📋 Your Task
Write a program that asks the user a series of questions and then prints a neatly formatted personal info card using their answers.

### ✅ Requirements

| Step | What to Do |
|---|---|
| 1 | Ask the user for their **name** and store it in a variable |
| 2 | Ask the user for their **age** and store it as an **integer** |
| 3 | Ask the user for their **favourite colour** and store it in a variable |
| 4 | Ask the user for their **favourite hobby** and store it in a variable |
| 5 | Print a formatted info card using string concatenation |
| **Bonus** | Add one more question of your choice and include it in the card |

### 🖥️ Expected Output
Your program should produce output that looks like this:

```
===========================
        My Info Card
===========================
Name:    Alex
Age:     17
Colour:  Blue
Hobby:   Soccer
===========================
```

### 💡 Hints
- Use `input()` to ask the user a question and store their answer in a variable
- Use `int(input())` when collecting age so it is stored as a number, not text
- Use string concatenation to insert variables into your printed lines (e.g. `print("Name:    " + name)`)
- When printing age, you will need to convert it back to a string using `str()` (e.g. `print("Age:     " + str(age))`)
- The `=` border lines are just regular `print()` statements with repeated characters

### 🖊️ Your Code

```python
# Challenge: The Personal Info Card
# Your Name:
# Date:

# Step 1: Ask the user for their name


# Step 2: Ask the user for their age (store as an integer)


# Step 3: Ask the user for their favourite colour


# Step 4: Ask the user for their favourite hobby


# Step 5: Print the formatted info card

```

### 🧪 Test Your Program
Run your program at least **3 times** using the inputs below and record what it printed:

| Test | Name | Age | Colour | Hobby | Did it print correctly? |
|---|---|---|---|---|---|
| 1 | Alex | 17 | Blue | Soccer | |
| 2 | Jordan | 14 | Green | Painting | |
| 3 | Your own info | | | | |

> **What did your program actually print for Test 1?**
>
> *(paste your output here)*

---

## 🏁 Reflection Questions

Answer the following questions in your own words:

1. What is the difference between a `str` and an `int`? Why did we need to convert the age?

> *Your answer:*

2. What does `input()` do? What does it return?

> *Your answer:*

3. What is string concatenation? How did you use it to print the info card?

> *Your answer:*

4. Why did you need to use `str()` when printing the age, even though you already stored it as a variable?

> *Your answer:*
