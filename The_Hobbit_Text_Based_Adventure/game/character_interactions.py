def talk_to_character(player, character_name):
    """Talk to a character in the current room"""
    room = player.current_room
    character = room.get_character_by_name(character_name)
    
    if character:
        print(f"\n{character.name}:")
        print(character.get_dialogue())
    else:
        print(f"There's no one called {character_name} here.")
        
def ask_character_about(player, character_name, topic):
    """Ask a character about a specific topic"""
    room = player.current_room
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