# Soru 3: Bir sayının faktöriyelini hesaplayan bir fonksiyon yazın.

""" 
sayi = int(input("Faktöriyel hesaplamak için değer giriniz: "))   # fonksiyonsuz çözüm
deger = 1
for i in range(sayi):
    deger = deger * (i+1)

print("Faktöriyel Sonucu: ",deger)
"""

def faktoriyel(sayi):
    faktoriyel = 1
    for i in range(1,sayi+1):
        faktoriyel *= i
    return faktoriyel

num = 6
print(faktoriyel(num))