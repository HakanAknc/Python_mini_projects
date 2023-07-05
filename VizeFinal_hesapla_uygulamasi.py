'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
   
'''

vize1 = int(input("1.Vize notunuz: "))
vize2 = int(input("2.Vize notunuz: "))
final = int(input("Final notunuz: "))
a = "1.koşul için:"
b = "2.koşul için:"

ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)
print("Ortalama: ",ortalama)

val = (ortalama >= 50) and (final >= 50)
val = (ortalama >= 50) or (final >= 70)

# a-)
if (ortalama >= 50):
    if (final >= 50):
        print(f"{a} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARILI")
    else:
        print(f"{a} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARISIZ. Finalden en az 50 almalısınız")
else:
    print(f"{a} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARISIZ")

# b-)
if (ortalama >= 50):
    print(f"{b} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARILI")
else:
    if (final >= 70):
        print(f"{b} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARILI. Fianlden 70 aldığnız için geçtiniz")
    else:
        print(f"{b} Öğrencinin ortalaması: {ortalama} geçme durumu: BAŞARISIZ.")