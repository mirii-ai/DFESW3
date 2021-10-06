
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_ = "student"
    
    def GetTestScore(self, score1,score2,score3): #you need to/MUST pass self through this function
        self.score1 = score1 #technically these three lines are not needed. 
        self.score2 = score2
        self.score3 = score3

        avg_score = (self.score1+self.score2+self.score3)/3 #you don't need self here!
        return(avg_score)
    #OR
    # def GetTestScore(self, score1, score2, score3):
    #     return (score1 + score2 + score3) / 3


Amelia = Student("Amelia", 23)
Chloe = Student("Chloe", 23)
Becca = Student("Becca", 22)

Becca.class_ = "History Teacher"

print(Becca.class_)
print(Amelia.age, Amelia.class_)
print(Chloe.age, Chloe.class_)

# print(getattr(Becca, "age"))
# print(Becca.age)

result_Chloe = Chloe.GetTestScore(33,65,47)
print(result_Chloe)