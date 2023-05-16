# EXERCICES XP ---------------------------------------------------
# Exercise 1 : Built-In Functions --------------------------------
def my_abs(arg: int):
    ''' abs() is a build-in function that return the absolut value of the given number '''
    print(abs(arg))

def my_int(arg: int):
    ''' int() is a build-in function converts a number or a string to its equivalent integer '''

def my_input(arg):
    ''' input() is a build-in function allows user input '''

my_abs(1234)
print(my_abs.__doc__)
print(my_int.__doc__)
print(my_input.__doc__)



# Exercise 2: Currencies -----------------------------------------
class Currency:
    def __init__(self, currencyy, amount):
        self.currencyy = currencyy
        self.amount = amount
    
    def __str__(self):
        return f"I have {self.amount} {self.currencyy}"
    
    def __int__(self):
        print(self.amount)
        return self.amount
    
    def __repr__(self):
        return print(f"I have {self.amount} {self.currencyy}")
    
    def __add__(self, other_amount):
        total_amount = self.amount + other_amount.amount
        if self.currencyy is not other_amount.currencyy:
            return f"TypeError: Cannot add between Currency type <dollar> and <shekel>"
        else:
            return f"The total amount is {total_amount}"
    
    def increase_amount(self):
        self.amount += 5
    
    def increase_by_other(self, other_amount):
        self.amount += other_amount.amount
        return self.amount
        
c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

c1.__str__()
c1.__int__()
c1.__repr__()
print(c1)

totalamount = int(c1) + 5
print(totalamount)

totalamount2 = c1 + c2
print(totalamount2)

print(c1)

c1.increase_amount()
print(c1)

c1.increase_by_other(c2)
print(c1)

totalfalseamount = c1 + c3
print(totalfalseamount)