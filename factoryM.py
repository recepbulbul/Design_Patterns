class car:
    def __init__(self,renk,yil):
        self.renk = renk
        self.yil = yil
        
    def modelbas(self):
        pass
    
class bmw(car):
    def __init__(self,renk,yil):
        super().__init__(renk,yil)
        self.model = 'bmw'
        
    def modelbas(self):
        return self.model
    
class merc(car):
    def __init__(self,renk,yil):
        super().__init__(renk,yil)
        self.model = 'merc'
    
    def modelbas(self):
        return self.model
    
class carfactory:
    def secim(self,model,renk,yil):
        if model == 'bmw':
            return bmw(renk,yil)
        
        elif model == 'merc':
            return merc(renk,yil)
       
carf = carfactory()

bmw1 = carf.secim('bmw','kirmizi',2001)

print(bmw1.yil)