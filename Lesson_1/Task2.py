a = int(input("Который час? "))
chas = a // 3600
min = (a - chas * 3600) // 60
sec = a - chas * 3600 - min * 60
print("%02d" % chas, "%02d" % min, "%02d" % sec, sep=":")
