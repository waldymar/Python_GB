from math import factorial

# gen = [factorial(el) for el in range(5)]
# print(gen)

n = int(input("Введите число: "))

def generator():
    en = 1
    for el in range(1, n + 1):
        en *= el
        yield en

g = generator()

for en in g:
    print(en, end=" ")
