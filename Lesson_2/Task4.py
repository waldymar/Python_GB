a = input("Введите какую-то строку: ")
b = a.split()
for i in range(len(b)):
    if len(b[i]) < 10:
        print(i + 1, b[i])
    else:
        print(i + 1, b[i][:10])


