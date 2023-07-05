# 8-) n'den m'ye kadar olan sayılardan 7'ye tam bölünenleri bulunuz? n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktır.

while True:
    n = int(input("Başlangıç sayısı giriniz : "))
    m = int(input("Bitiş sayısı giriniz : "))
    
    if n>=m:
        print("Başlangıç daha küçük olmalı, tekrar sayı giriniz.")
    else:
        break

toplam = 0

for i in range(n,m):
    if i%7 == 0:
        toplam += i
    
print("Yediye tam bölünenlerin toplamı = ", toplam)