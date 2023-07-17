isim = input("isminizi giriniz :" )
vize = int(input("vize notunuz : "))
final = int(input("final notunuz : "))

ortalama = vize*0.4 + final*0.6

if ortalama >= 60:
    print(f"{isim} dersten geçti")
else:
    print(f"{isim} dersten kaldı")