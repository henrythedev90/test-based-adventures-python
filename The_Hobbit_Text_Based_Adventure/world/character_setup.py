from entities.character import Gandalf, Thorin, Dwarves, Gollum, Elrond, Beorn, Smaug

def place_characters_in_world(great_east_road, dining_room, rivendell_room, gollum_cave_room, beorns_house_room, treasure_room):
    """Create characters and place them in appropriate locations in Middle-earth"""
    
    # Create characters
    gandalf = Gandalf(great_east_road)  # Gandalf is outside on East Road
    thorin = Thorin(None)  # Thorin hasn't arrived yet
    dwarves = Dwarves(dining_room)  # Dwarves are already in dining room
    elrond = Elrond(rivendell_room)
    gollum = Gollum(gollum_cave_room)
    beorn = Beorn(beorns_house_room)
    smaug = Smaug(treasure_room)
    
    # Add characters to their rooms
    great_east_road.add_character(gandalf)
    # Thorin isn't placed yet - he'll arrive later
    dining_room.add_character(dwarves)
    rivendell_room.add_character(elrond)
    gollum_cave_room.add_character(gollum)
    beorns_house_room.add_character(beorn)
    treasure_room.add_character(smaug)
    
    # Return all characters for reference
    characters = [gandalf, thorin, dwarves, elrond, gollum, beorn, smaug]
    return characters

def thorin_arrival(dining_room, thorin):
    """Trigger Thorin's arrival at the dining room"""
    if thorin.location is None:
        thorin.location = dining_room
        dining_room.add_character(thorin)
        return True
    return False 