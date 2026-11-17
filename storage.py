import json
from tamagotchi import Tamagotchi

def save_game(pets):
    pet_data = []

    for pet in pets:
        pet_info = {"name": pet.name, "hunger": pet.hunger, "health": pet.health, "boredom": pet.boredom, "exhaustion": pet.exhaustion, "alive": pet.alive}
        pet_data.append(pet_info)

    with open("save.json", "w") as save_file:
        json.dump(pet_data, save_file, indent=4)

    print(" ~ Game saved ~ \n")


def load_game():
    try:
        with open("save.json", "r") as save_file:
            saved_data = json.load(save_file)
        
        
        pets = []

        for object in saved_data:
            pet = Tamagotchi(object["name"])
            pet.hunger = object["hunger"]
            pet.health = object["health"]
            pet.boredom = object["boredom"]
            pet.exhaustion = object["exhaustion"]
            pet.alive = object["alive"]
            pets.append(pet)

        print("The save file has been loaded successfully! Continue..\n")
        return pets
        
    except FileNotFoundError:
        print("Loading Failed! \nNo saved game was found.\n")
        return None

    except(json.JSONDecodeError, KeyError, TypeError):
        print("The save file is invalid.\n")
        return None
