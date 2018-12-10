f = open('1.txt', 'r')
content = f.read()
#print(content)

a1 = []
for number in open("1.txt").readlines():
    a1.append(int(number))
#print(a1)

f.close()

#print(len(a1))
b=0
x=[]
for number in a1:
    b = b + number
    x.append(b)
#print(x)

c=547
y=[]
for number in a1:
    c = c + number
    y.append(c)
#print(y)

d=1094
z=[]
for number in a1:
    d = d + number
    z.append(d)
#print(z)

for number in x:
    for aaa in y:
        if number == aaa:
            print(aaa)

for number in y:
    for aaa in z:
        if number == aaa:
            print(aaa)

# Part 1
changes = a1
print(sum(changes))

# Part 2
from itertools import accumulate, cycle
seen = set()
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))
