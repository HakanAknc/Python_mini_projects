# Kullanıcıdan alınan iki sayıyı çarpan kodu yazınız?
a = int(input("a: "))
b = int(input("b: "))

def topla(a,b):
    return a * b

print("Sonuç:",topla(a,b))

print("**"*30)


# Kullanıcıdan alınan iki sayının büyük olanını ekrana yazdıran kodu yazınız?
x = int(input("x: "))
y = int(input("y: "))

def buyukOlan(x,y):
    if x>y:
        print("x büyüktür.")
    else:
        print("y büyüktür.")
    return "x:",x ,"y:",y     # buraya ne yazıcağımı bilemedimmmm
 
print(buyukOlan(x,y))