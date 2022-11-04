def first_last(str_for_searching):
    num = {str_for_searching.find('f'),str_for_searching.rfind('f')}
    [print(i, end =' ') for i in num if i !=-1]
first_last('omort')
