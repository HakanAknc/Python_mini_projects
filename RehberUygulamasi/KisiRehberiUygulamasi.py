rehber = {}   # boş bir dizi tanımlandı

def kisi_ekle():
    ad = input("Kişinin adını girin: ")
    tel = int(input("Kişinin telefonunu girin: "))
    rehber[ad] = tel
    print("Kişi rehbere eklendi.")

def kisi_sil():
    ad = input("Silmek istediğiniz kişinin adını girin: ")
    if ad in rehber:
        del rehber[ad]
        print("Kişi rehberden silindi.")
    else:
        print("Bu isimde bir kişi reberde bulunamadı.")

def kisi_ara():
    ad = input("Aramak istediğniz kişinin adını girin: ")
    if ad in rehber:
        tel = rehber[ad]
        print("Kişinin telefon numarası: ",tel)
    else:
        print("Bu isimde bir kişi rehberde bulunamadı.")

def rehberi_goster():
    if rehber:
        print("Rehberdeki kişiler: ")
        for ad, tel in rehber.items():
            print("Ad:", ad, "\tTelelfon:", tel)
    else:
        print("Rehber boş.")

def uygulama_calistir():
    print("Kişi Rehberi Uygulamsı")
    while True:
        print("\nYapmak istediğiniz işlemi seçiniz: ")
        print("1. Kişi Ekle")
        print("2. Kişi Sil")
        print("3. Kişi Ara")
        print("4. Rehberi Göster")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "1":
            kisi_ekle()
        elif secim == "2":
            kisi_sil()
        elif secim == "3":
            kisi_ara()
        elif secim == "4":
            rehberi_goster()
        elif secim == "5":
            print("Programdan çıkış yapılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

uygulama_calistir()
