# The Hobbit: An Unexpected Journey

A text-based adventure game based on J.R.R. Tolkien's "The Hobbit". Travel through Middle-earth, encounter familiar characters, and experience the journey of Bilbo Baggins through descriptive text and interactive gameplay.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Locations](#locations)
- [Characters](#characters)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

## Installation

No external dependencies are required. Just clone the repository and run the game with Python 3.

```bash
git clone <repository-url>
cd the-hobbit-adventure
python main.py
```

## How to Play

You play as Bilbo Baggins, a hobbit unexpectedly swept into an adventure with a company of dwarves. Navigate through Middle-earth using text commands to explore locations, interact with characters, and discover treasures.

### Basic Commands

| Command              | Description                          |
| -------------------- | ------------------------------------ |
| `north` (or `n`)     | Move north                           |
| `south` (or `s`)     | Move south                           |
| `east` (or `e`)      | Move east                            |
| `west` (or `w`)      | Move west                            |
| `up` / `down`        | Move up or down in certain locations |
| `in` / `out`         | Enter or exit certain locations      |
| `look`               | Look around the current location     |
| `map` (or `m`)       | Display a map of explored areas      |
| `inventory` (or `i`) | Check your inventory                 |
| `help`               | Display available commands & _hints_ |
| `quit`               | Exit the game                        |

### Character Interaction Commands

| Command                         | Description                            |
| ------------------------------- | -------------------------------------- |
| `talk to [character]`           | Start a conversation with a character  |
| `ask [character] about [topic]` | Ask a character about a specific topic |

### Item Commands

| Command      | Description                     |
| ------------ | ------------------------------- |
| `use [item]` | Use an item from your inventory |

## Game Features

### Interactive Storytelling

Experience the story of The Hobbit through descriptive text and character interactions. The game follows the journey from Bag End to the Lonely Mountain, with locations and characters faithful to Tolkien's world.

### Hint System

Throughout your adventure, the game provides contextual hints to guide you. When a hint is available in your current location, you'll see a notification. Simply type `help` to view the hint. Hints are available in key locations to:

- Guide you toward the next story beat
- Provide suggestions for interacting with characters
- Offer tactical advice for challenging situations
- Remind you of important game mechanics

The hint system is designed to be unobtrusive - it's there when you need guidance, but doesn't spoil the experience of discovery.

### Character Interactions

Speak with iconic characters from The Hobbit! Each character has unique dialogue and personality:

- **Gandalf** - Speaks in riddles and offers cryptic advice
- **Thorin** - Proud and determined to reclaim his homeland
- **The Dwarves** - Boisterous and hungry for adventure (and food!)
- **Elrond** - Wise and knowledgeable about ancient secrets
- **Gollum** - Obsessed with his "precious" and fond of riddles
- **Beorn** - Gruff but protective of his animal friends
- **Smaug** - Cunning, proud, and very dangerous

**Suggested topics to ask about:**

- Adventure
- Quest
- Ring/Precious
- Mountain/Erebor
- Treasure/Gold
- Arkenstone
- Map/Secret
- Forest/Mirkwood
- Animals
- Food
- Song/Music

### Dynamic Map System

As you explore Middle-earth, your map will expand to show the places you've visited. Use the `map` command to view your current location and plan your journey.

### Riddle Challenge

When you encounter Gollum in his cave beneath the Misty Mountains, you'll be challenged to a battle of wits. Answer his five riddles correctly (within a time limit) to win his precious ring!

### Inventory System

Collect and use items throughout your journey. The most valuable treasure might be a simple golden ring with unusual properties...

## Locations

Your adventure takes you through these iconic locations from The Hobbit:

- **Bag End** - Your cozy hobbit-hole where the adventure begins
- **The East Road** - The path through the peaceful Shire
- **Trollshaws** - Dangerous woods inhabited by hungry trolls
- **Rivendell** - The Last Homely House, refuge of the elves
- **Misty Mountains** - Treacherous peaks with hidden dangers
- **Goblin Tunnels** - Maze-like passages beneath the mountains
- **Underground Lake** - Dark waters where Gollum lurks
- **Beorn's House** - The home of the skin-changer
- **Mirkwood** - An ancient, enchanted forest full of peril
- **Laketown** - A settlement built upon the Long Lake
- **Lonely Mountain** - The ancient home of the dwarves
- **Dragon's Hoard** - Smaug's treasure chamber deep within the mountain

## Characters

Interact with these key characters from Tolkien's world:

- **Gandalf the Grey** - The wizard who initiates your adventure
- **Thorin Oakenshield** - Leader of the company seeking to reclaim Erebor
- **The Dwarves** - Fili, Kili, Dwalin, Balin, and the rest of Thorin's company
- **Lord Elrond** - The wise elf-lord of Rivendell
- **Gollum** - The wretched creature dwelling beneath the mountains
- **Beorn** - The skin-changer who can transform into a great bear
- **Smaug** - The terrible dragon guarding the dwarven treasure

## Project Structure

```
hobbit_adventure/
├── main.py             # Entry point for the game
├── game/
│   ├── __init__.py
│   ├── game_engine.py  # Main game loop and logic
│   ├── map_display.py  # Map rendering functionality
│   └── character_interactions.py # Character dialog systems
├── entities/
│   ├── __init__.py
│   ├── player.py       # Player character class
│   └── character.py    # NPC character classes
├── items/
│   ├── __init__.py
│   └── items.py        # Item classes including the Ring
└── world/
    ├── __init__.py
    ├── room.py         # Room class with hint system
    ├── bag_end.py      # Bag End generation
    ├── locations.py    # Middle-earth locations
    ├── character_setup.py # Character placement
    └── middle_earth.py # World generation and management
```

## Future Enhancements

The game is still growing! Planned enhancements include:

- Special encounters with trolls, spiders, and Smaug
- More items to find and use
- Puzzles based on events from the book
- Side quests and optional areas
- Save/load game functionality

---

_This project was created as a learning exercise for Python programming, focusing on object-oriented design, game state management, text-based user interfaces, and threading for timed events._

_"Far over the misty mountains cold, to dungeons deep and caverns old..."_
