from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el, end=" ")

с = 0
for em in cycle("HELLO"):
    if с > 10:
        break
    print(em, end="*")
    с += 1
