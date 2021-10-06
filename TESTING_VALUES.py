



# Amelia's test for pass by value or pass by value

def test(string):
    string = "Here I will change the string!"
    print("Inside the function, this is the string: " + string)

string = "My string is like this."
test(string)
print("Outside the function: " + string)

