class Enemy:

    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.health = 20
        self.damage = 10

    def hurt(self, damage):
        self.health -= damage

    def onTurn(self):
        self.player.hurt(self.damage)
        print(f"{self.name} hit player for {self.damage} damage.")