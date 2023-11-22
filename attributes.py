#attributes.py

class Attribute():
    
    def __init__(self,name):
        #initialist the attribute class
        self.name = name.lower()
        self.description = None
        
    def describe(self):
        print(f"There is {self.name} here,  what will you do with it > \n ")