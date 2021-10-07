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
    
    def transfer_money(self, from_budget, to_budget):
        money_available = self.funds_available(from_budget)

        if money_available > 0:
            print("Available money: ", money_available)
            print("Please type in the destination Budget category.")
            destination = to_budget
            print("Please type the amount you'd like to transfer.")
            amount = int(input())      
            if money_available > amount:
                self.available_funds -= amount
                to_budget.transfer_money() += amount
                print("transaction completed") 
            
        else:
            return("Insufficient funds to transfer budget over.")
        


Food = Budget("Food")
Clothing = Budget("Clothing")

Food.available_funds = 25.00
Food.budget = 20.00

Clothing.available_funds = 20.00
Clothing.budget = 15.00

print(Food.available_funds, Food.budget)


# class CategoryBudget():
#     def __init__(self,limit,category):
#         self.budget = limit        
#         self.category = category        
#         self.transactions = []



# class CategoryBudget():
#         transactions = []
#     def __init__(self,limit,category):
#         self.budget = limit        
#         self.category = category    
#         def deposit(self,amount):
#         self.transactions.append(amount)
#         self.cal_balance_()
#     def withdraw(self,amount):
#         self.transactions.append(-amount)
#         self.cal_balance_()
#     def transfer(self,amount,where):
#         where.deposit(amount)
#         self.withdraw(amount)
#         print(where.balance_())
#             def cal_balance_(self):
#         self.balance = 0        for i in self.transactions:
#             self.balance += i    def balance_(self):
#         if self.balance > self.budget:
#             difference = self.balance - self.budget            return(f"You have exceeded your budget of {self.budget} for {self.category} by {difference} ")
#         else:
#             return(f"Your balance for {self.category} is {self.balance}")
#     def ledger(self):
#         return(self.transactions)



class Budget():
    objects = [] #inialise variable    
    def __init__(self, category, balance):
        Budget.objects.append(self) #append list to keep track of all budgets        
        self.category = category #need category input for overview function to know name of budget as workaround        
        self.balance = balance    

    def statement(self):
        return(str(self.category) + " balance is £" + str(self.balance))

    def deposit(self, funds):
        self.balance += funds    
        
    def withdraw(self, funds):
        self.balance -= funds    
        
    def transfer(self, funds, targetcat):
        self.withdraw(funds)
        targetcat.deposit(funds)

def budgetoverview(category):
    total=0    
    for i in Budget.objects:
        total += i.balance    
    budgetoverview = (category.balance/total)*100    
    return str(category.category) + " makes up " + str(round(budgetoverview, 2)) + "% of the total budget."
    
    
Food = Budget("Food", 20000)
Clothing = Budget("Clothing", 10000)
Entertainment = Budget("Entertainment", 5000)
Travel = Budget("Travel", 10000)
Food.withdraw(5000)
Food.transfer(5000, Clothing)
print(Food.statement())
print(Clothing.statement())
print(Entertainment.statement())
print(Travel.statement())
print(budgetoverview(Food))