a = int(input("Результат 1го дня "))
b = int(input("Общий результат спортсмена составляет "))
count = 1
while a < b:
    count += 1
    a *= 1.1
print('На {}-й день спортсмен достиг результата — не менее {} км.'.format(count, b))