# Write a Python class to convert an integer to a roman numeral.

# class Change:

#     def change_roman(self, x):
#         self.x = x
#         val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

#         roman = ''
#         count = 0

#         while x > 0:
#             for number in range(x //val[count]):
#                 roman += rom[count]
#                 x -= val[count]
#             count += 1
#         return roman

# print(Change().change_roman(156))
        
class Change_back:

    def change_integer(self,number):
        self.number = number
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        use_this = rom[::-1]
        use_val= val[::-1]
        reverse_roman = []
    
        for i in range(len(use_this)): ##this reverses the roman numerals' order in the roman list 
            current = (use_this[i])[::-1] #so everything is backwards
            reverse_roman.append(current)

        # print(reverse_roman)
        # print(use_val)

        integer = 0
        roman = (number.split())[::-1]
        new_roman = []
        for i in range(len(roman)):
            if roman[i] == "M":
                if roman[i+1] == "C":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "D":
                if roman[i+1] == "C":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "C":
                if roman[i+1] == "X":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "L":
                if roman[i+1] == "X":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "X":
                if roman[i+1] == "I":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "V":
                if roman[i+1] == "I":
                    new = roman[i].join(roman[i+1])
                    new_roman.append(new)
                new_roman.append(roman[i])
            if roman[i] == "I":
                new_roman.append(roman[i])



