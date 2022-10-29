num_kassa = int(input())
numbers = [int(i) for i in input().split()]
#numbers = [21 10 45 48 37 12 12 34 17 10]
num22 = numbers[:num_kassa]
for i in numbers[num_kassa:]:
    k = min(num22)
    num22[num22.index(k)] = k+i
print(max(num22))