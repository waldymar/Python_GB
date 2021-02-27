with open("file_task4.txt", "r") as f_obj:
    content = f_obj.readlines()
    for w in content:
        ab = w.split(" - ")
        if ab[0] == "One":
            ab[0] = "Один"
        elif ab[0] == "Two":
            ab[0] = "Два"
        elif ab[0] == "Three":
            ab[0] = "Три"
        elif ab[0] == "Four":
            ab[0] = "Четыре"
        abc = " - ".join(ab)
        with open("file_task4_ru.txt", "a", encoding="UTF-8") as f_obj2:
            f_obj2.writelines(abc)
