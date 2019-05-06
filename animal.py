from random import randint
class animal():
    def __init__(self,name="",type="",bark="",atek=''):
        self.name = name
        self.type = type
        self.bark = bark
        self.atek = atek
        self.life = 100
        self.pos = (0, 0)

    def printAnimal(self):
        return "am animal".format(self.name)
    def health(self):
        if self.life > 0:
            self.life -= randint(0, self.life)
            print(self.life)

    def move(self):
        self.pos = (randint(-100,100), randint(-100,100))
        print(self.pos)

    def Few_Life(self):
        if self.life >=100:
            self.life -= 40

    def is_alive(self):
        if self.life > 0:
            return True
        else:
            return False

    def is_dead(self):
        if self.life == 0:
             return True
        else:
             return  False

    def __str__(self):
        return 'naem:{}\t type:{}\t bark:{}\t atek:{}\t'.format(self.naem, self.type, self.bark, self.atek)

class cat(animal):

    def __init__(self,name,type,bark,atek,mycolor,myspot):
        super().__init__(name,type,bark,atek)   #animal.__init__(self,name,type,bark)
        self.color = mycolor
        self.spot = myspot

    def __str__(self):
        return 'color:{}\t spot:{}\t'.format(self.color, self.spot,super().__str__())

    def my_bark(self):
        return "I'm barking".format(self.name)

    def printCat(self):
        print("am cat")

class dog(animal):

    def __init__(self,bv,lsk,name,type,bark):
        super().__init__(name,type,bark)
        self.bv = bv
        self.lsk = lsk

    def jogging(self):
        return 'I am Jogging'

    def printDog(self):
        return 'Am Dog'

    def __str__(self):
        return 'BV:{}\t LSK:{}\t'.format(self.bv, self.lsk, super().__str__())

class lions(animal):

    def __init__(self,protection=None,name="",type="",bark="",atek='' ):
        super().__init__(name="",type="",bark="",atek='')
        self.protection = protection

    def my_eat(self):
        return 'I eat meat'

    def __str__(self):
        return 'protection:{}\t'.format(self.protection,super().__str__())

obj1 = cat(name="lulu",type="cat",bark="Mewo",atek='yrs',mycolor="white",myspot=True)
obj1.printAnimal()
obj1.printCat()
print(obj1.name)
obj2 = cat(name='adad',type='cat',bark='yrs',atek='', mycolor='rad',myspot=True)
#print(obj2)
