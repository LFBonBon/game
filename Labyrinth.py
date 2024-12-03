import gvars
def start():
    print("The value of Mazedoor is:",gvars.Mazedoor)
class Character:
    def __init__(self,name,playerclass):
        self.name = name
        self.playerclass = playerclass
    health = 100
    strength = 50
    mana = 100
    stamina = 100

print("You are now well rested and Max HP. Now you enter the Labyrith, Domain of the Final Boss")
print("Because this is his domain the encounters of enemies is more common. To fight the final boss you must defeat his right hand man first")
print("but you are not ready yet, so you fight small enemies first")

import combat

def combat(player, minions):
    for minion in minions:
        print(f"\nA wild {minion.name} appears!\n")
        
        while minion.is_alive() and player.is_alive():
        
            player.status()
            minion.status()
            
        
            print("\nChoose your action:")
            print("1. Attack")
            print("2. Heal")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                player.attack_enemy(minion)
            elif choice == "2":
                player.heal()
            else:
                print("Invalid choice. You lost your turn!")

            if not minion.is_alive():
                print(f"{minion.name} has been defeated!")
                break

        
            minion.take_turn(player)
            
            if not player.is_alive():
                print(f"{player.name} has been defeated!")
                break

    if player.is_alive():
        print("\nCongratulations! You have defeated all the minions.")
    else:
        print("\nGame Over. You were defeated!")

def main():
    player = Character(name="Hero", health=100, attack=20, defense=5)
    
    Androids = [
        Android(name="Android", health=50, attack=10, defense=2),
        Android(name="Android", health=80, attack=15, defense=5),
        Android(name="Technoliath", health=120, attack=18, defense=7)
    ]
    
    combat(player, Androids)

print ("After defeating some of the Androids the Boss' right hand man takes notice of you and prepares to figth you")
print ("You are filled with immense fear but it slowly turns into courage")

def combat(player, boss):
    player = player.name
    boss = ("Boss' right hand man")
    while player.is_alive() and boss.is_alive():
        player.status()
        boss.status()
        

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            player.attack_enemy(boss)
        elif choice == "2":
            player.heal()
        else:
            print("Invalid choice. You lost your turn!")

        if not boss.is_alive():
            print(f"\n{boss.name} has been defeated!")
            break

        boss.take_turn(player)

        if not player.is_alive():
            print(f"\n{player.name} has been defeated!")
            break

    if player.is_alive():
        print("\nYou defeated the boss' right hand man! Congratulations!")
    else:
        print("\nGame Over. You were defeated by the boss' right hand man.")

def main():

    player = Character(player.name, health=100, attack=50)

    boss = Boss(name="Boss' right hand man", health=200, attack=20, )

    combat(player, boss)

print ("After defeating the boss' right hand man, you run and find a safe space where you rest up")
print ("the boss takes note of your fight with his right hand man and is in the hunt for you")
print ("for now, you are safe and rest up in the safe area you found")
