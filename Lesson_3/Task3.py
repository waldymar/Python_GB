def my_func(var1, var2, var3):
    b = min(var1, var2, var3)
    c = sum([var1, var2, var3])
    return c - b


d = my_func(20, 30, 10)
print(f"Сумма наибольших 2х аргументов равняется - {d}")
