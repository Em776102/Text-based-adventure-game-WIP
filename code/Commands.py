from Utility import clear
from Dev_Mode import dev_mode
from Save_Load import save_game
from Battle import battle
from Item import Item

direction_map = {"w": "north", "s": "south", "a": "west", "d": "east"}

def handle_command(command, player, current_room, world):
    clear()

    if not command:
        return current_room

    action = command[0].lower()

    # =====================
    # Quit
    # =====================
    if action == "q":
        confirm = input("Do you want to save before quitting? (y/n) ").lower()
        from Save_Load import save_game

        if confirm == "y":
            save_game(player, current_room)
            print("Game saved. Goodbye!")
            exit()
        elif confirm == "n":
            print("Goodbye!")
            exit()
        else:
            print("Quit canceled.")
            return current_room

    # =====================
    # Look
    # =====================
    elif action == "l":
        current_room.show()

    # =====================
    # Inventory
    # =====================
    elif action == "i":
        player.inventory.show_inventory()

    # =====================
    # Take Item
    # =====================
    elif action == "t":
        if len(command) > 1:
            item = command[1]
            if item in current_room.items:
                player.inventory.add_item(item)
                current_room.remove_item(item)
            else:
                print(f"There is no {item} here.")
        else:
            print("Take what?")

    # =====================
    # Movement (WASD)
    # =====================
    elif action in direction_map:
        direction = direction_map[action]
        exit_info = current_room.exits.get(direction)

        if not exit_info:
            print("You can't go that way.")
            return current_room

        # --- Locked exit check ---
        if exit_info.get("locked", False):
            key_required = exit_info.get("key")
            if key_required and key_required in player.inventory:
                print(f"You use the {key_required} to unlock the way {direction}.")
                exit_info["locked"] = False
            else:
                print(f"The way {direction} is locked.", end=" ")
                if key_required:
                    print(f"You need the {key_required}.")
                else:
                    print("It won't budge.")
                return current_room

        # --- Save previous room for fleeing ---
        previous_room = current_room

        # --- Move player ---
        next_room_name = exit_info["room"]
        next_room = world.get(next_room_name)

        if next_room:
            current_room = next_room
            current_room.show()

            # --- Trigger battle if enemy exists ---
            for enemy in current_room.enemies:
                if enemy.is_alive():
                    result = battle(player, enemy)
                    
                if result == "defeat":
                    print("Game Over.")
                    exit()
                
                elif result == "escaped":
                    print("You flee back!")
                    current_room = previous_room
                    current_room.show()
                    return current_room

        else:
            print(f"Room '{next_room_name}' does not exist in the world.")

    # =====================
    # Save
    # =====================
    elif action in ["save", "sv"]:
        from Save_Load import save_game
        save_game(player, current_room)

    # =====================
    # Stats
    # =====================
    elif action in ["st", "stats"]:
        player.show_stats()

    # =====================
    # Dev Mode
    # =====================
    elif action == "devdevgo":
        password = input("Enter password: ")
        if password == "dev@$^*)==j":
            result = dev_mode(player, world)
            if result:
                return result
        else:
            print("Wrong password!")
    #======================
    # Equiping
    #======================
    elif action == "eq":
        if len(command) < 2:
            print("Equip what?")
            return current_room

        item_name = " ".join(command[1:])

        for item in player.inventory.items:
            if item.name.lower() == item_name.lower():
                slot = item.type

                if slot not in player.equipment:
                    print("You can't equip that.")
                    return current_room

                old_item = player.equipment[slot]
                if old_item:
                    player.inventory.add_item(old_item)

                player.equipment[slot] = item
                player.inventory.remove_item(item)

                print(f"You equipped {item.name}.")
                return current_room

        print("You don't have that item.")

    
    # =====================
    # Unknown Command
    # =====================
    else:
        print(f"I don't understand '{action}'.")

    return current_room
