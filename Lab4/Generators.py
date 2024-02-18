""" #1
def SquareGen(n):
    for x in range(n+1):
        yield x*x
for i in SquareGen(5):
    print(i) """

""" #2
def EvenGen(p):
    for x in range(p+1):
        if x%2 == 0:
            yield x
n = int(input())
l = list(EvenGen(n))
for i in l:
    print(str(i), end="") 
    if i != l[-1]:
        print(", ", end="")  """

""" #3
def DivisionGen(a):
    for x in range(a+1):
        if x%3 == 0 and x%4 == 0:
            yield x
n = int(input())
l = list(DivisionGen(n))
print(l) """

""" def squares(a, b):
    for x in range(a, b+1):
        yield x*x
n1 = int(input())
n2 = int(input())
l = list(squares(n1, n2))
for x in l:
    print(x) """

def DownGen(n):
    for x in range(n, -1, -1):
        yield x
n = int(input())
l = list(DownGen(n))
print(l)