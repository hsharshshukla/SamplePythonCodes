import subprocess
# subprocess.Popen("C:\\Windows\\System32\\calc.exe") # opens Calculator
#
# calproc  = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# print(calproc.poll() ==None)
#
# print(calproc.wait()) #Doesnt return until calc closes
#
# print(calproc.poll())


#passing commnadline argument
notepadproc = subprocess.Popen(['C:\\Windows\\notepad.exe','F:\\test.txt']) #first launch notepad, then open file
