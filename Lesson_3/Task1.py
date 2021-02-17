def d_calc():
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    try:
        c = a / b
    except ZeroDivisionError:
        return
    return c


d = d_calc()
print(d)
