f = open('1.txt', 'r')
content = f.read()
#print(content)

a1 = []
for number in open("1.txt").readlines():
    a1.append(int(number))
print(a1)

f.close()

print(len(a1))
b=0
x=[]
for number in a1:
    b = b + number
    x.append(b)
print(x)
