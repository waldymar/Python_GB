sk = int(input("Сколько товаров хотите внести? "))
my_list, my_list_a, my_list_b, my_list_c, my_list_d = [], [], [], [], []
for i in range(1, sk + 1):
    a = input("Название товара: ")
    b = float(input("Цена товара: "))
    c = int(input("Количество товара: "))
    d = input("Единица товара: ")
    my_dict = {'название': a, 'цена': b, 'количество': c, 'ед': d}
    w = (i, my_dict)
    my_list.append(w)
    my_list_a.append(a)
    my_list_b.append(b)
    my_list_c.append(c)
    my_list_d.append(d)
    dict2 = {'название': my_list_a, 'цена': my_list_b, 'количество': my_list_c, 'ед': my_list_d}
print('Структура данных о товарах', my_list)
print('Аналитика о товарах', dict2)






