sepet = []    # Boş bir sepet oluşturuyoruz

def sepete_ekle(urun):
    sepet.append(urun)   # Sepete ürünü ekler
    print(f"{urun} sepete eklendi.")

sepete_ekle("Elma")
sepete_ekle("Armut")
sepete_ekle("Ayva")


def sepetten_cikar(urun):
    if urun in sepet:    # Önce istenen ürün spette var mı diye arar ve eğer varsa
        sepet.remove(urun)  # sepetten ürünü çıkarır
        print(f"{urun} sepetten çıkarıldı.")
    else:                                     # eğer yoksa
        print(f"{urun} sepetinizde bulunmuyor.")   # Sepete yok yazar

sepetten_cikar("Elma")
sepetten_cikar("Muz")
# sepetten_cikar("Armut")
# sepetten_cikar("Ayva")


def sepeti_goster():
    if sepet:
        print(f"{sepet} ürünler bunlardır.")
    else:
        print(f"{sepet} sepetiniz boş")
            
sepeti_goster()


def sepeti_temizle():
    sepet.clear()
    print("Sepet temizlendi")

sepeti_temizle()