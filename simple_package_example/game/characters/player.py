class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, enemy):
        enemy.health -= 10  # Simple attack logic