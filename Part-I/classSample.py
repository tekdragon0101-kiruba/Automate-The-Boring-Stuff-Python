class Dog:
    # class attributes
    animalType = 'mammal'
    def __init__(self, name):
        self.name = name
        print('Object created...')
    
    def speak(self):
        print('my name is {}.'.format(self.name.capitalize()))



if __name__ == '__main__':
    jack = Dog('jack')
    print(jack.__class__.animalType)
    jack.speak()
