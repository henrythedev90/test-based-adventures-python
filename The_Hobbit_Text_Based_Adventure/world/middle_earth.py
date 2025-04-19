from world.room import Room
from world.bag_end import create_bag_end
from world.locations import create_middle_earth_locations
from world.character_setup import place_characters_in_world

class MiddleEarth:
    def __init__(self):
        self.locations = []
        self.hobbit_hole = None
        self.fellowship = []
        self.create_middle_earth()
        
    def create_middle_earth(self):
        """Create the world of Middle-earth"""
        # Create Bag End complex
        hobbit_holes, front_door = create_bag_end()
        
        # Create other Middle-earth locations
        middle_earth_places, great_east_road = create_middle_earth_locations()
        
        # Connect Bag End to Middle-earth
        front_door.exits["out"] = great_east_road
        great_east_road.add_exit("in", front_door)
        
        # Place characters in the world
        feast_hall = [r for r in hobbit_holes if r.name == "Bag End Dining Room"][0]
        last_homely_house = [r for r in middle_earth_places if r.name == "Rivendell"][0]
        misty_mountains = [r for r in middle_earth_places if r.name == "Underground Lake"][0]
        skin_changer_home = [r for r in middle_earth_places if r.name == "Beorn's House"][0]
        lonely_mountain = [r for r in middle_earth_places if r.name == "Dragon's Hoard"][0]
        
        self.fellowship = place_characters_in_world(
            great_east_road,  # Put Gandalf on the East Road
            feast_hall,
            last_homely_house,
            misty_mountains,
            skin_changer_home,
            lonely_mountain
        )
        
        # Combine all locations
        self.locations = hobbit_holes + middle_earth_places
        
        # Find the starting room (Bilbo's bedroom) using the is_starting_room attribute
        for room in self.locations:
            if hasattr(room, 'is_starting_room') and room.is_starting_room:
                self.hobbit_hole = room
                break
                
        # Fallback in case the starting room isn't marked
        if not self.hobbit_hole:
            self.hobbit_hole = [r for r in hobbit_holes if r.name == "Bag End Bedroom"][0]
    
    def get_starting_location(self):
        """Return the starting location of the adventure"""
        return self.hobbit_hole
        
    def get_map_dimensions(self):
        """Get the dimensions needed for the map"""
        min_x = min(location.map_position[0] for location in self.locations)
        max_x = max(location.map_position[0] for location in self.locations)
        min_y = min(location.map_position[1] for location in self.locations)
        max_y = max(location.map_position[1] for location in self.locations)
        
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        
        return min_x, min_y, width, height 