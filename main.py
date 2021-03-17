#This program takes functionality of random module to generate a random number
'''Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
import random

l=['Rock','Paper','Scissor']
you=0
computer=0
draw=0
n=1
while(n<=5):
    computer_pick=random.choice(l)
    choose=input('Choose \nR --> Rock\nP --> Paper\nS --> Scissor\n').upper()
    if choose=='R':
        if computer_pick=='Rock':
            draw+=1
        elif computer_pick=='Paper':
            computer+=1
        else:
            you+=1
    elif choose=='P':
        if computer_pick=='Rock':
            you+=1
        elif computer_pick=='Paper':
            draw+=1
        else:
            computer+=1
    elif choose=='S':
        if computer_pick=='Rock':
            computer+=1
        elif computer_pick=='Paper':
            you+=1
        else:
            draw+=1
    n+=1

print(f'You won {you} times\nComputer won {computer} times\nDraws {draw} times')

if you>computer:
    print('You won')
elif computer>you:
    print('Computer won')
else:
    print('DRAW')
