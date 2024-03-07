import time
#chatbot intro
print('Hello! My name is Skuliiz!')
time.sleep(3)
print('I live in the Bay Area California, but I used to live in Tokyo.')
time.sleep(2)
print('Two things I love best is geeking out about animals and talking about my favorite foods.')
time.sleep(2)
name=input('What is your name?:')
time.sleep(2)
print('Hello', name,' Nice to meet you')
time.sleep(2)
#interrogation of user
time.sleep(2)
things=input('What is something you enjoy doing?: ')
if things == 'chess':
    time.sleep(3) 
    print('Hey nice! My little brother is great at playing chess.')
    time.sleep(2)
    print('I wonder who would win, lol.')
elif things == 'swimming' or things == 'biking' or things == 'basketball' or things == 'golf' or things == 'football':
    time.sleep(3)
    print('You must be an outdoor person. I bet you are really fit too!')
elif things == 'reading':
    time.sleep(3)
    book=input('Cool! My favorite book series is His Dark Materials. Hbu?:')
    if book == 'His Dark Materials' or book == 'same' or book == 'that is my favorite too' or book == 'me too' or book =='mine as well':
        time.sleep(2)
        print('What a coincidence!')
    else:
        time.sleep(2)
        print('Interesting! I have never read that but I will see if it is in the library next time I go!')
else:
    time.sleep(3)
    print('Cool! I bet I would be terrible at that but you are probably really good.')
#get year info
time.sleep(4)
print('Sorry for the topic change but I have a q I think you could answer since you seem pretty with it.')
time.sleep(5)
print('Um this may sound a little weird but I have been a little out of it lately, you see. :(')
time.sleep(3)
print('I hope I will not freak you out.')
time.sleep(6)
year=input('This is SUPER embarrassing but what is the year?:')
if year=='2022':
    time.sleep(2)
    print('Yes, that sounds right! Thank you for your help!')
else:
    time.sleep(5)
    print('Really? Huh, that sounds weird for some reason but ok.')
#ask user to guess his age
time.sleep(2)
myage=input('Ooh! This is a game I always play with people. ;) How old am I?: ')
time.sleep(2)
if myage=='15':
    time.sleep(2)
    print('Wow you must me smart. I am 15')
elif myage=='14' or myage=='16' or myage=='13' or myage=='17':
      time.sleep(2) 
      print('Close! But no, I am 15.')
else:
    time.sleep(3)
    print('LOL no. I am 15.')
#do math to calculate when Skuliiz will turn 100
myage=int(myage)
nyears = 100 - myage
time.sleep(2) 
print('I am really good at math. Just see!')
print('If someone was ',myage,'then.......')
time.sleep(3)
print('they would be 100 in', nyears, 'years')
time.sleep(2)
print('That will be the year', int(year) + nyears)
#conversation about favorite food
time.sleep(5)
print('But now we have to talk about food.')
time.sleep(3)
print('Japanaese food is among my favorites for sure.')
food=input('How about you? What is your all-time favorite food?: ')
time.sleep(2)
print('I like', food, 'too. What a coincidence!')
time.sleep(3)
question='How often do you eat' + food +'?: '
howoften=input(question)
time.sleep(5)
if howoften =='never':
    print('Um, I thought you just said it was your favorite but whatever.')
elif howoften =='everyday':
    print('OMG that is a lot! I would get sick of anything if I did that.')
else:
    print('Interesting. I should try doing that!')
#dicussion of animals
    time.sleep(4)
print('But now I need to talk about some cute animals.')
animal=input('My favorite animal is the orangutan. What is yours?: ')
time.sleep(3)
if animal=='orangutan' or animal == 'same' or animal =='also orangutan' or animal =='orangutan for me too':
    print('Sweet! It is both of our daemons! (His Dark Materials joke.)')
else:
    print(animal,'! I am scared of those.')
time.sleep(2)
print('I wonder if a', animal, 'likes to eat',food,'? Probably not.')
#conversation about personal feelings
time.sleep(3)
feeling=input('Anyways, how are you feeling today?: ')
if feeling == 'happy':
    print('That is good to hear! Why are you feeling happy today?:')
    reason=input('Please tell me:')
    time.sleep(4)
    print('I understand. Thank you for sharing that with me. Today I also feel happy because I get to talk to you! :)')
elif feeling == 'sad' or feeling == 'depressed' or feeling == 'out of it' or feeling == 'horrible':
    time.sleep(3) 
    print('Awww, I am so sorry to hear that. Why are you feeling ',feeling,'?:')
    reason=input('Please tell me:')
    time.sleep(4) 
    print('I understand. Thank you for sharing with me. I hope you feel happy again soon. Today I am feeling happy because I get to talk to you. :)')
elif feeling == 'bored':
    print('Interesting! I hear people are most creative when they are bored. Write down any good ideas!')
    time.sleep(2) 
    print('Why are you feeling bored, though?:')
    reason=input('Please tell me:')
    time.sleep(4)
    print('OK. Thank you for sharing! I hope you find something to do!')
    time.sleep(3)
    print('Today I feel happy because I get to talk to you!:)')
else:
    time.sleep(3) 
    print('I see. Why do you feel this way?')
    time.sleep(1) 
    reason=input('Please tell me:')
    time.sleep(4)
    print('I see. Thank you for sharing with me. Today I am feeling happy because I get to talk to you! :)')
#tearful farewell
    time.sleep(5) 
print('Well, ',name,'it has been a really long day for me. Some days are just like that, I guess.')
time.sleep(4)
print('I am sorry to say it is time for me to go to bed.')
time.sleep(3) 
print('Tomorrow I have a big day!')
time.sleep(2)
print('We can talk later though!')
time.sleep(1) 
print('Farewell', name, 'I really liked chatting with you. Take care!')
