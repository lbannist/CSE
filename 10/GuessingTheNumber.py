''' 
Day 1 - Introduction to Python and VSCode
print(), variables and output variables
Create "Hello World"

Day 2 - Input & Output
=input(
int()
commas
'''
age = 30
print("I am", age, "years old.")
# Output: I am 30 years old.
'''
str() vs. f-strings

'''
age = 30
message = "I am " + str(age) + " years old."
print(message)
# Output: I am 30 years old.

age = 30
message = f"I am {age} years old."
print(message)
# Output: I am 30 years old.


'''
Day 3 - Conditional Statements
if 
elif ("else if" in other programming languages)
else

'''


'''
Challenge - Create a guessing game
'''
# Number Guessing Game
# Concepts used: variables, if statements, input, output

print("================================")
print("   Welcome to the Guessing Game!")
print("================================")
print("I am thinking of a number between 1 and 10.")
print()

secret_number = 7

name = input("What is your name? ")
print("Hello, " + name + "! Let's play!")
print()

guess = input("What is your guess? ")
guess = int(guess)

print()

if guess == secret_number:
    print("🎉 Amazing! You got it, " + name + "!")
    print("The secret number was " + str(secret_number) + ".")

if guess < secret_number:
    print("Too low! Try a bigger number next time.")
    print("The secret number was " + str(secret_number) + ".")

if guess > secret_number:
    print("Too high! Try a smaller number next time.")
    print("The secret number was " + str(secret_number) + ".")

print()
print("Thanks for playing!")
