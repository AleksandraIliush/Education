a,b,c,d = [int(input()) for _ in range(4)]
[print(i, end = ' ') for i in range(a,b+1) if i%d==c]