class Variables:
    # Class variables
    year = 2025
    var1 = 1
    var2 = "two"
    var3 = 3.14
    var4 = [1, 2, 3]
    var5 = {"name": "John", "age": 30}
    var6 = True
    var7 = None
    var8 = (4, 5, 6)
    var9 = {7, 8, 9}
    var10 = "Hello, world!"

    def __init__(self):
        pass

    def operation1(self):
        # Return the value of var4
        return self.var4


if __name__ == '__main__':
    # Create an instance of the Variables class
    result = Variables()
    
    # Call the operation1 method
    result1 = result.operation1()
    
    # Create another instance of the Variables class
    variables1 = Variables()

    print("var8 value:", variables1.var8)
    print("Year:", Variables.year)

    # Iterate through and print the values returned by operation1
    for item in result1:
        print(item)
