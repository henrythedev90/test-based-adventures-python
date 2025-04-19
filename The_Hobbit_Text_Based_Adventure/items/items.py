class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.usable = False
    
    def use(self, player):
        """Use the item - to be overridden by child classes"""
        return f"You cannot use the {self.name} right now."
    
    def __str__(self):
        return self.name
    

    
class Ring(Item):
    def __init__(self):
        super().__init__(
            "Golden Ring", 
            "A plain golden ring that seems to whisper to you. It has strange markings that appear when heated."
        )
        self.usable = True
        self.is_worn = False
    
    def use(self, player):
        if not self.is_worn:
            self.is_worn = True
            return "You slip the ring onto your finger and suddenly become invisible!"
        else:
            self.is_worn = False
            return "You remove the ring from your finger and become visible again."

class Handkerchief(Item):
    def __init__(self):
        super().__init__(
            "Handkerchief", 
            "A fine embroidered handkerchief with your initials 'BB' in one corner. A hobbit never leaves home without one!"
        )
        self.usable = True
        
    def use(self, player):
        return "You pull out your handkerchief and dab your forehead. Very proper indeed!"

class PocketWatch(Item):
    def __init__(self):
        super().__init__(
            "Pocket Watch", 
            "A polished silver pocket watch that belonged to your father. It keeps excellent time."
        )
        self.usable = True
        
    def use(self, player):
        import time
        current_time = time.strftime("%I:%M %p", time.localtime())
        return f"You check your pocket watch. It's {current_time}. Perfect time for a second breakfast!"

class Pipe(Item):
    def __init__(self):
        super().__init__(
            "Wooden Pipe", 
            "Your favorite wooden pipe, carved with intricate designs. Perfect for smoking Old Toby leaf after meals."
        )
        self.usable = True
        self.is_lit = False
        
    def use(self, player):
        if not self.is_lit:
            self.is_lit = True
            return "You light your pipe and take a few puffs, blowing a perfect smoke ring. How relaxing!"
        else:
            self.is_lit = False
            return "You tap out your pipe and put it away." 