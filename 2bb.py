from collections import Counter
from itertools import combinations, compress

myFile = open('2.txt', 'r')
contents = myFile.read().strip().splitlines()
myFile.close()

c = [0, 0]
for i in contents:
    a = [j for i, j in Counter(i).most_common()]
    if 3 in a:
        c[0] += 1
    if 2 in a:
        c[1] += 1

print(c[0] * c[1])

for one, two in combinations(contents, 2):
    diff = [e1 == e2 for e1,e2 in zip(one, two)]
    if sum(diff) == (len(one)-1):
        res2 = ''.join(list(compress(one,diff)))
        break 
print(res2)
