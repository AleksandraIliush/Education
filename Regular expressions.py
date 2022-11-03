import re
def matchReIPV4(strRe):
    if re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{2}.[0-9]{2}',strRe):
        return True
    else:
        return False

def last_names(str_first_and_last_names):
    return re.findall(r'Michael ([A-Z]\w+)',str_first_and_last_names)

def matchDomain(email):
    if re.match(r'.+@testdomain', email):
        return 'valid'
    else:
        return 'not valid'
def matchDates(strDate):
    if re.match(r'\w*\s*\[(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|1[0-9]|2[0-8])))\]\w*\s*',strDate):
        return 'valid'
    else:
        return 'not valid'

print(matchReIPV4('123.456.78.90'))

str_Names = '''Michael, how are you? - Cool, how is John Williamns and Michael Jordan? 
I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James
, Michael Green AKA Star and Michael Wood?'''

print(last_names(str_Names))

print(matchDomain('123@testdomain.com'))

print(matchDates('[02-02] aaaaa'))