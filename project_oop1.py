from random import randint
class vehicles:

    def __init__(self,speed=0,color='black',type='car',brakes=None):
        self.fuel = 100
        self.speed = speed
        self.color = color
        self.type = type
        self.brakes = brakes
        self.life = 100
        self.pos = (0, 0)

    def __str__(self):
        return 'fuel:{}\t speed:{}\t color:{}\t type:{}\t'.format(self.fuel, self.speed, self.color, self.type)

    def filling(self):
        if self.fuel > 0:
            pass
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
    def speedup(self):
        if self.speed <= 15:
            self.speed += 30

    def slowdown(self):
        if self.speed >= 150:
            self.speed -= 60
            return 'Slow speed'
        return 'Speed ​​is good'

class car(vehicles):

    def __init(self,fuel=0,speed=0,color='black',type='car',brakes=None,transfer_soldiers=None):
        super().__init__(speed=0,color='black',type='car',brakes=None)
        self.transfer_soldiers = transfer_soldiers
        self.fuel = fuel

    def __str__(self):
        return 'transfer_soldiers:{}\t'.format(self.transfer_soldiers,super().__str__())

car1 = car(speed=100,color='erd',type='soldier carrier')
print(car1.filling())
print(car1.slowdown())

class Tanks(vehicles):

    def __init__(self,fuel=0,speed=0,color='black',type='car',brakes=None,attack=None,standard_cannon=120,thermal_imaging=None):
        super().__init__(speed=0,color='black',type='car',brakes=None)
        self.attack = attack
        self.standard_cannon = standard_cannon
        self.thermal_imaging = thermal_imaging

    def __str__(self):
        return 'attack:{}\t standard_cannon:{}\t thermal_imaging{}\t'.format(self.attack, self.standard_cannon,self.thermal_imaging
                  ,super().__str__())

class aircraft(vehicles):

    def __init__(self,selffuel=0,speed=0,color='black',type='car',brakes=None,shooting_hostility=None,air_strike=10):
        super().__init__(speed=0,color='black',type='car',brakes=None)
        self.shooting_hostility = shooting_hostility
        self.air_strike = air_strike

    def __str__(self):
        return 'shooting_hostility:{}\t air_strike:{}\t'.format(self.shooting_hostility, self.air_strike,
                             super(). __str__())

    def soldiers_take(self):
        return 'The soldiers were taken down successfully'

ci = vehicles(speed=80, color='red' ,type='teotl', brakes=True)
print(ci)
print(ci.slowdown())
print(ci.is_alive())