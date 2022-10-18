def IsSubstring(Pattern, Source):
    if Source.find(Pattern)==(-1):
        print('NO')
    else:
        print('YES')
Pattern=input()
Source=input()
IsSubstring(Pattern,Source)