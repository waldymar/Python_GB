ml = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# ml2 = [ml.count(a) for a in ml]
ml3 = []

"""1й способ"""
# for i in range(len(ml2)):
#     if ml2[i] == 1:
#         ml3.append(ml[i])
# print(ml3)

# ans = [ml3.append(ml[b]) for b in range(len(ml2)) if ml2[b] == 1]
# print(ml3)

"""2й способ"""
# for ab in ml:
#     if ml.count(ab) == 1:
#         ml3.append(ab)
# print(ml3)

ans = [ml3.append(ab) for ab in ml if ml.count(ab) == 1]
print(ml3)

"""3й способ"""
# for i in range(len(ml)):
#     count = 0
#     for j in range(len(ml)):
#         if ml[i] == ml[j]:
#             count += 1
# #    print(count)
#     if count == 1:
#         ml2.append(ml[i])
# print(ml2)

