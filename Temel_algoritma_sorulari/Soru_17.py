# 17- Kullanıcın girdiği mXn boyutta bir matris oluşturup bu matrisi rastgele sayılarla doldurunuz. 
# Bu matrisin transpozesini oluşturunuz?

import random

satir = int(input("Satır sayısı : "))
sutun = int(input("Sütün sayısı : "))

m = [[0 for x in range(sutun)] for y in range(satir)]
mt = [[0 for x in range(satir)] for y in range(sutun)]

for i in range(satir):
    for j in range(sutun):
        m[i][j] = random.randint(0,9)
        mt[i][j] = m[i][j]

print(m)
print(mt)