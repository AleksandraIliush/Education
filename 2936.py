import math
a=int(input())
b = int(input())
if a>1000 or b > 1000:
    print('Числа должны быть меньше 1000')
else:
    c = math.sqrt(a**2+b**2)
    print(c)