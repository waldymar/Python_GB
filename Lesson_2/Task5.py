rating = [7, 5, 3, 3, 2]
a = int(input("Введите новый элемент рейтинга: "))
rating.append(a)
rating.sort(reverse=True)
print(rating)
