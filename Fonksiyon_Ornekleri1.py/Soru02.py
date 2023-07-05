# Girilen 3 Sayıdan Büyük Olanı Bulma
# Kullanıcı tarafından girilen üç sayıdan büyük olanı bulunuz.

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

def buyukOlanıBulma(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    return z

sonuc = buyukOlanıBulma(x,y,z)
print(f"Büyük olan sayı: {sonuc}")