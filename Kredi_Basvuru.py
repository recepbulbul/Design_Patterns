class kredi:
    def __init__(self,isim,aylik_kazanc,mulkiyet):
        self.isim = isim
        self.aylik_kazanc = aylik_kazanc
        self.mulkiyet = mulkiyet
        
    def onay(self):
        pass
    
class konut_kredisi(kredi):
    def onay(self):
        if self.aylik_kazanc > 20000:
            if self.mulkiyet is True:
                print(f'{self.isim}, Kredi Basvurusu Onaylandi')
            else:
                print(f'{self.isim}, Maalesef Uygun Degilsiniz!')
        else:
            print(f'{self.isim}, Maalesef Uygun Degilsiniz!')

class kisisel_kredi(kredi):
    def onay(self):
        if self.aylik_kazanc > 10000:
            print(f'{self.isim}, Kredi Basvurunuz Onaylandi')
        else:
            print(f'{self.isim}, Maalesef Uygun Degilsiniz!')

class oto_kredisi(kredi):
    def onay(self):
        if self.aylik_kazanc > 15000:
            if self.mulkiyet is True:
                print(f'{self.isim}, Kredi Basvurunuz Onaylandi')
            else:
                print(f'{self.isim}, Maalesef Uygun Degilsiniz!')
        else:
            print(f'{self.isim}, Maalesef Uygun Degilsiniz!')
            
            
class gorevli:
    def __init__(self):
        self.sonraki_gorevli = None
        
    def gorev(self,istek):
        pass
    
    def sonraki_gorevli_tanimi(self,sonraki_gorevli):
        self.sonraki_gorevli = sonraki_gorevli
        
        
class konut_kredisi_gorevlisi(gorevli,konut_kredisi):
    def gorev(self,istek):
        if istek.__class__.__name__ == 'konut_kredisi':
            istek.onay()
        elif self.sonraki_gorevli is not None:
            self.sonraki_gorevli.gorev(istek)   
            
class kisisel_kredi_gorevlisi(gorevli,kisisel_kredi):
    def gorev(self,istek):
        if istek.__class__.__name__ == 'kisisel_kredi':
            istek.onay()
        elif self.sonraki_gorevli is not None:
            self.sonraki_gorevli.gorev(istek)


class oto_kredisi_gorevlisi(gorevli,oto_kredisi):
    def gorev(self,istek):
        if istek.__class__.__name__ == 'oto_kredisi':
            istek.onay()
        elif self.sonraki_gorevli is not None:
            self.sonraki_gorevli.gorev(istek)
            
ok = oto_kredisi('Recep', 13000, True)

konut_gorevli = konut_kredisi_gorevlisi()
kisisel_gorevli = kisisel_kredi_gorevlisi()
oto_gorevlisi = oto_kredisi_gorevlisi()

konut_gorevli.sonraki_gorevli_tanimi(kisisel_gorevli)
kisisel_gorevli.sonraki_gorevli_tanimi(oto_gorevlisi)

konut_gorevli.gorev(ok)






























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        