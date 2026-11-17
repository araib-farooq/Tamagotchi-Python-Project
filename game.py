from tamagotchi import Tamagotchi
import random

def create_pets():
    tama_list = [Tamagotchi("Tom"), Tamagotchi("Jerry"), Tamagotchi("Kev")]
    return tama_list

def select_pet(pets):
    while True:
        print("\n" + "-" * 42)
        print("CHOOSE YOUR PET".center(42))
        print("-" * 42)
        for pet in pets:
            print(f"  - {pet.name}")

        print("-" * 42)
        choice = input("\nSelect your Tamagotchi to interact with: \n").strip().lower()

        for pet in pets:
            if pet.name.lower() == choice:
                return pet

            
        print("Have you forgotten the name of your pets?")


def display_statistics(pets):
    alive = 0
    dead = 0
    health_total = 0
    hunger_total = 0
    boredom_total = 0
    exhaustion_total = 0

    for pet in pets:
        if pet.alive:
            alive += 1
            health_total += pet.health
            hunger_total += pet.hunger
            boredom_total += pet.boredom
            exhaustion_total += pet.exhaustion
        else:
            dead += 1
    print("\n" + "=" * 42)
    print("GAME STATISTICS".center(42))
    print("=" * 42)
    print(f"Living pets: {alive}")
    print(f"Dead pets: {dead}")

    if alive > 0:
        print(f"Average health: {health_total / alive}")
        print(f"Average hunger: {hunger_total / alive}")
        print(f"Average boredom: {boredom_total / alive}")
        print(f"Average exhaustion: {exhaustion_total / alive}\n")
    else:
        print("Averages are unavailable because no pets are alive.\n")
    print("=" * 42)


def idle(pets):
    for pet in pets:
        if pet.alive:
            pet.hunger += 2
            if pet.hunger >= 98:
                pet.hunger = 100
            pet.boredom += 1
            if pet.boredom >= 99:
                pet.boredom = 100
            pet.exhaustion += 1
            if pet.exhaustion >= 99:
                pet.exhaustion = 100
            if pet.hunger == 100:
                pet.health -= 5
                if pet.health <= 0:
                    pet.health = 0
                    pet.alive = False
                    print(f"{pet.name} died from hunger.....")

def random_events(pets):
    pets_alive = []

    for pet in pets:
        if pet.alive:
            pets_alive.append(pet)

    if pets_alive == []:
        return

    if random.randint(1, 5) != 1:
        return

    random_pet = random.choice(pets_alive)
    event = random.choice(["food", "sick", "energetic", "injury"])

    if event == "food":
        random_pet.hunger -= 10
        if random_pet.hunger < 0:
            random_pet.hunger = 0
        print(f"{random_pet.name} found some food and fed himself!!!\n")

    elif event == "sick":
        random_pet.health -= 15
        if random_pet.health < 0:
            random_pet.health = 0
        if random_pet.health == 0:
            random_pet.alive = False
        print(f"{random_pet.name} is severely sick because you gave him expired food!!!\n Careful of his health!\n")

    elif event == "energetic":
        random_pet.health += 15
        if random_pet.health > 100:
            random_pet.health = 100
        print(f"{random_pet.name} is healthy and energetic!\n Suddenly {random_pet.name} got extra 15 health!\n")

    elif event == "injury":
        random_pet.health -= 25
        if random_pet.health < 0:
            random_pet.health = 0
        if random_pet.health == 0:
            random_pet.alive = False
        print(f"{random_pet.name} got injured and hurt himself!!!\n Resulting in loss of 25 health!\n")


