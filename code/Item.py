class Item:
    def __init__(self, item_id, name, item_type, **data):
        self.id = item_id
        self.name = name
        self.type = item_type   # weapon, armor, consumable, key
        self.data = data        # NBT-style data

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "data": self.data
        }

    @staticmethod
    def from_dict(d):
        return Item(d["id"], d["name"], d["type"], **d["data"])

    def __str__(self):
        return self.name
