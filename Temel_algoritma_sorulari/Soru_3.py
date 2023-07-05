# 3-) Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız?

x = int(input("x sayısı : "))
y = int(input("y sayısı : "))
z = int(input("z sayısı : "))

if x>y and x>z:
    print("X sayısı büyüktür.")
elif y>x and y>z:
    print("Y sayısı büyüktür.")
else:
    print("Z sayısı büyüktür.")
    