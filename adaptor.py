class insan:
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
        
    def isim_dondur(self):
        return self.isim

class veritabani:
    def veriyiyazdir(self,veri):
        print(f"gelen veri {veri}")
        
class insan_adaptor(insan):
    def __init__(self,insan):
        self.insan = insan
        
    def veri_dondur(self):
        return self.insan.isim_dondur()
    
insan1 = insan('Recep',18)

insanadaptor = insan_adaptor(insan1)

verit = veritabani()

verit.veriyiyazdir(insanadaptor.veri_dondur())    