class kahve:
    def bedel(self):
        return 10
    
    def isim(self):
        return 'kahve'
    
    
class kahve_decorator(kahve):
    def __init__(self,kahve):
        self.kahve = kahve
        
    def bedel(self):
        return self.kahve.bedel()
    
    def isim(self):
        return self.kahve.isim()
    
class sutlu_kahve_decorator(kahve_decorator):
    def bedel(self):
        return self.kahve.bedel() + 5
    
    def isim(self):
        return 'sutlu ' + self.kahve.isim()
    
kahve = kahve()

sutlu_kahve = sutlu_kahve_decorator(kahve)

print(sutlu_kahve.isim(),sutlu_kahve.bedel())
    