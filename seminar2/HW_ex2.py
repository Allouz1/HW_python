# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N:'))
factorial = 1
lst = []

for i in range(1, n + 1):
    factorial = factorial * i
    lst.append(factorial)

print(lst)
