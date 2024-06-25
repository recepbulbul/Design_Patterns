class sekil:
    def ciz(self):
        pass
    
class daire(sekil):
    def ciz(self):
        return 'daire'
    
class ucgen(sekil):
    def ciz(self):
        return 'ucgen'
    
class sekilcomposite(sekil):
    def __init__(self):
        self.sekiller = []
        
    def ekle(self,sekil):
        self.sekiller.append(sekil)
    
    def cikar(self,sekil):
        self.sekiller.remove(sekil)
        
    def ciz(self):
        cizimler = []
        
        for i in self.sekiller:
            cizimler.append(i.ciz())
        
        for i in cizimler:
            print(i)
            
dairesekli = daire()
ucgensekli = ucgen()

sekilc = sekilcomposite()

sekilc.ekle(dairesekli)
sekilc.ekle(ucgensekli)

sekilc.ciz()
