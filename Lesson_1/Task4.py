num = int(input("Введите число "))
maxim = -1
while num != 0:
    a = num % 10
    if a > maxim:
        maxim = a
    num //= 10
print("Максимальная цифра в числе равно", maxim)