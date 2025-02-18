student = ['Bob','David','Alice','Charlie']

sorted_student = sorted(student, key = lambda x: x[1:])
print(sorted_student[1:])

prime_nos = lambda x:all(x % i != 0 for i in range(2,x))
y = int(input("Enter the Number to check for Prime number: "))
print(f"Prime Number of {y} is {prime_nos(y)}") 

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
days = filter(lambda day: day if len(day) == 6 else '',weekdays)

for d in days:
    print(d)
