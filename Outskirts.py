def Outskirts():
    import gvars
    import character
def start():
    print(gvars.Mazedoor)

print ("Welcome to the outskirts")
print ("Here is where you will train and learn to combat the evil of the world")

import combat
def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.status()
        enemy.status()

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            player.attack_enemy(enemy)
        elif choice == "2":
            player.heal()
        else:
            print("Invalid choice. You lost your turn!")

        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        enemy_choice = random.choice(["attack", "heal"])
        if enemy_choice == "attack":
            enemy.attack_enemy(player)
        else:
            enemy.heal()

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

def main():
    player = Character(Player.name, health=100, attack=50)
    
    android = []
    Minion(name="Android", health=50, attack=10),
    Minion(name="Android", health=80, attack=15),
    Minion(name="Technoliath", health=120, attack=18)

print ("Wow! You're a real conquerer of evil huh")

class Character:
    def __init__(self,name,playerclass):
        self.name = name
        self.playerclass = playerclass
    health = 100
    strength = 50
    mana = 100
    stamina = 100
def Levelup(self):
        print ("What do you want to level up?")
        choice = input("HP is health, STR is Strength, MAN is Mana, STAM is Stamina")
        match choice:
            case "HP":
                self.health += 10
                print("Health is now", self.health)
            case "STR":
                self.strength += 10
                print("Strength is now", self.strength)
            case "MAN":
                self.mana += 10
                print ("Mana is now", self.mana)
            case "STAM":
                self.stamina += 10
                print ("Stamina is now", self.stamina)

print ("Tutorial Complete")

