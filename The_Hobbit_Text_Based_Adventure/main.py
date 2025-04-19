#!/usr/bin/env python3

from game.game_engine import GameEngine

def main():
    """Display the introduction to the game"""
    print("*" * 60)
    print("*" * 60)
    print("       I DO NOT OWN THE RIGHTS OF THE HOBBIT OR ANY OF THE CHARACTERS")
    print("       This is a fan who loves this story and I figure I can use")
    print("       it as a way to practice my coding skills. Happy Coding!")
    print("*" * 60)
    print("*" * 60)
    print("==================================================")
    print("  THE HOBBIT: AN UNEXPECTED JOURNEY")
    print("  A text-based adventure through Middle-earth")
    print("==================================================")
    print()
    print("In a hole in the ground there lived a hobbit.")
    print("Not a nasty, dirty, wet hole, filled with the ends of worms")
    print("and an oozy smell, nor yet a dry, bare, sandy hole with")
    print("nothing in it to sit down on or to eat: it was a hobbit-hole,")
    print("and that means comfort.")
    print()
    print("You are Bilbo Baggins, a respectable hobbit of Bag End.")
    print("Little do you know that an adventure awaits...")
    print()
    print("Type 'help' for a list of commands.")
    print()
    
    # Create and start the game
    game = GameEngine()
    game.start()

if __name__ == "__main__":
    main()
