import random
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, hp, attack_power):
        # Strict private attributes
        self.__name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__attack_power = attack_power

    # __ Read-Only
    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def is_alive(self):
        return self.__hp > 0

    @property
    def attack_power(self):
        return self.__attack_power

    # reducing hp
    def take_damage(self, amount):
        # no negative health
        final_damage = max(0, int(amount))
        self.__hp -= final_damage
        if self.__hp < 0:
            self.__hp = 0
        
        print(f" > {self.__name} takes {final_damage} damage! (HP: {self.__hp}/{self.__max_hp})")

    # allows childrens to implement their own attack func
    @abstractmethod
    def attack(self, target):
        pass


# Characters

class Warrior(Character):
    def __init__(self, name):
        # High HP, Medium Attack
        super().__init__(name, hp=150, attack_power=15)
        self.__is_blocking = False

    def attack(self, target):
        print(f"{self.name} swings a heavy axe at {target.name}!")
        # attack
        target.take_damage(self.attack_power)

        # Sheild (20% chance)
        if random.random() < 0.20:
            self.__is_blocking = True
            print(f" * {self.name} raises their shield! (Next damage reduced by 50%)")
        else:
            self.__is_blocking = False

    def take_damage(self, amount):
        # Check if shield is raised
        if self.__is_blocking:
            print(f" * {self.name}'s shield absorbs the blow!")
            amount = amount * 0.5
            self.__is_blocking = False # Reset block after use
        
        # recieve damage
        super().take_damage(amount)


class Mage(Character):
    def __init__(self, name):
        # Stats: Low HP, High Attack
        super().__init__(name, hp=90, attack_power=25)
        self.__mana = 20 # special mage's variable

    def attack(self, target):
        # Magic (Arcane blast)
        mana_cost = 10
        
        if self.__mana >= mana_cost:
            self.__mana -= mana_cost
            damage = self.attack_power * 2
            print(f"{self.name} casts Arcane Blast on {target.name}! (Mana: {self.__mana})")
            target.take_damage(damage)
        else:
            # after mana ends
            self.__mana += 5
            damage = self.attack_power * 0.5
            print(f"{self.name} is out of Mana! Weak staff hit on {target.name}. (+5 Mana)")
            target.take_damage(damage)


class Rogue(Character):
    def __init__(self, name):
        # Stats: Medium HP, Medium Attack
        super().__init__(name, hp=110, attack_power=20)
        self.__is_dodging = False

    def attack(self, target):
        print(f"{self.name} strikes {target.name} from the shadows!")
        target.take_damage(self.attack_power)

        # dodge (30% chance)
        if random.random() < 0.30:
            self.__is_dodging = True
            print(f" * {self.name} vanishes into the shadows! (Next attack will miss)")
        else:
            self.__is_dodging = False

    def take_damage(self, amount):
        # Check if dodging
        if self.__is_dodging:
            print(f" * {self.name} dodges the attack completely!")
            amount = 0
            self.__is_dodging = False # Reset dodge after using it
        
        super().take_damage(amount)


# The Arena

def run_arena():
    print("Game Start")
    
    p = []
 
    def choose():
        c = int(input("Enter your character:\n1 = Warrior\n2 = Mage\n3 = Rogue\n> "))
        match c:
            case 1:
                return Warrior("Warrior")
            case 2: 
                return Mage("Mage")
            case 3:
                return Rogue("Rogue")
            case _:
                print("Invalid choice opting for the default character Warrior")
                return Warrior("Warrior")
   

    p.append(choose())
    p.append(choose())
    round_num = 1

    # Main Loop
    while p[0].is_alive and p[1].is_alive:
        print(f"\n--- Round {round_num} ---")
        
        # Player 1 turn
        p[0].attack(p[1])
        if not p[1].is_alive:
            print(f"\n>>> {p[1].name} has fallen! {p[0].name} wins!")
            break

        # Player 2 turn
        p[1].attack(p[0])
        if not p[0].is_alive:
            print(f"\n>>> {p[0].name} has fallen! {p[1].name} wins!")
            break
            
        round_num += 1

    print("Game End")

if __name__ == "__main__":
    run_arena()