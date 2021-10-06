# import boss

# boss.bad_boss("Bill Steves")

#---------------------------------------
## PYTHON DEBUGGING ##
#---------------------------------------
import pdb

# pdb.set_trace()

# books = ['1984', 'Winnie the Pooh', 'Jungle Book', 'Harry Potter', 'Pride and Prejudice', 'Enders Game', 'War and Peace', 'Star Wars']

# for bookItem in books:
#     if bookItem == '1984':
#         continue
#     print(bookItem)

# inputVar = int(input("Whole number: "))
# resultVar = 1
# while inputVar > 0:
#     resultVar = resultVar * inputVar
#     inputVar -= 1


# a = "aaa"
# b = "bbb"
# c = "ccc"

# final = a + b + c
# print(final)

# price= {'burger' : 10, 'fried egg':8, 'chips':3}
# user_funds = 10.31
# item_price = price['burger']

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds:
#     print("Sorry you don't have enough money")

## this function will need to be called
# def tailRecursion(factorial, result = 1):
#     if factorial == 1:
#         return result
#     else:
#         tempResult = factorial * result
#         return tailRecursion((factorial), tempResult)

## as long as a list is passed through the function this piece of code will work fine
# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))


# pdb.set_trace()
# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x):
#             if x % n == 0:
#                 return False
#         return True

# returnVar = is_prime(7)
# print(returnVar)

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n += 1

print(item_list[4])



# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n < 5:
#     for i in item_list:
#         print(item_list[i])

# print item_list[5]



#---------------------------------------
#---------------------------------------

# import boss

# dice1 = boss.dice()
# dice2 = boss.dice()

# print("DICE 1: ", dice1)
# print("DICE 2: ", dice2)