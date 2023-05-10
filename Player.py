class Player:

    def __init__(self):
        self.health = 100
        self.mana = 40

    def hurt(self, damage):
        self.health -= damage