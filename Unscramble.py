#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
def scramble(w):
    #turn string into list letters
    letters=list('fahrenheit')
    random.shuffle('f','a','h','r','e','n','h','e','i','t')
    scramble_word='fahrenheit'
    for i in letters:
        scramble_word=scramble_word + i
    return scramble_word
