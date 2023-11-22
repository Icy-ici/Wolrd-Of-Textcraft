#characters.py

class Character():
    def __init__(self,name):
        #initiasise the character variable
        self.name = name
        self.description = None
        self.conversation = None
    def describe(self):
        print(f"The {self.name} is here - what would you like to do > \n")
        
    def fight(self, item):
        print(f"{self.name} doesnt want to fight you")
        
    def talk(self):
        #talking to the character
        if self.conversation is not None:
            print(f"{self.name}: {self.conversation}")
        else:
            print(f" {self.name} wont talk to you ")
            
class Friend(Character):
    def __init__(self,name):
        #initialise the friend object by calling function of parent classes
        super().__init__(name)
    def fight(self, item):
        print(f"{self.name} doesnt want to fight you")
    
    
class Enemy(Character):
    def __init__(self,name):
        # initialise the emeny object by calling the function of parents
        super().__init__(name)
        self.weakness = None
        self.loot = None
        self.description = None
    
        
    
    
    def fight(self,item):
        #figthts the enemy with the item will determine whether they suvive
        if item == self.weakness:
            print(f" You have slain them")
            
            
            

            return True
        
        else:
            print("You have been killed")
            return False 
          
            
        
        
        
                            