# Liste İçindeki Sayıların Çarpımını Bulma
# Aşağıdaki listede verilmiş sayıların çarpımını bulunuz

liste = [1,2,3,4,5]

def carpim(liste):
    toplam = 1
    for i in liste:
        toplam *= i
    return toplam

sonuc = carpim(liste)
print(f"Listedeki sayıların toplamı: {sonuc}")