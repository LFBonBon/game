def Main():
    print("Welcome to the Game!")
    print("Choose your character:")
    
    character_1 = Character("Derrick the brawn")
    character_2 = Character("Jake the brains")
    
    print("1. Derrick - High defense, balanced attack.")
    print("2. Jake - High attack, lower defense.")
    
    
    choice = input("Enter '1' to choose Derrick or '2' to choose Jake: ")
    
    if choice == '1':
        player = character_1
        print("Derrick is fired up")
    elif choice == '2':
        player = character_2
        print("Jake is pleased to take this journey with you")
    else:
        print("Invalid choice.")

import gvars
gvars.initialize()