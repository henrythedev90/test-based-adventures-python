from entities.player import Player
from world.dungeon import Dungeon

class GameEngine:
    def __init__(self):
        self.dungeon = Dungeon()
        self.player = Player()
        self.is_running = False
        
    def start(self):
        """Start the game loop"""
        self.is_running = True
        
        # Place player in starting room
        starting_room = self.dungeon.get_starting_room()
        self.player.current_room = starting_room
        
        # Main game loop
        while self.is_running:
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
        
        # Display exits
        exits = room.get_exits()
        if exits:
            print("\nExits:", ", ".join(exits))
    
    def process_command(self, command):
        """Process the player's command"""
        if command == "quit" or command == "exit":
            self.is_running = False
            print("Thanks for playing!")
        
        elif command == "help":
            self.display_help()
        
        elif command in ["n", "north", "s", "south", "e", "east", "w", "west"]:
            self.move_player(command)
        
        elif command == "look":
            self.display_room()
        
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")
            
    def display_help(self):
        """Display the list of available commands"""
        print("\nAvailable Commands:")
        print("  north (n) - Move north")
        print("  south (s) - Move south")
        print("  east (e)  - Move east")
        print("  west (w)  - Move west")
        print("  look      - Look around the current room")
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
            print(f"You move {direction}.")
        else:
            print(f"You cannot go {direction} from here.") 