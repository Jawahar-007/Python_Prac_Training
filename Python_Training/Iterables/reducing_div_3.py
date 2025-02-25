class redudiv3:
    def __init__(self,items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.items):
            value = self.items[self.index]
            self.index += 1
            if value %3 !=0:
                return value
        raise StopIteration

def reduduv3(items):
    for i in items :
        if i % 3 !=0:
            yield i

    
ww = [1,3,6,9,7,5,10]
result = list(reduduv3(ww))
print(result)