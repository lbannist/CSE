"""
Phase 1: Character Creation System
Alberta CSE 1110: Structured Programming 1

This module teaches Python basics through an engaging character creation system.

Learning Objectives:
- Variables and data types (strings, integers)
- Input/output statements
- Functions and parameters
- Basic operators (arithmetic, comparison)
- While loops for iteration
- Conditional statements (if/elif/else)
- Random number generation

CSE 1110 Outcomes Addressed:
1.4: Decompose problems into IPO components
2.4.3-2.4.7: Use appropriate data types, variables, operators, and I/O
"""

import random


def display_banner():
    """
    Display the game title banner.
    Teaches: Functions, print statements, string formatting
    """
    print("\n" + "=" * 60)
    print("     WELCOME TO THE REALM OF PYTHON ADVENTURE!")
    print("=" * 60)
    print("\n  Your journey begins with character creation...\n")


def get_character_name():
    """
    Get and validate the character's name from the player.
    Teaches: Input, string variables, while loops, conditionals
    
    Returns:
        str: The validated character name
    """
    while True:  # Loop until valid input
        name = input("Enter your hero's name: ").strip()
        
        # Validation: Check if name is not empty
        if len(name) == 0:
            print("Error: Name cannot be empty. Please try again.\n")
            continue
        
        # Validation: Check if name is not too long
        if len(name) > 20:
            print("Error: Name is too long (max 20 characters). Please try again.\n")
            continue
        
        # Confirm name with player
        print(f"\nYou have chosen the name: {name}")
        confirm = input("Is this correct? (yes/no): ").lower()
        
        if confirm == "yes" or confirm == "y":
            return name
        else:
            print("\nLet's try again.\n")


def allocate_attribute_points():
    """
    Allow player to allocate points to health and mana.
    Teaches: Variables, arithmetic operators, while loops, conditionals
    
    Returns:
        tuple: (health, mana) values chosen by player
    """
    # Constants
    TOTAL_POINTS = 20
    BASE_HEALTH = 80
    BASE_MANA = 30
    POINTS_TO_HEALTH_RATIO = 5  # Each point gives 5 health
    POINTS_TO_MANA_RATIO = 3    # Each point gives 3 mana
    
    print("\n" + "-" * 60)
    print("ATTRIBUTE ALLOCATION")
    print("-" * 60)
    print(f"\nYou have {TOTAL_POINTS} points to allocate.")
    print(f"Starting Stats - Health: {BASE_HEALTH}, Mana: {BASE_MANA}")
    print(f"\nEach point in Health adds {POINTS_TO_HEALTH_RATIO} HP")
    print(f"Each point in Mana adds {POINTS_TO_MANA_RATIO} MP")
    print("\nChoose wisely! Warriors need health, mages need mana.\n")
    
    # Initialize variables
    points_remaining = TOTAL_POINTS
    health_points = 0
    mana_points = 0
    
    # Allocation loop
    while points_remaining > 0:
        # Display current status
        print(f"\nPoints Remaining: {points_remaining}")
        print(f"Current Health: {BASE_HEALTH + (health_points * POINTS_TO_HEALTH_RATIO)}")
        print(f"Current Mana: {BASE_MANA + (mana_points * POINTS_TO_MANA_RATIO)}")
        
        # Get player choice
        print("\nAllocate points to:")
        print("1. Health (+5 HP per point)")
        print("2. Mana (+3 MP per point)")
        print("3. Review and Confirm")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            # Allocate to health
            max_points = points_remaining
            print(f"\nYou can allocate up to {max_points} points to Health.")
            
            # Get number of points to allocate
            points_str = input(f"How many points? (0-{max_points}): ").strip()
            
            # Validate input is a number
            if not points_str.isdigit():
                print("Error: Please enter a valid number.")
                continue
            
            points = int(points_str)
            
            # Validate range
            if points < 0 or points > max_points:
                print(f"Error: Must be between 0 and {max_points}.")
                continue
            
            # Allocate points
            health_points += points
            points_remaining -= points
            print(f"\nAllocated {points} points to Health!")
        
        elif choice == "2":
            # Allocate to mana
            max_points = points_remaining
            print(f"\nYou can allocate up to {max_points} points to Mana.")
            
            # Get number of points to allocate
            points_str = input(f"How many points? (0-{max_points}): ").strip()
            
            # Validate input is a number
            if not points_str.isdigit():
                print("Error: Please enter a valid number.")
                continue
            
            points = int(points_str)
            
            # Validate range
            if points < 0 or points > max_points:
                print(f"Error: Must be between 0 and {max_points}.")
                continue
            
            # Allocate points
            mana_points += points
            points_remaining -= points
            print(f"\nAllocated {points} points to Mana!")
        
        elif choice == "3":
            # Review and confirm
            if points_remaining > 0:
                print(f"\nWarning: You still have {points_remaining} unallocated points!")
                confirm = input("Finish anyway? (yes/no): ").lower()
                if confirm != "yes" and confirm != "y":
                    continue
            
            # Calculate final stats
            final_health = BASE_HEALTH + (health_points * POINTS_TO_HEALTH_RATIO)
            final_mana = BASE_MANA + (mana_points * POINTS_TO_MANA_RATIO)
            
            # Display final stats
            print("\n" + "=" * 40)
            print("FINAL ATTRIBUTES")
            print("=" * 40)
            print(f"Health: {final_health} HP")
            print(f"Mana: {final_mana} MP")
            print(f"Unallocated Points: {points_remaining}")
            
            confirm = input("\nConfirm these stats? (yes/no): ").lower()
            if confirm == "yes" or confirm == "y":
                return (final_health, final_mana)
            else:
                # Reset and start over
                print("\nResetting allocation...\n")
                points_remaining = TOTAL_POINTS
                health_points = 0
                mana_points = 0
        
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
    
    # If loop exits naturally (all points allocated)
    final_health = BASE_HEALTH + (health_points * POINTS_TO_HEALTH_RATIO)
    final_mana = BASE_MANA + (mana_points * POINTS_TO_MANA_RATIO)
    return (final_health, final_mana)


def generate_starting_gold():
    """
    Generate a random amount of starting gold.
    Teaches: Random module, random number generation
    
    Returns:
        int: Random gold amount between 50 and 100
    """
    # Generate random gold between 50 and 100 (inclusive)
    gold = random.randint(50, 100)
    
    print("\n" + "-" * 60)
    print("STARTING WEALTH")
    print("-" * 60)
    print("\nYou search your pockets and count your gold...")
    print(f"You start your adventure with {gold} gold pieces!")
    
    return gold


def display_character_summary(name, health, mana, gold):
    """
    Display the complete character sheet.
    Teaches: Function parameters, string formatting, print statements
    
    Args:
        name (str): Character's name
        health (int): Character's health points
        mana (int): Character's mana points
        gold (int): Character's gold amount
    """
    print("\n" + "=" * 60)
    print("CHARACTER CREATION COMPLETE!")
    print("=" * 60)
    print(f"""
    Name:   {name}
    Health: {health} HP
    Mana:   {mana} MP
    Gold:   {gold} gold
    
    Class:  {"Warrior" if health > 120 else "Mage" if mana > 45 else "Balanced"}
    """)
    print("=" * 60)
    print("\nYour adventure is about to begin...")
    print("=" * 60)


def create_character():
    """
    Main function to orchestrate the character creation process.
    Teaches: Function calls, return values, variable assignment
    
    Returns:
        dict: Character data dictionary
    """
    # Display welcome banner
    display_banner()
    
    # Step 1: Get character name
    name = get_character_name()
    
    # Step 2: Allocate attribute points
    health, mana = allocate_attribute_points()
    
    # Step 3: Generate starting gold
    gold = generate_starting_gold()
    
    # Step 4: Display character summary
    display_character_summary(name, health, mana, gold)
    
    # Create and return character dictionary
    character = {
        "name": name,
        "health": health,
        "max_health": health,
        "mana": mana,
        "max_mana": mana,
        "gold": gold
    }
    
    return character


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    """
    Main program entry point.
    This runs when the script is executed directly.
    """
    
    print("\n" + "=" * 60)
    print("   PYTHON ADVENTURE - CHARACTER CREATION MODULE")
    print("   CSE 1110: Structured Programming 1")
    print("=" * 60)
    
    # Create the player character
    player = create_character()
    
    # Wait for user to continue
    input("\nPress Enter to continue to the game...")
    
    # Display character info one more time
    print("\n\nYour character is ready for adventure!")
    print(f"\nWelcome, {player['name']}!")
    print(f"HP: {player['health']}/{player['max_health']}")
    print(f"MP: {player['mana']}/{player['max_mana']}")
    print(f"Gold: {player['gold']}")
    
    print("\n[This is where the main game would begin...]")
    print("\nEnd of Phase 1 Demo\n")


# ============================================================================
# TEACHING NOTES
# ============================================================================
"""
INSTRUCTOR GUIDE - Phase 1 Teaching Progression

Week 1: Introduction to Python Basics
--------------------------------------
Concepts: print(), variables, data types
Activity: Students modify display_banner() to customize the welcome message
Exercise: Create their own banner with different symbols and text

Week 2: Input and String Operations
------------------------------------
Concepts: input(), string methods, string concatenation
Activity: Walk through get_character_name() line by line
Exercise: Add additional name validation (e.g., no numbers in name)

Week 3: Functions and Return Values
------------------------------------
Concepts: def, return, function calls
Activity: Analyze generate_starting_gold() and explain random.randint()
Exercise: Create a function that generates a random character age (18-30)

Week 4: Conditionals and Comparison
------------------------------------
Concepts: if/elif/else, comparison operators, boolean logic
Activity: Examine validation logic in get_character_name()
Exercise: Add a class suggestion based on name length (short=Warrior, long=Mage)

Week 5: While Loops and Iteration
----------------------------------
Concepts: while loops, loop control, break/continue
Activity: Step through allocate_attribute_points() loop iteration by iteration
Exercise: Add a "help" option that explains the allocation system

Week 6: Arithmetic and Variables
---------------------------------
Concepts: arithmetic operators, variable updates, constants
Activity: Calculate and display different point allocation scenarios
Exercise: Experiment with different POINTS_TO_HEALTH/MANA ratios

Week 7: Dictionaries and Data Structures
-----------------------------------------
Concepts: dictionaries, key-value pairs, data organization
Activity: Examine the character dictionary structure
Exercise: Add new attributes (level=1, experience=0)

Week 8: Integration and Testing
--------------------------------
Concepts: Testing, debugging, code organization
Activity: Test all functions with different inputs
Exercise: Add error handling for unexpected inputs


DIFFERENTIATION STRATEGIES
---------------------------

For Struggling Students:
- Provide partially completed functions with TODO comments
- Start with display_banner() which has no input/validation
- Use pair programming with stronger students
- Create flowcharts of the allocation process

For Advanced Students:
- Add character class selection (Warrior/Mage/Rogue)
- Implement different point allocation rules per class
- Create a "reroll" option to restart character creation
- Add character background story generation
- Implement save/load character to file


ASSESSMENT RUBRICS
------------------

Basic (50-64%):
✓ Can modify existing print statements
✓ Understands variable assignment
✓ Can use input() to get user data
✓ Can call existing functions

Proficient (65-79%):
✓ Can create simple functions with parameters
✓ Uses if/else statements correctly
✓ Implements basic loops
✓ Validates user input (one condition)

Advanced (80-100%):
✓ Creates complex functions with multiple parameters
✓ Uses nested conditionals effectively
✓ Implements complex loop logic
✓ Validates input with multiple conditions
✓ Adds creative enhancements


COMMON STUDENT ERRORS & SOLUTIONS
----------------------------------

Error: Infinite loops in allocation
Solution: Review loop exit conditions and break statements

Error: Type errors (string vs int)
Solution: Demonstrate int() conversion and .isdigit() checking

Error: Indentation errors
Solution: Use consistent spaces/tabs, show how Python uses indentation

Error: Variable scope confusion
Solution: Diagram which variables exist in which functions

Error: Not understanding return values
Solution: Use print() to show what functions return at each step


EXTENSION ACTIVITIES
--------------------

1. Character Portrait ASCII Art
   - Create ASCII art based on allocated stats
   - High health = muscular warrior art
   - High mana = robed mage art

2. Starting Equipment Selection
   - Based on stats, offer appropriate starting gear
   - Warriors get sword, Mages get staff

3. Character Background Generator
   - Random backstory based on name and stats
   - Use string concatenation and random.choice()

4. Multiplayer Character Comparison
   - Create multiple characters
   - Display them side-by-side
   - Determine who has best stats

5. Save Character to Text File
   - Preview of file I/O for future lessons
   - Write character data to a .txt file
"""