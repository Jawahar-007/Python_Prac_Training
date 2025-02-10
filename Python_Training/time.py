import time

start = time.time()
print("Start Time: ",start)
for i in range(0,5):
    print (i)
    time.sleep(3)
end_time = time.time()
print(" End _ TIme : ",end_time)
elapsed_time = end_time - start
print("\n Elapsed Time : %s" % elapsed_time)
