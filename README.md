# Text-Based Dungeon Crawler

A simple text-based dungeon crawler game written in Python. Explore rooms, navigate through a mysterious dungeon, and experience the adventure through descriptive text.

## Installation

No external dependencies are required. Just clone the repository and run the game with Python 3.

```bash
git clone <repository-url>
cd dungeon-crawler
python main.py
```

## How to Play

Navigate through the dungeon using directional commands. The game is played entirely through text input.

### Commands

- `north` or `n` - Move north
- `south` or `s` - Move south
- `east` or `e` - Move east
- `west` or `w` - Move west
- `look` - Look around the current room
- `help` - Display available commands
- `quit` or `exit` - Exit the game

## Project Structure

```
dungeon_crawler/
├── main.py             # Entry point for the game
├── game/
│   ├── __init__.py
│   └── game_engine.py  # Main game loop and logic
├── entities/
│   ├── __init__.py
│   └── player.py       # Player character class
└── world/
    ├── __init__.py
    ├── room.py         # Room class
    └── dungeon.py      # Dungeon generation
```

## Current Features

- Explore a dungeon with multiple interconnected rooms
- Simple navigation system
- Descriptive room text
- Command-based interface

## Planned Enhancements

- Combat system with enemies
- Items and inventory management
- Character stats and progression
- Puzzles and traps
- More extensive dungeon generation
- Save/load game functionality

## Development

This project was created as a learning exercise for Python programming, focusing on:

- Object-oriented design
- Game state management
- Text-based user interfaces

Feel free to fork this project and extend it with your own features!
