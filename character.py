class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        other.hp -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"

File: main.py
from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)

    print(hero)
    print(enemy)
    print()

    while hero.is_alive() and enemy.is_alive():
        hero.attack(enemy)
        if enemy.is_alive():
            enemy.attack(hero)
        print(hero)
        print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

if __name__ == "__main__":
    main()