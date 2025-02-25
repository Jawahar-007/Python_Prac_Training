names = ["Alice","Bob"]
age = [18,20]
for name,age in zip(names,age):
    print(f"{name} {age}")

from itertools import count,chain,