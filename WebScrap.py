# print("Hello Sonya")
# a= 5;
# b=5;
# r = a+b;
# print(r)
# for x in range(100):
#     print(x)


# message = "name is good"
# print (message)
#
# msg = "all is good"
# print(msg)
#
# msg="alls good"
# print(msg)
# msg1='Well"fargo"'  # prints -> Well"fargo"
# print(msg1)

# String
#
# name = "tanya tripathi"
# print(name)
#
# name = name.title()
# print("After title method operation name changes : "+name)
#
# print(name.lower())
# print(name.upper())

#
# first_name = "tanya"
# last_name = "tripathi"
# full_name = f"{first_name} {last_name}"
# # print(full_name)
# print(f"Hello! {full_name.title()}!")

#
# first_name ="shyam"
# last_name = "sundar"
# full_name = "{} {}".format(first_name,last_name)
# print(full_name)

# name = "\tHarsh" 	#adds a tab
# print(name)


# name = "Harsh\nShukla"
# print(name)
#
# name = 'python  '
# print(name)
# print(name.rstrip())


# #Numbers
# a = 2 + 3 * 4  #14
# print(a)
#
# b = (2+3)*4    #20
# print(b)
#
# c = 1+(3-1)*4    #9
# print(c)


# x, y, z = 0, 1, 2
# print(z, y, x)

# list
# genre = ['Action','Comedy','Drama']
# # print(genre[-2].upper())
#
# message = f"My Favourite genre is {genre[2].upper()}"
# print(message)
# genre[2]= 'Crime'
# message = f"My Favourite genre is {genre[2].upper()}"
# print(message)
# genre.append('Thriller')
# print(genre)
#
# genre.insert(1,'Drama')
# print(genre)
#
# del genre[3]
# print(genre)
#
# genre.pop()
# print(genre)
#
# genre.pop(1)
# print(genre)
#
# genre.remove('Action')
# print(genre)

# Organizing List
#Sorting sort()
# genre = ['scifi','action', 'thriller', 'comedy', 'drama']
# print(genre)
#
# genre.sort()
# print(genre)
#
# genre.sort(reverse=True)
# print(genre)

#sorted()
# genre = ['scifi','action', 'thriller', 'comedy', 'drama']
# print(genre)
# print(sorted(genre))
# print(genre)
# genre.reverse()
# print(genre)
#
# print("\nfor loop\n")
# for gen in genre:
#     print(gen)

# for gen in genre:
#     print(f"{gen.title()}, is good Genre\n")

#Numerical List
# number = list(range(6))
# print(number)
# number = list(range(1,5))
# print(number)

# squares = [value**2  for value in range(1,11)]
#
# print(squares)
# sqnum = squares[0:3]
# print(sqnum)
# sqnum = squares[:3]
# print(sqnum)
#
# for sq in squares[0:5]:
#     print(sq)
#
# sqnum = squares[:]
# sqnum.append(121)
# print(sqnum)
# print(squares)
#
# squares = [value**2  for value in range(1,11)]
# sqnum = squares[:]
# print(sqnum)
# sqnum.append(121)
# print(sqnum)
# print(squares)
#
# sqnum = squares
# sqnum.append(121)
# print(sqnum)
# print(squares)

#####Tuple
# dimension = (500,30)
# print(dimension[0],end='   ')
# print(dimension[1])
# dimension[0]=230  # gives error assignment of item not supports as tuples are immutable
# print(dimension)
#
# for dim in dimension:
#     print(dim)


####If Statement
# squares=[value**2 for value in range(1,11)]
# for sqnum in squares:
# 	if sqnum==81:
# 		print("Square of 9 : " , sqnum)
# 	else:
# 		print(sqnum)
#
# if(81 in squares):
#     print("square of 9  is in list")
#
# if(88 not in squares):
#     print("88 is not square")


#####Boolean Expression
# car='audi'
# print("Is car=='audi'? I predict True")
# print(car=='audi') #prints True

#list empty
# samplelist  = []
# if samplelist:
# 	print("All good")
# else:
# 	print("list is Emtpy")

###Dictionary

# cse_syllabus = {'sem1': 'math', 'sem2': 'algo', 'sem3': 'ds'}
# print(cse_syllabus)
#
# # print(cse_syllabus[0])  #Wrong gives error
# print(cse_syllabus['sem1'])  #prints math
# # print(cse_syllabus['math']) #wrong gives error
#
# cse_syllabus['sem4']='networking'
# print(cse_syllabus)
# print(cse_syllabus['sem4'])

# cse_sylalbus={}
# cse_syllabus = {'sem1': 'math', 'sem2': 'algo', 'sem3': 'ds'}
# cse_syllabus['sem1'] = 'm1'
# print(cse_syllabus)
#
# del cse_syllabus['sem1']
# print(cse_syllabus)
#
# cse_syllabus['sem1']=''
# print(cse_syllabus)
# print(cse_syllabus.get('sem1'))
# str = cse_syllabus.get('sem5','No value assigned')
# print(str)

##Loop - Dictionary
# cse_syllabus = {'sem1': 'math', 'sem2': 'algo', 'sem3': 'ds'}
# for key, value in cse_syllabus.items():
#     print("\nkey : ",key,end=" ")
#     print("    value : ",value)
#
# for key in cse_syllabus.keys():
#     print(key)
#
# for value in set(cse_syllabus.values()):
#     print(value)
#
# for key in sorted(cse_syllabus.keys()):
#     print(key)

###Nesting
##dictionary in a list
# cse_syllabus = {'sem1': 'math', 'sem2': 'algo', 'sem3': 'ds'}
# ec_syllabus = {'sem1': 'm1', 'sem2': 'devices'}
# elect_syllabus = {'sem3': 'English', 'sem5': 'eee'}
# syllabus = [cse_syllabus, ec_syllabus, elect_syllabus]
# # print(syllabus)
# # print(syllabus[0]['sem2'])
#
# for syl in syllabus:
#     print(syl)


##list in a dictionary
# cse_syllabus = {'sem1': ['English', 'mechanics', 'thermodynamics']}
# print(cse_syllabus)

##Dictionary in a dictionary
# elec_syllabus = {'sem3': {'sports': 'Footbal', 'math': 'm3'}, '': ''}
# print(elec_syllabus)

####Input Function
# message = input("hi Bro : ")
# print("m good")
#
# age = input("How old are you : ")
# if(age>25):
#     print(age)
# else:
#     print("Age is non numeric")
# print(int(age))

####While loop
# count = 1
# while count <= 5:
#     print(count)
#     count +=1

#using break keyword to exit loop
# prompt = "\nPlease enter places you have visited"
# prompt += "\n(Enter 'quit' when you are finished) : "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I have visited and liked {city.title()}!")

##Using continue keyword
# prompt = "\nPlease enter places you have visited"
# prompt += "\n(Enter 'quit' when you are finished)"
#
# while True:
#     city = input(prompt)
#
#     if city != 'quit':
#         print(f"I have visited and liked {city.title()}!")
#         continue
#     else:
#         print("Thanks for playing the game")

#Filling dictionary with user input

# responses = {}
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name : ")
#     fav_mountain = input("Which mountain would you like to climb?  ")
#
#     responses[name] = fav_mountain
#
#     repeat = input("Do wanna play more Type Y/N : ")
#     if repeat == 'N':
#         polling_active = False
#
# print(responses)

###FUNCTION
#BASIC
# def greet_user():
#     print("Hello!")
#
# greet_user()

#passing argument to function
#arguments and parameters are used interchangeably
# msg = "Hello Guys!"
# def say_hello(greet):
#     print(greet)
#
# say_hello(msg)

##passign with argument with name
# def printfullname(first_name, last_name):
#     print(first_name + last_name)
#
#
# printfullname(last_name="Shukla", first_name="Harsh")

#Default argument value
# def flight(source, destination='New Delhi,India'):
#     print(f"Flight is from {source.title()} to {destination.title()}")
#
#
# flight(source='London,UK')

#Return value
#
# def add(first_number, second_number):
#     print(first_number + second_number)
#
# sum = add(20, 10)
# sum = add(10, 15)

#Returning Dictionary
# def full_name(first_name, last_name):
#     person = {'first': first_name.title(), 'last': last_name.title()}
#     return person
#
# MyName = full_name('harsh', 'shukla')
# print(MyName)

#Integer in def
# a = 50
# def modify(a):
#     a += 5
#     print(a)        # prints -> 55
# modify(a)
# print(a)            #prints -> 50

#List in def
# names = ['Harsh', 'Shukla', 'Tanya']
#
# def modify(names):
#     names.pop()
#     print(names)
#
# modify(names)
# print(names)

#dictionary in def
#
# prices = {'book': '100', 'fruit': '50', 'vegetable': '150'}
#
# def modify(prices):
#     prices['book'] = '120'
#     print(prices)
#
# modify(prices)
# print(prices)

# Passing an Arbitary Number of Arguments - overloading
#sample code to display
# def display_numbers(*a):
#     print(a)
#
# display_numbers(1)
# display_numbers(1, 2, 6, 7, 8)

#sample code to add numbers

# def add_numbers(*a):
#     sum=0
#     for x in a:
#         sum += x
#     print(sum)
#
# # add_numbers(1)
# add_numbers(1,2,6,7,15) # prints->31


####Class
# class Dog:
#         def __init__(self,name,age):
#             self.name = name
#             self.age = age
#
#         def sit(self):
#             print(f"{self.name} is Sitting")
#
#         def roll_over(self):
#             print(f"{self.name} has rolled over")
#
# mydog = Dog('lab',3)
# mydog.sit()
#
# mydog.roll_over()
#
# print("name : ",mydog.name)


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_car_details(self):
#         return (f"{self.year.title()} {self.make.title()} {self.model.title()}")
#
#
# my_new_car = Car('audi','a4','2021')
# print(my_new_car.get_car_details())

# class Car:
#     def __init__(self):
#         pass
#     # self.make = make
#     # self.model = model
#     # self.year = year
#
#
#     def get_car_details(self,make,model,year):
#         return (f"{year.title()} {make.title()} {model.title()}")
#
# car = Car()
# print(car.get_car_details('audi','a4','2021'))


#Inheritance
# class ElectricCar(Car):
#
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 75
#
#     def describe_battery(self):
#         print(f"Battery is of {self.battery_size}-KWh")
#
# myTesla = ElectricCar('tesla', 'model s', '2021')
# # print(myTesla.get_car_details())
#
# myTesla.describe_battery()


####File Reading
# with open('F:\\test.txt') as file_object:
#     contents = file_object.read()
#
# # print(contents)
#     count =1
#     # for line in file_object:
#     for line in contents:
#         print(count,". ",line)
#         count +=1
#


####Writing to File
#Write to Empty file
# with open('F:\\sample.txt','w') as file_object:
#     file_object.write("My City is Bangalore")


#below code will override the file again and again, this will not append
# with open('F:\\sample.txt', 'w') as file_object:
#     for i in range(100):
#         msg = "CountXyez : " + str(i) +"\n"
#         file_object.write(msg)

#File will appended with new information , a stands for append
# with open('F:\\sample.txt', 'a') as file_object:
#     for i in range(100):
#         msg = "CountXyez : " + str(i) +"\n"
#         file_object.write(msg)

#### Exception i.e. use try-except block
#
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Division Zero invalid operation")



### try-except-else Block
# a=20
# b=5
# try:
#     answer = a / b
#
# except ZeroDivisionError:
#     print("Division Zero invalid operation")
#
# else:
#     print(answer)   #prints 4.0


###Storing Data ; json.dump(filename,data)
# import json  # import json module
#
# numbers = [2, 4, 5, 8, 11]
#
# filename = 'F:\\numbers.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)


###Reading data ; json.load(filename)
# import json
#
# filename = "F:\\numbers.json"
# with open(filename) as f:
#     a = json.load(f)
#
# print(a)


###Unit Test
#fun below, called for unit testing in Unittest.py
def fullname(first,last):
    fullname=f"{first} {last}"
    return fullname.title()

