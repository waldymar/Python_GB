a = int(input("Выберете количество элементов в списке: "))
b = []
for i in range(a):
    c = int(input("укажите элемент списка: "))
    b.append(c)
e = []
for k in range(len(b)):
    if k % 2 == 0 and k != (len(b) - 1):
        e.append(b[k + 1])
    elif k % 2 == 1:
        e.append(b[k - 1])
    else:
        e.append(b[k])
print("Изначальный лист =", b)
print("Измененный лист =", e)

