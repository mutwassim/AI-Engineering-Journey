"""
Part A: Warm-up (from Test 1).
Write a Book class with title, author, and pages and a display() method. 
Create two books and display them. Then: what happens with Book("Python", "Ali"), and why?
"""
class Book:
        def __init__(self,title,author,pages):
            self.title = title
            self.author = author
            self.pages = pages
        def display(self):
              print(self.title,self.author,self.pages)

a = Book("None of that is far","Nobody",504)
b = Book("Allah is watching","Me",806)

a.display()
b.display()


""" Write a Student class with name and marks, plus a classmethod from_string 
that builds a Student from "Sara,85". Marks must be an integer."""

class Student:
      def __init__(self,name,marks):
            self.name = name
            self.marks = marks

      @classmethod
      def from_string(cls,text):
            name,marks = text.split(",")
            return cls(name,int(marks))

s = Student.from_string("Sara,85")
print(s.name, s.marks)


class Graduate(Student):
    pass

g = Graduate.from_string("Ali,70")
print(type(g).__name__)

"""
Write the full BankAccount class
Requirements:

Instance method: deposit(amount)
Instance method: withdraw(amount), which must block overdrafts (can’t withdraw more than the balance)
Instance method: display_balance()
Class method: change the bank name
Static method: check whether an amount is positive
Then create two accounts, change the bank name, and display both balances

"""

class BankAccount:
      bankName = "HBL"

      def __init__(self,balance):
            self.balance = balance

      def deposit(self,amount):
            if BankAccount.isPositive(amount):
                self.balance += amount
                return self.balance
            else:
                  print("Invalid Amount")
      
      def withdraw(self,amount):
            if BankAccount.isPositive(amount):
                if self.balance>=amount:
                    self.balance -= amount
                    return self.balance
                else:
                    print("Insufficent Balance")
            else:
                    print("Invalid Amount")

      def display_balance(self):
            print(f"Balance: {self.balance}")

      @classmethod
      def change_bank_name(cls,text):
            cls.bankName = text

      @staticmethod
      def isPositive(amount):
            return amount>0

A = BankAccount(1000)
B = BankAccount(2000)

BankAccount.change_bank_name("Habib Bank Limited")

A.display_balance()
B.display_balance()


"""
Q6.Build this structure:

Person (parent) with name and age, and a method display() that prints them.
Student (child) adds student_id.
Teacher (child) adds salary.
Both children must use super().__init__() and must not repeat self.name = name or self.age = age.
Both children must override display() to print the common info plus their own field, using super().display().
Create one Student and one Teacher and call display() on each.

"""
class Person:
      def __init__(self,name,age):
            self.name = name
            self.age = age

      def display(self):
            print(self.name,self.age)

class Student(Person):
      def __init__(self,student_id, name, age):
            super().__init__(name, age)
            self.student_id = student_id

      def display(self):
            super().display()
            print(self.student_id)

class Teacher(Person):
      def __init__(self, salary, name, age):
            super().__init__(name, age)
            self.salary = salary
      def display(self):
            super().display()
            print(self.salary)

s = Student(5,"Ali",18)
t = Teacher(20000,"Iftikhar",30)

"""
Q6. Coding task (from your plan):

Create three notification classes: Email, SMS, WhatsApp.
Each implements its own send(message) method.
Use a common parent Notification whose send raises NotImplementedError.
Put one of each in a list and loop through it, calling send("Hello") on each.

Q7. Coding task: Rewrite BankAccount with a private __balance and a @property called balance 
with a setter that rejects negative values. Create one account, read the balance, set it to 500, then try -5.
"""

class Email :
    def __init__(self,message):
          self.message = message
    def send(self,message):
        print(message)
class SMS:
    def __init__(self,message):
          self.message = message
    def send(self,message):
        print(message) 
class WhatsApp:
    def __init__(self,message):
          self.message = message
    def send(self,message):
        print(message)
        
W = Whatsapp(s)