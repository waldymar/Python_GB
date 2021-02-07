a = int(input('Назовите число: '))
n = a
count = 0
while a != 0:
    count += 1
    a //= 10
pw = 10 ** count
nn = n * pw + n
nnn = nn * pw + n
summa = n + nn + nnn
print("Сумма чисел n + nn + nnn =", summa)


