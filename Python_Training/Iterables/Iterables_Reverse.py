class IteraReverse:
    def __init__(self,items):
        self.items = items
        self.index = len(items)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -=1
        return self.items[self.index]
    
rev_list = IteraReverse([10, 20, 30, 40])
for item in rev_list:
    print(item) 