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

    