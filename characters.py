class Char:
    def __init__(self, name, health, muscle, dodge, luck):
        self.name = name
        self.health = health
        self.muscle = muscle
        self.dodge = dodge
        self.luck = luck
        self.maxHealth = health

    def __str__(self):
        s = self
        return "Class: {} \n" \
               "Health: {}/{}\n" \
               "Strength: {}\n" \
               "Dodge: {}\n".format(s.name, s.health, s.maxHealth, s.muscle, s.dodge)

    def enemy(self):
        s = self
        return "Enemy Type: {} \n" \
               "Health: {}\n" \
               "Strength: {}\n" \
               "Dodge: {}\n".format(s.name, s.health, s.muscle, s.dodge)



theHero = Char("The Hero", 24, 7, 4, 3)
bell = Char("Argonaut", 16, 3, 12, 5)
zelda = Char("Link?", 13, 4, 8, 8)

# Enemies

slime = Char("Slime", 6, 3, 9, 6)
minotaur = Char("Minotaur", 10, 10, 0, 1)
whiteRabbit = Char("White Rabbit", 5, 2, 10, 10)
dragon = Char("Dragon", 20, 10, 0, 2)
golem = Char("Golem", 15, 8, 0, 4)
hero = Char("A Hero", 12, 4, 3, 2)
mimic = Char("Mimic", 13, 6, 6, 6)
rimuru = Char("True Slime", 20, 20, 20, 20)
greg = Char("Dungeon Master", 30, 20, 10, 0)