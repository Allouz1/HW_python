x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Втарая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
else:
    print('Четвёртая четверть')