# -- coding: utf-8 --
a = int(input('enter a='))
b = int(input('enter the b that < a b= '))
if a>b:
    for i in range(a, b-1 ,-1):
        if i%2!=0:
            print(i)
else:
    print(' a should be less b ')
