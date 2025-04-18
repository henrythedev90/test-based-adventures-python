class Character:
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location
        self.dialogue = {}
        self.quest = None
        self.has_met_player = False
    
    def add_dialogue(self, key, text):
        """Add a dialogue option for this character"""
        self.dialogue[key] = text
    
    def get_dialogue(self, key="greeting"):
        """Get a specific dialogue from this character"""
        if not self.has_met_player and "first_meeting" in self.dialogue:
            self.has_met_player = True
            return self.dialogue["first_meeting"]
        return self.dialogue.get(key, "The character doesn't respond.")
    
    def set_quest(self, quest):
        """Assign a quest to this character"""
        self.quest = quest
    
    def __str__(self):
        return self.name


class Gandalf(Character):
    def __init__(self, location=None):
        super().__init__(
            "Gandalf the Grey",
            "A tall wizard with a long grey beard, pointed hat, and staff. His eyes twinkle with wisdom and mischief.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"Good morning!\" says Gandalf. \"What do you mean? Do you wish me a good morning, "
            "or mean that it is a good morning whether I want it or not; or that you feel good this morning; "
            "or that it is a morning to be good on?\""
        )
        self.add_dialogue("greeting", 
            "\"You'll have a tale or two to tell when you come back,\" says Gandalf with a knowing smile."
        )
        self.add_dialogue("adventure", 
            "\"I am looking for someone to share in an adventure that I am arranging, "
            "and it's very difficult to find anyone.\" Gandalf's eyes twinkle with amusement."
        )
        self.add_dialogue("about_dwarves", 
            "\"They are coming to tea this afternoon. Expect them around four. "
            "Oh, and there might be... a few more than you'd expect.\""
        )
        self.add_dialogue("about_ring", 
            "Gandalf's expression grows serious. \"A ring, you say? Keep it secret. Keep it safe. "
            "There are many magic rings in this world, and none of them should be used lightly.\""
        )


class Thorin(Character):
    def __init__(self, location=None):
        super().__init__(
            "Thorin Oakenshield",
            "A proud dwarf with a long dark beard streaked with silver. He carries himself with regal bearing.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"So this is the Hobbit,\" says Thorin with barely concealed skepticism. "
            "\"Tell me, Mr. Baggins, have you done much fighting? Axe or sword, what's your weapon of choice?\""
        )
        self.add_dialogue("greeting", 
            "Thorin nods curtly in your direction. \"Burglar,\" he acknowledges."
        )
        self.add_dialogue("about_quest", 
            "\"We journey to the Lonely Mountain to reclaim our homeland and treasure from the dragon Smaug. "
            "It will be dangerous, but the reward... the reward will be beyond measure.\""
        )
        self.add_dialogue("about_arkenstone", 
            "Thorin's eyes gleam with intensity. \"The Arkenstone... the Heart of the Mountain. "
            "It is a gem like no other. Find it for me, burglar, and you will be richly rewarded.\""
        )


class Dwarves(Character):
    def __init__(self, location=None):
        super().__init__(
            "The Dwarves",
            "A rowdy group of dwarves - Fili, Kili, Dwalin, Balin, Oin, Gloin, Dori, Nori, Ori, Bifur, Bofur, and Bombur. "
            "They're loud, hungry, and eager for adventure.",
            location
        )
        self.add_dialogue("first_meeting", 
            "The dwarves bustle around your home, raiding your pantry and singing raucously. "
            "\"That's what Bilbo Baggins hates!\" they finish with a flourish, laughing uproariously."
        )
        self.add_dialogue("greeting", 
            "The dwarves greet you with a mix of nods, winks, and friendly slaps on the back."
        )
        self.add_dialogue("about_food", 
            "\"Any more food in this place?\" asks Bombur hopefully, patting his enormous belly."
        )
        self.add_dialogue("about_song", 
            "The dwarves break into a deep, haunting melody:\n\n"
            "\"Far over the misty mountains cold\n"
            "To dungeons deep and caverns old\n"
            "We must away ere break of day\n"
            "To seek the pale enchanted gold.\""
        )


class Gollum(Character):
    def __init__(self, location=None):
        super().__init__(
            "Gollum",
            "A pale, skeletal creature with large, luminous eyes. He speaks to himself, referring to 'my precious'.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"What is it, precious? What is it?\" hisses the creature. \"Is it tasty? Is it scrumptious? "
            "Is it crunchable?\" His eyes gleam hungrily in the dark."
        )
        self.add_dialogue("greeting", 
            "\"Thief! Baggins! We hates it forever!\" Gollum screeches, his eyes burning with malice."
        )
        self.add_dialogue("about_ring", 
            "\"My precious! Lost! Curse the Baggins, we hates it! Stole our birthday present, "
            "the thieves, the filthy little thieves!\" Gollum wails in anguish."
        )


class Elrond(Character):
    def __init__(self, location=None):
        super().__init__(
            "Lord Elrond",
            "A noble Elf-lord with ageless features and an air of ancient wisdom. He is both wise and kind.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"Welcome to Rivendell, Bilbo Baggins,\" says Elrond with a gracious smile. "
            "\"You are not the first hobbit I have seen, nor will you be the last. The road goes ever on.\""
        )
        self.add_dialogue("greeting", 
            "Elrond inclines his head slightly. \"Mae govannen, Master Baggins.\""
        )
        self.add_dialogue("about_map", 
            "Elrond studies the map carefully. \"Moon-letters,\" he says. \"These can only be read by the light "
            "of a moon of the same shape and season as the day they were written. The secrets of how to enter "
            "the mountain lie here, hidden to all but those who know how to find them.\""
        )


class Beorn(Character):
    def __init__(self, location=None):
        super().__init__(
            "Beorn",
            "An enormous man with wild black hair and beard. His arms are thick as tree trunks, and there's something... animal about him.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"Little bunny is getting nice and fat again on bread and honey,\" "
            "rumbles Beorn with a laugh that sounds half like a growl."
        )
        self.add_dialogue("greeting", 
            "Beorn nods gruffly in your direction, busy tending to his animals."
        )
        self.add_dialogue("about_animals", 
            "\"They are my friends,\" says Beorn, gently stroking a massive honeybee. \"They understand me, "
            "and I understand them. Better company than most who call themselves people, I find.\""
        )
        self.add_dialogue("about_forest", 
            "\"Do not stray from the path,\" warns Beorn seriously. \"Mirkwood is not like other forests. "
            "It's old, very old. Full of memory... and malice. The things that moved there once are now awake. "
            "Dark things.\""
        )


class Smaug(Character):
    def __init__(self, location=None):
        super().__init__(
            "Smaug",
            "A massive dragon with red-gold scales and gleaming yellow eyes. His long body is curled around mountains of treasure.",
            location
        )
        self.add_dialogue("first_meeting", 
            "\"Well, thief! I smell you and I feel your air. I hear your breath. Come along! "
            "Help yourself, there is plenty and to spare!\" The dragon's voice is a deep rumble that shakes the very mountain."
        )
        self.add_dialogue("greeting", 
            "Smaug's eye opens lazily, focusing on you with terrifying intelligence."
        )
        self.add_dialogue("about_treasure", 
            "\"This is MY treasure, MY hoard, accumulated over centuries. Every piece is known to me. "
            "Every coin, every gem, every trinket. I know when even the tiniest piece is... missing.\" "
            "Smaug's voice drops to a dangerous purr."
        )
        self.add_dialogue("taunt", 
            "\"You think flattery will keep you alive? I am Smaug the Magnificent, Smaug the Terrible! "
            "My armor is like ten shields, my teeth are swords, my claws spears, the shock of my tail a thunderbolt, "
            "my wings a hurricane, and my breath death!\""
        ) 