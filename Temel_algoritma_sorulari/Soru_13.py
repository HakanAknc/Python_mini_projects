# 13-) Kullanıcıdan 10 adet sayı alan ve tek ve çift sayıların adetini, toplamını ve ortalamalarını bulan programını yazınız?

s = 0
tek_sayac = 0
cift_sayac = 0
tek_toplam = 0
cift_toplam = 0

for i in range(1,11):
    s = int(input("Sayı giriniz : "))
    if s%2==1:
        tek_sayac += 1
        tek_toplam += s
    else:
        cift_sayac += 1
        cift_toplam += s

print()

print(tek_sayac, "adet tek sayı vardır. Toplamları = ", tek_toplam)
print("Tek sayıların ortalaması = ",tek_toplam/tek_sayac)

print()

print(cift_sayac, "adet çift sayı vardır. Toplamları = ", cift_toplam)
print("Çift sayıların ortalamsı = ", cift_toplam/cift_sayac)