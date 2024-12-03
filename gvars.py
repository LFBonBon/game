#Here is where we put any variables that we know we will check in other chapters-- keys, story events, world events, etc.

global Mazedoor #hypothetical variable to decide whether a door in the Labyrinth is open or closed
Mazedoor = False
def initialize(): #run at the start of the game to reset all "flags" or story events
    Mazedoor = False
