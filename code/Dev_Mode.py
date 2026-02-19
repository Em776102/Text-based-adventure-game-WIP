from Player import Player
from World_01 import World_01  # only if needed

def dev_mode(player, world):
    global dev_mode_commands
    dev_mode_commands = True
    print("Dev Mode Activated")
    print("Type 'exit' to leave Dev Mode.")

    while True:
        cmd = input("DEV> ").lower().split()
        if not cmd:
            continue

        action = cmd[0]

        # Leave dev mode
        if action == "exit":
            print("Exiting Dev Mode.")
            break

        # TELEPORT
        elif action == "tp":
            if len(cmd) < 2:
                print("Usage: tp <roomname>")
                continue
            roomname = cmd[1].capitalize()
            if roomname in world:
                print(f"Teleported to {roomname}")
                return world[roomname]
            else:
                print("Room does not exist.")

        # GIVE ITEMS
        elif action == "give":
            if len(cmd) < 2:
                print("Usage: give <item>")
                continue
            item = cmd[1]
            player.inventory.add_item(item)
            print(f"Gave item: {item}")

        else:
            print("Unknown dev command.")
