import random
from Item import Item

class Enemy:
    def __init__(self, name, hp, attack, defense, gold, loot):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.loot = loot if loot else []
    
    def is_alive(self):
        return self.hp > 0

    def deal_damage(self):
        return random.randint(self.attack - 2, self.attack + 2)
