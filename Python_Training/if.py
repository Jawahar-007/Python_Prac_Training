
def n_divisibles(list,num):
     
    divisibles = []
    for i in list:
        #check the number is divisible (42%6)
        if i % num == 0:
            divisibles.append(i)
    print(f"Divisibility numbers of {num}:\n")
    return divisibles

# def is_prime(n):
#     if n>=1:
#         for i in range(2,n):
#             if(i%n == 0):
#                 break
#         return True
#     else:
#         return False

l1 = []
n = int(input("Enter the number of elements:"))
for _ in range(n):
    l1.append(int(input()))
n1 = int(input("Enter the number to be checked for divisiblity of the List:"))
print(n_divisibles(l1,n1))