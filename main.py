from game import create_pets, select_pet, display_statistics, idle, random_events
from storage import save_game, load_game


def show_menu(pet):
    print("\n" + "=" * 42)
    print("TAMAGOTCHI PET FARM".center(42))
    print("=" * 42)
    print(f"Current pet: {pet.name}")

    if pet.alive:
        print(f"Health: {pet.health}/100 | Hunger: {pet.hunger}/100")
        print(f"Boredom: {pet.boredom}/100 | Exhaustion: {pet.exhaustion}/100")
    else:
        print("Status: DEAD")

    print("-" * 42)
    print("[F] Feed   [P] Play   [S] Sleep   [H] Heal")
    print("[C] Change pet   [D] Full status   [stats] Statistics")
    print("[save] Save game   [load] Load game   [q] Quit")
    print("=" * 42)

    return input("Choose an option: ").strip().lower()


print("Welcome to your pet farm!")
input("\nPress Enter to start...")

pets = create_pets()
chosen_pet = select_pet(pets)


while True:
    action = show_menu(chosen_pet)

    if action == 'f':
        chosen_pet.feed()
        if chosen_pet.alive:
            idle(pets)
            random_events(pets)
    elif action == 'p':
        chosen_pet.play()
        if chosen_pet.alive:
            idle(pets)
            random_events(pets)
    elif action == 's':
        chosen_pet.sleep()
        if chosen_pet.alive:
            idle(pets)
            random_events(pets)
    elif action == 'h':
        chosen_pet.heal()
        if chosen_pet.alive:
            idle(pets)
            random_events(pets)
    elif action == 'd':
        chosen_pet.status()
    elif action == 'c':
        chosen_pet = select_pet(pets)
        chosen_pet.status()
    elif action == 'stats':
        display_statistics(pets)
    elif action == 'save':
            save_game(pets)
    elif action == 'load':
            loaded_pets = load_game()
            if loaded_pets is not None:
                 pets = loaded_pets
                 chosen_pet = select_pet(pets)
    elif action == 'q':
        break    
    else:
        print("Inavlid action!!! Please enter a valid action.\n")






