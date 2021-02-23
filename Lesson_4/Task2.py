ml = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ml2 = []
cl = [ml2.append(ml[i + 1]) for i in range(len(ml) - 1) if ml[i + 1] > ml[i]]

# for i in range(len(ml) - 1):
#     if ml[i + 1] > ml[i]:
#         ml2.append(ml[i + 1])

print(ml2)
