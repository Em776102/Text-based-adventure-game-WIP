from Enemy import Enemy
from Item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}
        self.enemies = []  # <-- list of enemies

    # Display room info
    def show(self):
        print(f"\nYou are in {self.name}")
        print(self.description)

        if self.items:
            print("You see:", ", ".join(self.items))
        else:
            print("There are no items here.")

        if self.exits:
            exits_list = []
            for direction, info in self.exits.items():
                if info.get("locked", False):
                    exits_list.append(f"{direction} (locked)")
                else:
                    exits_list.append(direction)
            print("Exits:", ", ".join(exits_list))
        else:
            print("There are no exits.")

        if self.enemies:
            alive_enemies = [e.name for e in self.enemies if e.is_alive()]
            if alive_enemies:
                print("Enemies here:", ", ".join(alive_enemies))
            else:
                print("All enemies defeated here.")

    # Add an exit
    def add_exit(self, direction, room_name, locked=False, key=None):
        self.exits[direction] = {"room": room_name, "locked": locked, "key": key}

    # Remove an item
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    # Add a single enemy
    def add_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)
