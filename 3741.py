def delH(str_with_h):
    f_value = str_with_h.find('h')
    l_value = str_with_h.rfind('h')
    return str_with_h[0:f_value]+str_with_h[l_value+1:]
print(delH(input()))