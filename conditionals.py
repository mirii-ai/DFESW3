# var1 = "Brian" #this has to be brian for the code to work
# dictionary = {'key':'value', 'amelia':'sommer', 'amazing':'not cool', 'teacher':'leon', 'assistant':'brian'}

# if 'not cool' in dictionary.values():
#     print("not cool is in the values.")

# if not (var1 != "Brian" or not "leon" in dictionary.values()):
#     print("Leaon is in the list of values.")

# print("this line will always print")

# grade = int(input("Please type the mark of the test." ))

# if grade > 85:
#     print("DISTINCTION")
# elif grade >= 65 and grade <= 85:
#     print("PASS")
# else:
#     print("FAIL")


# if grade > 85:
#     print("DISTINCTION")
# if grade >= 65 and grade <= 85:
#     print("PASS")
# if grade < 65:
#     print("FAIL")

# inputNumVar = int(input("Type a whole number please. "))
# while inputNumVar > 0:
#     print(inputNumVar)
#     inputNumVar = inputNumVar - 1

# numvar2 = int(input("Type another number please. "))
# resultVar = 1
# while numvar2 > 0:
#     resultVar = resultVar * numvar2
#     numvar2 = numvar2 - 1
# print(resultVar)

#--------------------------------------

# DICTIONARIES

# dictionary = {'name':'amelia', 'size':'small', 'age':'sort of young'}
# for thingsVar in dictionary:
#     print(thingsVar + " is the key, and the value is: " + dictionary[thingsVar])
#--------------------------------------

#QA EXERCISES
# names = []
# i=0
# while i < 5:
#     name = input("Please type your name here! ")
#     names.append(name)
#     i += 1

# for name in names:
#     print(name + " is awesome!!")

#--------------------------------------
##the following for loop goes between the range of 10 and 21, printing i at intervals of 2
# for i in range (10,21,2):
#     print(i)

#--------------------------------------
#Checking if a word is a palindrome or not
#--------------------------------------

# userString = input("Please type a word here. ")
# reverseString = userString[::-1] #this reverses the order of a word

# if reverseString == userString:
#     print("This is a palindrome! Conrats!")
# else:
#     print("This word is not a palindrome.")

##ANOTHER WAY TO REVERSE A WORD:
# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1): #The -1 takes one off the length, the other -1 is the end point, the final -1 is the step
#   print(word[char], end="")
# print("\n")

#--------------------------------------
#--------------------------------------
# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = 5

# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")
# ##now print the same backwards
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")

#--------------------------------------
#--------------------------------------
# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# choice = input("Convert from Celcius or convert from Farenheit? c / f ")
# if choice == "c":
#     tempC = int(input("Please type the temperature degree in Celcius. "))

#     tempF = ((tempC/5)*9) + 32
#     print(str(tempC) + " degrees Celcius is " + str(tempF) + " degrees Farenheit.")
# elif choice == "f":
#     tempF = int(input("Please type the temperature degree in Farenheit. "))

#     tempC = ((tempF - 32)/9)*5
#     print(str(tempF) + " degrees Farenheit is " + str(tempC) + " degrees Celcius.")
# else:
#     print("You didn't type a registered character. Please go back and type either c or f.")

#--------------------------------------
#--------------------------------------
# Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# length = len(numbers)
# evennumbers=0
# oddnumbers=0
# for i in range(length):
#     if i % 2 == 0:
#         evennumbers += 1
#     else:
#         oddnumbers +=1

# print("Even numbers: " + str(evennumbers))
# print("Odd numbers: " + str(oddnumbers))


#--------------------------------------
#--------------------------------------
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).

# i = 1500
# divisible = []

# while i in range(1500,2700,1):
#     if i % 7 == 0 and i % 5 == 0:
#         divisible.append(i)
#     i += 1

# print(divisible)



#--------------------------------------
#--------------------------------------
#--------------------------------------
#yet another way of reversing a string
# inputted = str(input("Insert 9 number?"))

# strlen = len(inputted)

# slicedString = inputted[strlen::-1]
# print(slicedString)

# palinVar = input("TYPE: ")

# numChars = len(palinVar) -1
# raVnilap = ''

# while numChars >= 0:
#     raVnilap = raVnilap + palinVar[numChars]
#     numChars -= 1 #the opposite =- will erase the contents of the variable and set it to whatever is there

# if raVnilap == palinVar:
#     print("PALINDROME")
# else:
#     print("zan'nen")

#-----------------
## negative indexing.
# t = 'abcd'
# print(t[-1]) #returns d
# print(t[:-1]) # returns abc

# testVar = input('TEMPIN: ') #whatever
# lastIndex = len(testVar) - 1
# print(testVar[lastIndex]) #prints 'r'
# print(testVar[0:(lastIndex)]) #prints 'whateve'

#--------------------------------------
#--------------------------------------

#Write a Python program to guess a number between 1 to 9.
#Note : User is prompted to enter a guess. 
# #If the user guesses wrong then the prompt appears again until the guess is correct, 
# #on successful guess, user will get a "Well guessed!" message, and the program will exit.

# import random
# random_num = random.randint(1,10)
# guess = int(input("Please type a guess. "))

# while random_num != guess:
#     guess = int(input("Please keep guessing what the number may be! "))

# print("Correct! The correct number was "+ str(random_num))

#--------------------------------------
#--------------------------------------

#Write a Python program that prints each item and its corresponding type from the following list.

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for item in datalist:
#     #print (f"Type of  {item} is {type(item)}") THIS IS ANOTHER WAY OF DOING IT
#     print ("Type of",  item, " is ", type(item))

##interesting, this doesn't work with + but does with ,
##how to concatenate an unformatted string

#--------------------------------------
#--------------------------------------

# Three ways to print mismached variable types

# intVar = 10
# floatVar = 12.5
# stringVar = 'The two numbers are'
# print(f"This is an fstring {stringVar}: {intVar} & {floatVar}")
# print("This is a concat string" + stringVar  + " : " + str(intVar) + " & " + str(floatVar)) 
# print("This is a comma concat string ", stringVar, " : ", intVar, " & ", floatVar)

#--------------------------------------
#--------------------------------------

# temperature = input("Type any temperature you like. ")

# if "C" in temperature.upper():
#     print("CELCIUS")
# if "F" in temperature.upper():
#     print("FARENHEIT")

#--------------------------------------
#--------------------------------------

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# for i in range(0,6):
#     if i == 3 or i== 6:
#         continue
#     print(i)

#--------------------------------------
#--------------------------------------

#Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# x = 0
# y = 1
# list = []
# list.append(x)
# list.append(y)

# while y<50:
#     y2 = x+y
#     x = y
#     #list.append(x)
#     list.append(y2)
#     y = y2

# print(list)


    