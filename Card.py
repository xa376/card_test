class Card:

    def __init__(self, owner):
        self.owner = owner
        self.cost = 5
        self.damage = 10

    def activateOnTarget(self, target):
        target.hurt(self.damage)
        self.owner.mana -= self.cost
        print(f"player hit {target.name} for {self.damage}.")

    def toString(self):
        print("I AM A SIMPLE CARD")