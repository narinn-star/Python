class Animal:
    def setSpecies(self, species):
        self.spec = species

    def setLanguage(self, language):
        self.lang = language

    def speak(self):
        print('I am a {} and I {}.'.format(self.spec, self.lang))