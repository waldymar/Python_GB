def sum_num():
    e = "да"
    grtotal = 0
    flag = True
    while e.strip() != "нет":
        a = input("Введите строку чисел: ")
        b = a.split()
        total = 0
        for n in b:
            if n.isdigit() == True:
                total += float(n)
            else:
                flag = False
        grtotal += total
        # print(grtotal)
        if flag == True:
            print(grtotal)
            e = input("Желаете еще ввести строку чисел? Ответьте, пожалуйста, да или нет: ").lower()
        else:
            break
    return grtotal

print(f"Сумма чисел, введенных через пробел, равняется {sum_num()}")