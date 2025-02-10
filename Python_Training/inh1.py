class Dad:
   
    def action(self):
        return "Dad used to do sparring"
    
    def sports(self):
        print("Dad loves sports")
    # Private method to print a work ethics message
    def __Work_Ethics(self):
        print("Its a private function")

class First_Son(Dad):
    # Method to print a music-related message
   
    def start_music(self):
        print("First Son Starts singing")

   # Overriding the action method from Dad class
    def action(self):
        
        return "First Son Cooks well"
      #  Call the action method from Dad class
        # if super().action() is not None:
        #     print("Son hides action")
       

class Second_Son(Dad):
    
    def start_dance(self):
        print("Second Son Dances well!!!!")
    def action(self):
        print("Second Son does the art well!!!")

class Mom(First_Son,Second_Son):
    def __init__(self):
        super().__init__()
        print("Mom initialised")
    def action(self):
        
        if super().action() is not None:
            
            print ("Super class of Mom Action()", end=":  ")
            super().action()
        else:
            print("Mom is a great cook")
        

        
son1 = First_Son()
son2 = Second_Son()


print("Call the action method on the instance son1",end=": ")
son1.action()
son1.start_music()
print("Access the private method from Dad class ",end=": ")
son1._Dad__Work_Ethics()
# print(f"Status of Dad: {son2.action()}")
# print(son2.action_dad())
son2.start_dance()


mom1 = Mom()
mom1.action()
mom1.start_music()
mom1.sports()