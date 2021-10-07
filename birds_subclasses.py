from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False



class Owl(Bird):
    def reproduce(self):
        self.babies += 6
        return self.babies


    def noise(self):
        return "Twit Twoo"

    def eat(self):
        return "Peck peck"
## we have used Polymorphism to override the reproduce method, 
# Abstraction with the eat method and Inheritance in this child class.


class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
            return self.babies

##For this subclass we have used Polymorphism to override the reproduce 
# method and Fly and extinct variables, Encapsulation to keep the babies variable from 
# being directly accessed as well as Inheritance again to create a child class of Bird.

JohnTheDodo = Dodo()
FredTheDodo = Dodo()

SamuelTheOwl = Owl()
RingoTheOwl = Owl()

JohnTheDodo.extinct = False
print(JohnTheDodo.extinct)
print(FredTheDodo.extinct)
print(RingoTheOwl.reproduce())


print(FredTheDodo.eat())
print(JohnTheDodo.reproduce(), JohnTheDodo.noise())
print(RingoTheOwl.noise())



