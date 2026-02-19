from Inventory import Inventory
from Item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.base_attack = 6
        self.base_defense = 3
        self.level = 1
        self.inventory = Inventory()
        self.xp = 0
        self.gold = 0
        self.equipment = {"weapon": None, "armor": None}

    def is_alive(self):
        return self.hp > 0

    def show_stats(self):
        weapon = self.equipment["weapon"]
        armor = self.equipment["armor"]

        print(f"HP: {self.hp}")
        print(f"Gold: {self.gold}")
        print(f"Weapon: {weapon.name if weapon else 'None'}")
        print(f"Armor: {armor.name if armor else 'None'}")

    def attack_power(self):
        dmg = self.base_attack
        if self.equipment["weapon"]:
            dmg += self.equipment["weapon"].data.get("damage", 0)
        return dmg

    def defense_power(self):
        defense = self.base_defense
        if self.equipment["armor"]:
            defense += self.equipment["armor"].data.get("defense", 0)
        return defense
