class Itera:
    def __init__(self,start,end,step):
        self.current = start
        self.end = end 
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

cust_range = Itera(1,10,2)

for num in cust_range:
    print(num)