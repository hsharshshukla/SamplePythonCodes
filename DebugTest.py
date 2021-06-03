import logging
logging.basicConfig(filename='DebugTest.txt',level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')

a  = 10
logging.debug('first no : ' + str(a))
b= 76
logging.debug('second no : ' + str(b))

sum = a+b


logging.debug('Sum of 2 numbers : ' + str(sum))
print(sum)