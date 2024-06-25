import copy

class prot:
    def cogalt(self):
        return copy.deepcopy(self)
        
class animal(prot):
    def __init__(self,yas,yemek):
        self.yas = yas
        self.yemek = yemek
        
    def yasatla(self):
        self.yas += 1
        
hayvan1 = animal(12, 'et')

hayvan2 = hayvan1.cogalt() 

print(hayvan1 == hayvan2)

hayvan1.yasatla() 

print(hayvan1.yas,hayvan2.yas)    
