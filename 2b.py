from collections import Counter
from difflib import SequenceMatcher

myFile = open('2.txt', 'r')
contents = myFile.read().strip().splitlines()
#myFile.close()

c = [0, 0]
for i in contents:
    a = [j for i, j in Counter(i).most_common()]
    if 3 in a:
        c[0] += 1
    if 2 in a:
        c[1] += 1

    # for i in contents:
    #     for j in contents:
    #         diffs = 0
    #         for idx, ch in enumerate(i):
    #             if ch != j[idx]:
    #                 diffs +=1
    #             if diffs == 1:
    #                 ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
    #                 print("Part Two:", ''.join(ans))
print(c[0] * c[1])

result = None
for x in myFile:
    for y in myFile:
        ratio = SequenceMatcher(None, x, y).ratio()
        if ratio == (len(x)-1)/len(x):
            result = [z for z in lists(x) if z in list(y)]
            break
        if result:
            break 
    print(''.join(result))


