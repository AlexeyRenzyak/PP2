""" #1
def GramsToOunces(grams):
    ounces = grams/28.3495231
    return ounces
print(round(GramsToOunces(float(input())), 2)) """

""" #2
def FahrenheitToCentigrade(f):
    c = (5 / 9) * (f - 32)
    return c
print(round(FahrenheitToCentigrade(float(input())), 2)) """

""" #3
def solve(numheads, numlegs):
    leg_surplus = numlegs - numheads*2
    rabbits = leg_surplus/2
    chickens = numheads-rabbits
    return [int(rabbits), int(chickens)]
solution = solve(35, 94)
print(solution[0], "Rabbits")
print(solution[1], "Chickens") """

""" #4
def filter_prime(numbers):
    is_prime = True
    result = []
    for i in numbers:
        is_prime = True
        if i <= 1:
            continue
        for x in range(1, round(i/2)+1):
            if i%x == 0 and i != x and x != 1 or i <= 1:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result
        
data = input()
data = data.split(" ")
for x in range(len(data)):
    data[x] = int(data[x])
print(filter_prime(data)) """

""" #5
import itertools
def permutator(string):
    permlist = itertools.permutations(string)
    stringperms = []
    for x in permlist:
        s = ""
        for y in x:
            s += y
        if s not in stringperms:
            stringperms.append(s)
    for x in stringperms:
        print(x)
            
st = input()
permutator(st) """

""" #6
def StringReverser(string):
    slist = string.split(" ")
    slist = slist[::-1]
    finalst = ""
    for x in slist:
        finalst += x + " "
    finalst.strip()
    return finalst
st = input()
print(StringReverser(st)) """

""" #7
def has_33(nums):
    for x in range(len(nums)-1):
        if nums[x] == 3 and nums[x+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3])) """

#8
def spy_game(nums):
    counter = 0
    for x in range(len(nums)):
        if counter == 0:
            if nums[x] == 0:
                counter += 1
            elif nums[x] == 7:
                counter = 0
        if counter == 1:
            if nums[x] == 0:
                counter += 1
            elif nums[x] == 7:
                counter = 0
        if counter == 2:
            if nums[x] == 7:
                return True
            elif nums[x] == 0:
                counter = 0

    return False
#print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
#print(spy_game([1,7,2,0,4,5,0]))


