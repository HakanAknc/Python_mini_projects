# Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python programı

genislik = input("Genişlik :")
yukseklik = input("Yükseklik : ")
 
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print ("Alan :",alan)
    return alan
 
dikdortgenAlan(genislik, yukseklik)
