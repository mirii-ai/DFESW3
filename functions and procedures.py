# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

#---------------------------------------
#---------------------------------------
#QA

# def grading(name, hw_score, assessment_score, exam_score):
#     student_name = name
#     total = 175
#     student_total = hw_score + assessment_score + exam_score
#     overall = (student_total/175) * 100

#     return student_name, overall


# studentname = input("Please type student name: ")
# while hw > 25:
#     hw = int(input("Homework score: "))
# while asmnt > 50:
#     asmnt = int(input("Assessment score: "))
# while exam > 100:
#     exam = int(input("Exam score: "))
# name, grade = grading(studentname, hw, asmnt, exam)
# print("Student name : ", name, " Overall ICT grade : " , round(grade), "%")

#---------------------------------------
#---------------------------------------
#W3RESOURCE
#QUESTION1

# def find_max(num1, num2, num3):
#     list = [num1, num2, num3]

#     new = sorted(list)

#     print(new)
#     return(new[-1])

# number1 = int(input("Please type a number. "))
# number2 = int(input("Please type a number. "))
# number3 = int(input("Please type a number. "))
# biggest = find_max(number1, number2, number3)

# print("The max is: " + str(biggest))


#---------------------------------------
#---------------------------------------
# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def sorted_list(list_name):
#     func_list = list_name

#     return_list = sorted(func_list)

#     return(return_list)

# times = int(input("How many items would you like to insert? "))
# input_list = []

# for i in range(times):
#     number = int(input("Please type a number you'd like to input. "))
#     input_list.append(number)



# print("SORTED LIST: ")
# finished_list = sorted_list(input_list)
# print(finished_list)

#---------------------------------------
#---------------------------------------
# Write a Python function to multiply all the numbers in a list.

# def multiply_numbers(inputted_list):
#     func_list = inputted_list

#     total = 1

#     for number in range(len(func_list)):
#         total = total * func_list[number]

#     return total

# times = int(input("How many items would you like to insert? "))
# input_list = []

# for i in range(times):
#     number = int(input("Please type a number you'd like to input. "))
#     input_list.append(number)

# print(input_list)
# mult_total= multiply_numbers(input_list)

# print("The multiplied total is: " + str(mult_total))


#---------------------------------------
#---------------------------------------
#Write a Python program to reverse a string.

# def reverse_string(string):
#     func_string = string

#     reversed_string = func_string[::-1]

#     return(reversed_string)

# OR

# def reverse_string2(string):
#     func_string = string
#     reversed_string = ""
#     for character in func_string:
#         reversed_string = character + reversed_string
    
#     return reversed_string

# inp = input("Please type a string to be reversed: ")

# test1 = reverse_string(inp)
# test2 = reverse_string2(inp)

# print("FUNCTION 1 : " + inp + " REVERSED : " + test1)
# print("FUNCTION 2 : " + inp + " REVERSED : " + test2)


#---------------------------------------
#---------------------------------------
# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

# def factorial(number):
#     num = number
#     total = 1
#     for i in range(1, num+1):
#         total = total * i
#         #print(total)
    
#     return total

# numero = int(input("What number? "))
# number_factorial = factorial(numero)

# print("The factorial of ", numero, " is ", number_factorial)

#---------------------------------------
#---------------------------------------
#Write a Python function to check whether a number falls in a given range.

# def in_range(chosen, range_list):

#     number = chosen
#     list = sorted(range_list)
#     lowest = list[0]
#     highest = list[1]

#     if number in range(lowest, highest):
#         return(1)
#     else:
#         return(0)

# chosen_number = int(input("What number are you searching for? "))
# range_nos = []
# for i in range(2):
#     chosen_range = int(input("What range are you searching within? "))
#     range_nos.append(chosen_range)

# answer = in_range(chosen_number, range_nos)
# range_nos = sorted(range_nos)

# if answer == 1:
#     print(chosen_number, " is within the range of ", range_nos[0], " and ", range_nos[1], ".")
# elif answer == 0:
#     print(chosen_number, " is NOT within the range of ", range_nos[0], " and ", range_nos[1], ".")
# else:
#     "This code has not worked."

#---------------------------------------
#---------------------------------------
#Write a Python function that accepts a string and 
# calculates the number of upper case letters and lower case letters.

#-_-_-_-_-_-_-_
# for character in string:
#     if character.isdigit():
#         print("Found a number!")
#     else:
#         print("hmmmmm")
#-_-_-_-_-_-_-_
    
# def count_cases(string):
#     newstring = []
#     for character in string: #this bit makes sure there are no numbers in the string. If there is, they are removed
#         if not character.isdigit():
#             newstring.append(character)

#     completed = ""
#     complete= completed.join(newstring)


#     upper_case = 0
#     lower_case = 0
#     for character in complete:
#         if character.isupper():
#             upper_case += 1
#         elif character.islower():
#             lower_case += 1
    
#     return(complete, upper_case, lower_case)

# string = input("Please type anything you like. : ")

# absolute, upper, lower = count_cases(string)

# print("Your string: ", absolute)
# print("UPPER CASE LETTERS: ", upper)
# print("LOWER CASE LETTERS: ", lower)

#---------------------------------------
#---------------------------------------
#Write a Python function that takes a list 
# and returns a new list with unique elements of the first list.

# def find_unique(flist):
#     new = flist
#     unique_list=[]
#     for item in new:
#         if item not in unique_list:
#             unique_list.append(item)
#         else:
#             continue
    
#     return(unique_list)


# times = int(input("How many items would you like to insert? "))
# input_list = []

# for i in range(times):
#     number = int(input("Please type a number you'd like to input. "))
#     input_list.append(number)

# unique_list = find_unique(input_list)

# print("ORIGINAL LIST: ", input_list)
# print("UNIQUE LIST: ", unique_list)

#---------------------------------------
#---------------------------------------
# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and 
# that has no positive divisors other than 1 and itself.

# def is_prime(check):
#     numero = check
#     other = 0
#     for i in range(1, numero+1):
#         if numero % i == 0:
#             other += 1
#     other -= 2 #to take away the iterations of 1 and itself

#     if other == 0:
#         return(1)
#     else:
#         return(0)
    
# number = int(input("What number would you like to check? "))

# answer = is_prime(number)

# if answer == 1:
#     print("The number ", number, " is a prime number.")
# elif answer == 0:
#     print("The number ", number, " is NOT a prime number.")
# else:
#     print("This code has not worked.")

#---------------------------------------
#---------------------------------------
# Write a Python program to print the even numbers from a given list.

# def even_number(inputt):
#     list = inputt
#     evens = []
#     for number in list:
#         if number % 2 == 0:
#             evens.append(number)
    
#     return(evens)

# times = int(input("How many items would you like to insert? "))
# input_list = []

# for i in range(times):
#     number = int(input("Please type a number you'd like to input. "))
#     input_list.append(number)

# evens_only = even_number(input_list)

# print("ORIGINAL LIST: ", input_list)
# print("EVEN NUMBERS: ", evens_only)

#---------------------------------------
#---------------------------------------
# Write a Python function to check whether a number is perfect or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal
# to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the 
# number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors 
# (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors,
# and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
# ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
# This is followed by the perfect numbers 496 and 8128.

# def find_perfect(number):
#     numero = number

#     divisors = []
#     for i in range(1, numero):
#         if numero % i == 0:
#             divisors.append(i)
    
#     print("NUMBERS THAT GO INTO ", numero, ": ", divisors)

#     total = 0
#     for number in divisors:
#         total += number
    
#     print("The added total for the divisors of ", numero, " is ", total, ".")
#     if total == numero:
#         return(1)
#     else:
#         return(0)
    
# number = int(input("What number would you like to check? "))

# answer = find_perfect(number)

# if answer == 1:
#     print("The number ", number, " is a perfect number.")
# elif answer == 0:
#     print("The number ", number, " is NOT a perfect number.")
# else:
#     print("The code has not worked.")


#---------------------------------------
#---------------------------------------



#---------------------------------------
#---------------------------------------


#---------------------------------------
#---------------------------------------



#---------------------------------------
#---------------------------------------