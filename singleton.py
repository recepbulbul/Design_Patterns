class singleton:
    _instance = None
    isim = 'Recep'
    
    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
            
        return self._instance
    
    def addegis(self):
        self.isim = 'Basak'
    
s1 = singleton()
s2 = singleton()

s1.addegis()

print(s1 == s2,s2.isim)