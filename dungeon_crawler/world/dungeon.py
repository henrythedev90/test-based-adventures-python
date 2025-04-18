from world.room import Room
from entities.character import Gandalf, Thorin, Dwarves, Gollum, Elrond, Beorn, Smaug

class Dungeon:
    def __init__(self):
        self.rooms = []
        self.starting_room = None
        self.characters = []
        self.create_dungeon()
        
    def create_dungeon(self):
        """Create a world based on The Hobbit's journey"""
        # Create rooms based on locations from The Hobbit
        bag_end = Room("Bag End", 
                     "You stand in the cozy, circular entrance hall of Bag End. "
                     "A warm fire crackles in the hearth, and the smell of fresh-baked "
                     "scones wafts from the kitchen. A perfectly respectable hobbit-hole, "
                     "with perfectly circular doors and windows.")
        
        east_road = Room("The East Road", 
                      "The well-traveled East Road stretches before you. "
                      "Rolling green hills of the Shire surround you on all sides. "
                      "In the distance, you can see smoke rising from hobbit chimneys.")
        
        trollshaws = Room("Trollshaws", 
                     "A dark, foreboding forest stretches around you. "
                     "Something smells foul in the air, and you notice a flickering light "
                     "between the trees - perhaps a campfire? You hear gruff voices arguing.")
        
        rivendell = Room("Rivendell", 
                      "The Last Homely House east of the sea unfolds before you. "
                      "Beautiful elven architecture blends with the natural cliffs and waterfalls. "
                      "The air feels clean and refreshing, and elven songs can be heard in the distance.")
        
        misty_mountains = Room("Misty Mountains Pass", 
                            "A narrow, treacherous mountain path winds its way through "
                            "the towering peaks of the Misty Mountains. The wind howls fiercely, "
                            "and far below you can see sharp rocks and certain death.")
        
        gollum_cave = Room("Underground Lake", 
                         "A vast underground cavern stretches before you, with a dark lake "
                         "in its center. The water is black and still as glass. "
                         "On a small rocky island, you spot a pale, skeletal creature "
                         "hunched over, muttering to itself. Its large eyes gleam in the darkness.")
        
        goblin_tunnels = Room("Goblin Tunnels", 
                           "Winding, cramped tunnels carved roughly into the mountain. "
                           "The air is stale and foul. Crude drawings and markings cover the walls, "
                           "and you can hear screeching and cackling in the distance.")
        
        beorns_house = Room("Beorn's House", 
                          "A large wooden hall built from massive oak logs. "
                          "Animal carvings adorn every surface, and large bees buzz lazily through the air. "
                          "The owner is nowhere to be seen, but the great table is laden with honey, cream, and bread.")
        
        mirkwood = Room("Mirkwood Forest", 
                      "Ancient, twisted trees block out the sun in this dark forest. "
                      "The air feels heavy and enchanted, making your head swim. "
                      "Spider webs cling to the branches, some alarmingly large.")
        
        laketown = Room("Laketown", 
                       "A town built entirely on wooden platforms over a vast lake. "
                       "Boats and barges move between the buildings, which rise up from the water "
                       "on thick wooden pillars. Fish are hung to dry from every available surface.")
        
        lonely_mountain = Room("Lonely Mountain", 
                             "The imposing entrance to the Lonely Mountain looms before you. "
                             "Ancient dwarvish runes are carved into the stone gate. "
                             "From within, you detect a faint smell of smoke and... dragon.")
        
        treasure_room = Room("Dragon's Hoard", 
                           "Mountains of gold coins, precious gems, and ancient artifacts "
                           "fill this vast chamber. The treasure of Erebor glitters in the dim light. "
                           "At the center of it all, a massive dragon lies curled around a particularly "
                           "large pile of gold.")
        
        # Set map positions
        # Layout is organized roughly west to east, following the journey
        bag_end.map_position = (1, 3)
        east_road.map_position = (2, 3)
        trollshaws.map_position = (3, 3)
        rivendell.map_position = (4, 3)
        misty_mountains.map_position = (5, 3)
        goblin_tunnels.map_position = (5, 2)
        gollum_cave.map_position = (5, 1)
        beorns_house.map_position = (6, 3)
        mirkwood.map_position = (7, 3)
        laketown.map_position = (8, 3)
        lonely_mountain.map_position = (9, 3)
        treasure_room.map_position = (9, 2)
        
        # Connect the rooms (west to east journey)
        bag_end.add_exit("east", east_road)
        
        east_road.add_exit("west", bag_end)
        east_road.add_exit("east", trollshaws)
        
        trollshaws.add_exit("west", east_road)
        trollshaws.add_exit("east", rivendell)
        
        rivendell.add_exit("west", trollshaws)
        rivendell.add_exit("east", misty_mountains)
        
        misty_mountains.add_exit("west", rivendell)
        misty_mountains.add_exit("east", beorns_house)
        misty_mountains.add_exit("down", goblin_tunnels)
        
        goblin_tunnels.add_exit("up", misty_mountains)
        goblin_tunnels.add_exit("down", gollum_cave)
        
        gollum_cave.add_exit("up", goblin_tunnels)
        
        beorns_house.add_exit("west", misty_mountains)
        beorns_house.add_exit("east", mirkwood)
        
        mirkwood.add_exit("west", beorns_house)
        mirkwood.add_exit("east", laketown)
        
        laketown.add_exit("west", mirkwood)
        laketown.add_exit("east", lonely_mountain)
        
        lonely_mountain.add_exit("west", laketown)
        lonely_mountain.add_exit("in", treasure_room)
        
        treasure_room.add_exit("out", lonely_mountain)
        
        # Create characters and place them in appropriate locations
        gandalf = Gandalf(bag_end)
        thorin = Thorin(bag_end)
        dwarves = Dwarves(bag_end)
        elrond = Elrond(rivendell)
        gollum = Gollum(gollum_cave)
        beorn = Beorn(beorns_house)
        smaug = Smaug(treasure_room)
        
        # Add characters to their rooms
        bag_end.add_character(gandalf)
        bag_end.add_character(thorin)
        bag_end.add_character(dwarves)
        rivendell.add_character(elrond)
        gollum_cave.add_character(gollum)
        beorns_house.add_character(beorn)
        treasure_room.add_character(smaug)
        
        # Store characters for later reference
        self.characters = [gandalf, thorin, dwarves, elrond, gollum, beorn, smaug]
        
        # Add custom properties for Gollum's room
        gollum_cave.is_riddle_room = True
        gollum_cave.riddle_challenged = False
        gollum_cave.riddles = [
            {
                "question": "What has roots as nobody sees, is taller than trees, up, up it goes, and yet never grows?",
                "answer": "mountain"
            },
            {
                "question": "Thirty white horses on a red hill, first they champ, then they stamp, then they stand still.",
                "answer": "teeth"
            },
            {
                "question": "Voiceless it cries, wingless flutters, toothless bites, mouthless mutters.",
                "answer": "wind"
            },
            {
                "question": "An eye in a blue face saw an eye in a green face. 'That eye is like to this eye' said the first eye, 'but in low place, not in high place.'",
                "answer": "sun"
            },
            {
                "question": "This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down.",
                "answer": "time"
            }
        ]
        
        # Add rooms to dungeon
        self.rooms = [bag_end, east_road, trollshaws, rivendell, misty_mountains, 
                     goblin_tunnels, gollum_cave, beorns_house, mirkwood, 
                     laketown, lonely_mountain, treasure_room]
        self.starting_room = bag_end
    
    def get_starting_room(self):
        """Return the starting room of the dungeon"""
        return self.starting_room
        
    def get_map_dimensions(self):
        """Get the dimensions needed for the map"""
        min_x = min(room.map_position[0] for room in self.rooms)
        max_x = max(room.map_position[0] for room in self.rooms)
        min_y = min(room.map_position[1] for room in self.rooms)
        max_y = max(room.map_position[1] for room in self.rooms)
        
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        
        return min_x, min_y, width, height 