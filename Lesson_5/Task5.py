with open("file_task5.txt", "a") as f_obj:
    total = 0
    for i in range(5):
        content = int(input("Введите число: "))
        total += content
        ab = f_obj.write(str(content) + " ")
    print(total)



