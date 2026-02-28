"""
Phase 2: Basic Combat System
Alberta CSE 1120: Structured Programming 2

This module teaches advanced programming concepts through turn-based combat.

Learning Objectives:
- While loops for game loops
- Complex if/elif/else decision trees
- Comparison operators (<, >, <=, >=, ==, !=)
- Boolean logic (and, or, not)
- Random numbers for game mechanics
- Multiple variable tracking and updates
- Nested conditional blocks
- Iterative blocks and flow control

CSE 1120 Outcomes Addressed:
1.1-1.9: Algorithms using selection and iteration
2.1-2.9: Translation to code with control structures
"""

import random


# ============================================================================
# MONSTER CREATION FUNCTIONS
# ============================================================================

def create_goblin():
    """
    Create a Goblin monster (weak enemy).
    Teaches: Dictionary creation, data organization
    
    Returns:
        dict: Monster data with stats
    """
    return {
        "name": "Goblin",
        "max_health": 30,
        "health": 30,
        "min_damage": 3,
        "max_damage": 8,
        "gold_reward": (10, 25),
        "experience": 15
    }


def create_orc():
    """
    Create an Orc monster (medium enemy).
    Teaches: Different stat balancing
    
    Returns:
        dict: Monster data with stats
    """
    return {
        "name": "Orc",
        "max_health": 50,
        "health": 50,
        "min_damage": 5,
        "max_damage": 12,
        "gold_reward": (20, 40),
        "experience": 30
    }


def create_troll():
    """
    Create a Troll monster (strong enemy).
    Teaches: High-difficulty enemy design
    
    Returns:
        dict: Monster data with stats
    """
    return {
        "name": "Troll",
        "max_health": 80,
        "health": 80,
        "min_damage": 8,
        "max_damage": 15,
        "gold_reward": (40, 60),
        "experience": 50
    }


def create_random_monster():
    """
    Create a random monster encounter.
    Teaches: Random selection, function calls
    
    Returns:
        dict: Randomly selected monster
    """
    monster_types = [create_goblin, create_orc, create_troll]
    
    # Weighted probability - Goblins more common than Trolls
    weights = [0.5, 0.35, 0.15]  # 50% Goblin, 35% Orc, 15% Troll
    
    # Choose random monster based on weights
    monster_creator = random.choices(monster_types, weights=weights)[0]
    
    return monster_creator()


# ============================================================================
# COMBAT DISPLAY FUNCTIONS
# ============================================================================

def display_combat_header(player, monster):
    """
    Display the combat header with combatant names.
    Teaches: String formatting, visual presentation
    
    Args:
        player (dict): Player character data
        monster (dict): Monster data
    """
    print("\n" + "=" * 60)
    print(f"COMBAT: {player['name']} vs {monster['name']}")
    print("=" * 60)


def display_combat_status(player, monster):
    """
    Display current health status for both combatants.
    Teaches: Multiple variable display, formatting
    
    Args:
        player (dict): Player character data
        monster (dict): Monster data
    """
    print(f"\n{player['name']} HP: {player['health']}/{player['max_health']} " +
          f"| MP: {player['mana']}/{player['max_mana']}")
    print(f"{monster['name']} HP: {monster['health']}/{monster['max_health']}")


def display_action_menu():
    """
    Display the combat action menu.
    Teaches: Menu creation, user interface design
    """
    print("\n--- Your Turn ---")
    print("1. Attack")
    print("2. Defend")
    print("3. Use Potion")
    print("4. Try to Flee")


# ============================================================================
# COMBAT ACTION FUNCTIONS
# ============================================================================

def player_attack(player, monster):
    """
    Execute player's attack action.
    Teaches: Damage calculation, random ranges, variable updates
    
    Args:
        player (dict): Player character data
        monster (dict): Monster data
        
    Returns:
        int: Damage dealt
    """
    # Base damage from weapon (would come from equipped weapon)
    base_damage = 10
    
    # Add randomness to damage (±3 damage variance)
    damage = random.randint(base_damage - 3, base_damage + 3)
    
    # Critical hit chance (20% for double damage)
    if random.random() < 0.20:  # 20% chance
        damage *= 2
        print(f"\n💥 CRITICAL HIT! 💥")
    
    # Apply damage to monster
    monster["health"] -= damage
    
    print(f"You attack {monster['name']} for {damage} damage!")
    
    return damage


def player_defend(player):
    """
    Execute player's defend action.
    Teaches: State modification, temporary effects
    
    Args:
        player (dict): Player character data
        
    Returns:
        bool: True if defending this turn
    """
    print("\nYou brace yourself for the next attack!")
    print("Incoming damage will be reduced by 50%.")
    
    return True  # Player is now defending


def use_health_potion(player):
    """
    Use a health potion to restore HP.
    Teaches: Inventory management, min/max calculations
    
    Args:
        player (dict): Player character data
        
    Returns:
        bool: True if potion was used successfully
    """
    # Check if player has potions
    if player.get("health_potions", 0) <= 0:
        print("\nYou don't have any health potions!")
        return False
    
    # Calculate healing amount (don't exceed max health)
    heal_amount = 30
    actual_healing = min(heal_amount, player["max_health"] - player["health"])
    
    # Apply healing
    player["health"] += actual_healing
    player["health_potions"] -= 1
    
    print(f"\nYou drink a health potion and restore {actual_healing} HP!")
    print(f"Health potions remaining: {player['health_potions']}")
    
    return True


def try_to_flee(player, monster):
    """
    Attempt to flee from combat.
    Teaches: Probability, boolean returns, risk/reward
    
    Args:
        player (dict): Player character data
        monster (dict): Monster data
        
    Returns:
        bool: True if successfully fled, False otherwise
    """
    flee_chance = 0.30  # 30% base chance to flee
    
    # Higher level monsters are harder to flee from
    # (This could be enhanced with monster "level" attribute)
    
    if random.random() < flee_chance:
        print(f"\nYou successfully escaped from the {monster['name']}!")
        return True
    else:
        print(f"\nYou couldn't escape! The {monster['name']} blocks your path!")
        return False


def monster_attack(player, monster, player_defending=False):
    """
    Execute monster's attack action.
    Teaches: Similar to player attack, conditional damage reduction
    
    Args:
        player (dict): Player character data
        monster (dict): Monster data
        player_defending (bool): Whether player is defending
        
    Returns:
        int: Damage dealt to player
    """
    # Calculate damage in monster's range
    damage = random.randint(monster["min_damage"], monster["max_damage"])
    
    # Apply defense reduction if player is defending
    if player_defending:
        damage = damage // 2  # Reduce damage by 50%
        print(f"\nYour defense absorbs some of the attack!")
    
    # Apply damage to player
    player["health"] -= damage
    
    print(f"{monster['name']} attacks for {damage} damage!")
    
    return damage


# ============================================================================
# MAIN COMBAT LOOP
# ============================================================================

def combat_loop(player, monster=None):
    """
    Main combat loop - handles turn-based combat until victory or defeat.
    Teaches: While loops, complex conditionals, state management, game loop
    
    Args:
        player (dict): Player character data
        monster (dict, optional): Monster to fight. Creates random if None.
        
    Returns:
        bool: True if player won, False if player lost or fled
    """
    # Create random monster if none provided
    if monster is None:
        monster = create_random_monster()
    
    # Display combat start
    display_combat_header(player, monster)
    print(f"\nA wild {monster['name']} appears!")
    
    # Initialize combat variables
    total_damage_dealt = 0
    total_damage_taken = 0
    turns = 0
    player_defending = False
    
    # Main combat loop - continues until someone reaches 0 HP or player flees
    while monster["health"] > 0 and player["health"] > 0:
        turns += 1
        
        # Display current status
        display_combat_status(player, monster)
        
        # Reset defending status at start of turn
        defending_this_turn = False
        
        # ===== PLAYER TURN =====
        display_action_menu()
        
        # Get player action
        action = input("\nChoose action (1-4): ").strip()
        
        # Process player action
        if action == "1":
            # Attack
            damage = player_attack(player, monster)
            total_damage_dealt += damage
            
        elif action == "2":
            # Defend
            defending_this_turn = player_defend(player)
            
        elif action == "3":
            # Use potion
            potion_used = use_health_potion(player)
            if not potion_used:
                # If no potion available, turn is wasted
                print("You fumble in your pack but find nothing!")
            
        elif action == "4":
            # Try to flee
            if try_to_flee(player, monster):
                print("\nYou escaped from combat!")
                return False  # Combat ended, player fled
            # If flee fails, monster gets a free attack (handled below)
            
        else:
            print("\nInvalid action! You hesitate and lose your turn!")
        
        # Check if monster is defeated
        if monster["health"] <= 0:
            break  # Exit loop, player won
        
        # ===== MONSTER TURN =====
        print(f"\n--- {monster['name']}'s Turn ---")
        
        # Monster attacks
        damage_taken = monster_attack(player, monster, defending_this_turn)
        total_damage_taken += damage_taken
        
        # Check if player is defeated
        if player["health"] <= 0:
            break  # Exit loop, player lost
        
        # Small pause for readability
        input("\nPress Enter to continue...")
    
    # ===== COMBAT ENDED =====
    print("\n" + "=" * 60)
    
    # Determine outcome
    if player["health"] <= 0:
        # Player defeated
        print("💀 YOU HAVE BEEN DEFEATED! 💀")
        print(f"\nThe {monster['name']} stands victorious over you.")
        print("\n=== GAME OVER ===")
        return False
        
    elif monster["health"] <= 0:
        # Player victory
        print("🎉 VICTORY! 🎉")
        print(f"\nYou defeated the {monster['name']}!")
        
        # Award gold
        gold_earned = random.randint(*monster["gold_reward"])
        player["gold"] = player.get("gold", 0) + gold_earned
        print(f"You earned {gold_earned} gold!")
        
        # Award experience
        exp_earned = monster["experience"]
        player["experience"] = player.get("experience", 0) + exp_earned
        print(f"You gained {exp_earned} experience!")
        
        # Display combat statistics
        print(f"\n--- Combat Statistics ---")
        print(f"Turns survived: {turns}")
        print(f"Total damage dealt: {total_damage_dealt}")
        print(f"Total damage taken: {total_damage_taken}")
        print(f"Damage per turn: {total_damage_dealt / turns:.1f}")
        
        return True
    
    # This shouldn't be reached, but just in case
    return False


# ============================================================================
# HELPER FUNCTIONS FOR TESTING
# ============================================================================

def create_test_player():
    """
    Create a test player character for demonstration.
    
    Returns:
        dict: Player character with basic stats
    """
    return {
        "name": "Hero",
        "health": 100,
        "max_health": 100,
        "mana": 50,
        "max_mana": 50,
        "gold": 100,
        "experience": 0,
        "health_potions": 3
    }


def test_combat_system():
    """
    Test the combat system with a demo battle.
    """
    print("=" * 60)
    print("COMBAT SYSTEM TEST")
    print("=" * 60)
    
    # Create test player
    player = create_test_player()
    
    print("\nStarting combat test...")
    print("You'll fight a random monster.")
    input("Press Enter to begin...")
    
    # Run combat
    victory = combat_loop(player)
    
    # Display result
    print("\n" + "=" * 60)
    if victory:
        print("Test completed successfully - Player won!")
    else:
        print("Test completed - Player was defeated or fled.")
    print("=" * 60)
    
    # Display final player status
    print(f"\nFinal Player Status:")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Gold: {player['gold']}")
    print(f"Experience: {player['experience']}")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    """
    Main program entry point.
    This runs when the script is executed directly.
    """
    
    print("\n" + "=" * 60)
    print("   PYTHON ADVENTURE - COMBAT SYSTEM MODULE")
    print("   CSE 1120: Structured Programming 2")
    print("=" * 60)
    
    # Run test
    test_combat_system()
    
    print("\n\nEnd of Phase 2 Demo\n")


# ============================================================================
# TEACHING NOTES
# ============================================================================
"""
INSTRUCTOR GUIDE - Phase 2 Teaching Progression

Week 1: Introduction to Game Loops
-----------------------------------
Concepts: While loops, loop conditions, infinite loops
Activity: Analyze the main combat_loop() while condition
Exercise: Modify the loop to add a turn limit (e.g., max 20 turns)

Key Teaching Points:
- The loop continues WHILE both combatants have health > 0
- Using 'and' to combine multiple conditions
- How to break out of loops with 'break' statement
- Why we check monster["health"] <= 0 after player turn

Student Exercise:
Create a simple loop that counts turns and displays a message every 5 turns


Week 2: Complex Conditionals and Menu Systems
----------------------------------------------
Concepts: if/elif/else chains, string comparison, input validation
Activity: Walk through the action menu system step by step
Exercise: Add a new action option (e.g., "5. Check Stats")

Key Teaching Points:
- Using elif for mutually exclusive choices
- Why we use .strip() on input
- What happens with invalid input
- How to nest conditionals (action within action)

Student Exercise:
Add input validation that keeps asking until valid choice (1-4) is entered


Week 3: Random Numbers and Probability
---------------------------------------
Concepts: random.randint(), random.random(), probability
Activity: Experiment with critical hit chance and flee chance
Exercise: Adjust probabilities and observe results over multiple battles

Key Teaching Points:
- random.randint(a, b) gives integers from a to b (inclusive)
- random.random() gives float from 0.0 to 1.0
- Comparing random.random() < 0.20 for 20% chance
- Why we use random for game unpredictability

Student Exercise:
Create a luck system that increases critical hit chance by 5% per level


Week 4: Functions and Return Values
------------------------------------
Concepts: Function parameters, return values, boolean returns
Activity: Trace the flow when player_attack() is called
Exercise: Create a new function player_magic_attack() with mana cost

Key Teaching Points:
- How parameters pass data into functions
- Why some functions return values and others don't
- Using return True/False for yes/no questions
- The difference between print() and return

Student Exercise:
Modify player_attack() to return a tuple: (damage, was_critical)


Week 5: State Management and Variable Tracking
-----------------------------------------------
Concepts: Multiple variables, dictionary updates, persistent state
Activity: Track how player["health"] changes throughout combat
Exercise: Add a "combo" counter that increases damage on consecutive attacks

Key Teaching Points:
- How dictionaries store related data together
- Updating values with += and -=
- Why we need total_damage_dealt and total_damage_taken
- Resetting state at appropriate times (defending_this_turn)

Student Exercise:
Add a "dodge" stat that has 10% chance to avoid all damage


Week 6: Boolean Logic and Conditionals
---------------------------------------
Concepts: and, or, not operators, complex conditions
Activity: Examine all the conditional checks in combat
Exercise: Add a "stunned" status that skips player's turn

Key Teaching Points:
- and: both conditions must be true
- or: at least one condition must be true
- not: reverses a boolean
- Combining operators: if health > 0 and not stunned

Student Exercise:
Create a "berserker" mode when health < 25% (double damage, can't defend)


Week 7: Nested Loops and Control Flow
--------------------------------------
Concepts: break, continue, nested conditionals
Activity: Map out the flow of combat from start to finish
Exercise: Add an "inner loop" for multi-hit attacks

Key Teaching Points:
- break exits the nearest loop
- continue skips to next iteration
- Why we break after monster is defeated
- Nesting if statements inside while loops

Student Exercise:
Add a special attack that hits 3 times, but each hit needs a separate check


Week 8: Integration and Testing
--------------------------------
Concepts: Integration, edge cases, debugging
Activity: Test combat with various scenarios (low health, no potions, etc.)
Exercise: Find and fix bugs, add error handling

Key Teaching Points:
- Test with extreme values (0 health, 1000 damage)
- What happens if player has no potions?
- Preventing negative health values
- Making the game "feel" fair and fun

Student Exercise:
Create a "test suite" that runs 100 combats and reports win/loss ratio


DIFFERENTIATION STRATEGIES
---------------------------

For Struggling Students:
- Start with just attack action, add others gradually
- Provide flowcharts of the combat loop
- Use print() statements to show variable values
- Pair program with stronger students
- Focus on getting basic combat working first

For Advanced Students:
- Implement status effects (poison, burn, freeze)
- Add elemental damage types (fire, ice, lightning)
- Create boss battles with multiple phases
- Implement an AI that chooses monster actions
- Add equipment that modifies combat stats
- Create a combo system for chaining attacks


ASSESSMENT RUBRICS
------------------

Basic (50-64%):
✓ Combat loop works with attack option
✓ Health tracking functions properly
✓ Victory/defeat conditions work
✓ Basic damage calculation implemented

Proficient (65-79%):
✓ All 4 actions implemented and working
✓ Defend reduces damage correctly
✓ Potions restore health properly
✓ Flee chance works as expected
✓ Multiple monster types implemented
✓ Combat statistics tracked

Advanced (80-100%):
✓ Critical hits implemented
✓ Status effects working
✓ Boss battles or special encounters
✓ Combat feels balanced and fun
✓ Creative additions (combos, counters, etc.)
✓ Professional code quality


COMMON STUDENT ERRORS & SOLUTIONS
----------------------------------

Error: Infinite loop in combat
Solution: Check while condition includes health > 0 for BOTH combatants

Error: Monster still attacks after dying
Solution: Add "if monster['health'] <= 0: break" after player attack

Error: Can use infinite potions
Solution: Check potion count before use, decrement after

Error: Negative health values
Solution: Use max(0, health - damage) or check after damage

Error: Defend lasts multiple turns
Solution: Reset defending_this_turn = False at start of each turn

Error: Input validation missing
Solution: Add while loop around input until valid choice


EXTENSION ACTIVITIES
--------------------

1. Monster AI System
   - Monsters choose actions based on their health
   - Low health = try to flee or heal
   - High health = aggressive attacks

2. Combat Log
   - Keep a list of all actions taken
   - Display at end of combat
   - Save to file for review

3. Equipment Effects
   - Weapon affects damage range
   - Armor reduces damage taken
   - Accessories provide special abilities

4. Experience and Leveling
   - Track experience from victories
   - Level up when threshold reached
   - Increase stats on level up

5. Multiple Enemy Battles
   - Fight 2-3 enemies at once
   - Choose which enemy to target
   - Enemies take turns attacking

6. Environmental Effects
   - Rain: lightning spells more effective
   - Dark: harder to flee
   - Sacred ground: healing more effective


INTEGRATION WITH OTHER PHASES
------------------------------

This combat system will integrate with:
- Phase 1: Use player character from character creation
- Phase 3: Equipment affects damage calculations
- Phase 4: Add spell casting as combat option
- Phase 5: This combat is triggered by random encounters
- Phase 6: Loot drops after victory
- Phase 7: Return to town after combat to heal
- Phase 8: Combat is core game loop mechanic


DEBUGGING TIPS FOR STUDENTS
----------------------------

1. Use print() to see variable values
   Example: print(f"DEBUG: player health = {player['health']}")

2. Test with easy monsters first
   Set monster health = 5 for quick testing

3. Add temporary invincibility for testing
   Comment out damage to player during development

4. Test each action individually
   Don't try to test everything at once

5. Use input() to pause and inspect
   Add input("Press enter...") to pause execution

6. Keep a list of test cases
   - Win combat
   - Lose combat  
   - Flee successfully
   - Flee and fail
   - Use potion when have some
   - Use potion when have none
   - Defend then get hit
   - Critical hit


ASSESSMENT QUESTIONS
--------------------

1. Why do we use a while loop instead of a for loop for combat?
2. What would happen if we removed the "break" statements?
3. How does the random.random() < 0.20 check work for critical hits?
4. Why do we need both min_damage and max_damage for monsters?
5. What is the purpose of the defending_this_turn variable?
6. How could you make combat more interesting?


REAL-WORLD CONNECTIONS
-----------------------

Discuss how these concepts apply to:
- Video game combat systems (Pokemon, Final Fantasy)
- Turn-based board games (chess, checkers)
- Real-time strategy games (planning vs execution)
- Game balance and fairness
- Player engagement and fun factor
- Risk vs reward decision making
"""