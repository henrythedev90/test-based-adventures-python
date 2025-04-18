class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.usable = False
    
    def use(self, player):
        """Use the item - to be overridden by child classes"""
        return f"You can't use the {self.name} right now."
    
    def __str__(self):
        return self.name
    

    
class Ring(Item):
    def __init__(self):
        super().__init__(
            "The Ring", 
            "A simple golden ring, cool to the touch. When you wear it, "
            "you feel a strange sensation, as if you're becoming less visible."
        )
        self.usable = True
    
    def use(self, player):
        """Use the ring to temporarily become invisible"""
        return "You slip the ring on your finger. The world seems to fade, " \
               "and you feel as though you've stepped into the realm of shadows." 