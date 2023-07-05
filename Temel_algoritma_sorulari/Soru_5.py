# 5-) Vize notunun %40'ını, Final notunun %60'ını alarak ortalama notu hesaplayan, 
# ortalama 50 den büyükse "Geçti", küçükse "Kaldı" yazan programı yazınız?

vize = int(input("Vize notu giriniz : "))
final = int(input("Final notu giriniz : "))

ortalama = (float(vize * 0.4) + (final * 0.6))
print("Ortalamanız = ", ortalama)

if ortalama >= 50:
    print("Geçtiniz :)")
elif ortalama < 50:
    print("Kaldınız :(")
else:
    print("Yanlış değer girdiniz.")