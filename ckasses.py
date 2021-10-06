# classes should always start with a capital letter

class Dog:
    #this bit until init is what I referred to as 'the first part of the code'
    breed = 'Corgi'
    height = 16
    energy = 'medium'

    def __init__(self, breed, height, energy):
        self.breed = breed
        self.height = height
        self.energy = energy

    #now we need to have a method. It's a procedure/ function

    def speak(self): #needs to havea special variable that tells the function it's part of a class
        #we always need a variable at the start that's used by the class
        print("Woof")

    def whatami(self):
        print(self.breed)

# you can create objects within classes

#these ones return the first set. You can change attributes within the ()
# bilbo_waggins = Dog()
# chewbarka = Dog()
# chewbarka.breed = 'Spaniel' #you can change the attributes like this

# print(bilbo_waggins.breed)
# print(chewbarka.breed)

#these ones use the __init__ function. This makes the first part of the code redundant 
bilbo_waggins = Dog('Corgi', 16, 'medium')
chewbarka = Dog('Spaniel', 10, 'high')
havoc = Dog('Cavapoo', 3, 'ultimate')

chewbarka.whatami() #will print Spaniel
print(bilbo_waggins.breed)
print(havoc.energy)


#--------------------------------------------------------
#--------------------------------------------------------

# class Cloud_login():
#     username = 'admin'
#     password = 'password13'
#     auth_url = 'https://thecloud.cloud'

#     def login(self,username,password,auth_url):
#         #code

# prodcloud = cloud_login()
# prodcloud.username = 'admin_leon'
# prodcloud.password = 'leon_password123'

# testcloud = cloud_login()
# testcloud.username = 'test_user'
# testcloud.password = 'test_password123'

# testcloud.login()
# prodcloud.login()
