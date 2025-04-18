from world.room import Room

class Dungeon:
    def __init__(self):
        self.rooms = []
        self.starting_room = None
        self.create_dungeon()
        
    def create_dungeon(self):
        """Create a simple dungeon with a few connected rooms"""
        # Create rooms
        entrance = Room("Dungeon Entrance", 
                       "You stand at the entrance of a dark, foreboding dungeon. " 
                       "The stone walls are damp and covered in moss. "
                       "The air is stale and smells of earth and decay.")
        
        hallway = Room("Stone Hallway", 
                      "A long, narrow hallway stretches before you. "
                      "Torches flicker on the walls, casting eerie shadows. "
                      "The floor is worn smooth from countless footsteps.")
        
        chamber = Room("Ancient Chamber", 
                      "This circular chamber appears to be some kind of ritual space. "
                      "Strange symbols are carved into the floor, and "
                      "a broken altar stands in the center.")
        
        armory = Room("Abandoned Armory", 
                     "Weapon racks line the walls of this room, though "
                     "most are empty or hold only rusted remains. "
                     "A few chests sit in the corner, their locks long broken.")
        
        crypt = Room("Forgotten Crypt", 
                    "Stone sarcophagi line the walls of this cold room. "
                    "The lids of several have been pushed aside, revealing "
                    "empty interiors. A chill permeates the air.")
        
        # Connect the rooms
        entrance.add_exit("north", hallway)
        
        hallway.add_exit("south", entrance)
        hallway.add_exit("east", armory)
        hallway.add_exit("north", chamber)
        
        chamber.add_exit("south", hallway)
        chamber.add_exit("west", crypt)
        
        armory.add_exit("west", hallway)
        
        crypt.add_exit("east", chamber)
        
        # Add rooms to dungeon
        self.rooms = [entrance, hallway, chamber, armory, crypt]
        self.starting_room = entrance
    
    def get_starting_room(self):
        """Return the starting room of the dungeon"""
        return self.starting_room 