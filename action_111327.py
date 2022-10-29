f = open('Input.txt', 'r')
string_words = ''
k=0
for lines in f:
    string_words+=lines
for i in string_words.split():
    k+=int(i)
f.close()

f2 = open('Output.txt', 'a')
f2.write(str(k)+'\n')
f2.close()