def OperationSum(a,b):
    return a+b
def OperationSubstruction(a,b):
    return a-b
def OperationMultiplication(a,b):
    return a*b
def OperationDivision(a,b):
    return a/b
def OperationExp(a,b):
    return a**b

print('------------------------------')
print('|Вас приветствует калькулятор.|')
print('|Введите номер операции      .|')
print('|Доступные операции:          |')
print('|1 :  +                       |')
print('|2 :  -                       |')
print('|3 :  *                       |')
print('|4 :  /                       |')
print('|5 :  **                      |')
print('|Для выхода введите EXIT      |')
print('------------------------------')

while True:
    operation = input()
    if operation.upper()=='EXIT':
        print('Работа с калькулятором завершена.')
        break
    a = int(input())
    b = int(input())
    if operation == '1':
        print(OperationSum(a,b))
    elif operation == '2':
        print(OperationSubstruction(a, b))
    elif operation == '3':
        print(OperationMultiplication(a, b))
    elif operation == '4':
        try:
            print(OperationDivision(a, b))
        except ZeroDivisionError:
            print('Ошибка деления на 0')
    else:
        print(OperationExp(a, b))