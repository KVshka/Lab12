'''
Вариант 24

Вычислить сумму знакопеременного ряда |х*3n!|/(3n)!, где х-матрица ранга к (к и матрица задаются случайным образом),
 n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
 У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого +.'''

import numpy as np 
import random
from decimal import Decimal

#Исходные данные
k = random.randint(1,4)
t = int(input('Введите кол-во знаков после запятой t: '))
x = np.random.randint(-1, 1, size=(k, k))

sum = 0
n=1

#Вычисление факториала
def factorial(n):
    i=1
    for j in range(1, 3*n):
        i *= j
    return i

#Вычисление суммы знакопеременного ряда
while True:
    sum+=((-1)**(n+1))*np.linalg.det((x*factorial(n)).astype("float64"))/factorial(n)
    if Decimal(str(abs(sum))).as_tuple().exponent*(-1) > t:
        break
    n+=1

print("Сумма знакопеременного ряда: " + str(sum))