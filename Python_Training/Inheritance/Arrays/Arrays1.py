import array as arr
l = {1,2,3,4,5,5,3,1}

a = arr.array('i',l)
print(a)

sliced_array = a[3:4]
print(sliced_array)

sliced_array = a[5:]
print(sliced_array)

