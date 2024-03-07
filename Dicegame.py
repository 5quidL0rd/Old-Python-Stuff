#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#dice game
#step1 in main program area - start game
import time
def roll_again(choices,dice_list):
    print('Rolling again....')
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i]=='r':
            dice_list[i] = random.randint(1,6)
    time.sleep(3)
number_dice=input('Enter number of dice:')
number_dice=int(number_dice)
ready=input('Ready to commence? Hit any key to proceed.')
import random
def roll_dice(n):
    dice=[]#start with empty list of dice
    #add random numbers between 1 to 6 to the list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice
#step 2 in main program area - roll dice
#User turn to roll
user_rolls=roll_dice(number_dice)
print('User first roll:',user_rolls)
#Computer's turn to roll
print('Computers turn')
computer_rolls=roll_dice(number_dice)
print('Computer first roll:',computer_rolls)
#Step 3
def find_winner(cdice_list,udice_list):
    computer_total=sum(cdice_list)
    user_total=sum(udice_list)
    print('Computer total',computer_total)
    print('User total',user_total)
    if user_total>computer_total:
        print('User wins')
    elif user_total<computer_total:
       print('Computer wins')
    else:
        print('It is a tie!')         
#step 4
user_choices=input("Enter h to hold or r to \ roll again:")
# check length of user input
while len(user_choices) != number_dice:
    print('You must enter', number_dice,\
          'choices')
    user_choices=input("Enter h to hold or r \ to roll again:")
#step 6
def computer_strategy2(n):
    print('Computer is thinking....')
    time.sleep(3)
    choices=''
    for i in range(n):
        if computer_rolls[i]<5:
            choices=choices+'r'
        else:
            choices=choices+'h'
    return choices
computer_choices=computer_strategy2(number_dice)
print('Computer Choice:',computer_choices)
roll_again(computer_choices,computer_rolls)
print('Computer new Roll:',computer_rolls)
def computer_strategy1(n):
    print('Computer is thinking.....')
    time.sleep(3)
    choices = ''
    for i in range(n):
        choices=choices + 'r'
    return choices
def computer_strategy2(n):
    print('Computer is thinking.....')
    time.sleep(3)
    choices=''
    for i in range(n):
        if computer_rolls[i]<5:
            choices=choices+'r'
        else:
            choices=choices+'h'
    return choices
#final line in code  
find_winner(computer_rolls,user_rolls)


