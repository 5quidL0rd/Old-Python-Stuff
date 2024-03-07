#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import time

#introduction
print('Welcome to the Kingdom of Angalor, the realm of shadows!')
print('*******************************************************')
print('You have traveled to the Kingdom of Angalor in order to find the Shadow Crown.')
time.sleep(3)
print('You have gone exploring by yourself down some dark, abandoned tunnels made by goblins.')
print('You can pick one item to have with you-')
print('map(m), sword(s), magic_cloak(c), wizard_staff(w)')
item=input('Which do you choose?:')
while not(item=='m' or item=='s' or item=='c' or item=='w'):
    item=input('Please enter one of the afore stated letters.')
print('You hear a howl.')
choice1=input('Will you approach the noise or flee? Enter y or n:')
while not (choice1 == 'y' or choice1 == 'n'):
    choice1=input('That is an invalid input. Enter y or n: ')
if choice1== 'y':
    print('You go deeper ino the tunnels, crouching and making as little noise as possible as you approach.')
    time.sleep(3)
    print('Suddenly, the howling stops.')
    time.sleep(3)
    print('You are now LOST in the tunnels!')
    print('You try to call for help, but no one answers your calls.')

    #Time to choose your direction 
    direction=input('How will you proceed? north, south, east, or west:')
    if direction =='north':
        print('You find an abandoned goblin hut in the tunnels.')
        time.sleep(2)
        if item == 'm':
            print('You use your map of the tunnels to find an exit.')
            print('On your way out you find the Shadow Crown and bring it with you.')
            print('CONGRATULATIONS! You have won the game.')
        else:
            print('If you had a map, you could escape. ALAS!')
            time.sleep(2)
            print('You are hopelessly lost still. You starve to death in these tunnels.')
            print('DEFEAT!')
    elif direction =='south':
        print('You find an underwater river with a broken bridge.')
        if item == 'w' or item == 'c':
            print('You chose an item that can fix the bridge.')
            time.sleep(3)
            print('You fix the bridge, cross it, and discover the Shadow Crown on the other side.')
            print('You return to the surface with the crown.')
            print('CONGRATULATIONS! You have won the game.')
        else:
            print('If you had a magic cloak or a wizarding staff, you could magically fix the bridge.')
            print('You attempt to cross the river and drown.')
            print('DEFEAT!')
    if direction =='west':
        print('You are walking and trip over something.')
        time.sleep(2)
        print('You TRIPPED over the Shadow Crown!')
        time.sleep(2) 
        print('Well your foot is hurt and now you cannot walk and are still lost, Shadow Crown or no Shadow Crown. You starve to death in these tunnels, gnawing on your crown.')
        print('DEFEAT!')
    elif direction =='east' : 
        print('You reach a tunnel opening that is guarded by hobgoblins! AND one of them is wearing the Shadow Crown!')
        if item == 's':
            print('You charge forward and attack the hobgoblins with your blade and take the Crown.')
            time.sleep(3) 
            print('You behead several and wound the rest. Before reinforcements arrive you charge from the tunnels with your Shadow Crown!')
            print('CONGRATULATIONS! You have won the game.')
        else:
            print('If you had a sword you could fight your way to freedom.')
            time.sleep(2) 
            print('With roars of delight the hobgoblins leap forward. It has been a long time before they have feasted on soft flesh.')
            print('DEFEAT!')
else:
    print('Intelligent. No risk taking. There will be plenty of that in the future, you are sure.')
    time.sleep(3) 
    print('You start walking out of the tunnels.')
    time.sleep(2) 
    print('You realize you took too many right and left turns, and are now LOST!')
    time.sleep(2) 
    print('The howling behind you is growing LOUDER and LOUDER. You panic!')

#TIME FOR A LOOP
    action=input('Do you flee (f) or stand your ground? (g)')
    if action == 'g':
        print('You prepare for combat but realize you are so scared you cannot hold your ground.')
        time.sleep(3) 
    input('You must now flee!(press f)')
    print('You are running very fast down the tunnels, but the sound grows VERY LOUD')
    #Answer a question to proceed
    print('Suddenly a vampire springs from a side tunnel.')
    answer=input('She says, "Name my favorite type of food and I can save you.":')
    if answer.lower() =='blood':
        time.sleep(2) 
        print('She says, "Correct! Very nutritious."')
        time.sleep(2) 
        print('The vampire shows you a way out. She even gives you the Shadow Crown as a gift of her appreciation as you leave.')
        print('CONGRATULATIONS! You have won the game!')
    else:
        print('She did not approve of your answer. She bites you on the neck and drains you of your blood.')
        time.sleep(3) 
        print('You slowly bleed the rest of the way out and perish in these tunels.')
        print('DEFEAT!')



        
