class isci:
    def __init__(self):
        self.sonraki_isci = None
        
    def sonraki_isci_tanimi(self,sonraki_isci):
        self.sonraki_isci = sonraki_isci
        
    def gorev(self,istek):
        pass
        
class isci1(isci):
    def gorev(self,istek):
        if istek == 'Gorev1':
            print(f'Gorev Halledildi, {__class__.__name__}')
        elif self.sonraki_isci is not None:
            self.sonraki_isci.gorev(istek)
            
class isci2(isci):
    def gorev(self,istek):
        if istek == 'Gorev2':
            print(f'Gorev Halledildi, {__class__.__name__}')
        elif self.sonraki_isci is not None:
            self.sonraki_isci.gorev(istek)
            
class isci3(isci):
    def gorev(self,istek):
        if istek == 'Gorev3':
            print(f'Gorev Halledildi, {__class__.__name__}')
        elif self.sonraki_isci is not None:
            self.sonraki_isci.gorev(istek)
        else:
            print('Basaramadik')
            
isci1 = isci1()
isci2= isci2()
isci3 = isci3()

isci1.sonraki_isci_tanimi(isci2)
isci2.sonraki_isci_tanimi(isci3)

gorev_listesi = ['Gorev1','Gorev2','Gorev3','Gorev4']

for i in gorev_listesi:
    isci1.gorev(i)