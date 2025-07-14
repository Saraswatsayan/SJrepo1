class Student():
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def avg(self):
        return (self.subject1 + self.subject2 + self.subject3) / 3

s1 = Student("Ravi", 67,89,77)
print(s1.avg())

#Practice - Create Account class with 2 attributes - balance & account no.
#           Create methods for debit,credit & printing the balance.

class Account:

    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    def debit(self, amount):
        self.balance =- amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance =+ amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 =  Account(10000, 111000)
acc1.debit(1000)
acc1.credit(40000)





