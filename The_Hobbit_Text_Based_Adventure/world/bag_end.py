from world.room import Room

def create_bag_end():
    """Create the multiple rooms within Bag End"""
    # Create rooms within Bag End
    entrance_hall = Room("Bag End Entrance Hall", 
                       "The circular entrance hall of Bag End welcomes visitors with its warm wooden panels "
                       "and perfectly round doorway. Pegs for coats and hats line one wall, and the polished "
                       "floor gleams in the soft light.")
    
    living_room = Room("Bag End Living Room",
                     "The cozy living room centers around a cheerful fireplace with a mantle covered in "
                     "trinkets and family portraits. Comfortable armchairs and a writing desk occupy the space, "
                     "and bookshelves line the walls with maps and history books.")
    
    kitchen = Room("Bag End Kitchen",
                 "A well-stocked kitchen with bundles of herbs hanging from the ceiling, copper pots "
                 "gleaming on the shelves, and a large wooden table in the center. The pantry beyond "
                 "is filled with preserved foods, cheeses, and several barrels of fine ale.")
    
    dining_room = Room("Bag End Dining Room",
                     "An elegant dining room with a long wooden table surrounded by chairs. "
                     "The walls are adorned with decorative plates and silverware is neatly arranged "
                     "in a cabinet. This room could easily seat a dozen guests for dinner.")
    
    study = Room("Bag End Study",
               "A small but comfortable study filled with books, scrolls, and maps. "
               "A writing desk faces the window that looks out over the garden. "
               "Quills, ink pots, and parchment are neatly arranged, ready for use.")
    
    bedroom = Room("Bag End Bedroom",
                 "Sunlight streams through the round window of Bilbo's bedroom, illuminating dust motes dancing in the air. "
                 "The comfortable four-poster bed has a patchwork quilt that your mother made years ago, still rumpled from sleep. "
                 "A wardrobe filled with your finest waistcoats and trousers stands against one wall. "
                 "A small bedside table holds a water basin, a half-read book, and a candle guttered from last night's reading. "
                 "Through the window, you can see your beautiful garden and the peaceful Shire beyond. "
                 "It's going to be another perfect, uneventful day in Bag End... or so you think.")
    bedroom.is_starting_room = True  # Mark this as the starting room
    
    # Connect the rooms within Bag End
    entrance_hall.add_exit("east", living_room)
    entrance_hall.add_exit("south", dining_room)
    entrance_hall.add_exit("out", None)  # Will be connected to East Road later
    
    living_room.add_exit("west", entrance_hall)
    living_room.add_exit("north", study)
    living_room.add_exit("east", kitchen)
    living_room.add_exit("south", bedroom)
    
    kitchen.add_exit("west", living_room)
    kitchen.add_exit("south", dining_room)
    
    dining_room.add_exit("north", entrance_hall)
    dining_room.add_exit("north-east", kitchen)
    
    study.add_exit("south", living_room)
    
    bedroom.add_exit("north", living_room)
    
    # Set map positions for a zoomed-in version of Bag End
    # When in Bag End, we'll use a different map scale
    entrance_hall.map_position = (2, 2)
    entrance_hall.is_in_bag_end = True
    
    living_room.map_position = (3, 2)
    living_room.is_in_bag_end = True
    
    kitchen.map_position = (4, 2)
    kitchen.is_in_bag_end = True
    
    dining_room.map_position = (3, 3)
    dining_room.is_in_bag_end = True
    
    study.map_position = (3, 1)
    study.is_in_bag_end = True
    
    bedroom.map_position = (3, 4)
    bedroom.is_in_bag_end = True
    
    # Group all Bag End rooms
    bag_end_rooms = [entrance_hall, living_room, kitchen, dining_room, study, bedroom]
    
    # Mark all rooms as part of Bag End
    for room in bag_end_rooms:
        room.area = "Bag End"
    
    # Add hints to important rooms
    bedroom.hint = "It's a beautiful day outside. Perhaps you should get out of bed and explore your home."
    living_room.hint = "To meet Gandalf, go west to the entrance hall, then out to the East Road."
    entrance_hall.hint = "The world awaits outside your door. Try going 'out' to reach the East Road."
    
    return bag_end_rooms, entrance_hall  # Return all rooms and the entrance hall