class Dad:
   
    def action(self):
        print("Dad used to do sparring")
    
    # Private method to print a work ethics message
    def __Work_Ethics(self):
        print("Its a private function")

class First_Son(Dad):
    # Method to print a music-related message
   
    def start_music(self):
        print("First Son Starts singing")

   # Overriding the action method from Dad class
    def action(self):
        print("First Son Cooks well")
        # Call the action method from Dad class
        if super().action() :
            print("Son hides action")
        

class Second_Son(Dad):

    def start_dance(self):
        print("Second Son Dances well!!!!")
    def action(self):
        print("Second Son does the art well!!!")

        
son1 = First_Son()
# Call the action method on the instance
son1.action()
son1.start_music()
# Access the private method from Dad class using name mangling
son1._Dad__Work_Ethics()