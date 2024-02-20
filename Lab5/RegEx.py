import re

""" #1
p = re.compile('ab*$')
print(p.match('abb'))
print(p.match('abbb'))
print(p.match('a'))
print(p.match('ac')) """

""" #2
p = re.compile('ab{2,3}$')
print(p.match('abb'))
print(p.match('abbb'))
print(p.match('a'))
print(p.match('abbbb')) """

""" #3
p = re.compile('([a-z]_)*[a-z]$')
print(p.match("a_s"))
print(p.match("g_")) """

#4
""" p = re.compile('([A-Z])([a-z])+$')
print(p.match('Agse'))
print(p.match('D')) """

#5
#p = re.compile(r'a[\w\W]*b$')
""" print(p.match('ab'))
print(p.match('aefe3434#$#feb')) 
print(p.match('befe3434#$#feb'))  """

#6
#p = re.compile(r'[\s,.]')
""" s1 = 'dsa,ds.  AA'
print(re.sub(p, ":", s1)) """

#7
#p = re.compile(r'_([a-z])')
""" s1 = 'one_two_three'
s1 = s1.capitalize()
print(re.sub(p, lambda m:m.group(1).upper() , s1)) """

""" #8
p = re.compile(r'[A-Z][a-z]*')
s1 = "OneTwoThree"
print(re.findall(p, s1))  """

""" #9
p = re.compile(r'[A-Z][a-z]*')
s1 = "OneTwoThreeFour"
l1 = re.findall(p, s1)
res = ""
for x in l1:
    res += x
    res += ' '
res = res.strip()
print(res) """

#10
p = re.compile(r'([A-Z])')
s1 = 'OneTwoThree'
s1 = s1[0].lower()+s1[1:]
print(re.sub(p, lambda m:'_'+m.group(0).lower() , s1)) 