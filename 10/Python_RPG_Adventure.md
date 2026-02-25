# Python Side-Scrolling RPG Adventure
## Student Assignment Guide
**CSE 1110 & 1120: Structured Programming**

---

## 📚 Table of Contents

- [Welcome](#welcome)
- [Phase 1: Character Creation System](#phase-1-character-creation-system)
- [Phase 2: Basic Combat System](#phase-2-basic-combat-system)
- [Phase 3: Equipment & Inventory](#phase-3-equipment--inventory)
- [Phase 4: Magic System](#phase-4-magic-system)
- [Phase 5: Random Encounters](#phase-5-random-encounters)
- [Phase 6: Loot & Treasure](#phase-6-loot--treasure)
- [Phase 7: Town Hub & NPCs](#phase-7-town-hub--npcs)
- [Phase 8: Complete Integration](#phase-8-complete-integration)
- [Final Project Requirements](#final-project-requirements)
- [Grading & Submission](#grading--submission)
- [Resources & Help](#resources--help)

---

## 🎮 Welcome

Welcome, future game developer! Throughout this course, you'll build a complete text-based RPG game from scratch. Each phase introduces new programming concepts through fun, engaging challenges. By the end, you'll have a playable game to share with friends and family!

### Project Overview

You'll create a side-scrolling adventure game featuring:
- ⚔️ Turn-based combat system
- 🎒 Equipment and inventory management
- ✨ Magic spells and abilities
- 👾 Random monster encounters
- 💰 Loot and treasure system
- 🏰 Town hub with NPCs (healer, shopkeeper)
- 📊 Character progression and stats

### How This Works

Each phase has **three difficulty levels**:
- **Level 1 (Core)**: Required for 50-64% - Core functionality
- **Level 2 (Enhanced)**: Required for 65-79% - Enhanced features
- **Level 3 (Advanced)**: Required for 80-100% - Creative additions

Complete higher-level tasks to earn a better grade!

---

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

### ✨ Assignment Tasks

#### Level 1: Core (Required for 50-64%)

- [ ] **Task 1.1**: Modify `display_banner()` to show your own game title
- [ ] **Task 1.2**: Test `get_character_name()` with different inputs
- [ ] **Task 1.3**: Run the complete program and create a character
- [ ] **Task 1.4**: Take a screenshot of your character summary
- [ ] **Task 1.5**: Write down what each function does in your own words

#### Level 2: Enhanced (Required for 65-79%)

- [ ] **Task 2.1**: Add comments explaining each function's purpose
- [ ] **Task 2.2**: Modify starting gold range to 75-150
- [ ] **Task 2.3**: Change health/mana ratios (try +10 HP and +5 MP per point)
- [ ] **Task 2.4**: Add input validation to prevent negative numbers
- [ ] **Task 2.5**: Create 3 different characters with different stat builds

#### Level 3: Advanced (Required for 80-100%)

- [ ] **Task 3.1**: Add character class selection (Warrior/Mage/Rogue)
  - Warrior: 100 HP, 20 MP base
  - Mage: 70 HP, 50 MP base
  - Rogue: 85 HP, 35 MP base

- [ ] **Task 3.2**: Create a "reroll" feature to restart character creation

- [ ] **Task 3.3**: Add a "quick start" option with preset character builds

- [ ] **Task 3.4**: Implement character age selection (18-30)
  - Younger characters: +5 MP, -5 HP per year under 25
  - Older characters: +5 HP, -5 MP per year over 25

- [ ] **Task 3.5**: Add character background story generator
  - Use `random.choice()` to select story elements
  - Display based on character stats and choices

### 📤 Submission Requirements

Submit these files to the assignment folder:

1. **phase1.py** - Your complete Python code
2. **screenshot.png** - Screenshot showing character creation working
3. **reflection.txt** - Answers to reflection questions (below)

### 🤔 Reflection Questions

Answer these in `reflection.txt`:

1. What does the while loop in `allocate_attribute_points()` do? Why is it necessary?
2. Why do we need to validate user input in `get_character_name()`?
3. Explain the difference between `health_points` and `final_health` variables.
4. How does `random.randint(50, 100)` work? What values can it return?
5. What would happen if you allocated 25 points instead of 20? How does the code prevent this?
6. How could you make the character creation more interesting or engaging?

### 📊 Grading Rubric - Phase 1 (100 points)

#### Functionality (40 points)
- [ ] **10 pts** - Program runs without errors
- [ ] **8 pts** - Banner displays correctly with custom title
- [ ] **8 pts** - Name input and validation works properly
- [ ] **10 pts** - Point allocation system functions correctly
- [ ] **4 pts** - Random gold generates in correct range

#### Code Quality (30 points)
- [ ] **8 pts** - Proper indentation and formatting throughout
- [ ] **8 pts** - Meaningful variable names used consistently
- [ ] **8 pts** - Comments explain what code does clearly
- [ ] **6 pts** - Functions are used appropriately

#### Completeness (20 points)
- [ ] **5 pts** - All Level 1 tasks completed
- [ ] **8 pts** - Level 2 tasks attempted/completed
- [ ] **7 pts** - Level 3 tasks attempted/completed

#### Reflection (10 points)
- [ ] **10 pts** - All questions answered thoughtfully with specific examples

**TOTAL: _____ / 100**

### 💡 Tips for Success

- ✅ Test your code frequently - run it after each change
- ✅ Use descriptive variable names (not just 'x' or 'a')
- ✅ Read error messages carefully - they tell you what's wrong
- ✅ Ask for help if you're stuck for more than 15 minutes
- ✅ Save your work often (Ctrl+S or Cmd+S)
- ✅ Comment your code so you remember what it does

### ⚠️ Common Mistakes to Avoid

- ❌ Forgetting to convert `input()` to `int()` when needed
- ❌ Not indenting code inside functions properly
- ❌ Misspelling variable names
- ❌ Forgetting to return values from functions
- ❌ Not testing with different types of input

---

## Phase 2: Basic Combat System

### 📖 Overview

Build on Phase 1 by adding a simple turn-based combat system where your character fights monsters. This introduces more complex decision-making and game loop concepts.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 1.1-1.9, 2.1-2.9

### 🎯 Learning Objectives

- ✅ Use while loops for game loops
- ✅ Implement complex if/elif/else decision trees
- ✅ Work with comparison operators (`<`, `>`, `<=`, `>=`, `==`, `!=`)
- ✅ Understand boolean logic (`and`, `or`, `not`)
- ✅ Use random numbers for game mechanics
- ✅ Track and update multiple variables simultaneously

### 🛠️ What You're Building

A combat system featuring:

1. **Monster Creation** - Generate monsters with random stats
2. **Turn-Based Loop** - Alternating player and monster turns
3. **Player Actions** - Attack, Defend, Use Item, Flee
4. **Damage Calculation** - Random damage ranges with modifiers
5. **Health Tracking** - Monitor HP for player and monster
6. **Victory/Defeat** - Conditions and outcomes
7. **Combat Summary** - Display battle statistics

### 📝 Starter Code Structure

```python
def create_monster(monster_type):
    """Returns monster dictionary with stats"""
    
def display_combat_status(player, monster):
    """Shows current HP for both combatants"""
    
def player_attack(player, monster):
    """Calculate and apply player damage"""
    
def monster_attack(player, monster):
    """Calculate and apply monster damage"""
    
def combat_loop(player, monster):
    """Main combat function
    Returns True if player wins, False if defeated"""
```

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create a simple monster dictionary with name, health, damage
- [ ] **Task 1.2**: Implement basic attack function (player deals 5-15 damage)
- [ ] **Task 1.3**: Create combat loop that runs until one side reaches 0 HP
- [ ] **Task 1.4**: Display combat messages ("You hit for X damage!")
- [ ] **Task 1.5**: Show victory or defeat message when combat ends

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add player action menu (Attack/Defend/Flee)
- [ ] **Task 2.2**: Implement defend action (reduces damage by 50%, can't attack same turn)
- [ ] **Task 2.3**: Add flee option (30% escape chance, failed escape = monster gets free attack)
- [ ] **Task 2.4**: Create 3 different monster types (Goblin-weak, Orc-medium, Troll-strong)
- [ ] **Task 2.5**: Add critical hit system (20% chance for 2x damage)

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Implement status effects
  - Poison: 2 damage per turn for 3 turns
  - Stun: Skip next turn

- [ ] **Task 3.2**: Add combo attack system
  - Track consecutive attacks
  - Bonus damage for 3+ hits in a row

- [ ] **Task 3.3**: Create boss monster encounter
  - Much higher HP (150+)
  - Special attacks
  - Phase change at 50% HP

- [ ] **Task 3.4**: Add combat statistics tracking
  - Total damage dealt/taken
  - Turns survived
  - Accuracy percentage

- [ ] **Task 3.5**: Implement difficulty scaling (monsters get stronger based on player wins)

### 📊 Grading Rubric - Phase 2 (100 points)

#### Functionality (40 points)
- [ ] **10 pts** - Combat loop works correctly without infinite loops
- [ ] **10 pts** - All player actions function properly
- [ ] **8 pts** - Damage calculations are accurate
- [ ] **6 pts** - Victory/defeat conditions trigger correctly
- [ ] **6 pts** - Random elements work as intended

#### Code Quality (30 points)
- [ ] **8 pts** - Code is well-organized and readable
- [ ] **8 pts** - Functions are used appropriately
- [ ] **8 pts** - Comments explain complex logic
- [ ] **6 pts** - Variable names are descriptive

#### Completeness (20 points)
- [ ] **5 pts** - All Level 1 tasks completed
- [ ] **8 pts** - Level 2 tasks completed
- [ ] **7 pts** - Level 3 tasks completed

#### Creativity (10 points)
- [ ] **10 pts** - Added unique features or creative improvements

**TOTAL: _____ / 100**

---

## Phase 3: Equipment & Inventory

### 📖 Overview

Create an equipment and inventory system that lets players collect and use items. This introduces working with lists and dictionaries to manage game data.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 2.3-2.9

### 🎯 Learning Objectives

- ✅ Use nested dictionaries to store item data
- ✅ Work with lists to track inventory
- ✅ Implement add/remove operations
- ✅ Compare and select items
- ✅ Update character stats based on equipment
- ✅ Handle inventory limits and constraints

### 🛠️ What You're Building

1. **Equipment Database** - Weapons, shields, armor with stats
2. **Player Inventory** - Track owned items and quantities
3. **Equip/Unequip** - Change equipped items
4. **Item Comparison** - Compare stats side-by-side
5. **Inventory Display** - Show all items clearly
6. **Item Usage** - Use consumables (potions)

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create weapon dictionary with 3 weapons (name, damage, price)
- [ ] **Task 1.2**: Create shield dictionary with 2 shields (name, defense, price)
- [ ] **Task 1.3**: Make player inventory as a dictionary (track current weapon/shield)
- [ ] **Task 1.4**: Create `equip_weapon()` function
- [ ] **Task 1.5**: Display currently equipped items

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add health and mana potions to inventory
- [ ] **Task 2.2**: Implement `use_potion()` (Health potion = 30 HP, Mana = 20 MP)
- [ ] **Task 2.3**: Create inventory display function showing all items with quantities
- [ ] **Task 2.4**: Add item comparison feature (compare two weapons side-by-side)
- [ ] **Task 2.5**: Implement inventory limits (max 20 items total)

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Add armor system (helmet, chest, boots with different bonuses)
- [ ] **Task 3.2**: Create item rarity system (Common/Rare/Epic/Legendary with color coding)
- [ ] **Task 3.3**: Implement item durability (items degrade with use, need repair)
- [ ] **Task 3.4**: Add item sets (wearing matching items = bonus)
- [ ] **Task 3.5**: Create item crafting system (combine items to make better ones)

### 📊 Grading Rubric - Phase 3 (100 points)

#### Functionality (40 points)
- [ ] **10 pts** - Item database complete and accessible
- [ ] **10 pts** - Inventory system works correctly
- [ ] **8 pts** - Equip/unequip functions work
- [ ] **6 pts** - Potions restore HP/MP correctly
- [ ] **6 pts** - Inventory display is clear and organized

#### Code Quality (30 points)
- [ ] **8 pts** - Efficient data structures used
- [ ] **8 pts** - Functions handle errors gracefully
- [ ] **8 pts** - Code is well-commented
- [ ] **6 pts** - No duplicate code

#### Completeness (20 points)
- [ ] **5 pts** - Level 1 tasks completed
- [ ] **8 pts** - Level 2 tasks completed
- [ ] **7 pts** - Level 3 tasks completed

#### Usability (10 points)
- [ ] **10 pts** - Interface is user-friendly and intuitive

**TOTAL: _____ / 100**

---

## Phase 4: Magic System

### 📖 Overview

Add a spell-casting system with different spells that consume mana. This teaches resource management and complex function interactions.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 1.5-1.9, 2.6-2.9

### 🎯 Learning Objectives

- ✅ Implement resource management (mana costs)
- ✅ Create spell effects system
- ✅ Handle multiple conditions and checks
- ✅ Build spell selection interface
- ✅ Calculate spell effectiveness
- ✅ Balance game mechanics

### 🛠️ What You're Building

1. **Spell Database** - 5+ spells with different effects
2. **Mana Cost System** - Track and deduct mana
3. **Spell Casting** - Execute spell effects
4. **Spell Effects** - Damage, healing, buffs, debuffs
5. **Cooldown System** - Powerful spells need recharge time
6. **Spell Upgrades** - Level up spells for better effects

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create spell dictionary with 3 spells
  - Fireball: 20 damage, 15 mana
  - Heal: 25 HP restore, 10 mana
  - Lightning: 30 damage, 25 mana

- [ ] **Task 1.2**: Implement mana checking (can't cast if insufficient mana)
- [ ] **Task 1.3**: Create `cast_spell()` function
- [ ] **Task 1.4**: Display available spells with mana costs
- [ ] **Task 1.5**: Update combat to include spell casting option

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add 2 more spells with unique effects (Ice Blast, Shield)
- [ ] **Task 2.2**: Implement spell levels (spells get stronger as they level up)
- [ ] **Task 2.3**: Add mana regeneration (restore 5 mana per turn)
- [ ] **Task 2.4**: Create spell cooldown system (powerful spells need 2-3 turns to recharge)
- [ ] **Task 2.5**: Add spell failure chance based on remaining mana

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Implement spell combinations (cast 2 spells for bonus effect)
- [ ] **Task 3.2**: Add elemental system (Fire/Ice/Lightning counter each other)
- [ ] **Task 3.3**: Create ultimate spell (requires full mana, massive effect)
- [ ] **Task 3.4**: Implement spell learning system (find spell books, learn new spells)
- [ ] **Task 3.5**: Add mana cost reduction items (Wizard's Robes = -20% cost)

### 📊 Grading Rubric - Phase 4 (100 points)

#### Functionality (40 points)
- [ ] **12 pts** - All spells work correctly
- [ ] **10 pts** - Mana system functions properly
- [ ] **8 pts** - Spell effects apply correctly
- [ ] **6 pts** - Spell menu is functional
- [ ] **4 pts** - Integration with combat works seamlessly

#### Code Quality (30 points)
- [ ] **8 pts** - Spell data well-organized
- [ ] **8 pts** - Functions are modular and reusable
- [ ] **8 pts** - Clear documentation
- [ ] **6 pts** - Efficient algorithms

#### Completeness (20 points)
- [ ] **5 pts** - Level 1 complete
- [ ] **8 pts** - Level 2 complete
- [ ] **7 pts** - Level 3 complete

#### Creativity (10 points)
- [ ] **10 pts** - Unique spell effects and creative mechanics

**TOTAL: _____ / 100**

---

## Phase 5: Random Encounters

### 📖 Overview

Build a system that randomly generates monster encounters as the player explores. Uses `random.choice()`, probability, and encounter tables.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 1.6-1.9

### 🎯 Learning Objectives

- ✅ Use `random.choice()` for selection
- ✅ Implement probability systems
- ✅ Create encounter tables
- ✅ Handle multiple outcomes
- ✅ Balance difficulty scaling

### 🛠️ What You're Building

1. **Encounter System** - Random monster generation
2. **Probability Tables** - Different encounter rates
3. **Monster Variety** - Multiple enemy types
4. **Difficulty Scaling** - Monsters get stronger over time
5. **Escape Mechanics** - Avoid unwanted fights
6. **Exploration Loop** - Step-by-step adventure

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create list of 3 monster types
- [ ] **Task 1.2**: Use `random.choice()` to select random monster
- [ ] **Task 1.3**: Create simple exploration loop (10 steps)
- [ ] **Task 1.4**: 30% chance of encounter per step
- [ ] **Task 1.5**: Display encounter messages

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add 5 different monster types with varying difficulty
- [ ] **Task 2.2**: Implement weighted probability (rare monsters less common)
- [ ] **Task 2.3**: Create "safe zones" with no encounters
- [ ] **Task 2.4**: Add treasure chest encounters (10% chance)
- [ ] **Task 2.5**: Track steps traveled and display to player

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Dynamic difficulty (monsters scale with player stats)
- [ ] **Task 3.2**: Boss encounter every 25 steps
- [ ] **Task 3.3**: Create encounter zones (forest, cave, mountain with different monsters)
- [ ] **Task 3.4**: Add weather effects (rain increases encounters by 20%)
- [ ] **Task 3.5**: Implement "lucky" and "unlucky" streaks

### 📊 Grading Rubric - Phase 5 (100 points)

**Same structure as previous phases:** 40 pts Functionality, 30 pts Code Quality, 20 pts Completeness, 10 pts Creativity

---

## Phase 6: Loot & Treasure

### 📖 Overview

Create a loot drop system where defeated monsters and treasure chests give random rewards. Teaches weighted probability and reward systems.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 2.6-2.9

### 🎯 Learning Objectives

- ✅ Implement loot tables
- ✅ Use weighted probability
- ✅ Create rarity systems
- ✅ Balance rewards
- ✅ Manage item drops

### 🛠️ What You're Building

1. **Loot Tables** - Items monsters can drop
2. **Rarity System** - Common to Legendary items
3. **Gold Drops** - Random currency amounts
4. **Equipment Drops** - Weapons, armor, etc.
5. **Treasure Chests** - Special loot containers
6. **Drop Rates** - Balanced probability

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create `generate_loot()` function
- [ ] **Task 1.2**: Random gold drops (10-50 based on monster)
- [ ] **Task 1.3**: 50% chance for health potion drop
- [ ] **Task 1.4**: Display loot to player
- [ ] **Task 1.5**: Add loot to inventory

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add equipment drops (10% chance)
- [ ] **Task 2.2**: Create treasure chest system
- [ ] **Task 2.3**: Implement rarity levels (Common/Rare/Epic)
- [ ] **Task 2.4**: Higher rarity = better stats
- [ ] **Task 2.5**: Loot summary after combat

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Boss-specific loot tables
- [ ] **Task 3.2**: Item sets (collect all pieces for bonus)
- [ ] **Task 3.3**: "Luck" stat affects drop rates
- [ ] **Task 3.4**: Special event drops (holiday items)
- [ ] **Task 3.5**: Loot history and statistics

---

## Phase 7: Town Hub & NPCs

### 📖 Overview

Build a town area with NPCs (healer, shopkeeper) where players can rest, heal, buy/sell items. Introduces state management and NPC dialogue.

**Alberta Curriculum Alignment:** CSE 1120 Outcomes 1.1-1.9, 2.1-2.9

### 🎯 Learning Objectives

- ✅ Create NPC interaction system
- ✅ Implement shop mechanics
- ✅ Build economy (buying/selling)
- ✅ Manage game states
- ✅ Create navigation menus

### 🛠️ What You're Building

1. **Town Navigation** - Move between locations
2. **Healer NPC** - Restore HP/MP for gold
3. **Shop System** - Buy and sell items
4. **Economy** - Item pricing and gold management
5. **Services** - NPC-provided benefits
6. **State Management** - Track town vs adventure mode

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create town menu (Healer/Shop/Leave)
- [ ] **Task 1.2**: Implement healer (restore full HP/MP for 50 gold)
- [ ] **Task 1.3**: Create basic shop (buy 3 items)
- [ ] **Task 1.4**: Display current gold
- [ ] **Task 1.5**: Validate purchases (enough gold)

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add sell functionality (75% of purchase price)
- [ ] **Task 2.2**: Multiple healer options (HP only, MP only, both)
- [ ] **Task 2.3**: Shop inventory updates (limited stock)
- [ ] **Task 2.4**: NPC dialogue system
- [ ] **Task 2.5**: Inn for saving game

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Multiple shops (weapon shop, armor shop, magic shop)
- [ ] **Task 3.2**: Quest system (NPC gives quests)
- [ ] **Task 3.3**: Reputation system (better prices with high rep)
- [ ] **Task 3.4**: Special events in town
- [ ] **Task 3.5**: Town upgrades (unlock new services)

### 📊 Grading Rubric - Phase 7 (100 points)

**Same structure:** 40 pts Functionality, 30 pts Code Quality, 20 pts Completeness, 10 pts Creativity

---

## Phase 8: Complete Integration

### 📖 Overview

Combine all previous phases into a complete, playable game. Add main menu, save/load, game over conditions, and final polish.

**Alberta Curriculum Alignment:** All CSE 1110/1120 Outcomes

### 🎯 Learning Objectives

- ✅ Integrate multiple systems
- ✅ Debug complex interactions
- ✅ Polish user experience
- ✅ Test thoroughly
- ✅ Create complete game loop

### 🛠️ What You're Building

1. **Main Menu** - Start, Load, Quit
2. **Game Loop** - Town → Adventure → Town cycle
3. **Win Conditions** - Complete objectives
4. **Game Over** - Death and restart
5. **Statistics** - Track player progress
6. **Polish** - Fix bugs, improve UX

### ✨ Assignment Tasks

#### Level 1: Core (50-64%)

- [ ] **Task 1.1**: Create main menu
- [ ] **Task 1.2**: Integrate all phases
- [ ] **Task 1.3**: Game over on death
- [ ] **Task 1.4**: Victory condition (defeat 10 monsters)
- [ ] **Task 1.5**: Test all systems together

#### Level 2: Enhanced (65-79%)

- [ ] **Task 2.1**: Add save/load system (to file)
- [ ] **Task 2.2**: Statistics tracking
- [ ] **Task 2.3**: Multiple difficulty levels
- [ ] **Task 2.4**: Story elements and narrative
- [ ] **Task 2.5**: Credits screen

#### Level 3: Advanced (80-100%)

- [ ] **Task 3.1**: Achievement system
- [ ] **Task 3.2**: New Game+ mode
- [ ] **Task 3.3**: Multiple endings
- [ ] **Task 3.4**: Easter eggs and secrets
- [ ] **Task 3.5**: Comprehensive testing and bug fixes

---

## Final Project Requirements

### 📋 Complete Game Must Include

Your final game must have **ALL** of these features:

✅ Character creation with stats allocation (Phase 1)
✅ Turn-based combat system (Phase 2)
✅ Equipment and inventory management (Phase 3)
✅ Spell casting with mana (Phase 4)
✅ Random monster encounters (Phase 5)
✅ Loot drops and treasure (Phase 6)
✅ Town hub with healer and shop (Phase 7)
✅ Working game loop and menus (Phase 8)

### 🎯 Final Project Grading (200 points)

#### Functionality (80 points)
- [ ] **20 pts** - All systems work together seamlessly
- [ ] **15 pts** - No major bugs or crashes
- [ ] **15 pts** - Game is playable from start to finish
- [ ] **15 pts** - All features from phases 1-7 present and functional
- [ ] **15 pts** - Game balance is reasonable (not too easy/hard)

#### Code Quality (50 points)
- [ ] **15 pts** - Well-organized code structure (logical file/function organization)
- [ ] **15 pts** - Comprehensive comments explaining complex sections
- [ ] **10 pts** - Efficient algorithms used throughout
- [ ] **10 pts** - No significant code duplication

#### Creativity (40 points)
- [ ] **15 pts** - Unique features added beyond requirements
- [ ] **15 pts** - Creative game mechanics or systems
- [ ] **10 pts** - Interesting story, theme, or setting

#### Presentation (30 points)
- [ ] **10 pts** - Game is visually appealing (good text formatting, colors)
- [ ] **10 pts** - Clear instructions provided to player
- [ ] **10 pts** - Professional presentation and polish

**TOTAL: _____ / 200**

### 📤 Final Submission

Submit in a folder named `YourName_FinalProject`:

1. All Python files (.py)
2. README.md with:
   - How to run the game
   - Controls and features
   - Any special notes
3. Screenshots or demo video
4. Final reflection (2-3 paragraphs on what you learned)

---

## 📚 Resources & Help

### Getting Help

If you get stuck:

1. **Read the error message carefully** - It tells you what's wrong
2. **Check your indentation** - Python is strict about this
3. **Review the example code** - Compare your code to examples
4. **Ask a classmate** - Explain the problem to someone else
5. **Check Python documentation** - [docs.python.org](https://docs.python.org)
6. **Ask your teacher** - That's what we're here for!

### Useful Python Documentation

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Random Module](https://docs.python.org/3/library/random.html)
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [String Formatting](https://docs.python.org/3/tutorial/inputoutput.html)

### Common Python Errors

**IndentationError**: Check that your code is indented consistently
**NameError**: Variable doesn't exist - check spelling
**TypeError**: Wrong data type - use `int()` or `str()` to convert
**KeyError**: Dictionary key doesn't exist - check spelling
**IndexError**: List index out of range - check your loop

### Tips for Success

✅ **Start early** - Don't wait until the due date
✅ **Save often** - Use Ctrl+S or Cmd+S frequently
✅ **Test frequently** - Run your code after every change
✅ **Comment as you go** - Don't wait until the end
✅ **Back up your work** - Use Google Drive, OneDrive, or GitHub
✅ **Ask questions** - No question is too simple

### Academic Integrity

**You MAY:**
- Discuss ideas and strategies with classmates
- Help each other debug errors
- Share general approaches to problems

**You MAY NOT:**
- Copy another student's code word-for-word
- Submit AI-generated code as your own work
- Use code you don't understand or can't explain

**When in doubt, ask your teacher!**

If you use code from the internet or AI assistance, you must:
1. Cite the source in a comment
2. Understand how it works
3. Be able to explain it to your teacher

---

## 🎉 Final Thoughts

Building this game is a significant achievement! You're learning real programming skills that professional developers use every day. Don't get discouraged if you encounter bugs or errors - debugging is a huge part of programming.

Remember:
- Every expert programmer started as a beginner
- Mistakes are how we learn
- Asking for help is a sign of strength, not weakness
- Your game doesn't have to be perfect - it just needs to work!

**Good luck on your coding adventure!** 🚀

---

*© 2024 Python RPG Project - Alberta CSE 1110/1120*
*This guide aligns with the Alberta Education Computer Science Program of Studies*
