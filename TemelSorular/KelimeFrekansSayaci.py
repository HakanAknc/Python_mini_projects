# Kelime Frekans Sayacı: Kullanıcının girdiği metindeki her kelimenin kaç kez tekrarlandığını sayan bir program.

def kelime_frekansi():    # kelime_frekansi() adında bir fonksiyon tanımlanır
    metin = input("Metin girin: ")   # Kullanıcıdan metin girişi alınır ve input() fonksiyonu ile metin adlı bir değişkene atanır.
    kelimeler = metin.split()    # Metindeki kelimeleri ayırmak için split() fonksiyonu kullanılır.

    frekanslar = {}    # frekanslar adında boş bir sözlük (dictionary) oluşturulur.
    for kelime in kelimeler:    # for döngüsü ile kelimeler listesindeki her bir kelime üzerinde gezinilir. 
        frekanslar[kelime] = frekanslar.get(kelime, 0) + 1

    print("Kelime Frekansları: ")
    for kelime,frekans in frekanslar.items():  # kinci for döngüsünde, frekanslar.items() fonksiyonu kullanılarak, frekanslar sözlüğündeki her bir anahtar-değer çifti (kelime ve frekans) üzerinde gezinilir. 
        print(f"{kelime}: {frekans}")   # Her bir kelime ve frekans çifti, print() fonksiyonu ile ekrana yazdırılır.

kelime_frekansi()




# frekanslar[kelime] = frekanslar.get(kelime, 0) + 1

"""
a. frekanslar.get(kelime, 0) ifadesi, frekanslar sözlüğünde kelime anahtarının varsa bu anahtarın değerini döndürür. 
Eğer kelime anahtarı sözlükte yoksa, 0 değeri döndürür. 
Bu sayede daha önce oluşturulmamış kelimenin frekansı için başlangıç değeri olarak 0 kullanılır.

b. + 1 ifadesi, her bir kelimenin frekansının 1 artırılması anlamına gelir. Yani her bir kelimenin frekansı, sözlükteki değeri kadar artar.

c. frekanslar[kelime] ifadesi, kelime adlı anahtara karşılık gelen değeri günceller. 
Eğer kelime anahtarı daha önce sözlükte yoksa, yeni bir anahtar oluşturulur ve değeri 1 olur. 
Eğer kelime anahtarı zaten sözlükte varsa, değeri 1 artırılarak güncellenir.
"""