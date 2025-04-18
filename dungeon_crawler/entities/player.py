class Player:
    def __init__(self):
        self.name = "Adventurer"
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []
        self.current_room = None
        
    def move(self, direction, dungeon):
        """Attempt to move the player in the given direction"""
        if self.current_room.has_exit(direction):
            next_room = self.current_room.get_exit_room(direction)
            self.current_room = next_room
            return True
        return False
    
    def take_damage(self, amount):
        """Reduce player health by damage amount considering defense"""
        actual_damage = max(1, amount - self.defense)
        self.health -= actual_damage
        return actual_damage
    
    def heal(self, amount):
        """Heal the player by the given amount"""
        self.health = min(self.max_health, self.health + amount)
    
    def add_to_inventory(self, item):
        """Add an item to the player's inventory"""
        self.inventory.append(item)
        
    def is_alive(self):
        """Check if the player is still alive"""
        return self.health > 0 