
# Strings
[![Watch the video](https://img.youtube.com/vi/Yveo5hCrGLE/maxresdefault.jpg)](https://youtu.be/Yveo5hCrGLE)

### [Watch this video on YouTube](https://youtu.be/Yveo5hCrGLE)


# Numbers
[![Watch the video](https://img.youtube.com/vi/5ZOxqAGWy70/maxresdefault.jpg)](https://youtu.be/5ZOxqAGWy70)

### [Watch this video on YouTube](https://youtu.be/5ZOxqAGWy70)


# 10 Most Common String Functions in Python

---

## 1. `len()`
Returns the number of characters in a string.
```python
len("hello")  # 5
```

---

## 2. `.lower()` / `.upper()`
Converts a string to all lowercase or uppercase.
```python
"Hello".lower()  # "hello"
"Hello".upper()  # "HELLO"
```

---

## 3. `.strip()`
Removes leading and trailing whitespace.
```python
"  hello  ".strip()  # "hello"
```

---

## 4. `.replace()`
Replaces one substring with another.
```python
"I like cats".replace("cats", "dogs")  # "I like dogs"
```

---

## 5. `.split()`
Splits a string into a list based on a delimiter.
```python
"a,b,c".split(",")  # ["a", "b", "c"]
```

---

## 6. `.join()`
Joins a list of strings into one string.
```python
",".join(["a", "b", "c"])  # "a,b,c"
```

---

## 7. `.find()`
Returns the index of the first occurrence of a substring, or `-1` if not found.
```python
"hello".find("l")  # 2
```

---

## 8. `.count()`
Counts how many times a substring appears.
```python
"banana".count("a")  # 3
```

---

## 9. `.startswith()` / `.endswith()`
Checks if a string starts or ends with a given substring.
```python
"hello".startswith("he")  # True
"hello".endswith("lo")    # True
```

---

## 10. f-strings (Formatted Strings)
Embeds variables directly into strings.
```python
name = "Alice"
f"Hello, {name}!"  # "Hello, Alice!"
```

---

These functions cover the vast majority of everyday string manipulation tasks you'll encounter as a beginner. Getting comfortable with these will make working with text in Python feel effortless.

# F-Strings
This is a relatively new way of working with strings

The old way to use a variable in a print statement.  Still 100% valid and will work
```python
name = "Bob"

print ("Hello, my name is " + name + " !!")
```

But now there are f-strings.  The print statement can be written as the following.

```python
print(f"Hello, my name is {name}!!)
```
Does seem like it saves much time, but as more and more is in your print statement, the value of f-strings will evolve.

[![Watch the video](https://img.youtube.com/vi/H_TPIAEJl68/maxresdefault.jpg)](https://youtu.be/H_TPIAEJl68)

### [Watch this video on YouTube](https://youtu.be/H_TPIAEJl68)
