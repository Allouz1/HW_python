# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [0, 1]:
        return 1 
    else:
        return fib(n - 1) + fib(n - 2)


def negfib(n):
    if n in [-1, -2]:
        return -1
    else:
        return negfib(n - 1) + negfib(n - 2)


k = int(input('Введите число фибаначи: '))
lst = []

for e in range (k):
    lst.append(negfib(e))

print(lst)
