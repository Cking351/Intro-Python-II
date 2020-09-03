from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms
### Day 2 MVP
# ////////////////////////////////////////////////////////////////////////////////////
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

"""
Create an item class that takes //name, description, location maybe?//
Create a treasure item that is in the treasure room?
- When you reach the treasure room and pick up the treasure, player wins and game ends
"""
# //////////////////////////////////////////////////////////////////////////////////////
Main_Item = Item("Treasure", "The secret treasure")
item2 = Item("Sword", "An old sword over the mantle..")
item3 = Item("Old Bucket", "An old bucket..this doesnt seem useful")
item4 = Item("Used Toothbrush", "I've been missing one of those..")
item5 = Item("Slingshot", "Huh, everything is coming up slingshot")
item_container = [item2, item3, item4, item5]

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ),

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
# current_location = f"Location: {p1.location.name}\n{p1.location.description}"
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# def moving(place, heading):
#     if hasattr(p1.location, heading):
#         p1.location = p1.location.heading
#         print(f"Location: {p1.location.name}\n{p1.location.description}")
#     else:
#         print("\nYou go {place} and find the way blocked")
# #
# #
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print("Search through the rooms and find the treasure!\nTo quit at anytime, press 'q'\n")

start_game = input("\nPress any key continue")

while True:

    prompt = input("\nWhich Direction Shall You Take? N? S? W? E?\n")
    if prompt[0] == "q":
        quit("You have left the game")
    elif prompt[0] == "n":
        if hasattr(p1.location, "n_to"):
            p1.location = p1.location.n_to
            print(f"\nLocation: {p1.location.name}\n{p1.location.description}\n}")
        else:
            print("\nYou go North and find the way blocked\n")
    elif prompt[0] == "e":
        if hasattr(p1.location, "e_to"):
            p1.location = p1.location.e_to
            print(f"\nLocation: {p1.location.name}\n{p1.location.description}\n")
        else:
            print("\nYou go East and find the way blocked\n")
    elif prompt[0] == "w":
        if hasattr(p1.location, "w_to"):
            p1.location = p1.location.w_to
            print(f"\nLocation: {p1.location.name}\n{p1.location.description}\n")
        else:
            print("\nYou go West and find the way blocked\n")
    elif prompt[0] == "s":
        if hasattr(p1.location, "s_to"):
            p1.location = p1.location.s_to
            print(f"\nLocation: {p1.location.name}\n{p1.location.description}\n")
        else:
            print("\nYou head South and find the way blocked")
    else:
        print("\nYou go South and find the way blocked\n")
