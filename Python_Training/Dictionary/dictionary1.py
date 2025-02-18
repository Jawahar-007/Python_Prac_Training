# key = ['Rogan','Kamal','Santhosh']
# values = ['Python','React','NodeJs']

# data = zip(key,values)
# print(data)
from collections import defaultdict

class MyDefaultDict(defaultdict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

tuple_list = [("A",10),("B",4),("A",5),("C",7),("B",1),("C",8)]

grouped_data = MyDefaultDict(list)

for key,value in tuple_list:
    grouped_data[key].append(value)

print(grouped_data)
print(grouped_data['C'])

grouped_data = {k: sum(v) for k , v in grouped_data.items()}

print(grouped_data)
print(grouped_data.get('D', "Key 'D' is missing"))  # Example of accessing a missing key