# Girilen 2 Sayıdan Büyük Olanı Bulma
# Kullanıcı tarafından girilen iki sayıdan büyük olanı bulunuz.

a = int(input("a: "))
b = int(input("b: "))

def büyükOlan(a, b):
    if a > b:
        return a 
    return b

sonuc = büyükOlan(a,b)
print(f"Büyük olan sayı: {sonuc}")