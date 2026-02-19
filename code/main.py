# Libraries
import sys, os, random, time

# Utility and core systems
from Utility import clear
from Utility import slow
from Utility import wait
from Player import Player
from Inventory import Inventory
from Room import Room
from World_01 import World_01
from Commands import handle_command
from Save_Load import load_game, save_game
from Battle import battle
from Dev_Mode import dev_mode
from Item import Item
from Enemy import Enemy

# Initialize world
world = World_01()
SAVE_FILE = "Quixotic_Sonder_Save.json"

# Optional Matrix Easter Egg
if random.randint(0, 100) == 100:
    for _ in range(100):
        print("\033[92m" + "01"*56 + "\033[0m")
        time.sleep(0.02)
    clear()
    
# -------- Title Screen --------
def title_screen():
    while True:
        print("====================")
        print("  Quixotic Sonder")
        print("====================")
        print("1. New Game")
        print("2. Load Game")
        print("3. Credits")
        print("4. Quit")
        print("Controls: w/a/s/d")
        print("sv/save = save")
        print("i = Inventory")
        print("l = Look")
        print("t = Take")
        print("Q = quit")
        print("st/stats = Show Stats")

        choice = input("> ").strip()
        if choice == "1":
            if os.path.exists(SAVE_FILE):
                print("A save file already exists. Override? (y/n)")
                if input("> ").lower() == "y":
                    return "new"
            else:
                return "new"
        elif choice == "2":
            if os.path.exists(SAVE_FILE):
                return "load"
            else:
                print("No saved game found!")
        elif choice == "3":
            print("Game created by Ari")
            input("\nPress ENTER to go back...")
        elif choice == "4":
            print("Thanks for playing!")
            sys.exit()

# -------- Player Setup --------
choice = title_screen()
slow("Enter your character name: ")
player_name = input("> ").strip()

if player_name.lower() in ["idk", "i dont know", "i don't know"]:
    slow(f"Really?, {player_name}?")
    slow("I'm choosing it for you, funny guy.")
    player_name = "IDIOT LOL"
elif player_name.lower() in ["Random", "random", "r", "R", "random name", "Random name", "random Name", "Random Name", "RANDOM NAME"]:

    FIRST_NAMES = [
        "Aren", "Liora", "Kael", "Nyx", "Orin", "Sylas", "Vera", "Thane", "Elowen", "Rook",
        "Mira", "Dorian", "Ash", "Iris", "Bram", "Kora", "Lucan", "Faye", "Rowan", "Zane",
        "Alric", "Seren", "Jax", "Lyra", "Eamon", "Talia", "Corin", "Maeve", "Finn", "Rhea",
        "Drake", "Isla", "Nolan", "Vixen", "Cass", "Oren", "Piper", "Soren", "Nova", "Caleb",
        "Freya", "Galen", "Hazel", "Ivo", "Juniper", "Kellan", "Luna", "Magnus", "Nia", "Otis",
        "Percy", "Quinn", "Reed", "Sable", "Tobin", "Ulric", "Vale", "Willow", "Xander", "Yara",
        "Zara", "Arlo", "Bex", "Cyrus", "Dahlia", "Ember", "Flint", "Greer", "Hollis", "Indigo",
        "Juno", "Knox", "Lark", "Maddox", "Nash", "Opal", "Phoenix", "Rune", "Skye", "Tamsin",
        "Uriah", "Vaughn", "Wren", "Xia", "Yves", "Zephyr", "Atlas", "Briar"
    ]

    LAST_NAMES = [
        "Blackwood", "Stormveil", "Ironhart", "Moonfall", "Graves", "Holloway", "Nightbloom", "Ravenscar", "Ashcroft", "Duskryn",
        "Frostmere", "Emberlyn", "Thornfield", "Wraithmoor", "Silverlock", "Crowe", "Darkwater", "Windmere", "Vexley", "Stoneward",
        "Bloodworth", "Oakenshield", "Mistwalker", "Grimshaw", "Dawnbringer", "Shadowfen", "Brightmoor", "Ironwill", "Duskhaven", "Flintlock",
        "Snowfall", "Gravewind", "Hawthorne", "Cinderfall", "Nightwatch", "Stormborn", "Ashenford", "Rimewood", "Blacktide", "Sunreach",
        "Fallowmere", "Wolfsbane", "Deepwater", "Highridge", "Emberfall", "Moonshadow", "Thunderscar", "Goldleaf", "Dreadmoor", "Starling",
        "Ironcrest", "Hollowgrave", "Frostward", "Shadebrook", "Windscar", "Darkspire", "Silverthorn", "Ravenholt", "Stonehelm", "Firebrand",
        "Mournwatch", "Brightfall", "Stormwatch", "Ashwalker", "Nightvale", "Grimvale", "Coldstream", "Shadowmere", "Duskfall", "Ironbark",
        "Sunwhisper", "Moonspire", "Wyrdwood", "Blackfen", "Crowsend", "Frostveil", "Emberwatch", "Graveborn", "Stormreach", "Nightwind",
        "Ironshade", "Dawnhollow", "Mistvale", "Flameward", "Shadowcrest", "Silvermoor", "Ashenmere", "Voidwalker"
    ]

    player_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

player = Player(player_name)

player.inventory.items.append("Torch")

# -------- Load Game --------
if choice == "load":
    data = load_game()
    if data:
        player.name = data["name"]
        player.hp = data["hp"]
        player.level = data["level"]
        player.xp = data.get("xp", 0)
        player.inventory.items = data["inventory"]
        current_room = world.get(data.get("current_room", "Well"))
    else:
        current_room = world.get("Well")
else:
    current_room = world.get("Well")

# -------- Game Start --------
slow(f"\nWelcome, {player.name}! Your adventure begins...")
current_room.show()

# -------- Main Game Loop --------
while True:
    command = input("> ").lower().split()
    current_room = handle_command(command, player, current_room, world.rooms)
    
