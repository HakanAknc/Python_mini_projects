# 12-) 0 ile 1000 arasındaki Asal sayıları bulan programı yazınız?
# Sadece 1'e ve kendisine bölünen sayı
# 13 -> 2, 3, 4, ... , 12

# Kullanıcıdan alınan sayının asal olup olmadığını kontrol ettik
"""
bolen_sayac = 0

sayi = int(input("Sayı giriniz : "))

for i in range(2,sayi):
    if(sayi%i==0):
        bolen_sayac += 1

if bolen_sayac == 0:
    print("Sayı asaldır.")
"""



# 0 ile 1000 arası asal kontrolü

bolen_sayac = 0

for j in range(3,1000):
    bolen_sayac = 0
    for i in range(2,j):
        if(j%i==0):
            bolen_sayac += 1
        
    if bolen_sayac == 0:
        print(j)