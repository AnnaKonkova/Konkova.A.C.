# -- coding: utf-8 --
a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)
c = 0
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        c += 1
print(c)
