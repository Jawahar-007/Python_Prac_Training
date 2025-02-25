class Fibonacci:
    def __init__(self,max_terms):
        self.max_terms = max_terms
        self.a , self.b = 0 , 1
        self.count =0 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_terms:
            raise StopIteration
        self.count += 1
        fib = self.a
        self.a , self.b = self.b , self.a + self.b
        return fib
    
my_nums = Fibonacci(6)
for num in my_nums:
    print(num)
