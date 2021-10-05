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





#---------------------------------------
#---------------------------------------





#---------------------------------------
#---------------------------------------





#---------------------------------------
#---------------------------------------