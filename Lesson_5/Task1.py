with open("my_file.txt", "w") as f_obj:
    stop = False
    while stop == False:
        content = input("Введите данные построчно: ")
        f_obj.write(content + "\n")
        if not content:
            stop = True
