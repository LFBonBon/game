import random
import character

def rock_paper_scissors_combat(player_move, enemy_move, player, enemy):
    print(f"\n{player.name} chose {player_move}, {enemy.name} chose {enemy_move}")

    if player_move == enemy_move:
        print("It's a tie!")
        return 0  
    elif (player_move == 'Rock' and enemy_move == 'Scissors') or \
         (player_move == 'Scissors' and enemy_move == 'Paper') or \
         (player_move == 'Paper' and enemy_move == 'Rock'):
        print(f"{player.name} wins this round!")
    
        damage = random.randint(10, 20)
        enemy.take_damage(damage)
        return
    else:
        print(f"{enemy.name} wins this round!")
    
        damage = random.randint(10, 20)
        player.take_damage(damage)
        return -1 

