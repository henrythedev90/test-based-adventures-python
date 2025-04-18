class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Direction: connected room
        self.items = []  # Items in the room
        self.enemies = []  # Enemies in the room
        
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