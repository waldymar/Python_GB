"""1й способ через **"""
def my_func(x, y):
    z = x ** y
    return z


print(f"Результат возведения числа в степень равен: {round(my_func(3, -3), 2)}")

"""2й способ через цикл"""
def my_func2(x, y):
    a = 1
    for i in range(abs(y)):
        a *= 1 / x
    return a

print(f"Результат возведения числа в степень равен: {round(my_func2(3, -3), 2)}")

