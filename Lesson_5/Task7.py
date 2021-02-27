import json

with open("file_task7.txt", "r") as f_obj:
    content = f_obj.readlines()
    total = 0
    total_pr = 0
    dict_res = {}
    for line in content:
        # print(line)
        ab = line.split(" ")
        # print(ab)
        res = int(ab[2]) - int(ab[3])
        # print(res)
        total += res
        if res > 0:
            total_pr += res
        dict = {ab[0]: res}
        dict_res.update(dict)
    dict_avg = {"Average profit": total_pr}
    list_final = [dict_res, dict_avg]
    # print(total)
    # print(total_pr)
    # print(dict_res)
    # print(dict_avg)
    # print(list_final)

with open("my_file.json", "w") as write_f:
    json.dump(list_final, write_f)
    json_str = json.dumps(list_final)
    print(json_str)
