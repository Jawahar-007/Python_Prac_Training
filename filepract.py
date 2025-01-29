# import pandas as pd
# import re

# #Read the CSV file
# csv_file = "london_houses - Copy.csv"
# data = pd.read_csv(csv_file)

# #Save the Data_Frame to a file
# txt_file = "london_houses_copy.txt"
# data.to_csv(txt_file,sep="\t",index=False)

# print(f"CSV File '{csv_file}' has been successfully converted to TXT file '{txt_file}'.")

# #file reading starts here
# i = 1
# with open(txt_file) as file:

#     for e_line in file:
#         print(f"{i} - {e_line}")

class Calculator_operations:

    def __init__(self,i=0):
        self.i =i

    def add(self,a,b):
        print(self.i)
        return a + b+ self.i
    
    def sub(self,a,b):
        print(self.i)
        return a - b - self.i
    
    def mul(self,a,b):
        print(self.i)
        return a*b*self.i
    
    def divide(self,a,b):
        if(a ==0 or b == 0 or self.i):
            return "Division by zero is not allowed"
        print(self.i)
        return a/b/self.i
    
    def mod(self,a,b):
        print(self.i)
        if(a ==0 or b == 0 or self.i == 0):
            return "Modulus by zero is not allowed"
        return a % b % self.i 
    
calc = Calculator_operations(2)

#calc.__init__(10,20)
add = calc.add(10,0)
sub = calc.sub(23,67)
mul = calc.mul(9,8)
div = calc.divide(7,7)
mod = calc.mod(8,3)
print(f"Addition: {add} \nDivision: {div}\nSubtract: {sub}\nMultiplication: {mul}\nModulus: {mod}")