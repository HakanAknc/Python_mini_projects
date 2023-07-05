# 18- Kullanıcıdan alınan 4 basamaklı bir sayıyı yazı ile yazınız? 
# Kullanıcı 3215 girmiş olsun "üç bin iki yüz on beş" ekrana yazılsın.

birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
yuzler = ["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]
binler = ["","bin","ikibin","üçbin","dörtbin","beşbin","altıbin","yedibin","sekizbin","dokuzbin"]

sayi = int(input("4 basamaklı sayı giriniz : "))

s = str(sayi)

print(binler[int(s[0])],yuzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])