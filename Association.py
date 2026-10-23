class Employer():
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age 
        self.pay = pay

class Employee():
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def my_wage(self):
        return self.pay
    def pay_Difference(self, num):
        return num - self.pay

King = Employer("Arachnid", 35, 1000000)
SiC = Employee("Wemmbu", 25, 50000,)

print (f'Pay Difference: {SiC.pay_Difference(King.pay)}')
