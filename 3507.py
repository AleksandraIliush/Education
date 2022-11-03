def same_num(a,b,c):
    s_new = {a,b,c}
    if len(s_new)==3:
        return 0
    else:
        return 4-len(s_new)
a,b,c = int(input()), int(input()), int(input())
print(same_num(a,b,c))