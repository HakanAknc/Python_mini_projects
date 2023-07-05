# 2-) Kullanıcıdan iki sayı alarak bunların toplamını ve ortalamasını ekrana yazan programı yazınız?

toplam = 0

sayi1 = int(input("1.Sayı'yı giriniz : "))
sayi2 = int(input("2.Sayı'yı giriniz : "))

toplam = sayi1 + sayi2
ortalama = float(toplam) / 2

print("Toplam = " , toplam)
print("Ortalam = " , ortalama)