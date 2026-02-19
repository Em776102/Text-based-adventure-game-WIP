from Item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You picked up {item.name}.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
            return

        print("Inventory:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name}")
