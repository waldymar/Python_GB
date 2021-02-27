with open("file_task2.txt", "r") as f_obj:
    content = f_obj.readlines()
    a = int(len(content))
    print(f"Количество строк в файле равняется {a}")
    for i in range(a):
        ab = content[i].replace("\n", "")
        b = len(ab.replace(" ", ""))
        print(f"В {i + 1}-й строке {b} букв")

