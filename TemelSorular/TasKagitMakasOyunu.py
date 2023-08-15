import random

def tas_kagit_makas():   # tas_kagit_makas() adında bir fonksiyon tanımlandı
    secenekler = ["Taş", "Kağıt", "Makas"]   # secenekler adında bir liste oluşturuldu

    while True:  # sonsuz döngü
        print("1. Taş")
        print("2. Kağıt")
        print("3. Makas")
        print("4. Çıkış")

        secim = int(input("Seçiminizi girinizç. (1-3): "))  # kullanıcıdan seçim alındı

        if secim == 4:  # eğer 4'e eşitse
            print("Çıkış yapılıyor...")
            break  # program durduruldu

        elif secim in [1, 2, 3]:
            bilgisiyar_secim = random.choice(secenekler)  # bilgisiyardan rastgele seçenek alınır
            kullanici_secim = secenekler[secim - 1]   # kullanıcıdan seçenek alınır 

            print(f"Siz: {kullanici_secim} / Bilgisiyar: {bilgisiyar_secim}")  # ekrana yazdırılır

            if kullanici_secim == bilgisiyar_secim: 
                print("Berabere!")
            elif (kullanici_secim == "Taş" and bilgisiyar_secim == "Makas") or \
                 (kullanici_secim == "Kağıt" and bilgisiyar_secim == "Taş") or \
                 (kullanici_secim == "Makas" and bilgisiyar_secim == "Kağıt"):
                print("Tebrikler kazandınız   :) ")
            else:
                print("Bilgisayar kazandı!")
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

tas_kagit_makas()