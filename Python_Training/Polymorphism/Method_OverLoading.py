class Overloading:
    def __init__(self):
        pass

    # Method to add up to three numbers with default arguments
    def add(self, a=None, b=None, c=None):
        s = 0
        if a is not None:
            s += a
        if b is not None:
            s += b
        if c is not None:
            s += c
        return s

o = Overloading()

# Testing the add method with different number of arguments
print("BY 3 args ", o.add(12, 31, 21))  # output 64
print("BY 2 args ", o.add(12, 31))       # output 43
print("BY 1 args ", o.add(12))           # output 12

# Alternative method using variable-length arguments
# def add(self, *args):
#     return sum(args)