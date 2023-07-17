isim = input("İsminizi girin: ")   # Eksik ekleme yapılcak

ortalama = float(input("Ortalamınız: "))

if ortalama >= 85:
    print(f"Tebrikler {isim}. Takdir belgesi aldın")
elif (70 <= ortalama) and (ortalama < 85):
    print(f"Tebrikler {isim}. Teşekkür belgesi aldın")
else:
    print(f"Malesef {isim}. Belge alamdın")