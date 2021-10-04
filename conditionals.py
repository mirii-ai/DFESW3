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

# for char in range(len(word) - 1, -1, -1):
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

choice = input("Convert from Celcius or convert from Farenheit? c / f ")
if choice == "c":
    tempC = int(input("Please type the temperature degree in Celcius. "))

    tempF = ((tempC/5)*9) + 32
    print(str(tempC) + " degrees Celcius is " + str(tempF) + " degrees Farenheit.")
elif choice == "f":
    tempF = int(input("Please type the temperature degree in Farenheit. "))

    tempC = ((tempF - 32)/9)*5
    print(str(tempF) + " degrees Farenheit is " + str(tempC) + " degrees Celcius.")
else:
    print("You didn't type a registered character. Please go back and type either c or f.")

#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
#--------------------------------------
