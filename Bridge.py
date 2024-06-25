class motor:
    def calistir(self):
        pass
    
class elektrik_motor(motor):
    def calistir(self):
        print('Elektrik motoru calistiriliyor')
        
class petrol_motor(motor):
    def calistir(self):
        print('Petrol motoru calistiriliyor')
        
class car:
    def __init__(self,motor):
        self.motor = motor
        
    def baslat(self):
        print(f"arac su motor ile calistiriliyor {self.motor.__class__.__name__}")
        
    def calistir(self):
        return self.motor.calistir()
    
motor1 = elektrik_motor()

arac1 = car(motor1)

arac1.baslat()
arac1.calistir()