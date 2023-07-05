# 7-) 1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz? n sayısı kullanıcıdan alınacaktır

toplam = 0

n = int(input("n sayısını giriniz : "))

for i in range(n):
    if i%2 == 1:
        toplam += i
print("Tek sayıların toplamı : " , toplam)