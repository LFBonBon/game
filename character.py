import random

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

    def player_take_damage(self, damage):
        self.health -= max(0, damage)
    
    def player_is_alive(self):
        return self.health > 0
    
    def player_attacks_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        return damage
    
class Jake(Character):
    def __init__(self, name, health, attack, defense, mana):
        super().__init__(name, health, attack, defense) 
        self.mana = mana 
        self.max_mana = mana  
        self.spells = {
            'fireball': {'damage': 25, 'mana_cost': 10},
            'ice_shard': {'damage': 15, 'mana_cost': 5},
            'heal': {'damage': -20, 'mana_cost': 8},
        }

    def cast_spell(self, spell_name, target):
        if spell_name not in self.spells:
            print(f"{self.name} cannot cast {spell_name}!")
            return
        
        spell = self.spells[spell_name]
        
        if self.mana < spell['mana_cost']:
            print(f"Not enough mana to cast {spell_name}!")
            return
        
        self.mana -= spell['mana_cost']
        
        damage = spell['damage']
        
        if damage < 0:
            healed = target.take_damage(damage)
            print(f"{self.name} casts {spell_name} and heals {target.name} for {abs(damage)}!")
        else:
            damage_dealt = target.take_damage(damage)
            print(f"{self.name} casts {spell_name} and deals {damage_dealt} damage to {target.name}!")

    def regenerate_mana(self):
        regen = random.randint(5, 15) 
        self.mana = min(self.mana + regen, self.max_mana) 
        print(f"{self.name} regenerates {regen} mana. Current mana: {self.mana}")

    def __str__(self):
        return f"{super().__str__()}, Mana = {self.mana}"
    
class Derrick(Character):
    def __init__(self, name, health, attack, defense, rage=0):
        super().__init__(name, health, attack, defense)  
        self.rage = rage  
        self.max_rage = 100  

    def enter_rage(self):
        if self.rage == self.max_rage:
            print(f"{self.name} is already at full rage!")
            return
        
        self.attack += 10
        self.defense += 5
        self.rage = self.max_rage
        print(f"{self.name} enters a rage! Attack and Defense increased temporarily!")

    def perform_rage_attack(self, target):
        if self.rage < 50:
            print(f"{self.name} doesn't have enough rage to perform a rage attack!")
            return
        
        damage = self.attack + 20
        self.rage -= 50  
        print(f"{self.name} performs a RAGE ATTACK on {target.name} dealing {damage} damage!")
        target.take_damage(damage)

    def recover_rage(self):
        recover = random.randint(5, 15)
        self.rage = min(self.rage + recover, self.max_rage) 
        print(f"{self.name} recovers {recover} rage. Current rage: {self.rage}")

    def __str__(self):
        return f"{super().__str__()}, Rage = {self.rage}"


    

class Android(Character):

    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.retreat_threshold = 30  

    def swarm_attack(self, target):
        damage = random.randint(5, 10)  
        print(f"{self.name} performs a Swarm Attack on {target.name} dealing {damage} damage!")
        return target.take_damage(damage)

    def retreat(self):
        if self.health <= self.retreat_threshold:
            print(f"{self.name} retreats from battle due to low health!")
            return True
        return False

    def attack(self, target):
        if not self.retreat():
            damage = self.attack
            print(f"{self.name} attacks {target.name} and deals {damage} damage!")
            return target.take_damage(damage)
        return 0

    def __str__(self):
        return f"{super().__str__()}, Retreat Threshold = {self.retreat_threshold}"
    
 
class Technoliath(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.taunt_duration = 1 
    
    def smash_attack(self, target):
        damage = self.attack + 30  
        self.defense -= 5  
        print(f"{self.name} performs a Smash Attack on {target.name} dealing {damage} damage!")
        return target.take_damage(damage)
    
    def ground_stomp(self, targets):
        damage = random.randint(10, 20)  
        print(f"{self.name} performs a Ground Stomp, dealing {damage} damage to all enemies!")
        for target in targets:
            target.take_damage(damage)
    
    def taunt(self, target):
        print(f"{self.name} taunts {target.name}, forcing them to attack only {self.name}!")
        self.taunt_duration = 2  
    
    def attack(self, target, all_targets=None):
        if all_targets:  
            self.ground_stomp(all_targets)
        else:
            damage = self.attack
            print(f"{self.name} attacks {target.name} and deals {damage} damage!")
            target.take_damage(damage)
    
    def __str__(self):
        return f"{super().__str__()}, Taunt Duration = {self.taunt_duration}"

class Boss(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.enrage_threshold = 50 
        self.is_enraged = False
        self.minions = [] 

    def enrage(self):

        if self.health <= (self.enrage_threshold / 100) * self.health:
            if not self.is_enraged:
                print(f"{self.name} becomes ENRAGED! Attack power increased!")
                self.attack += 15 
                self.is_enraged = True
            else:
                print(f"{self.name} is already ENRAGED!")

    def summon_minions(self, minion_class, num_minions):
        print(f"{self.name} summons {num_minions} minions to the battlefield!")
        for _ in range(num_minions):
            minion = minion_class(f"Minion {_+1}", 50, 10, 2)
            self.minions.append(minion)

    def ultimate_attack(self, target):
        if self.health <= (self.enrage_threshold / 100) * self.health and self.is_enraged:
            damage = self.attack + 30  
            print(f"{self.name} uses its ULTIMATE ATTACK on {target.name} and deals {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{self.name} is not enraged enough to use the Ultimate Attack!")

    def attack(self, target, all_targets=None):

        if all_targets:
            self.ultimate_attack(target)
        else:
            damage = self.attack
            print(f"{self.name} attacks {target.name} and deals {damage} damage!")
            target.take_damage(damage)

    def __str__(self):
        return f"{super().__str__()}, Enraged = {self.is_enraged}"
    
class FinalTechBoss(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.phase_threshold = self.health * 0.5  
        self.current_phase = 1
        self.is_enraged = False
    
    def check_phase(self):
        if self.health <= self.phase_threshold and self.current_phase == 1:
            print(f"{self.name} has entered Phase 2!")
            self.current_phase = 2
            self.attack += 10
            self.defense -= 2  

    def normal_attack(self, target):
        damage = self.attack
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        return target.take_damage(damage)

    def fire_breath(self, targets):
        if self.current_phase == 2:
            damage = random.randint(20, 30)
            print(f"{self.name} uses Fire Breath, dealing {damage} damage to all enemies!")
            for target in targets:
                target.take_damage(damage)
    
    def charge_attack(self, target):
        if self.current_phase == 2:
            damage = self.attack + 15 
            print(f"{self.name} charges at {target.name} with great force, dealing {damage} damage!")
            return target.take_damage(damage)
    
    def attack(self, target, all_targets=None):
        """Boss performs an attack or special ability based on current phase."""
        self.check_phase() 
        
        if self.current_phase == 1:
            self.normal_attack(target)
        elif self.current_phase == 2:
            if all_targets:
                self.fire_breath(all_targets)
            else:
                self.charge_attack(target)
    
    def __str__(self):
        return f"{super().__str__()}, Phase = {self.current_phase}"
    
class NPC:
    def __init__(self, name, quest):
        self.name = name
        self.quest = quest  

    def give_quest(self):
        print(f"{self.name}: I have a quest for you!")
        print(f"Quest: {self.quest.description}")
        print(f"Objective: Defeat {self.quest.required_enemies} enemies")
        print("Good luck!")

    def reward(self, character):
        print(f"{self.name}: Congratulations on completing the quest!")
        print(f"Reward: {self.quest.reward}")
        self.quest.apply_reward(character)


class Quest:
    def __init__(self, description, required_enemies, reward):
        self.description = description
        self.required_enemies = required_enemies  
        self.reward = reward  

    def apply_reward(self, character):
        if self.reward == "heal":
            heal_amount = random.randint(20, 50)
            character.health += heal_amount
            print(f"{character.name} receives {heal_amount} HP as a reward!")
        elif self.reward == "attack_boost":
            boost = random.randint(5, 10)
            character.attack += boost
            print(f"{character.name} receives an attack boost of {boost}!")
        elif self.reward == "defense_boost":
            boost = random.randint(3, 7)
            character.defense += boost
            print(f"{character.name} receives a defense boost of {boost}!")


def combat(player, minions, quest):
    defeated_enemies = 0
    for minion in minions:
        if defeated_enemies >= quest.required_enemies:
            break
        
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
                defeated_enemies += 1
                break

            minion.take_turn(player)
            
            if not player.is_alive():
                print(f"{player.name} has been defeated!")
                break

    if player.is_alive() and defeated_enemies >= quest.required_enemies:
        print("\nCongratulations! You have completed the quest.")
        npc.reward(player)
    elif not player.is_alive():
        print("\nGame Over. You were defeated!")