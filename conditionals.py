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

inputNumVar = int(input("Type a whole number please. "))
while inputNumVar > 0:
    print(inputNumVar)
    inputNumVar = inputNumVar - 1

numvar2 = int(input("Type another number please. "))
resultVar = 1
while numvar2 > 0:
    resultVar = resultVar * numvar2
    numvar2 = numvar2 - 1
print(resultVar)