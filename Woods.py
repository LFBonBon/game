import gvars
import character
def start():
    gvars.Mazedoor = True
    Labyrinth.start()

print("After training in the Outskirts, you are now perpared for battle")
print("A villager sees your skill and decides to give you a quest")

import combat
def main():
    player = Character(player.name, health=100, attack=20, defense=5)

    quest = Quest(description="Defeat the androids to earn a reward!", required_enemies=3, reward="attack_boost")
    npc = NPC(name="Quest Giver", quest=quest)

    androids = []
    Minion(name="Android", health=50, attack=10, defense=2),
    Minion(name="Android", health=80, attack=15, defense=5),
    Minion(name="Technoliath", health=120, attack=18, defense=7)

    npc.give_quest()

    combat(player, androids, quest)

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


print("after completing the quest the villager thanks you and treats you to food and shelter to rest up for you next adventure")


