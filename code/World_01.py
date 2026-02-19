from Room import Room
from Enemy import Enemy
from Item import Item

class World_01:
    def __init__(self):
        self.rooms = {}

        self.well = Room("Well", "A deep, 25-foot hole lined with random stone, unpolished and soaked, with a tunnel facing north.")
        self.tunnel = Room("Tunnel", "An old, makeshift tunnel that almost looks like a passageway to a nuclear bunker.")
        self.dungeon = Room("Dungeon", "A damp room covered in stone just like the well; there is an old, rotting door with metal crimpings to the sides of the door, almost as decoration. And there are moldy wooden chests presumably empty of spider infestations.")
        self.droom1 = Room("Dungeon Room 1", "Same as the last room but desolate and empty. There a door, similar to the last, to your right and in front of you. The one to your right seems locked...")
        self.droom2 = Room("Dungeon Room 2", "Same as last time, an old, decrepit, stone room; but there's a spider in front of you!")
        self.droom3 = Room("Dungeon Room 3", "You find yourself infront of two greem slimes in the same exact kind of room, honestly you dont need this kind of dialogue; you already know what it looks like.")
        self.droom4 = Room("Dungeon Room 4", "Theres a dumb looking skeleton infront of you; nevermind, get over with it.")
        self.droom5 = Room("Dungeon Room 5", "You walk in ready to defeat anything, when the air infront of you starts to crack and shatters as a dragon flies through!")
        
        # Exits stored as room names (strings)
        self.well.add_exit("north", "Tunnel")
        self.tunnel.add_exit("north", "Dungeon")
        self.tunnel.add_exit("south", "Well")
        self.dungeon.add_exit("south", "Tunnel")
        self.dungeon.add_exit("east", "Dungeon Room 1")
        self.droom1.add_exit("west", "Dungeon")
        self.droom1.add_exit("north", "Dungeon Room 2")
        self.droom1.add_exit("east", "Dungeon Room 3", locked=True, key="Wooden Key")
        self.droom2.add_exit("south", "Dungeon Room 1")
        self.droom3.add_exit("west", "Dungeon Room 1")
        self.droom3.add_exit("east", "Dungeon Room 4")
        self.droom4.add_exit("west", "Dungeon Room 3")
        self.droom4.add_exit("north", "Dungeon Room 5", locked=True, key="Silver Key")
        self.droom5.add_exit("south", "Dungeon Room 4")
        
        # Register rooms
        self.register(self.well)
        self.register(self.tunnel)
        self.register(self.dungeon)
        self.register(self.droom1)
        self.register(self.droom2)
        self.register(self.droom3)
        self.register(self.droom4)
        self.register(self.droom5)
        
        #Enemies Loot
        spider_loot = [Item("spider_eye", "Spider Eye", "consumable")]
        slime_loot = [Item("slime_gel", "Slime Gel", "consumable")]
        skeleton_loot =[Item("bone", "Bone", "weapon")]
        dragon_loot = [Item("dragon_scale", "Dragon Scale", "armor")]
        #Enemies
        spider = Enemy("Spider", hp=6, attack=2, defense=3, gold=2, loot=spider_loot)
        slime = Enemy("Slime", hp=4, attack=3, defense=0, gold=3, loot=slime_loot)
        skeleton = Enemy("Skeleton", hp=10, attack=6, defense=2, gold=10, loot=skeleton_loot)
        dragon = Enemy("Dragon", hp=30, attack=10, defense=10, gold=50, loot=dragon_loot)
        
        #Enemy to room asignment
        
        self.droom2.add_enemy(spider)
        self.droom3.add_enemy(slime)
        self.droom3.add_enemy(slime)
        self.droom4.add_enemy(skeleton)
        self.droom5.add_enemy(dragon)
        
    def register(self, room):
        self.rooms[room.name] = room

    def get(self, room_name):
        # make case-insensitive
        return self.rooms.get(room_name)
