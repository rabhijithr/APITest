import collections
import os

b = os.path.abspath("RoughScripts.py")
print(b)

print(__file__)

str4 = '14-12-2018'

print(str4.split('-'))
newstr = str4.split('-')
print(newstr[0] + ' ', newstr[1])

print(str4[0:5])

str1 = "Hello Everyone here"

str2 = "hey all"

str3 = "kolar\ngold\nfields"

print(str1)
print(str1[0])
print(str1[1:4])

print(str1[:6] + "All")

print(str1.split())

print(str1.split('l'))

print(str1.split('l', 1))

print(str1.split('l', 2))

print(str2.capitalize())

print(str3.splitlines())

spli = str3.splitlines()

print(spli[0])
print(len(spli[0]))


for x in spli:
    print(x + str(len(x)))

print(" ========= Format Method =========")
for x in spli:
    print("{} {}".format(x, len(x)))


for y in spli:
    for z in y:
        print(z)


lp = [len(x) for x in spli]

print(lp)

sp = []
sp = spli

print(sp)

print(str1.center(40))

print(str1.center(30, '\\'))

print(str1.count('e'))

# To print the number of character occurences in a string
# a='dqdwqfwqfggqwq'
x = dict((letter, str1.count(letter)) for letter in set(str1))
print(x)


results = collections.Counter(str1)
print(results)

string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"

Final = [x for x in string if x in vowels]

print(Final)
print(len(Final))

string = string.casefold()

print(string)

count = {}.fromkeys(vowels, 0)

counter = 0

for x in string:
    if x in vowels:
        # print(list(x))
        count[x] = count[x] + 1

print(count)

b = type(counter)
print(b)

a = type(count)
print(a)

c = type(Final)
print(c)
