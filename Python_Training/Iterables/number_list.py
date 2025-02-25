# class Iterables_Prac:
#     def __init__(self,items):
#         self.items = items
#         self.index = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         if self.index == 0:
#             value = -1
#         elif self.index == len(self.items) -1:
#             value = self.items[self.index]
#         else:
#             value = self.items[self.index - 1] + self.items[self.index]

#         self.index += 1
#         return value 

def generator_iterables(items):
    for i in range(len(items)):
        if i == 0: 
            yield -1
        elif i == len(items) - 1:
            yield items[i]
        else:
            yield items[i - 1] + items[i]
# Create an instance of IterablesTest with the given list
cut_list = [2,7,1,8]

# Iterate through the iterable object
for num in generator_iterables(cut_list):
    print(num)
