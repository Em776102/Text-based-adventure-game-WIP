import random
from Player import Player
from Enemy import Enemy
from Item import Item
from Utility import clear

def battle(player, enemy):
    print(f"\nA {enemy.name} appears!")
    
    while player.is_alive() and enemy.is_alive():
        print("\n--- Battle ---")
        print(f"{player.name} HP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")

        choice = input("\n(a)ttack  (r)un: ").lower()

        # Player turn
        if choice == "a":
            damage = max(1, player.attack_power() - enemy.defense + random.randint(-1, 2))
            enemy.hp -= damage
            print(f"You deal {damage} damage to the {enemy.name}.")

        elif choice == "r":
            if random.random() < 0.5:
                print("You successfully escaped!")
                return "escaped"
            else:
                print("You failed to escape!")

        else:
            print("Invalid action.")
            continue

        # Enemy turn
        if enemy.is_alive():
            damage = max(1, enemy.deal_damage() - player.defense_power())
            player.hp -= damage
            print(f"The {enemy.name} hits you for {damage} damage.")

    if player.is_alive():
        print(f"\nYou defeated the {enemy.name}!")
        current_room.show()
        return "victory"
    else:
        print("\nYou were defeated...")
        return "defeat"
