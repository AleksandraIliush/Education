with open('Text_111329.txt','r') as f:
    line_in_file = f.readlines()
    print(line_in_file[::-1])
    for i in line_in_file[::-1]:
        print(i.replace('\n', ''))
