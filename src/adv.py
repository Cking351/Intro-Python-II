from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
p1 = Player("Player 1", room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
import sys
while True:
    prompt = input("Which Direction Shall Ye Take? N? S? W? E?")
    if len(sys.argv) == 1:
        if prompt[0] == "q":
            break
        elif prompt[0] == "n":
            if hasattr(p1.location, "n_to"):
                p1.location = p1.location.n_to
                print("\nYou have traveled North!\n")
            else:
                print("\nYou go North and find the way blocked\n")
                continue
        elif prompt[0] == "e":
            if hasattr(p1.location, "e_to"):
                p1.location = p1.location.e_to
                print("\nYou continue to the east!\n")
            else:
                print("\nYou go East and find the way blocked\n")
                continue
        elif prompt[0] == "w":
            if hasattr(p1.location, "w_to"):
                p1.location = p1.location.w_to
                print("Your journey continues West!")
            else:
                print("\nYou go West and find the way blocked\n")
                continue
        elif prompt[0] == "s":
            if hasattr(p1.location, "s_to"):
                p1.location = p1.location.s_to
                print("\nYou continue South")
            else:
                print("\nYou go South and find the way blocked\n")
    else:
        print(sys.argv)