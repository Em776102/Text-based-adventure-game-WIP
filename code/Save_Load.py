import json, os
from Player import Player
from Inventory import Inventory
from Item import Item

SAVE_FILE = "Quixotic_Sonder_Save.json"

def save_game(player, current_room):
    data = {
        "player": {  # all player info goes inside "player"
            "name": player.name,
            "hp": player.hp,
            "level": getattr(player, "level", 1),  # optional if you have levels
            "xp": getattr(player, "xp", 0),       # optional if you have xp
            "gold": player.gold,
            "inventory": [item.to_dict() for item in player.inventory.items],
            "equipment": {
                slot: player.equipment[slot].to_dict() if player.equipment[slot] else None
                for slot in player.equipment
            }
        },
        "room": current_room.name  # current room
    }

    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Game saved!")
    except Exception as e:
        print(f"Failed to save game: {e}")

def load_game(world, filename="Quixotic_Sonder_Save.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        player_data = data["player"]
        room_name = data["room"]

        # --- Rebuild player ---
        from Player import Player
        from Inventory import Inventory

        player = Player(player_data["name"])
        player.hp = player_data["hp"]
        player.gold = player_data["gold"]

        # Inventory
        player.inventory.items = [Item.from_dict(i) for i in player_data["inventory"]]

        # Equipment
        player.equipment = {
            slot: Item.from_dict(i) if i else None
            for slot, i in player_data["equipment"].items()
        }

        # --- Get current room ---
        current_room = world.get(room_name)
        if not current_room:
            print(f"Warning: Room '{room_name}' not found. Starting in default room.")
            current_room = list(world.values())[0]  # fallback

        print("Game loaded successfully!")
        return player, current_room

    except FileNotFoundError:
        print("No save file found.")
        return None, None

