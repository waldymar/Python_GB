with open("file_task3.txt", "r") as f_obj:
    content = f_obj.readlines()
    num = len(content)
    total = 0
    for line in content:
        ab = line.split(" - ")
        abc = int(ab[1].replace("\n", ""))
        if abc < 20000:
            print(ab[0])
        total += abc
    sr_zp = total / num
    print(sr_zp)