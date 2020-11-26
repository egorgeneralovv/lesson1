z = int(input('Введите целое положительное число: '))
max = z % 10
z = z // 10
while z > 0:
    if z % 10 > max:
        max = z % 10
    z = z // 10
    print('Самая большая цифра в числе: ', max)