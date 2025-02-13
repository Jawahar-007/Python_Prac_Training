import array as arr

def find_indices(lst, target):
    #Dictionary to store the number and its index
    num_map = {}
    result = []
    for i, num in enumerate(lst):
        print("Debug: Iteration", i, "- Current number:", num)
        complement = target - num 
        print("Complement : ",complement)
        if complement in num_map:   
            for index in num_map[complement]:
                print("Debug: Found complement at index", index, "Pair:", [index, i])
                result.append([index,i])

        if num in num_map:
            num_map[num].append(i)
            print(" Appending index to existing key in num_map:", num_map)

        else:
            num_map[num] = [i]  # Store the index of the current number
            print("Creating new key in num_map:", num_map)

    print("Debug: Final result:", result)
    return result    #return the empty list if no pair was found	

num = arr.array('i',list(map(int,input("Enter the list of numbers seperated by spaces: ").split())))

# a = arr.array('i',num)
target = int(input("Enter the target number should be received after added: ")) 

print("Type of num got array: ",type(num))

print("Indices : ",find_indices(num,target) ,"\n Type of result : " , type(find_indices(num,target)))