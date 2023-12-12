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
a=1
fact=1
#Вычисление факториала
def factorial(fact, a, n):
    for j in range(a, 3*n):
        fact *= j
    return fact

#Вычисление суммы знакопеременного ряда
while True:
    fact=factorial(fact,a,n)
    sum+=((-1)**(n+1))*np.linalg.det((x*fact).astype("float64"))/fact
    if Decimal(str(abs(sum))).as_tuple().exponent*(-1) > t:
        break
    a=3*n
    n+=1

print("Сумма знакопеременного ряда: " + str(sum))
