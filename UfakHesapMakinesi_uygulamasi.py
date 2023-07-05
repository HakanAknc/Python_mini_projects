"""
sayi1 = float(input("sayı1: "))    # Fonksiyon kullanılmadan yapılan Hesap Makinesiii
sayi2 = float(input("sayi2: "))

islem = input("Hangi işlemi yapmak istiyorsunuz (+,-,*,/): ")

if islem=="+":
    print("Toplam: ",sayi1+sayi2)
elif islem=="-":
    print("Çıkarma: ",sayi1-sayi2)
elif islem=="*":
    print("Çarpma: ",sayi1*sayi2)
elif islem=="/":
    print("Bölme: ",sayi1/sayi2)
else:
    print("Yanlış bir yere bastınız!!!")
"""

sayi1 = float(input("sayı1: "))   
sayi2 = float(input("sayi2: "))

islem = input("Hangi işlemi yapmak istiyorsunuz (+,-,*,/): ")
print("Seçtiğiniz işlem: ",islem)

def sonc(sayi1,sayi2):
    if islem=="+":
        print("Toplam: ",sayi1+sayi2)
    elif islem=="-":
        print("Çıkarma: ",sayi1-sayi2)
    elif islem=="*":
        print("Çarpma: ",sayi1*sayi2)
    elif islem=="/":
        print("Bölme: ",sayi1/sayi2)
    else:
        print("Yanlış bir yere bastınız!!!")
    return "sayı1:",sayi1,"sayı2:",sayi2      ## buraya ne yazıcağımı gene bilemedimmmm

print(sonc(sayi1,sayi2))