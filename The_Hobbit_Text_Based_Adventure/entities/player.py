class Player:
    def __init__(self):
        self.name = "Bilbo Baggins"
        self.current_room = None
        self.inventory = []
        self.health = 100
        self.max_health = 100
        self.add_starting_items()
        
    def add_starting_items(self):
        """Add Bilbo's starting items"""
        from items.items import Handkerchief, PocketWatch, Pipe
        
        # Items Bilbo would naturally have at the start
        self.add_to_inventory(Handkerchief())
        self.add_to_inventory(PocketWatch())
        self.add_to_inventory(Pipe())
        
    def add_to_inventory(self, item):
        """Add an item to the player's inventory"""
        self.inventory.append(item)
        
    def remove_from_inventory(self, item):
        """Remove an item from the player's inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            
    def take_damage(self, amount):
        """Take damage, reducing health"""
        self.health -= amount
        if self.health < 0:
            self.health = 0
            
    def heal(self, amount):
        """Heal the player, increasing health"""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
    
    def move(self, direction, dungeon):
        """Attempt to move the player in the given direction"""
        if self.current_room.has_exit(direction):
            next_room = self.current_room.get_exit_room(direction)
            self.current_room = next_room
            return True
        return False
    
    def is_alive(self):
        """Check if the player is still alive"""
        return self.health > 0 