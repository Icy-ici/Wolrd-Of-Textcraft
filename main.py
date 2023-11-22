#main.py  

from item import Item 
from character import Enemy, Friend
from room import Room
from attributes import Attribute 


#creating races
races = {"dwarf":"Children of the Titens they were to shape and guard the earth from deap within",
         "night elf":"One of the oldest races on Azeroth, Powerful and Mystical Race ",
         "gnome":"Excitable with an innate curiosity for anything mechanical. They are gadget hounds and good at it too",
          "human":"Proud hardworking people and the most versitile possible race",
        "tauren":"The Tauren revere the hunt and respect the bounty of thr land greatly",
         "orc":"The most scarred of races. Not quite bright but umatched in their cunning an d ferocity",         
         "undead":"Once normal human beings until the plague swept through their villages and turned them into the creatures they are today",
         "troll":"Barbarous and superstitious, they carry a seething hatred for all other races",
         }
print("Welcome to the World of Textcraft based of World of Warcraft (a few differant of my favourite expansions mixed together) \n \n ")
while True:
    print("World of Texcraft is built on war and conflict. \nThe races have found themselves choosing sides and allying in order to stay safe from their many enemies and the creaturs that roam it. \nTwo factions have come of this; the horde and the alliance. \nThe Alliance consists of the Human, Night Elf, Dwarf and Gnome, while the Horde consits of the Orc, Troll, Undead and Tauren. \nChoosing a faction means choosing a side in the war so consider carefully. \n \n \n")
    for character in races.items():
        print(character[0].capitalize(),":",character[1])
        
    choice = input("Who would you like to be > ").lower().strip()
    if choice in races.keys():
        chosenCharacter = races[choice]
        break
print(" \n \n Worthy Choice \n ")


#creating classes
classes = {"druid":"The keepers of Nature, they can transform into many differant creatures",
           "hunter":"These species care nothing for the war between Horde and Alliance; their lives are fillled with their own struggle to find food and live from day to day",
           "mage":"Called by magic, they dedicate their lives to practicing, studying and spreading it throughout the world of Azeroth",
           "paladin":"The champions of Light, God and dedicated fighters",
           "priest":"Holy and Shadow are elemental forces of the gods. These are the individualsto seek to use them within the world",
           "rogue":"All that it takes to be a Rogue is an individual nature drawn to working behind the scenes and a willingess to let certain laws and strictures slide",
           "sharman":"The spiritual leader of their clans and tribes, guiding the people to their destinies",
           "warlock":"Mages but they use the dark chaotic magic",
           "warrior":"Anyone interested in tactics and the feel of melee battle can find satisfaction and happiness in being a warrior"
           }
print("\n \nNow that you have chosen you race, its time to choose a class - classes determine what kind of player you are and what you want to be\n")
for player in classes.items():
    print(player[0].capitalize(),":",player[1])
    
chosenPlayer = classes[input("\nWho would you like to choose > ").lower()]
print("\n \n Worthy Choice \n")



#create rooms
Azeroth = Room("Azeroth")
Azeroth.description = "A dangerous, beautiful, magical, and inspiring world. \nA world filled with discovery, innovation, and wonder. \nA world worth fighting for \n"

Barrens = Room("Barrens")
Barrens.description = "One of the largest zones and a central hub for travel between regions \n "

Kalmidor = Room("Kalmidor")
Kalmidor.description = "A wide deserted area consisting of many towns but vast open desert space \n"

Easternkingdoms = Room("Eastern Kingdoms")
Easternkingdoms.description = "The home of the undead \n"

Lorderon = Room("Tristfall Glades")
Lorderon.description = "The home of the undead, caught between the mindless death of the scourage and the equal foulness of life they happily left behind \n"

Pandaria = Room("Pandaria")
Pandaria.description = "A legendary place of bamboo forests and the mysterious pandaren empire"

Northrend = Room("Northrend")
Northrend.description = "The northern icy continent of Azeroth"

Crossroads = Room("Crossroads")
Crossroads.description = "The Largest town in the Barrens"

Icecrown = Room("Ice Crown Glacier")
Icecrown.description = "The home of the Litch King"

Zandalar = Room("Zandalan")
Zandalar.description = "Island in the southern seas, invaded by the blood trolls"

#linking rooms
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
Chromie.conversation = "Hello Friend: Your quest is to explore Azeroth and clear the places from the bad \nA good place to start are the Tristfall Glades \nGood Luck"

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

#Small Instructional Piece
print("In this game, you have a few options when entering an area, you can either fight or talk to a charcter. \nYou can walk between areas by typing the direction. \nIf you see any items lying around, its a good idea to take them. \nYou can find differant attributes for your character around - type claim to claim them. \nAfter killing an enemie, typing loot is a good idea to see if they dropped anything for you.\nTo find out what items and attributes you have press 'b' to acsess your action bar. \nTalking to Chromie will give you your first quest!")


#--------------------------------------MAIN LOOP--------------------------------------------#

while running:
    

    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        
        
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
            
    elif command =="fight":
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
                
                
    elif command =="take":
        if current_room.item is not None:
            bag.append(current_room.item)
            print(f"Item added to action bar")
            current_room.item = None
        else:
            print("I can't take that")
     
    elif command =="claim":
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
                
    elif command =="loot":
        if current_room.item is not None:
            bag.append(current_room.item)
            print("You have looted the Death Night, finding a sword, you can acsess this in your action bar")
            current_room.item = None 
        else:
            print("I cant loot that")
        
            
        
    elif command == "quit":
        running = False
    else:
        print("Thats not a command")
    
    






