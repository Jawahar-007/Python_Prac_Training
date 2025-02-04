class Calculator_operations:

    def __init__(self,i=0):
        self.i = i

    def add(self,a,b):
        print(self.i)
        return a + b + self.i
    
    def sub(self,a,b):
        print(self.i)
        return a - b - self.i
    
    def mul(self,a,b):
        print(self.i)
        if self.i == 0:
            result = a*b
        else:    
            result = a*b*self.i
        return result
    
    def divide(self,a,b):
        print(self.i)
        if(a ==0 or b == 0 or self.i==0):
            return a/b
        else:
            return a/b/self.i
 
    def mod(self,a,b):
        print(self.i)
        if a ==0 or b == 0 and self.i==1 or self.i == 0:
            result = a % b
        else:
            result = a % b % self.i 
        return result
    
calc = Calculator_operations()

#calc.__init__(10,20)
add = calc.add(10,0)
sub = calc.sub(23,67)
mul = calc.mul(9,8)
div = calc.divide(7,7)
mod = calc.mod(8,3)
print(f"Addition: {add} \nDivision: {div}\nSubtract: {sub}\nMultiplication: {mul}\nModulus: {mod}")