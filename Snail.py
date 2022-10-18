#Пользователь задает размер квадратной матрицы
k = int(input())
#Сначала создаем матрицу, состоящую только из 0
a=[[0 for j in range(k)] for i in range(k)]
#Число , по порядку, которое будем подставлять
count = 1
#Первая вспомогательная переменная для определения среза
Point1 = 0
#Вторая вспомогательная переменная для определения среза
Point2 = 1
#Третья вспомогательная переменная для определения среза
Point3 = k-1
#Четвертая вспомогательная переменная для определения среза
Point4 = k
#Пятая вспомогательная переменная для определения среза
Point5 = k-2
while count <= k*k:
    #Заполнение строки слева-направо
    for i in range(Point1,Point2,1):
        for j in range(Point1,Point4,1):
            a[i][j] = count
            count += 1
    #Заполнение строки сверху вних
    for i in range(Point2,Point4,1):
        for j in range(Point3,Point5,-1):
            a[i][j] = count
            count += 1
    #Заполнение строки справа-налево
    for i in range(Point3,Point5,-1):
        for j in range(Point5,Point1,-1):
            a[i][j] = count
            count += 1
    #Заполнение строки снизу вверх
    for i in range(Point3,Point1,-1):
        for j in range(Point1,Point2,1):
            a[i][j] = count
            count += 1
    Point1 += 1
    Point2 += 1
    Point3 -= 1
    Point4 -= 1
    Point5 -= 1
#Вывод итоговой матрицы
for i in a:
    print(*i)

