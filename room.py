#room.py

class Room():
    def __init__(self,room_name):
        
        #initialise the room object
        
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.attribute = None 
        
        
        
    def describe(self):
        #display a descriton of the room
        print(f" \n You're at {self.name} \n")
        print(self.description)
        if self.character is not None:
            self.character.describe()
        if self.item is not None:
            self.item.describe()
        if self.attribute is not None :
            self.attribute.describe()
        
            
        
        for direction in self.linked_rooms:
            print(f"To the {direction} is {self.linked_rooms[direction].name}")
        
    def link_rooms(self, room_to_link, direction):
        #links the provided room in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
        
    def move(self, direction):
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        print("That way is foreign territory, stay out")
        return self
            
            