import array as arr

def sorting_list(input_list):
    sorted_list = []
    for i in input_list:
        sorting_length = len(sorted_list)
        if i < 0:
            sorted_list.insert(sorting_length, i)
        else:
            sorted_list.insert(0, i)
    return sorted_list

def display_array_and_list(input_list):
    # Original list
    print(f"Input List Entered {input_list}")
    
    # Processing list
    sorted_list = sorting_list(input_list)
    
    # Creating an array
    array_data = arr.array('i', input_list)
    
    # Slicing operations
    sliced_array1 = array_data[3:4]
    sliced_array2 = array_data[5:]
    
    # Reversing array
    array_data.reverse()
    #Removing excessive number 1 in the list ; Should pass some args in remove()
    array_data.remove(1)
    array_data.pop()
    
    # Displaying results
    print("Original List:", input_list)
    print("Processed List (Sorted List):", sorted_list)
    print("Original Array:", array_data.tolist())  # Convert array to list for better display
    print("Sliced Array [3:4]:", sliced_array1.tolist())
    print("Sliced Array [5:]:", sliced_array2.tolist())
    print("Reversed Array:", array_data.tolist())

input2_array  = list(map(int,input("Enter the array number leaving spaces in a line: ").split()))
print("Array input 2: ", input2_array)
# Input and function call
input_list1 = [-1, 1, -2, 3, -4, 5, 5, -3, 1]

display_array_and_list(input_list1)