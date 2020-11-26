time = int(input('Введите время в секундах: '))
hours = time / 3600
minutes = time / 60
seconds = time / 1
print(f'Формат времени чч:мм:сс {hours:.2f} : {minutes:.2f} : {seconds:.2f}')