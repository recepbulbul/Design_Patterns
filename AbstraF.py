class animal:
    def speak(self):
        pass
    
class dog(animal):
    def speak(self):
        return 'haw'
    
class cat(animal):
    def speak(self):
        return 'meow'
    
class food:
    def kind(self):
        pass
    
class dogfood(food):
    def kind(self):
        return 'meat'
    
class catfood(food):
    def kind(self):
        return 'milk'
    
class animalfactory:
    def __init__(self,hayvan):
        self.hayvan = hayvan
        
    def olustur(self):
        if self.hayvan == 'dog':
            return dog(),dogfood()
        
        elif self.hayvan == 'cat':
            return cat(),catfood()
        
af = animalfactory('dog')

hayvan= af.olustur()

print(hayvan[1].kind())
        
