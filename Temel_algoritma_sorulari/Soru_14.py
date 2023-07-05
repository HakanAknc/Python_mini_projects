# 14- Kullanıcının istediği kadar sayıyı, kullanıcıdan alarak bir diziye aktaran, 
# bu sayıların toplamını ve ortalamasını bulan programını yazınız?

adet = int(input("Kaç adet sayı girmek istiyorsunuz : "))

dizi = []

for i in range(adet):
    dizi.append(int(input("Sayı giriniz : ")))

print(dizi)

toplam = 0

for x in dizi:
    toplam += x

print("Toplam = ",toplam)
print("Ortalama = ",toplam/adet)