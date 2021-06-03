import time, datetime,threading

print("Start of Program")

def takeANap():
    time.sleep(5)
    print('Wake Up!')

threadobj = threading.Thread(target=takeANap)
threadobj.start()

print('End of Program')

