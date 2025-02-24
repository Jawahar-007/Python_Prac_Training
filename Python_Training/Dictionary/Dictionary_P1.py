my_dict = {'name':'AA','age':23,'city':'San Francisco'}
my_dict['job'] = 'Engineer'
print("\n Added category in dictionary: ",my_dict)
my_dict.pop('age')
print("After Popping the [age]: ",my_dict)
my_dict['city'] = 'New York'
print("Updated dictionary of [city]: ",my_dict)
new_dict = {'country':'USA','hobby':'Dancing'}
my_dict.update(new_dict)
print("\nMerging the dictionaries: ",my_dict)

print("\nAccessing the dicts keys: ",my_dict.keys())
print("\n Accessing the dict values: ",my_dict.values())
print("\n Accesing the dict items: ", my_dict.items())

my_dict['height'] = 18.6
filtered_dict = {k:v for k,v in my_dict.items() if isinstance (v,float)}
print(filtered_dict)
my_dict.pop('height')

sorted_dict = dict(sorted(my_dict.items()))
print("\n Dictionary sorted with keys: ",sorted_dict)
sorted_by_values = dict(sorted(my_dict.items(),key= lambda item:item[1]))
print("\n Dictionary sorted by values: by string",sorted_by_values)
