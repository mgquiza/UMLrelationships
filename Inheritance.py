class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
    def use_magic(self, amount):
        self.mp -= amount

class Soul(Character):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp, mp)
        self.modified_mp = 1.9
    def use_magic(self, amount):
       modified_mp = amount - self.modified_mp
       super().use_magic(modified_mp)

Soul = Soul("Frisk", 120, 200)
print (f'inital mp: {Soul.mp}')
Soul.use_magic(50)
print (f'mp after magic: {Soul.mp}')
