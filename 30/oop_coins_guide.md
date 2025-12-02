# Python OOP Coin Collector Assignment Guide

## 🎯 Introduction

Welcome to the Coin Collector project! In this assignment, you'll build an **inventory management system** for cataloguing coins. This project takes your understanding of functions and methods to the next level by showing you how to organize related functions into **classes**.

### Why Use Classes and Methods?

As programs grow, we need better ways to organize our code. Imagine you're creating a video game with multiple characters. Each character needs to track their own health, inventory, and weapons. Without organization, your code becomes confusing:

```python
# Without classes - messy and confusing!
hero_health = 100
villain_health = 150
hero_inventory = []
villain_inventory = []

def update_health(character_name, amount):
    # Which health variable do we update?
```

With classes, everything stays organized:

```python
# With classes - clean and clear!
hero = Character("Hero")
villain = Character("Villain")

hero.update_health(-10)  # Crystal clear!
villain.update_health(-20)
```

**Think of it this way:**
- A **class** is like a blueprint for creating objects (like a blueprint for a house)
- An **object** is a specific instance created from that blueprint (like an actual house built from the blueprint)
- A **method** is an action that object can perform (like opening the house's door)

In this assignment, the `Coin` class is your blueprint, and each coin you create (penny, nickel, dime) is an object with its own unique properties!

---

## 📋 Assignment Overview

Create a coin collector inventory system that allows users to:
- View details about Canadian coins
- Add new coins to their collection
- Search for specific coins
- Calculate total collection value
- Get change combinations

**File name:** `[YourName]_OOP_Coins.py`

---

## 🏗️ Step-by-Step Implementation Guide

### **Phase 1: Build the Basic Coin Class**

#### Step 1.1: Create the Class Structure

```python
class Coin:
    """A class to represent a coin in a collection"""
    
    def __init__(self, name, radius, country):
        """
        Constructor - initializes a new coin object
        Parameters:
            name (str): The coin's name (e.g., "penny", "dime")
            radius (float): The coin's radius in millimeters
            country (str): Country of origin
        """
        self.name = name
        self.radius = radius
        self.country = country
```

**Understanding `self`:**
- `self` refers to the specific coin object you're working with
- When you create `penny = Coin("penny", 9.5, "Canada")`, `self.name` becomes `penny.name`

#### Step 1.2: Add Calculation Methods

```python
    def circumference(self):
        """
        METHOD - Calculates the circumference of the coin
        Formula: C = 2πr
        Returns: circumference in millimeters (float)
        """
        import math
        return 2 * math.pi * self.radius
    
    def area(self):
        """
        METHOD - Calculates the surface area of one side of the coin
        Formula: A = πr²
        Returns: area in square millimeters (float)
        """
        import math
        return math.pi * (self.radius ** 2)
    
    def get_country(self):
        """
        METHOD - Returns the country of origin
        Returns: country name (str)
        """
        return self.country
```

---

### **Phase 2: Create Initial Coin Collection**

#### Step 2.1: Research Canadian Coin Dimensions

Find the actual radii/diameters of Canadian coins. Here's example data:

| Coin | Diameter (mm) | Radius (mm) |
|------|---------------|-------------|
| Penny | 19.05 | 9.525 |
| Nickel | 21.2 | 10.6 |
| Dime | 18.03 | 9.015 |
| Quarter | 23.88 | 11.94 |

#### Step 2.2: Initialize Your Collection

```python
def initialize_coins():
    """
    FUNCTION - Creates the initial list of Canadian coins
    Returns: list of Coin objects
    """
    all_coins = []
    
    # Create coin objects and add to list
    penny = Coin("penny", 9.525, "Canada")
    nickel = Coin("nickel", 10.6, "Canada")
    dime = Coin("dime", 9.015, "Canada")
    quarter = Coin("quarter", 11.94, "Canada")
    
    all_coins.append(penny)
    all_coins.append(nickel)
    all_coins.append(dime)
    all_coins.append(quarter)
    
    return all_coins
```

---

### **Phase 3: Build the Menu System**

```python
def main():
    """Main program with menu loop"""
    all_coins = initialize_coins()
    
    while True:
        print("\n=== COIN COLLECTOR MENU ===")
        print("1. View coin details")
        print("2. Add new coin")
        print("3. Calculate total value")
        print("4. Search for a coin")
        print("5. Make change")
        print("Type 'exit' to quit")
        
        choice = input("\nEnter your choice: ").lower()
        
        if choice == 'exit':
            print("Thank you for using Coin Collector!")
            break
        
        # Handle menu choices
        if choice == '1':
            view_coin_details(all_coins)
        elif choice == '2':
            add_new_coin(all_coins)
        # Add other menu options...
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

---

### **Phase 4: Expand the Coin Class**

#### Step 4.1: Update Constructor with Material and Value

```python
class Coin:
    """Enhanced coin class with material and value"""
    
    def __init__(self, name, radius, country, material, value):
        """
        Constructor - initializes a new coin object
        Parameters:
            name (str): The coin's name
            radius (float): The coin's radius in millimeters
            country (str): Country of origin
            material (str): What the coin is made of (e.g., "copper", "nickel")
            value (int): The coin's value in cents
        """
        self.name = name
        self.radius = radius
        self.country = country
        self.material = material
        self.value = value
```

#### Step 4.2: Update Your Initial Coins

```python
def initialize_coins():
    """Creates initial list with material and value"""
    all_coins = []
    
    penny = Coin("penny", 9.525, "Canada", "copper-plated steel", 1)
    nickel = Coin("nickel", 10.6, "Canada", "nickel-plated steel", 5)
    dime = Coin("dime", 9.015, "Canada", "nickel-plated steel", 10)
    quarter = Coin("quarter", 11.94, "Canada", "nickel-plated steel", 25)
    
    all_coins.extend([penny, nickel, dime, quarter])
    return all_coins
```

---

### **Phase 5: Implement Required Features**

#### Feature 1: View Coin Details

```python
def view_coin_details(coin_list):
    """
    FUNCTION - Displays detailed information about a selected coin
    Parameter: coin_list (list of Coin objects)
    """
    print("\nAvailable coins:")
    for i, coin in enumerate(coin_list, 1):
        print(f"{i}. {coin.name.capitalize()}")
    
    choice = input("\nSelect a coin number: ")
    
    # Validate and display
    try:
        index = int(choice) - 1
        selected_coin = coin_list[index]
        
        print(f"\n--- {selected_coin.name.upper()} Details ---")
        print(f"The surface area of one side of a {selected_coin.name} is {selected_coin.area():.2f} square millimeters")
        print(f"A {selected_coin.name}'s circumference is {selected_coin.circumference():.2f} millimeters")
        print(f"The {selected_coin.name} is made of {selected_coin.material}")
        print(f"It has a value of {selected_coin.value} cents")
        
    except (ValueError, IndexError):
        print("Invalid selection!")
```

#### Feature 2: Add New Coin

```python
def add_new_coin(coin_list):
    """
    FUNCTION - Allows user to add a new coin to the collection
    Parameter: coin_list (list of Coin objects)
    """
    print("\n--- Add New Coin ---")
    
    name = input("Enter coin name: ").lower()
    radius = float(input("Enter radius in mm: "))
    country = input("Enter country: ")
    material = input("Enter material: ")
    value = int(input("Enter value in cents: "))
    
    new_coin = Coin(name, radius, country, material, value)
    coin_list.append(new_coin)
    
    print(f"\n{name.capitalize()} added successfully!")
```

#### Feature 3: Calculate Total Value

```python
def calculate_total_value(coin_list):
    """
    FUNCTION - Calculates the total value of all coins in collection
    Parameter: coin_list (list of Coin objects)
    Returns: total value in cents (int)
    """
    total = 0
    for coin in coin_list:
        total += coin.value
    return total

# In your main menu:
# total = calculate_total_value(all_coins)
# print(f"Total collection value: {total} cents (${total/100:.2f})")
```

#### Feature 4: Linear Search for Coin

```python
def search_coin(coin_list):
    """
    FUNCTION - Searches for a coin by name using linear search
    Parameter: coin_list (list of Coin objects)
    """
    search_name = input("\nEnter coin name to search: ").lower()
    
    # Linear search
    found = False
    for coin in coin_list:
        if coin.name.lower() == search_name:
            print(f"\n--- {coin.name.upper()} Found! ---")
            print(f"Name: {coin.name}")
            print(f"Radius: {coin.radius} mm")
            print(f"Country: {coin.country}")
            print(f"Material: {coin.material}")
            print(f"Value: {coin.value} cents")
            print(f"Circumference: {coin.circumference():.2f} mm")
            print(f"Area: {coin.area():.2f} sq mm")
            found = True
            break
    
    if not found:
        print(f"\nCoin '{search_name}' not found in collection.")
```

#### Feature 5: Make Change

```python
def make_change(coin_list):
    """
    FUNCTION - Calculates minimum coins needed for an amount
    Parameter: coin_list (list of Coin objects)
    """
    amount = int(input("\nEnter amount in cents: "))
    
    # Sort coins by value (highest first) for greedy algorithm
    sorted_coins = sorted(coin_list, key=lambda c: c.value, reverse=True)
    
    remaining = amount
    change = []
    
    for coin in sorted_coins:
        if remaining >= coin.value:
            count = remaining // coin.value
            remaining = remaining % coin.value
            change.append((count, coin.name))
    
    if remaining > 0:
        print(f"Cannot make exact change for {amount} cents")
    else:
        print(f"\nChange for {amount} cents:")
        for count, name in change:
            print(f"{count} {name}(s)")
```

---

## ✅ Requirements Checklist

### Phase 1: Basic Class
- [ ] `Coin` class created with `__init__` constructor
- [ ] Instance variables: `name`, `radius`, `country`
- [ ] `circumference()` method implemented
- [ ] `area()` method implemented
- [ ] `get_country()` method implemented

### Phase 2: Initial Collection
- [ ] Research actual Canadian coin dimensions
- [ ] Create list with 4 Canadian coins
- [ ] All coins stored as `Coin` objects

### Phase 3: Menu System
- [ ] Menu displays all options
- [ ] Loop continues until user exits
- [ ] Input validation handles invalid choices

### Phase 4: Expanded Class
- [ ] Added `material` instance variable
- [ ] Added `value` instance variable
- [ ] Constructor updated
- [ ] Print statements updated with new info

### Phase 5: Advanced Features
- [ ] View coin details from list
- [ ] Add new coins during runtime
- [ ] Calculate total collection value
- [ ] Linear search with "not found" handling
- [ ] Make change algorithm works correctly

### General Requirements
- [ ] File named: `[YourName]_OOP_Coins.py`
- [ ] All methods only calculate/return (no printing inside methods)
- [ ] Main program handles all print statements
- [ ] Proper comments explaining code
- [ ] Program fully integrated with menu

---

## 💡 Programming Tips

### Understanding Objects vs Variables

```python
# Regular variable
radius = 9.5

# Object with multiple properties
penny = Coin("penny", 9.5, "Canada", "copper", 1)

# Accessing object properties
print(penny.radius)  # 9.5
print(penny.circumference())  # Calls method
```

### The Constructor (`__init__`)

The constructor runs automatically when you create a new object:

```python
# This line triggers __init__
my_coin = Coin("loonie", 13.3, "Canada", "brass", 100)

# Now my_coin has all those properties!
print(my_coin.name)  # "loonie"
```

### Why Methods Don't Print

Methods calculate and return values so they're reusable:

```python
# GOOD - Method returns value
def area(self):
    return math.pi * (self.radius ** 2)

# In main:
area_value = penny.area()
print(f"Area is {area_value}")  # You control the message

# BAD - Method prints directly
def area(self):
    print(f"Area is {math.pi * (self.radius ** 2)}")  # Inflexible!
```

### Linear Search Explained

Linear search checks each item one by one:

```python
# Looking for "dime" in the list
for coin in coin_list:  # Check each coin
    if coin.name == "dime":  # Is this the one?
        print("Found it!")
        break
```

---

## 🧪 Testing Your Program

Test each feature thoroughly:

### Test 1: View Coin Details
- Select each coin in your collection
- Verify calculations are correct (use calculator to check)

### Test 2: Add New Coin
- Add a loonie (26.5mm diameter, brass, 100 cents)
- Add a toonie (28mm diameter, bi-metallic, 200 cents)
- Verify they appear in the collection

### Test 3: Calculate Total Value
- With 4 basic coins: 1 + 5 + 10 + 25 = 41 cents
- After adding loonie and toonie: 241 cents

### Test 4: Search
- Search for existing coin: "quarter"
- Search for non-existent coin: "bitcoin"
- Test with different capitalizations

### Test 5: Make Change
- 85 cents = 3 quarters + 1 dime
- 67 cents = 2 quarters + 1 dime + 1 nickel + 2 pennies
- 15 cents = 1 dime + 1 nickel

---

## 🎓 Key Learning Objectives

By completing this assignment, you'll master:

1. **Class Structure**: How to create blueprints for objects
2. **Constructors**: How objects are initialized
3. **Instance Variables**: Data that belongs to each object
4. **Methods**: Functions that belong to objects
5. **Object Creation**: Making multiple instances from one class
6. **List Management**: Storing and manipulating objects in lists
7. **Algorithms**: Linear search and greedy change-making
8. **Program Architecture**: Organizing code with classes and functions

---

## 🚀 Extension Challenges (Optional)

Want to go further? Try these:

1. **Sorting**: Add ability to sort coins by value, name, or size
2. **Statistics**: Calculate average coin size or most common material
3. **Save/Load**: Save collection to a file and load it next time
4. **Currency Conversion**: Add coins from other countries with exchange rates
5. **GUI**: Create a graphical interface using tkinter

---

## 📚 Common Mistakes to Avoid

❌ **Printing inside methods**
```python
def area(self):
    print(f"Area is {math.pi * self.radius ** 2}")  # NO!
```

✅ **Return from methods, print in main**
```python
def area(self):
    return math.pi * self.radius ** 2  # YES!

# In main:
print(f"Area is {penny.area()}")
```

❌ **Forgetting `self` parameter**
```python
def circumference():  # Missing self!
```

✅ **Always include `self` in methods**
```python
def circumference(self):  # Correct!
```

❌ **Creating variables instead of objects**
```python
penny_name = "penny"
penny_radius = 9.5
# Hard to manage!
```

✅ **Create objects**
```python
penny = Coin("penny", 9.5, "Canada", "copper", 1)
# Everything organized!
```

---

Good luck with your Coin Collector program! 🪙✨