import character

print ("After resting your stats are now back to max and you are ready to fight the final boss")
print ("now you face the the Final boss. There is no turning back")
print ("you are ready to fight")

import combat 
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

    while character.health > 0 and boss.health > 0:
        character.attack(boss)
        if boss.health <= 0:
            print(f"{boss.name} is defeated!")
            break
        
        if boss.health < 50 and boss.phase == 1:
            boss.phase_two()

        boss.attack(character)
        if character.health <= 0:
            print(f"{character.name} has been defeated.")
            break
print ("You did it! You beat the boss")
print ("Peace is now restored to the land. Thank you for playing")