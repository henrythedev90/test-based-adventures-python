from entities.player import Player
from world.dungeon import Dungeon
from items.items import Ring
import time
import threading

class GameEngine:
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = Player()
        self.is_running = False
        self.timer_running = False
        self.time_limit = 60  # 60 seconds (1 minute) per riddle
        self.has_won_riddle_challenge = False
        
    def start(self):
        """Start the game loop"""
        self.is_running = True
        
        # Place player in starting room
        starting_room = self.dungeon.get_starting_room()
        self.player.current_room = starting_room
        
        # Mark the starting room as visited
        starting_room.visited = True
        
        # Main game loop
        while self.is_running:
            # Check if this is a riddle room and hasn't been challenged yet
            current_room = self.player.current_room
            if hasattr(current_room, 'is_riddle_room') and current_room.is_riddle_room and not current_room.riddle_challenged:
                self.start_riddle_challenge()
                current_room.riddle_challenged = True
            
            # Display current room
            self.display_room()
            
            # Get player command
            command = input("> ").strip().lower()
            
            # Process command
            self.process_command(command)
    
    def display_room(self):
        """Display the current room description"""
        room = self.player.current_room
        print(f"\n{room.name}")
        print("-" * len(room.name))
        print(room.description)
        
        # Display characters in the room
        if room.characters:
            print(room.get_characters_description())
        
        # Display exits
        exits = room.get_exits()
        if exits:
            print("\nExits:", ", ".join(exits))
            
        # Display special options for Gollum's cave
        if hasattr(room, 'is_riddle_room') and room.is_riddle_room and room.riddle_challenged and not self.has_won_riddle_challenge:
            print("\nSpecial: You can type 'challenge gollum' to try the riddle challenge again.")
    
    def process_command(self, command):
        """Process the player's command"""
        if command == "quit" or command == "exit":
            self.is_running = False
            print("Thanks for playing!")
        
        elif command == "help":
            self.display_help()
        
        elif command in ["n", "north", "s", "south", "e", "east", "w", "west", "up", "down", "in", "out"]:
            self.move_player(command)
        
        elif command == "look":
            self.display_room()
            
        elif command == "map" or command == "m":
            self.display_map()
            
        elif command == "inventory" or command == "i":
            self.display_inventory()
            
        elif command.startswith("talk to ") or command.startswith("speak to ") or command.startswith("talk "):
            # Extract character name
            if command.startswith("talk to "):
                character_name = command[8:].strip()
            elif command.startswith("speak to "):
                character_name = command[9:].strip()
            else:
                character_name = command[5:].strip()
                
            self.talk_to_character(character_name)
            
        elif command.startswith("ask ") and " about " in command:
            # Format: "ask [character] about [topic]"
            parts = command[4:].split(" about ", 1)
            if len(parts) == 2:
                character_name, topic = parts
                self.ask_character_about(character_name.strip(), topic.strip())
            else:
                print("I don't understand. Try 'ask [character] about [topic]'.")
            
        elif command.startswith("use "):
            item_name = command[4:].strip()
            self.use_item(item_name)
            
        elif command == "challenge gollum" and hasattr(self.player.current_room, 'is_riddle_room') and not self.has_won_riddle_challenge:
            self.start_riddle_challenge()
        
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")
            
    def display_help(self):
        """Display the list of available commands"""
        print("\nAvailable Commands:")
        print("  north (n) - Move north")
        print("  south (s) - Move south")
        print("  east (e)  - Move east")
        print("  west (w)  - Move west")
        print("  up/down   - Move up or down where applicable")
        print("  in/out    - Enter or exit where applicable")
        print("  look      - Look around the current location")
        print("  map (m)   - Display the map of Middle-earth")
        print("  inventory (i) - Check your inventory")
        print("  talk to [character] - Speak with a character")
        print("  ask [character] about [topic] - Ask a character about something")
        print("  use [item] - Use an item from your inventory")
        
        # Add conditional help for Gollum's challenge
        if hasattr(self.player.current_room, 'is_riddle_room') and not self.has_won_riddle_challenge:
            print("  challenge gollum - Try the riddle challenge again")
            
        print("  help      - Display this help message")
        print("  quit      - Exit the game")
        
    def move_player(self, command):
        """Move the player in the given direction"""
        # Convert short direction names to full names
        direction_map = {
            "n": "north",
            "s": "south",
            "e": "east",
            "w": "west"
        }
        
        # Get the full direction name
        direction = direction_map.get(command, command)
        
        # Try to move player
        if self.player.current_room.has_exit(direction):
            next_room = self.player.current_room.get_exit_room(direction)
            self.player.current_room = next_room
            
            # Mark the room as visited
            next_room.visited = True
            
            print(f"You move {direction}.")
        else:
            print(f"You cannot go {direction} from here.")
    
    def talk_to_character(self, character_name):
        """Talk to a character in the current room"""
        room = self.player.current_room
        character = room.get_character_by_name(character_name)
        
        if character:
            print(f"\n{character.name}:")
            print(character.get_dialogue())
        else:
            print(f"There's no one called {character_name} here.")
            
    def ask_character_about(self, character_name, topic):
        """Ask a character about a specific topic"""
        room = self.player.current_room
        character = room.get_character_by_name(character_name)
        
        if not character:
            print(f"There's no one called {character_name} here.")
            return
            
        # Try to find a matching dialogue topic
        topic_key = None
        
        # Map common topics to dialogue keys
        topic_map = {
            "yourself": "greeting",
            "you": "greeting",
            "who are you": "greeting",
            "adventure": "adventure",
            "quest": "about_quest",
            "journey": "about_quest",
            "mountain": "about_quest",
            "mountains": "about_quest",
            "ring": "about_ring",
            "precious": "about_ring",
            "dwarves": "about_dwarves",
            "dwarf": "about_dwarves",
            "food": "about_food",
            "meal": "about_food",
            "song": "about_song",
            "music": "about_song",
            "map": "about_map",
            "secret": "about_map",
            "treasure": "about_treasure",
            "gold": "about_treasure",
            "animal": "about_animals",
            "animals": "about_animals",
            "forest": "about_forest",
            "mirkwood": "about_forest",
            "arkenstone": "about_arkenstone",
            "heart": "about_arkenstone"
        }
        
        # Check if the topic matches any in our map
        for key, value in topic_map.items():
            if key in topic.lower():
                topic_key = value
                break
                
        # If we found a matching topic, get the dialogue
        if topic_key and topic_key in character.dialogue:
            print(f"\n{character.name}:")
            print(character.get_dialogue(topic_key))
        else:
            print(f"\n{character.name} has nothing to say about that.")
    
    def display_map(self):
        """Display the dungeon map"""
        print("\n== Middle-earth Map ==")
        print("Legend: [X] Current Location, [O] Visited Location, [ ] Unexplored")
        print("         |   North")
        print("         v")
        
        # Get map dimensions
        min_x, min_y, width, height = self.dungeon.get_map_dimensions()
        
        # Create an empty grid filled with None
        grid = [[None for _ in range(width)] for _ in range(height)]
        
        # Place rooms in the grid
        for room in self.dungeon.rooms:
            if room.map_position:
                x, y = room.map_position
                grid_x = x - min_x
                grid_y = y - min_y
                grid[grid_y][grid_x] = room
        
        # Draw the map
        for y in range(height):
            # First line: top borders
            line = ""
            for x in range(width):
                room = grid[y][x]
                if room and (room.visited or room == self.player.current_room):
                    line += "+---"
                else:
                    line += "    "
            line += "+"
            print(line)
            
            # Second line: room symbol and connections
            line = ""
            for x in range(width):
                room = grid[y][x]
                if room and (room.visited or room == self.player.current_room):
                    # Room symbol
                    if room == self.player.current_room:
                        line += "| X "
                    else:
                        line += "| O "
                else:
                    line += "    "
            line += "|"
            print(line)
            
            # Third line: horizontal connections
            line = ""
            for x in range(width):
                room = grid[y][x]
                if room and (room.visited or room == self.player.current_room):
                    if x < width - 1 and grid[y][x+1] and "east" in room.exits and room.exits["east"] == grid[y][x+1]:
                        line += "+---"
                    else:
                        line += "+   "
                else:
                    line += "    "
            line += "+"
            print(line)
        
        print()
            
    def display_inventory(self):
        """Display the player's inventory"""
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            print("\nInventory:")
            for item in self.player.inventory:
                print(f"- {item.name}: {item.description}")
                
    def use_item(self, item_name):
        """Use an item from the player's inventory"""
        for item in self.player.inventory:
            if item.name.lower() == item_name.lower():
                if item.usable:
                    result = item.use(self.player)
                    print(result)
                else:
                    print(f"You can't use {item.name} right now.")
                return
        print(f"You don't have a {item_name} in your inventory.")
    
    def start_riddle_challenge(self):
        """Start the riddle challenge with Gollum"""
        room = self.player.current_room
        
        print("\n" + "=" * 50)
        print("Gollum approaches, his eyes gleaming in the darkness.")
        print("'We likes games, yes we do, precious! Let's play riddles!'")
        print("'If it wins, we shows it the way out. If it loses, we eats it!'")
        print("'Five riddles, one minute each, yes precious!'")
        print("=" * 50 + "\n")
        
        # Track correct answers
        correct_answers = 0
        
        # Ask each riddle
        for i, riddle in enumerate(room.riddles):
            print(f"Riddle #{i+1}: {riddle['question']}")
            print(f"You have {self.time_limit} seconds to answer...")
            
            # Start the timer
            self.timer_running = True
            timer_thread = threading.Thread(target=self.countdown_timer)
            timer_thread.daemon = True
            timer_thread.start()
            
            # Get the answer
            start_time = time.time()
            answer = input("Your answer: ").strip().lower()
            elapsed_time = time.time() - start_time
            
            # Stop the timer
            self.timer_running = False
            
            # Check if time ran out
            if elapsed_time > self.time_limit:
                print("\nTime's up! Gollum cackles with glee.")
                print("'Too slow, too slow! We wins, precious!'")
                self.player.take_damage(10)
                print(f"You lose 10 health points. Current health: {self.player.health}")
                return
            
            # Check the answer
            if answer == riddle['answer']:
                print("'Correct! Clever, clever it is!' Gollum hisses, looking disappointed.")
                correct_answers += 1
            else:
                print(f"'Wrong! The answer is {riddle['answer']}!' Gollum cackles with glee.")
        
        # Determine the outcome
        if correct_answers >= 3:  # Need to answer at least 3 correctly to win
            print("\nGollum scowls, defeated. 'It won the game, precious. We must give it a present.'")
            print("Reluctantly, Gollum reaches into a hidden pocket and pulls out a small golden ring.")
            print("'Take it! We doesn't need it anymore...' he mutters, before scurrying away into the darkness.")
            
            # Add the ring to player's inventory if they don't already have it
            has_ring = any(isinstance(item, Ring) for item in self.player.inventory)
            if not has_ring:
                self.player.add_to_inventory(Ring())
                
            # Mark the challenge as won
            self.has_won_riddle_challenge = True
        else:
            print("\nGollum laughs cruelly. 'It lost the game! Stupid, stupid!'")
            print("He lunges at you, but you manage to fend him off. He retreats into the shadows.")
            print("You feel weakened by the encounter.")
            print("You can try again by typing 'challenge gollum' when in this room.")
            
            # Player loses health
            self.player.take_damage(10)
            print(f"You lose 10 health points. Current health: {self.player.health}")
    
    def countdown_timer(self):
        """Run a countdown timer for riddles"""
        start_time = time.time()
        while self.timer_running and (time.time() - start_time < self.time_limit):
            time.sleep(0.1)  # Check every 0.1 seconds
            
        # Time's up if we're still running
        if self.timer_running:
            print("\nTime's up!")
            self.timer_running = False 