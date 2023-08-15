def diktorgen_hesaplma():  # fonkiyon oluşturuldu
    uzunluk = float(input("Dikdörtgeni uzunluğunu girin : "))  # uzunluk alındı
    genislik = float(input("Dikdörgenib genişliğini girin : "))  # genişlik alındı

    alan = uzunluk * genislik   # formüller
    cevre = 2 * (uzunluk * genislik)

    print(f"Dikdörtgenin alanı = {alan}")   # yazdırma
    print(f"Dikdörtgenin çevresi = {cevre}")

diktorgen_hesaplma()

