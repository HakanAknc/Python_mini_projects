while True:
   print("1. Toplama (+)")
   print("2. Çıkarma (-)")
   print("3. Çarpma  (*)")
   print("4. Bölme   (/)")
   print("5. Çık")
   print("Hangi işlemi yapmak istiyorsun (1-5): ", end="")
   ch = int(input())
   if ch>=1 and ch<=4:
      print("\nİki sayı giriniz : ", end="")
      numOne = float(input())
      numTwo = float(input())
   if ch==1:
      res = numOne + numTwo
      print("\nSonuç =", res)
   elif ch==2:
      res = numOne - numTwo
      print("\nSonuç =", res)
   elif ch==3:
      res = numOne * numTwo
      print("\nSonuç =", res)
   elif ch==4:
      res = numOne / numTwo
      print("\nSonuç =", res)
   elif ch==5:
      print("Uygulamadan çıkıldı")
      break
   else:
      print("\nGeçerli bir sayı giriniz.")
   print("------------------------")