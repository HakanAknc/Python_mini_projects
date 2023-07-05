isim = input("İsminizi giriniz: ")
yas = int(input("Yaşınız: "))
egitim = input("Eğitim durumunuz: ")

if yas >= 18:
    if (egitim == "lise") or (egitim == "üniversite"):
        print(f"{isim} Ehliyet alabilirsin. Hayırlı olsun :) ")
    else:
        print(f"{isim} Eğitim durumun yetersiz.       :( ")
else:
    print(f"{isim} Evlat yaşın yetmiyor büyüde gel...")
