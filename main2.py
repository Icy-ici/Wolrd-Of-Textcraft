from item import Item
from room import Room
from character import Enemy, Friend
from attributes import Attribute


# Creating Charactes

heroes = {"Knight",
          "Mage",
          "Thief",
          "Ranger",
          "Warrior"
          }
while True:
    print("Still the same baisic game")
    for character in heroes.items():
        print(character[0].capitalize(), ":", character[1])
    choice = input("What would you like to chose").lower().strip()
    if choice in heroes.keys():
        chosenCharacter = heroes[choice]
        break 
print("Worthy Choice")

# Creating Types
types = {"Paladin", 
        "Sharman",
        "Warlock"}
for player in types.items():
    print(player[0].capitalize(), ":", player[1])
chosenPlayer = types[input("\nWho would you like to choose > ").lower()]
print("\n \n Worthy Choice \n")


#create rooms
Azeroth = Room("Azeroth")
Barrens = Room("Barrens")
Kalmidor = Room("Kalmidor")
Easternkingdoms = Room("Eastern Kingdoms")
Lorderon = Room("Tristfall Glades")
Pandaria = Room("Pandaria")
Northrend = Room("Northrend")
Crossroads = Room("Crossroads")
Icecrown = Room("Ice Crown Glacier")
Zandalar = Room("Zandalan")
#Link Rooms
Azeroth.link_rooms(Kalmidor, "West")
Azeroth.link_rooms(Northrend, "North")
Azeroth.link_rooms(Easternkingdoms, "East")
Azeroth.link_rooms(Pandaria, "South")
Easternkingdoms.link_rooms(Lorderon, "North")
Easternkingdoms.link_rooms(Azeroth, "West")
Lorderon.link_rooms(Easternkingdoms, "South")
Northrend.link_rooms(Azeroth, "South")
Northrend.link_rooms(Icecrown, "North")
Kalmidor.link_rooms(Azeroth, "East")
Kalmidor.link_rooms(Barrens, "South")
Barrens.link_rooms(Kalmidor, "North")
Barrens.link_rooms(Crossroads, "South")
Pandaria.link_rooms(Azeroth, "North")
Pandaria.link_rooms(Zandalar, "East")
Crossroads.link_rooms(Barrens, "North")
Icecrown.link_rooms(Northrend, "South")
Zandalar.link_rooms(Pandaria, "West")

#creating NPC characters
Chromie= Friend("Chromie")
Chromie.conversation = "Hello Friend: Your quest is to explore Azeroth and clear the places from the bad " \
"\nA good place to start are the Tristfall Glades " \
"\nGood Luck"

Sergra_Darkthorn = Friend("Sergra Darkthorn")
Sergra_Darkthorn.conversation = "What brings you here. Did you know I fought the Grand Empress Shek'zara once. He has little immunity to magic"
litch = Enemy("The Great Litch King")
litch.weakness = "fire"
litch.description = "The master and lord of the Scourage, which he rules telepathically as he sits atop his Frozen Throne"
julakdoom = Enemy("Julak-Doom")
julakdoom.weakness = "fists"
oondaska = Enemy("Oondaska the Great")
oondaska.weakness = ("magic")
argus = Enemy("Argus the Unmaker")
argus.weakness = "sword"
kraulok = Enemy("Dunegorger Kraulok")
kraulok.weakness = "thunderfury"

#add characters and their rooms
Azeroth.character = Chromie
Kalmidor.character = argus
Icecrown.character = litch
Lorderon.character = julakdoom
Pandaria.character = oondaska
Crossroads.character = Sergra_Darkthorn
Zandalar.character = kraulok


#create items
fire = Item("Fire")
sword = Item("Sword")
fists = Attribute("Fists")
magic = Attribute("Magic")
thunderfury = Item("Thunderfury")


#adding items to the room
Barrens.item = fire
Northrend.item = thunderfury
Azeroth.attribute = fists
Easternkingdoms.attribute = magic

#adding loot to enemies
Lorderon.item = sword

#initialising variables 
current_room = Azeroth
running = True
bag = []

print("In this game, you have a few options when entering an area. "
"\nYou can either fight or talk to a charcter."
"\nYou can walk between areas by typing the direction. "
"\nIf you see any items lying around, its a good idea to take them - type t to take. "
"\nYou can find differant attributes for your character around - type c to claim them. "
"\nAfter killing an enemie - type l to claim loot."
"\nTo find out what items and attributes - type b"
"\nTalking to Chromie will give you your first quest!")

while running:
    current_room.describe()
    command = input("> ").lower()
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command) 
    elif command == "t":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to") 
    elif command =="f":
        if current_room.character is not None:
            weapon = input("What will you fight with >").lower()
            available_weapons =[]
            for item in bag:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                else:
                    running = False
            else:
                print(f"I can't fight that: You dont have {weapon}")
                print("You Died:")
                running = False 
    elif command =="t":
        if current_room.item is not None:
            bag.append(current_room.item)
            print(f"Item added to action bar")
            current_room.item = None
        else:
            print("I can't take that")
    elif command =="c":
        if current_room.attribute is not None:
            bag.append(current_room.attribute)
            print("Attribute added to action bar")
            current_room.attribute = None
        else:
            print("I cant claim that")
    elif command =="b":
        if bag == []:
            print("Your action bar is empty")
        else:
            print("You have:")
            for item in bag:
                print(f" - {item.name}")      
    elif command =="l":
        if current_room.item is not None:
            bag.append(current_room.item)
            print("You have looted the Death Night, finding a sword, "
            "\n You can acsess this in your action bar")
            current_room.item = None 
        else:
            print("I cant loot that")
    elif command == "q":
        running = False
    else:
        print("Thats not a command")
    
    






