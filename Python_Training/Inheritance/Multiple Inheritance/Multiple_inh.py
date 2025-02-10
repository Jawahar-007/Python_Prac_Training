class First_Son:
    def music(self):
        print("First Son loves music")
    def action(self):
        print("First Son plays cricket")

class Second_Son:
    def dance(self):
        print("Second Son loves dancing")
    def action(self):
        print("Second Son plays football")

class Mom(First_Son,Second_Son):
    def action(self):
        print("Mom loves to cook")
        super().action()
        print("Mom hides action")
        

    
mom = Mom()
mom.action()
mom.music()
mom.dance()    