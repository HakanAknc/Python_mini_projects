# Benim eksik olan çözümüm
"""
isim = input("İsimini öğrenebilirmiyim: ")
print("Hoşgeldin ",isim)
pizza = input("Hangi boy pizza istersiniz: ")
ekstra = input("Patates ister misiniz: ")

if pizza == "Küçük boy":
    print(f"{pizza} pizzanız hazırlanıyor. Borcunuz: 25 TL Afiyet olsun :)")
elif pizza == "Orta boy":
    print(f"{pizza} pizzanız hazırlanıyor. Borcunuz: 30 TL Afiyet olsun :)")
elif pizza == "Büyük boy":
    print(f"{pizza} pizzanız hazırlanıyor. Borcunuz: 35 TL Afiyet olsun :)")
else:
    print("Yanlış siparişi girdiniz.")
"""

# Çözüm

print("H ∞ H Pizza'ya Hoşgeldiniz :)")

boyut = input("Ne boyut bir pizza istiyorsunuz? 'S', 'M' veya 'L': ")    
ekstra_peynir = input("Fazladan peynir istiyor musunuz? (Evet/Hayır): ")
icecek = input("İçecek alıyor musunuz? (Evet/Hayır): ")

hesap = 0

if boyut == "S":
    hesap += 20
elif boyut == "M":
    hesap += 25
else:
    hesap += 30

if ekstra_peynir == "Evet":
    if boyut == "S":
        hesap += 2    # S için +2
    else:
        hesap += 3    # M, L için +3

if icecek == "Evet":
    hesap += 2

print(f"Toplam tutar: {hesap} TL.")