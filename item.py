#item.py

class Item():
    
    def __init__(self,name):
        #initialist the item class
        self.name = name.lower()
        self.description = None
    
    def describe(self):
        print(f"There is {self.name} here,  what will you do with it >")
    
    