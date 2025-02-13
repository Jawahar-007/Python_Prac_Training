import array as arr

def find_indices(lst, target):
    #Dictionary to store the number and its index
    num_map = {}
    for i, num in enumerate(lst):
        complement = target - num 
        if complement in num_map:
            return [num_map[complement] , i] #Return indices of two number
        num_map[num] = i  # Store the index of the current number

    return [] #return the empty list if no pair was found

num = arr.array('i',list(map(int,input("Enter the list of numbers seperated by spaces: ").split())))

# a = arr.array('i',num)
target = int(input("Enter the target number should be received after added: ")) 

print("Type of num got array: ",type(num))

print("Indices : ",find_indices(num,target) , " Type of result : " , type(find_indices(num,target)))