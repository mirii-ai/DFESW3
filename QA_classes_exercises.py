
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.class_ = "student"
    
#     def GetTestScore(self, score1,score2,score3): #you need to/MUST pass self through this function
#         self.score1 = score1 #technically these three lines are not needed. 
#         self.score2 = score2
#         self.score3 = score3

#         avg_score = (self.score1+self.score2+self.score3)/3 #you don't need self here!
#         return(avg_score)
#     #OR
#     # def GetTestScore(self, score1, score2, score3):
#     #     return (score1 + score2 + score3) / 3


# Amelia = Student("Amelia", 23)
# Chloe = Student("Chloe", 23)
# Becca = Student("Becca", 22)

# Becca.class_ = "History Teacher"

# print(Becca.class_)
# print(Amelia.age, Amelia.class_)
# print(Chloe.age, Chloe.class_)

# # print(getattr(Becca, "age"))
# # print(Becca.age)

# result_Chloe = Chloe.GetTestScore(33,65,47)
# print(result_Chloe)

#---------------------------------------------------------
#---------------------------------------------------------
##//LETTERCHECKER CLASS EXERCISE//##

# class Letterchecker:
     
#     def __init__(self):
#         self.vowels = ['a','e','i','o','u']
#         self.straightlines = ['a','e','f','h','i','k','l','m','t','v','w','x','y','z']


#     def search_for_vowels(self, string):
#         count = 0
#         for letter in string:
#             if letter in self.vowels:
#                 count +=1
#             else:
#                 continue
        
#         if count >= 1:
#             return("True, there is a vowel", count)

#         else:
#             return("False, there are no vowels")
    
#     def search_for_straight_lines(self, string):
#         count = 0
#         slines = []
#         for letter in string:
#             if letter in self.straightlines:
#                 count +=1
#                 new = letter.upper()
#                 slines.append(new)
#             else:
#                 continue
        
#         if count >= 1:
#             return("True, there are letters with straight lines when capitalised", count, slines)

#         else:
#             return("False, there are no letters that have straight lines when capitalised.")

        

# Variable_to_check = Letterchecker() #we can use this end point as many times as we like
# ##find vowels
# vowel_word = "hippo"
# response, count = Variable_to_check.search_for_vowels(vowel_word)

# print("Word: ", vowel_word, " : ", response, " : Total vowels: ", count)
# ## find straight letters
# straight_word = "find a straight letter"
# sresponse, scount, slist = Variable_to_check.search_for_straight_lines(straight_word)
# print("Word: ", straight_word, " : ", sresponse, " : Total straights: ", scount, " : Straights in the string: " , slist)


## Teacher's code:

# class Letterchecker():
#     vowels = 'aeiou'
#     def checkthing(self,x):
#         return x.lower() in self.vowels #like an if statement- is the letter in 'vowels'

# vowlchecker = Letterchecker() #creates an object called vowelchecker using letterchecker
##calling the method inside the class
# for i in 'thequickbrownfoxjumpedoverthelazydog':
#     print(vowlchecker.checkthing(i))

# class Letterchecker():
#     def __init__(self, letterCheck):
#         self.letterCheck = letterCheck.lower()

#     def checkthing(self,x):
#         return x.lower() in self.letterCheck 

# vowelChecker = Letterchecker('aeiou')
# letterswithoneendpoint = Letterchecker('p')
# horizontalsymmetry = Letterchecker('bcdehikox')

# for i in "hello":
#     print(horizontalsymmetry.checkthing(i)) #you need to check every letter once!