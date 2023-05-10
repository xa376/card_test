from Card import *
from Menu import *
from Player import *
from Enemy import *
from MenuOption import *

def main():

    menu = Menu()
    player = Player()
    card = Card(player)
    enemy = Enemy("ogre", player)
    menu.addOption(MenuOption("card", lambda: card.activateOnTarget(enemy))) 

    turn = 1
    while True:

        print(f"\n\nTurn {turn}:")
        print(f"YOUR HEALTH: {player.health}")
        print(f"YOUR MANA: {player.mana}")
        print(f"ENEMY HEALTH: {enemy.health}")
        for i, choice in enumerate(menu.choices):
            print(f"{i} {choice[0]}")

        userInput = input("Make a choice: ")

        if userInput.isdigit():
            menu.chooseOption(int(userInput))

        if enemy.health < 1:
            print("ENEMY DEAD")
            break

        enemy.onTurn()

        if player.health < 1:
            print("PLAYER DEAD")
            break

        turn += 1

if __name__ == "__main__":
    main()