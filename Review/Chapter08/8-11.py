class Animal:
    def setSpecies(self, species):
        self.spec = species

    def setLanguage(self, language):
        self.lang = language

    def speak(self):
        print('I am a {} and I {}.'.format(self.spec, self.lang))
    
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age
    
flipper = Animal()
flipper.setSpecies('dolphin')
flipper.setAge(3)
print(flipper.getAge())