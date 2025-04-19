from entities.player import Player
from world.middle_earth import MiddleEarth
from items.items import Ring
from game.map_display import display_map
from game.character_interactions import talk_to_character, ask_character_about
from world.character_setup import thorin_arrival
import time
import threading

class GameEngine:
    def __init__(self):
        self.middle_earth = MiddleEarth()
        self.player = Player()
        self.is_running = False
        self.timer_running = False
        self.time_limit = 60  # 60 seconds (1 minute) per riddle
        self.has_won_riddle_challenge = False
        self.has_met_dwarves = False
        self.thorin_has_arrived = False
        
    def display_introduction(self):
        # Wait for player to press Enter to continue
        input("\nPress Enter to begin your adventure...")
        
    def start(self):
        """Start the game loop"""
        self.is_running = True
        
        # Display introduction
        self.display_introduction()
        
        # Place player in starting room
        starting_room = self.middle_earth.get_starting_location()
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
            
            # Check for special story events
            self.check_story_events()
            
            # Display current room
            self.display_room()
            
            # Get player command
            command = input("> ").strip().lower()
            
            # Process command
            self.process_command(command)
    
    def check_story_events(self):
        """Check for and trigger story events based on the player's actions"""
        current_room = self.player.current_room
        
        # Check if player has met the dwarves in dining room
        dining_room = None
        for room in self.middle_earth.locations:
            if room.name == "Bag End Dining Room":
                dining_room = room
                break
                
        if dining_room and current_room == dining_room:
            # Check for characters
            for character in current_room.characters:
                if character.name == "The Dwarves" and not self.has_met_dwarves:
                    self.has_met_dwarves = True
                    print("\n" + "=" * 50)
                    print("As you enter the dining room, you find it filled with dwarves!")
                    print("They're raiding your pantry, eating your food, and singing loudly.")
                    print("=" * 50)
                    
                    # Schedule Thorin's arrival after meeting the dwarves
                    if not self.thorin_has_arrived:
                        self.schedule_thorin_arrival(dining_room)
    
    def schedule_thorin_arrival(self, dining_room):
        """Schedule Thorin's arrival after a delay"""
        # We'll use a timer to make Thorin arrive after a few turns
        self.thorin_arrival_timer = threading.Timer(60.0, self.make_thorin_arrive, args=[dining_room])
        self.thorin_arrival_timer.daemon = True
        self.thorin_arrival_timer.start()
    
    def make_thorin_arrive(self, dining_room):
        """Make Thorin arrive at the dining room"""
        if not self.thorin_has_arrived:
            # Find Thorin in the characters list
            thorin = None
            for character in self.middle_earth.fellowship:
                if character.name == "Thorin Oakenshield":
                    thorin = character
                    break
                    
            if thorin and thorin_arrival(dining_room, thorin):
                self.thorin_has_arrived = True
                
                # If player is in the dining room, announce Thorin's arrival
                if self.player.current_room == dining_room:
                    print("\n" + "=" * 50)
                    print("There's a loud, commanding knock at the door.")
                    print("The dwarves fall silent. \"He is here,\" Gandalf says solemnly.")
                    print("Thorin Oakenshield, the leader of the dwarven company, has arrived.")
                    print("=" * 50)
    
    def display_room(self):
        """Display the current room description"""
        room = self.player.current_room
        
        # Show area information if the room is part of a larger area
        if room.area:
            print(f"\n{room.area} - {room.name}")
            print("-" * (len(room.area) + len(room.name) + 3))
        else:
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
            
        # Indicate if a hint is available
        if room.hint:
            print("\n(Type 'help' to see a hint for this location)")
            
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
            display_map(self.player, self.middle_earth)
            
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
                
            talk_to_character(self.player, character_name)
            
        elif command.startswith("ask ") and " about " in command:
            # Format: "ask [character] about [topic]"
            parts = command[4:].split(" about ", 1)
            if len(parts) == 2:
                character_name, topic = parts
                ask_character_about(self.player, character_name.strip(), topic.strip())
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
        
        # Display room hint if available
        current_room = self.player.current_room
        if current_room.hint:
            print("!" * 50)
            print(f"\nHINT!: {current_room.hint}")
            print("!" * 50)
        
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
            
            # Mark the location as visited
            next_room.visited = True
            
            print(f"You move {direction}.")
        else:
            print(f"You cannot go {direction} from here.")
            
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