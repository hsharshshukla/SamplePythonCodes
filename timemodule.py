###Keeping Time, Scheduling Tasks, and Launching Programs
#Time module
import time

#time.time()
print(time.time())  #epoch time

#time.ctime()
print(time.ctime()) #local time in string representation
print(time.ctime(time.time()))

##time.sleep()
# time.sleep(2)
# print("tick Tock")

#round epoch time
print(round(time.time(),2))

