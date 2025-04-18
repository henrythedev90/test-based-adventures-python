#!/usr/bin/env python3

from game.game_engine import GameEngine

def main():
    print("Welcome to Dungeon Crawler!")
    print("Explore the dungeon, defeat monsters, and find treasure!")
    print("Type 'help' for a list of commands.")
    print()
    
    # Create and start the game
    game = GameEngine()
    game.start()

if __name__ == "__main__":
    main()
