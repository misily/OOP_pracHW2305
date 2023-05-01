class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('just like animals, animals,like animals')


class Dog(Animal):
    def speak(self):
        print('왱알왱알')


class Cat(Animal):
    def speak(self):
        print('멍멍!')



