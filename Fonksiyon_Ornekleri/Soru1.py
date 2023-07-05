# Soru 1: Parametre olarak bir liste alan ve listenin elemanlarını toplayan bir fonksiyon yazın.

def liste_topla(liste):
    toplam = sum(liste)
    return toplam

my_list = [1,2,3,4,5]
print(liste_topla(my_list))

