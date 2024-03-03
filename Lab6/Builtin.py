#1
""" l = [0, 24, 2, 5, 7]
m = 2
l = list(map(lambda a:a*m, l))
print(l) """

#2
""" def upperlower(s):
    if s.isupper():
        return 1
    if s.islower():
        return 0

string = str(input()).replace(" ", "")
l = list(string)
l = list(map(upperlower, l))
l = sum(l)
uppercase = l
lowercase = len(string) - l
print("Uppercase:",uppercase)
print("Lowercase:",lowercase) """

#3
""" string = str(input())
stringr = "".join(reversed(string))
print(stringr)
if string == stringr:
    print("A palindrome")
else:
    print("Not a palindrome") """


#4
""" import time
import math
val = int(input())
delay = int(input())
time.sleep(delay*0.001)
print("Square root of", val, "after", delay, "milliseconds is", math.sqrt(val)) """

#5
sampletuple1 = (True, False, True)
sampletuple2 = (True, True, True, True, True)
print(all(sampletuple1))
print(all(sampletuple2))
