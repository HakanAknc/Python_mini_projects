# 19-) Tersten yazıldığında da aynı değeri olan sayılara Palindrom sayılar denir. 
# Örnek olarak "1991" veya "34543" sayıları tersten yazılsa bile aynı değerde olurlar. 
# 1000 - 100000 sayıları arasındaki palindromları bulan programı yazınız?

for i in range(1000, 100000):
    s = str(i)
    t = s[::-1]
    if s == t:
        print(s)