from animal import *
from project_oop1 import *
from projet_oop import *
chal1 = [Tanks(),vehicles(),aircraft(), soldiers(), doctors(),commanders()]
chal2 = [lions(),people()]
player1 = player(1, chal1)
player2 = player(2, chal2)

done = False
while True:
    round +=1
    print('round' , round)
    print('player', player1.naem)
    player1.all_character()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('player',player2.naem)
    player2.all_character()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    if player1.check_all() or player2.check_all():
        print('End Game')
        break

if (player1.check_all()& player2.check_all()):
    print('the players drow')
elif (player1.check_all()):
    print('player1 is winner')
    print('player2 is lost')
else:
    print('player1 is winner')
    print('player2 is lost')


