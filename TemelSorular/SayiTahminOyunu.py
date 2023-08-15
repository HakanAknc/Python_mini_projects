# Sayı Tahmin Oyunu: Bilgisayarın rastgele bir sayı tuttuğu ve kullanıcının bu sayıyı tahmin etmeye çalıştığı bir oyun.

import random       # random kütüphanesi kullanıldı

def sayi_tahmin_oyunu():   # fonksiyon tanımı kullanıldı
    rastgele_sayi = random.randint(1, 100)   # 1-100 arasında sayı alındı ekrandan
    tahmin_hakki = 5    # kullanıcıya 5 hak verildi

    while tahmin_hakki > 0:   # döngü kuruldu
        tahmin = int(input("Tahmininizi giriniz (1-100 arası): "))  # kullanıcıdan tahmin alındı
        if tahmin == rastgele_sayi:   # eğer tahmin doğruysa
            print("Tebrikler! Doğru tahmin ettiniz.")
            break  # programı durdur
        elif tahmin < rastgele_sayi:   # eğer tahmin küçükse 
            print("Daha büyük bir sayı girin.")
        else:   # eğer tahmin büyükse
            print("Daha küçük bir sayı girin.")

        tahmin_hakki -= 1   # tahmin hakkını birer birer azalt
    
    if tahmin_hakki == 0:   # eğer tahmin hakkı sıfıra eşitse
        print("Tahmin hakkınız bitti. Rastgele sayı:", rastgele_sayi)

sayi_tahmin_oyunu()     # sayı_tahmin_oyunu fonksiyonunu çağır
