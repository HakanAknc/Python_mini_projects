# 15-) Kullanıcının istediği büyüklükte bir diziyi 0-100 arasında rastgele oluşturulmuş sayılarla doldurup 
# bu sayıların standart sapmasını hesaplayınız

import random
import math

u = int(input("Dizi uzunluğunu giriniz : "))

dizi = []

for i in range(u):
    dizi.append(random.randint(0,100))

print(dizi)

toplam = 0

for x in dizi:
    toplam += x

print("Toplam = ", toplam)
ortalama = toplam / u
print("Ortalama = ", ortalama)

fark_toplam = 0

for x in dizi:
    fark = x - ortalama
    fark = fark**2
    fark_toplam += fark

ssapma = math.sqrt(fark_toplam/u)

print("Standar sapma = ",ssapma)