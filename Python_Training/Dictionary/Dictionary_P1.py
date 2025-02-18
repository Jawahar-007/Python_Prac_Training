# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 1. Adding items
my_dict['job'] = 'Engineer'
print("After adding an item:", my_dict)

# 2. Removing items
my_dict.pop('age')  # Removes key 'age'
print("After removing an item:", my_dict)

# 3. Updating values
my_dict['city'] = 'San Francisco'
print("After updating a value:", my_dict)

# 4. Merging dictionaries
new_dict = {'country': 'USA', 'hobby': 'Reading'}
my_dict.update(new_dict)
print("After merging dictionaries:", my_dict)

# 5. Accessing keys, values, and items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 6. Filtering a dictionary (e.g., keeping only items with string values)
filtered_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("Filtered dictionary (only strings):", filtered_dict)

# 7. Sorting a dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))
print("Dictionary sorted by keys:", sorted_dict)

# Sorting a dictionary by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_by_values)