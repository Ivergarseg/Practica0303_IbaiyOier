a = input()
b = input()
print(a)
print(b)

c = (a.split(' '))

d = (b.split(' '))
print(c)
print(d)
cont_A = 0
cont_B = 0
for x in range (0, len(c)):
    print(c[x])
    print(d[x])
    if c[x] > d[x]:
        cont_A += 1
    if c[x] < d[x]:
        cont_B += 1
print(str(cont_A) + ' ' + str(cont_B))

