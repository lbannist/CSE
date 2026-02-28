## Phase 1: Character Creation System

### 📖 Overview

Build the foundation of your RPG game by creating a character creation system. Players will name their hero, allocate points to health and mana, and receive starting gold.

**Alberta Curriculum Alignment:** CSE 1110 Outcomes 1.1-1.8, 2.1-2.6

### 🎯 Learning Objectives

By completing this phase, you will learn to:
- ✅ Use variables to store different types of data (strings, integers)
- ✅ Get input from users and validate it
- ✅ Create functions to organize your code
- ✅ Use loops to repeat actions
- ✅ Make decisions with if/elif/else statements
- ✅ Generate random numbers
- ✅ Work with dictionaries to store character data

### 🛠️ What You're Building

A character creation system that includes:

1. **Welcome Banner** - Display game title with ASCII art
2. **Name Entry** - Get and validate character name (not empty, max 20 chars)
3. **Point Allocation** - Distribute 20 points between Health and Mana
   - Base stats: 80 Health, 30 Mana
   - Each Health point adds +5 HP
   - Each Mana point adds +3 MP
4. **Starting Gold** - Random amount between 50-100 gold pieces
5. **Character Summary** - Display complete character sheet
6. **Data Storage** - Store character info in a dictionary

### 📝 Starter Code Structure

You'll work with these functions:

```python
def display_banner():
    """Shows the game title - Uses print() statements"""
    
def get_character_name():
    """Gets and validates player name - Returns string"""
    
def allocate_attribute_points():
    """Lets player distribute 20 points - Returns (health, mana) tuple"""
    
def generate_starting_gold():
    """Creates random gold 50-100 - Returns integer"""
    
def display_character_summary(name, health, mana, gold):
    """Shows complete character sheet - No return value"""
    
def create_character():
    """Main function that calls all others - Returns character dict"""
```
