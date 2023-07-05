# Benim eksik olan çözümüm
"""
sifre = 12345 
hak = 5
sayac = 0

while hak >= 5:
    hak -= 1
    sayac += 1
    parola = int(input("Parola gririniz: "))

    if hak == sifre:
        print(f"{sayac}.Tebrikler.")
        break
    else:
        print(f"{sayac}.Malesef yanlış")
"""

# Çözüm

sayi = 1
sayac = 0

while sayi <= 5:
    sayi += 1
    sayac += 1
    parola = int(input("Parola giriniz: "))
    if parola == 123:
        print(f"{sayac}.hakkınız: Girdiğiniz parola doğru  :)")
        break
    else:
        print(f"{sayac}.hakkınız: Girdiğiniz parola yanlış  :(")