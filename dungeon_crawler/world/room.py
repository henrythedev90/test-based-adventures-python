class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Direction: connected room
        self.items = []  # Items in the room
        self.enemies = []  # Enemies in the room
        self.characters = []  # Characters in the room
        self.visited = False  # Track if player has visited this room
        self.map_position = None  # Used for map display (x, y) coordinates
        
    def add_exit(self, direction, room):
        """Add an exit to another room"""
        self.exits[direction] = room
        
    def get_exit_room(self, direction):
        """Get the room in the given direction"""
        return self.exits.get(direction)
        
    def has_exit(self, direction):
        """Check if the room has an exit in the given direction"""
        return direction in self.exits
        
    def get_exits(self):
        """Get a list of available exit directions"""
        return list(self.exits.keys())
    
    def add_item(self, item):
        """Add an item to the room"""
        self.items.append(item)
        
    def remove_item(self, item):
        """Remove an item from the room"""
        if item in self.items:
            self.items.remove(item)
            
    def add_enemy(self, enemy):
        """Add an enemy to the room"""
        self.enemies.append(enemy)
        
    def remove_enemy(self, enemy):
        """Remove an enemy from the room"""
        if enemy in self.enemies:
            self.enemies.remove(enemy)
            
    def add_character(self, character):
        """Add a character to the room"""
        self.characters.append(character)
        if character.location is None:
            character.location = self
            
    def remove_character(self, character):
        """Remove a character from the room"""
        if character in self.characters:
            self.characters.remove(character)
            
    def get_character_by_name(self, name):
        """Find a character in the room by name"""
        name = name.lower()
        for character in self.characters:
            if character.name.lower() == name or name in character.name.lower():
                return character
        return None
        
    def get_characters_description(self):
        """Get a description of characters in the room"""
        if not self.characters:
            return ""
            
        if len(self.characters) == 1:
            return f"\n{self.characters[0].name} is here. {self.characters[0].description}"
            
        description = "\nPresent here are:"
        for character in self.characters:
            description += f"\n- {character.name}: {character.description}"
            
        return description 