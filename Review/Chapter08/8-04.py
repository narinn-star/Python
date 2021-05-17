class Animal:
    '동물을 나타내는 클래스'
    
    def __init__(self, species = 'animal', language = 'make sounds'):
        self.spec = species
        self.lang = language

    def setSpecies(self, species):
        '동물 종을 설정'
        self.spec = species
    
    def setLanguage(self, language):
        '동물 언어를 설정'
        self.lang = language
    
    def speak(self):
        '동물이 말하는 문장을 출력'
        print('I am a {} and I {}.'.format(self.spec, self.lang))

snoopy = Animal('dog', 'bark')
snoopy.speak()

tweety = Animal('canary')
tweety.speak()

animal = Animal()
animal.speak()