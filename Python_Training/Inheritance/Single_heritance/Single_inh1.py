class Dad:

    def __init__(self):
        print("Dad Initialise")
   
    def action(self):
        print("Dad used to do sparring")
    
    # Private method to print a work ethics message
    def __Work_Ethics(self):
        print("Its a private function")

class First_Son(Dad):
    
    def __init__(self):
        print("First Son class Initialised")
   
    def start_music(self):
        print("First Son Starts singing")

   # Overriding the action method from Dad class
    def action(self):
        print("First Son Cooks well")
        # Call the action method from Dad class
        super().action()
        print("Son hides action")


son = First_Son()
son.action()