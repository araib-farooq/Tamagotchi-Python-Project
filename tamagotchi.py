class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.health = 100
        self.boredom = 50
        self.exhaustion = 20
        self.alive = True

    def status(self):
        print("\n" + "=" * 42)
        print("PET STATUS".center(42))
        print("=" * 42)
        print(f"Name: {self.name}")
        if self.alive:
            print(f"Hunger: {self.hunger}")
            print(f"Health: {self.health}")
            print(f"Boredom: {self.boredom}")
            print(f"Exhaustion: {self.exhaustion}")
            print("Status: Alive\n")
            if self.health <= 20:
                print(f"Warning: {self.name}'s health is low !!!")
        else:
            print(f"Name: {self.name}")
            print("Status: Dead\n")
        print("=" * 42)


    def heal(self):
        if self.alive:
            if self.health >= 80:
                self.health = 100
            else:
                self.health = self.health + 20
            print(f"{self.name} has been healed!\n")
        else:
            print(f"{self.name} is dead...\n")


    def feed(self):
        if self.alive:
            if self.hunger >= 20 and self.hunger <= 100:
                self.hunger = self.hunger - 20
            else:
                self.hunger = 0
            print(f"{self.name} was fed!\n")
        else:
            print(f"{self.name} is dead...\n")

    def play(self):
        if self.alive:
            if self.boredom >= 20:
                self.boredom = self.boredom - 20
            else:
                self.boredom = 0
    
            if self.hunger >= 90:
                self.hunger = 100
            else:
                self.hunger = self.hunger + 10

            if self.exhaustion >= 90:
                self.exhaustion = 100
            else:
                self.exhaustion = self.exhaustion + 10
            print(f"{self.name} liked playing!\n")
        else:
            print(f"{self.name} is dead...\n")

    def sleep(self):
        if self.alive:
            if self.exhaustion <= 25:
                self.exhaustion = 0
            else:
                self.exhaustion = self.exhaustion - 25
    
            if self.hunger >= 95:
                self.hunger = 100
            else:
                self.hunger = self.hunger + 5
            print(f"{self.name} has been put to sleep!\n")
        else:
            print(f"{self.name} is dead...\n")


