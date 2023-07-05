# 9-) Kullanıcıdan ismini alıp ekrana tersten yazan programı yazınız?

isim = input("İsminizi giriniz : ")

# 1.Yol
# isim = isim [::-1]
# print(isim)

# 2.Yol
uzunluk = len(isim)
print(uzunluk)
ters = " "
for i in range(uzunluk -1,-1,-1):
    ters += isim[i]

print(ters)