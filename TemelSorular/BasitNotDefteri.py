def not_defteri():   # not_defteri adında fonksiyon oluşturuldu
    notlar = []    # notlar adında boş dizi oluşturuldu
    while True:   # sonsuz döngü oluşturuldu
        print("1. Not Ekle")
        print("2. Notları Göster")
        print("3. Çıkış")

        secim = int(input("Seçim yapınız. (1-3): "))  # kullanıcıdan seçim alınıdı

        if secim == 3:
            print("Çıkış yapılıyor...")
            break

        elif secim == 1:  # eğer seçim bire eşitse
            not_icerik = input("Not içeriğini giriniz: ")   # kullanıcıdan not alınıyor
            notlar.append(not_icerik)   # kullanıcıdan alınan not içerikleri notlar dizisine ekleniyor
            print("Not başarıyla eklendi.")
        
        elif secim == 2:  # eğer seçim ikiye eşitse
            if notlar:   
                print("Notlar: ")
                for i, not_ in enumerate(notlar, start=1):
                    print(f"{i}, {not_}")
            else:
                print("Not defteri boş.")

        else:
            print("Geçersiz seçim. Tekrar deneyin.")
        
not_defteri()