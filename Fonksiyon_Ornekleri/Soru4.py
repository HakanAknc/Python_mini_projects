# Soru 4: İki sayı arasındaki tüm asal sayıları döndüren bir fonksiyon yazın.

# # 1.Çözüm
# sayi1 = int(input("sayı1: "))
# sayi2 = int(input("sayı2: "))

# def asalSayiBulma(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# asalSayiBulma(sayi1,sayi2)

print("*"*30)
# 2.Çözüm
def asal_sayilar(baslangic, bitis):
    asal_sayilar = []
    for sayi in range(baslangic, bitis + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar

start = 10
end = 30
print(asal_sayilar(start, end)) 