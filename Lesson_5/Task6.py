with open("file_task6.txt", "r", encoding="UTF-8") as f_obj:
    content = f_obj.readlines()
    res_dict = {}
    for line in content:
        # print(line)
        sp = line.split(":")
        # print(sp)
        sp2 = sp[1].split(" ")
        # print(sp2)
        total = 0
        for ab in sp2:
            abc = ab.split("(")
            # print(abc)
            for num in abc:
                # print(num)
                if num.isdigit() is True:
                    total += int(num)
        # print(total)
        # dict = {}
        # dict[sp[0]] = total
        dict = {sp[0]: total}
        res_dict.update(dict)
    print(res_dict)

