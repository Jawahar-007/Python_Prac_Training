class Transport:
    insured = "insured"
    def __init__(self,cusname,cost,insured,type):
        self.cusname = cusname    
        self.cost = cost
        self.type = type
        self.insured = insured

    def test(self,model):
        return f"{self.cusname} has opted {model} for Test Drive"
    
    def sales(self,model):

        return f"{self.cusname} has opted {model} for Sales"

class Car(Transport):
    def accelerate(self):
        return f"{self.cusname} has opted for driven for test Drive"
    
testCar1 = Car()
print(testCar1.accelerate("Ram",))
