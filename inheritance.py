
#Inheritance

class Character:
    def __init__(self):
        self.health = 100

class Blacksmith(Character):
    def __init__(self):
        super(Blacksmith, self).__init__()

bs = Blacksmith()
print bs.health
