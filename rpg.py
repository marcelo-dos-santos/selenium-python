

from ast import Break
from mimetypes import init
import string
from tkinter import N
import sys

welcome = """
**** CASTLEVANIA SYMPHONY OF PYTHON - Write by Mikami (* ^ ω ^) ****

This game is only for learning porpurses do not copy or sell, and if you sell it, please send my share.

Have Fun!
"""
print(welcome)

print('Please, in this game only reply with yes or no or the system ill be afraid and then shoutdown ( ; ω ; )')
print('and in the the damages fields only reply with int numbers, thanks 	(=^･ω･^=)\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ')

dracula_enters = """
You finally manage to reach the main hall of the castle, and between the darkness and the horror you can see a shadow sitting on the throne in the middle of the hall... little by little your eyes begin to get used to the darkness
allowing you to see that the shadow in if its something, not just something but Count Dracula, owner and current owner of the castle
//if they dont pay all taxes to the IRS by next month it wont be anymore// 
  quickly their eyes meet and he makes you a solemn question.')
"""
print(dracula_enters)

pilesofpixel = input('What its a man?\n')
print('yes you are ritgh, a man is a miserable', pilesofpixel)

#############################################




name = input('Whats your name, human?')
age = input('how many storms you witness?')
print('Welcome to my castle, glad to see you here, Vampire Slayer', name , age,'years old')
threaten = input('threat your enemy! ')
print(name,'have threaten Dracula!\n','You Says -', threaten)
print('DRACULA Says!- It was not by my hand that i once again given flesh, i was called here by HUMANS who wish to pay ME tributes.   ')
print('narrator - Dont let he scares you, threaten him again!')
turn2 =input('Your turn, what you gonna say it? ')
print('You say- ',turn2)
print('BATTLE PHASE!!!!, prepare your ass!')


damage_turn2 = int (input('HOW MANY DAMAGE YOU DEAL SCUM?'))
print('YOU DEAL', damage_turn2, 'damage in the supreme lord DRACULA!!')
dracula_life = str (print('Dracula has recive', damage_turn2, 'damage and have only 20% of his life\n', 'What you are gonna do now, huh?'))

quest1 = input(' DRACULA Says -do you still have the strength to fight me?') 

if quest1 =='yes':
    print('Dracula Says- COME ON AND FACE ME, HUMAN!!! ITS TIME TO YOUR END............')
elif quest1 =='no': print('Dracula Says- I KNOW IT, SURRENDER FOR ME FOOL!!')
else: print('Dracula Says- THATS NOT WHAT I ASKED FOLL!!, (just choose yes or no, please :)')

quest2 = input('Dracula Says- are you SURE ABOUT THAT HUH? ARE YOU REEEEAAAAALLLLLYYYY SURE ABOUT YOUR DECISION??????????????') 
if quest2 =='yes':
    print('Dracula Says- OK NOW ITS SERIOUSLY, ITS TIME TO DRAIN YOUR BLOOD WITH LITTLE STRAWS!!!')
elif quest2 =='no': print('I KNOW IT, SURRENDER FOR ME FOOL!!')
else: print('OH MY BATMAN,THATS NOT WHAT I ASKED MAGGOT, DO NOT TRY TO TRICK ME!!!, (just choose yes or no, please :)')

print('Dracula Says- Sooo.....just so I can get this right, are you really willing to try to kill me?    ó_ó  ')

quest1troll = input('Dracula says- Let me quest you one more time again, please respond my question correctly,....do you still have the strength to fight me? kindly - Lord Supreme "Your big Bat" Dracula  (◕‿◕✿)')
if quest1troll =='yes':
    print('COME ON AND FACE ME, HUMAN!! PREPARE FOR THE BATTLE!!!!!! - Dracula appears to be angry and i dont know why')
elif quest1troll =='no': print('I KNOW IT, SURRENDER FOR ME FOOL!!')

else: print('I WILL NOT WASTE MY TIME WITH YOUR BRAINLESS HEAD, THE GAME IS OVER GOODBYE >:(')

if quest1troll != 'yes': sys.exit()


dracula_life = 1000
player_life = 100

print('BATTLE PHASE AGAIN!!\n', 'Dracula blood starts to recharge and becoming more powerful than never, Dracula has',dracula_life, 'points of life, its huge ritgh? ლ(¯ロ¯"ლ)')
player_damge1 =  int (input('Narrator - Roll a dice and see how many damage you do on Dracula heatl bar, reminder Dracula has 1000 points of life, i already said its huge?\n How many damage you deal in the count?'),)

if player_damge1 < dracula_life:
    print('Nice try but you are not capable do kill the supreme Lord, you will need SILVER BULLETS and eventually a BIG GUN to kill him or maybe just asking they gently to leave you alone idk ヽ( `д´*)ノ ')

while player_damge1 >dracula_life:
  print('I WILL NOT DIE SO EASY LIKE THIS, HUMAN MUHAHAHA!! 	ψ( ` ∇ ´ )ψ ')
  break
print('test')


      