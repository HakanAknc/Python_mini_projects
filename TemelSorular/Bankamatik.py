HakanHesap = {
    "ad": "Hakan AKINCI",
    "hesapNo": "123456789",
    "bakiye": 10000,
    "ekHesap": 5000
}

EvrenHesap = {
    "ad": "Evren AKINCI",
    "hesapNo": "987654321",
    "bakiye": 8000,
    "ekHesap": 4000
}

def parCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye']  -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap ['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüm bakiye yetersiz")
            bakiyeSorgula(hesap)        

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

parCek(HakanHesap, 5000)