# 20-) Kullanıcıdan alınan bir cümlede kaç adet kelime olduğunu ve kaç adet harf olduğunu bulan programı yazınız?

s = input("Bir string giriniz :")

bosluk_sayac = 0

for i in s:
    if i == " ":
        bosluk_sayac += 1

print("Boşluk adedi : ",bosluk_sayac)
print("Kelime sayısı : ",bosluk_sayac+1)
print("Harf sayısı : ",len(s))