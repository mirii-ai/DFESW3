# #---------------------------------------------------------
# #---------------------------------------------------------
# “Create a Budget class that can instantiate objects based on different budget categories 
# like food, clothing, and entertainment. These objects should allow for depositing and withdrawing 
# funds from each category, as well computing category balances and transferring balance amounts 
# between categories”


class Budget:
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.available_funds = 0 #need to define these independently
        self.budget = 0
    
    def funds_available(self):
        money_now = self.available_funds
        return(money_now)
    
    def transfer_money(self, from_budget):
        money_available = self.funds_available(from_budget)

        if money_available > 0:
            print("Available money: ", money_available)
            print("Please type in the destination Budget category.")
            destination = input()
            print("Please type the amount you'd like to transfer.")
            amount = int(input())      
            if money_available > amount:
                self.available_funds -= amount
            
        else:
            return("Insufficient funds to transfer budget over.")
        


Food = Budget("Food")
Clothing = Budget("Clothing")

Food.available_funds = 25.00
Food.budget = 20.00

Clothing.available_funds = 20.00
Clothing.budget = 15.00

print(Food.available_funds, Food.budget)