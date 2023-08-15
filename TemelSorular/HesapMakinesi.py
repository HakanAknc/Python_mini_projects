# Hesap Makinesi: Temel matematiksel işlemleri (toplama, çıkarma, çarpma, bölme) yapabilen bir hesap makinesi.

def hesap_makinesi():   # fonksiyon oluşturuldu
    while True:
        print("*"*10)
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")
        print("*"*10)
        print()

        secim = int(input("İşlem seçin (1-5): "))     # kullanıcıdan seçim yapılması istendi

        if secim == 5:   # eğer seçim 5'e eşitse
            print("Çıkış yapılıyor...")
            break  # programı durdur

        sayi1 = float(input("Birinci sayıyı giriniz = "))   # kullanıcıdan sayı alındı
        sayi2 = float(input("İkinci sayıyı giriniz = "))

        if secim == 1:
            sonuc = sayi1 + sayi2
        elif secim == 2:
            sonuc = sayi1 - sayi2
        elif secim == 3:
            sonuc = sayi1 * sayi2
        elif secim == 4:
            sonuc = sayi1 / sayi2
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
            continue
        
        print()
        print("Sonuç : ",sonuc)
    
hesap_makinesi()

        