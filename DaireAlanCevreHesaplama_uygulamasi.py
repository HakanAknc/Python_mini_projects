# Dairenin alanını ve çevresini hesaplayan programın Python kodunu yazınız. Dairenin yarıçapını kullanıcıdan alınız.

# Dairenin alanı : pi * yarıçap * yarıçap
# Dairenin çevresi : 2 * pi * yarıçap

pi = 3,14159
yaricap = int(input("Alan giriniz: "))

daireAlan = pi * yaricap * yaricap
daireCevre = 2 * pi * yaricap

print("Dairenin alanı: ", daireAlan, ", dairenin çevresi: ", daireCevre)