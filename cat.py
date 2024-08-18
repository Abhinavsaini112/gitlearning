class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print('Sound made by the animal')
class Cat(Animal):
    def __init__(self,name,breed,color):
        Animal.__init__(self,name,species='Cat')
        self.breed=breed
        self.color=color

    def make_sound(self):
        super().make_sound()
        print('Meowing')
        print("Cat are so sweet ")
    def show_info(self):
        print(self.name)
        print(self.species)
        print(self.breed)
        print(self.color)
        print(super().make_sound())
        print('Meowing')
# obj=Animal('Simba','Pursian')
# obj.make_sound()

obj2=Cat('Mufasa','Pursian','White')
obj2.show_info()