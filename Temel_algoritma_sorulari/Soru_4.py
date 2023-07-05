# 4-) İkinci dereceden ax2 + bx + c = 0 denkleminin diskriminant çözümünü yapınız? 
# Kullanıcıdan a,b ve c değerlerini alarak deltayı hesaplayınız?

import math

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

delta = b**2 - 4*a*c
print("Delta = " , delta)

if delta > 0:
    kok1 = (-b + math.sqrt(delta)) / (2*a)
    kok2 = (-b - math.sqrt(delta)) / (2*a)
    print("Denklemin iki farklı kökü vardır.")
    print("Kök 1 = " , kok1)
    print("Kök 2 = " , kok2)
elif delta == 0:
    kok = -b/(2*a)
    print("Denklemin çakışık kökü vardır.")
    print("kök1 = kök2 = " , kok)
else:
    print("Denklemin kökü yoktur.")
