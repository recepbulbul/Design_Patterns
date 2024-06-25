class car:
    def __init__(self):
        self.parcalar = []
        
    def addparca(self,parca):
        self.parcalar.append(parca)
        
    def aracparcalari(self):
        for i in self.parcalar:
            print(i)
            
class carbuilder:
    def motor(self):
        pass
    
    def renk(self):
        pass
    
    def model(self):
        pass
    
class bmwbuilder(carbuilder):
    def __init__(self):
        self.car = car()
        
    def motor(self):
        self.car.addparca('motor1')
        
    def renk(self):
        self.car.addparca('mavi')
        
    def model(self):
        self.car.addparca('2010')
        
    def aracolustur(self):
        return self.car
    
    
class director:
    def __init__(self,builder):
        self.builder = builder
        
        
    def olusturucu(self):
        self.builder.motor()
        self.builder.renk()
        self.builder.model()
        return self.builder.aracolustur()
        
        
bmw = bmwbuilder()
direc = director(bmw)

aracbmw = direc.olusturucu() 

aracbmw.aracparcalari()


       
        
        
        
        
        
        
        
        
        
        
        
        
        