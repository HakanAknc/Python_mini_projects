print("1. Otel LUİ")
print("2. Otel ŞAKA")
print("3. Otel ÇANKIRI")

secim = input("Lütfen bir otel seçiniz (1-3): ")

if secim == "1":
    print("Otel LUİ seçildi.")
    oda_sayisi =list(range(1, 11))              # Örneğin, Otel A'da 10 adet oda olduğunu varsayalım
    print("Otel LUİ için oda sayısı):", oda_sayisi)
    oda_secimi =int(input("Lütfen bir oda  seçiniz (1-10): "))
    print("Otel LUİ için oda seçildi:")
    if oda_secimi in [1,2,3]:
        print("Seçilen odalar doludur.  *** Kusurbakmayın ***" )
    else:
        print("Seçilen odalar boştur.  İyi tatiller :)" )

elif secim == "2":
    print("Otel ŞAKA seçildi.")
    oda_sayisi = list(range(1, 16))
    print("oda sayısı (otel ŞAKA):",oda_sayisi)
    oda_secimi = int(input ("lütfen bir oda seçiniz(1-15): "))
    print("Otel ŞAKA için oda seçildi:")
    if oda_secimi in [8,10,13,15]:
        print("seçtiğiniz odalar doludur")
    else:
        print("seçtiğiniz odalar boştur")


elif secim == "3":
    print("Otel ÇANKIRI seçildi.")
    oda_sayisi = list(range(1,6))
    print("oda sayısı (otel ÇANKIRI):",oda_sayisi)
    oda_secimi = int(input("lütfen bir oda seçiniz(1-5):"))
    print("Otel ÇANKIRI için oda seçildi:", )
    if oda_secimi in [1,3]:
        print("seçtiğiniz odalar doludur")
    else:
        print("seçtiğiniz odalar boştur")
    
else:
    print("Geçersiz seçenek!")