""" #1
class StringMaster:
    def __init__(self):
        self.data = ""
    def getString(self):
        self.data = input()
    def printString(self):
        print(self.data.upper())
example = StringMaster()
example.getString()
example.printString() """

""" #2-3
class Shape:
    def __init__(self):
        pass
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)
s = Rectangle(2,3)
s.area() """

""" #4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(str(self.x)+","+str(self.y))
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, point2):
        return math.sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)
p1 = Point(1, 1)
p2 = Point(2, 2)
print(round(p1.dist(p2), 2))
p1.move(0, 0)
p1.show()
print(round(p1.dist(p2), 2)) """

""" #5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        if (self.balance - money) >= 0:
            self.balance -= money 
    pass

acc = Account("Somebody", 1000)
print(acc.balance)
acc.deposit(100)
print(acc.balance)
acc.withdraw(1200)
print(acc.balance)
acc.withdraw(600)
print(acc.balance)
acc.deposit(1000)
print(acc.balance) """

#6
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
nlist2 = list(filter(lambda a: all([a%x != 0 for x in range(2, a)]) and a>1, nlist))
print(nlist2)