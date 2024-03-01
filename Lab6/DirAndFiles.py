import os

#1
#path = r"C:\Users\ACER\Desktop\dirtest"
""" mode = 'FD'
match mode:
    case 'FD':
        for x in os.listdir(path):
            print(x)
    case 'F':
        for x in os.listdir(path):
            if not os.path.isdir(path+"\\"+x): print(x)
    case 'D':
        for x in os.listdir(path):
            if os.path.isdir(path+"\\"+x): print(x) """

#2
#path = r"C:\Users\ACER\Desktop\dirtest\1.txt"
""" print("Existence:", os.path.exists(path))
print("Readability:", os.access(path, os.R_OK))
print("Writability:", os.access(path, os.W_OK))
print("Executability:", os.access(path, os.X_OK)) """

#3
#path = r"C:\Users\ACER\Desktop\dirtest\1.txt"
""" print("Existence:", os.path.exists(path))
print("Filename:", os.path.basename(path))
print("Directory portion:", os.path.dirname(path)) """

#4
""" f = open("Lab6/4Test.txt", "r")
c = 0
while f.readline():
    c += 1
print(c) 
f.close()"""

#5
""" f = open("Lab6/5Test.txt", "w")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in l:
    f.write(str(x) + '\n') 
f.close() """

#6
""" import string
for x in list(string.ascii_uppercase):
     f = open(x + '.txt', "w")
     f.close()  """

#7
""" f1 = open("Lab6/7Transmitter.txt", "r")
t = f1.read()
f2 = open("Lab6/7Receiver.txt", "w")
f2.write(t)
f1.close()
f2.close() """

#8
path = r"C:\Users\ACER\Desktop\dirtest\1.txt"
print("Existence:", os.path.exists(path))
print("Availability:", os.access(path, os.W_OK))
if os.path.exists(path):
    os.remove(path)
    print("Deletion successful")
else:
    print("Deletion error")