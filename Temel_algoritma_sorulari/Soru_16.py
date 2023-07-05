# 16- 3X3 rastgele sayılardan oluşan 2 matris oluşturun.Bu matrislerin, toplamını hesaplayınız.

import random

m1 = [[0 for x in range(3)] for y in range(3)]
m2 = [[0 for x in range(3)] for y in range(3)]
mt = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        m1[i][j] = random.randint(0,5)
        m2[i][j] = random.randint(0,5)
        mt[i][j] = m1[i][j] + m2[i][j]

print(m1)
print(m2)
print(mt)
