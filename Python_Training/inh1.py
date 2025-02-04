class Dad:
    def action(self):
        print("He used to do sparring")
    
    def __private_function(self):
        print("Its a private function")

class First_Son(Dad):
    def start_music(self):
        print("Starts singing")

    def action(self):
      
        print(self.action())
        print("Used to Cook")

son1 = First_Son()
son1.action()