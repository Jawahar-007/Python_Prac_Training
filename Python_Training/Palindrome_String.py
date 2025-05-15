string = input("Enter a Palindrome (e.g., MOM,REFER)")
if(string == string[::-1]):
    print("Palindrome!")
else:
    print("Non- Palindrome!!")

def palind_num(num):
    
    temp = num 
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 +dig
        num = num // 10
    if (temp == rev):
        print("Palindrome!!")
    else:
        print("Non - Palindrome!!!")

num = int(input("Enter the value: "))
palind_num(num)