boy = int(input("Boyunuz cm cinsinden giriniz: : "))
yas = int(input("Yaşınız: "))

if boy >=  165:
    if yas >= 18:
        print("Buyrun biletiniz iyi eğlenceler. ")
    else:
        print("Yaşınız yetmiyor.")
else:
    print("Boyunuz yetmiyor.")