class silah:
    def kusan(self):
        print('Silahlar Kusanildi')
        
    def silahbirak(self):
        print('Silahlar Birakildi')
        
class bayrak:
    def yarila(self):
        print('Bayrak Yariya Indirildi')
        
    def goklerde(self):
        print('Bayrak Goklerde Dalgalaniyor')
        
class can:
    def cal(self):
        print('Savas Canı Calınıyor')
        
class saldiri:
    def emir(self):
        print('Saldiri Emri Verildi')
        
    def anlasma(self):
        print('Taraflar Uzlasmaya Vardi')
        
class savasbarisfacade:
    def __init__(self,silah,bayrak,can,saldiri):
        self.silah = silah
        self.bayrak = bayrak
        self.can = can
        self.saldiri = saldiri

    def savas(self):
        print('Savas Vakti!')
        self.silah.kusan()
        self.bayrak.yarila()
        self.can.cal()
        self.saldiri.emir()
        
    def baris(self):
        print('Baris Vakti!')
        self.silah.silahbirak()
        self.bayrak.goklerde()
        self.saldiri.anlasma()


silah = silah()
bayrak = bayrak()
can = can()
saldiri = saldiri()

facade = savasbarisfacade(silah, bayrak, can, saldiri)

facade.savas()
print('-------------')
facade.baris()















        
        
        
        