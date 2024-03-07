#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#Guess my number
secret_number=42
n=input('Guess the secret number between 1 and 100 ')
n=int(n) #convert user input into an integer

while not (n==secret_number):
    if n >secret_number:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
    n = input('Make another guess between 1 and 100 ')
    n=int(n)
print('The mice will be most pleased. This is the answer to the meaning of life, the universe, everything.')
