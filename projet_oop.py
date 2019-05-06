from random import randint
class player:
    def __init__(self,naem,level,type,length,characters=[]):
        self.naem = naem
        self.level = level
        self.type = type
        self.length = length
        self.characters = characters

    def all_character(self):
        for i in self.characters:
            if i.is_alive:
                i.move()
                print(i)
                print('>>>>>>>>>>>>>>>>>>>>>')
    def check_all(self):
        return all([i.is_dead() for i in self.characters])

    def welcome(self):
        return '{} \t Welcome to the game'.format(self.naem)
    def  move(self):
        return 'I Am Moveing'

    def eat(self):
        return 'I Am Eat'


from random import randint
class people:
    def __init__(self, skill=None):
        self.life = 100
        self.skill = skill
        self.pos = (0,0)
####
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
####
    def __str__(self):
        return 'move:{}\t life:{}\t skill:{}\t'.format(self.move, self.life, self.skill,)

    from random import randint
####

    ######
class soldiers(people):

     def __init__(self,skill=None,id_soldiers=None, name=None, rank=None,
                  soldiers_assigned='pedestrian',defense=True,attack=None):
         super().__init__(skill=None)
         self.id_soldiers = id_soldiers
         self.name = name
         self.rank = rank
         self.soldiers_assigned = soldiers_assigned
         self.defense = defense
         self.attack = attack

     def eat(self):
         return 'name:{}\t I can eat'.format(self.name)

     def therapy(self):
         return 'I needed a treatment'

     def __str__(self):
         return 'id_soldiers:{}\t naem:{}\t rank:{}\t'.format(self.id_soldiers, self.naem, self.rank,
                           super().__str__())

class doctors(people):

    def __init__(self,naem=None, medical_tools= None,move=None,life=100,skill=None,pos=(0,0)):
        super().__init__(skill=None)
        self.naem = naem
        self.medical_tools = medical_tools

    def Treatment_the_wounded(self):
        return 'I am the doctor treating the wound'

    def __str__(self):
        return 'naem:{}\t Treatment_the_wounded{}\t'.format(self.naem,self.Treatment_the_wounded())

class commanders(people):

    def __init__(self,naem=None,power=None, strict_personality=None, give_order=None,skill=None):
        super().__init__(skill=None)
        self.power = power
        self.strict_personality = strict_personality
        self.give_order = give_order
        self.naem = naem
    def print_commanders(self):
        return 'I am '.format(self.naem)

    def give_order(self):
        return 'Give orders to soldiers'

    def __str__(self):
        return 'give_order:{}\t'.format(self.give_order())

