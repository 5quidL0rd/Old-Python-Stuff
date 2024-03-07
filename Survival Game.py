#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

from tkinter import *
import random

# make window
window = Tk()
window.title('Spider Survival Game')

# create a canvas to put objects on the screen
canvas = Canvas(window, width=400, height=400, bg = 'black')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text= 'Spider Survival Game', \
fill='white', font = ('Helvetica', 30))

# set up score display using label widget
score = 0
score_display = Label(window, text="Score :" + str(score))
score_display.pack()

# set up level display using label widget
level = 1
level_display = Label(window, text="Level :" + str(level))
level_display.pack()

# create an image object using the gif file
player_image = PhotoImage(file="stickfigure.gif")
# use image object to create a character at position 200, 360
mychar = canvas.create_image(200, 360, image = player_image)

# variables and lists needed for managing spiders
spider_image=PhotoImage(file="spider.gif")
yposition=random.randint(1,400)
spider=canvas.create_image(0,yposition,image=spider_image)
#add spider to list
spider_list.append(spider)

if key == "Up":
    move_direction="Up"
elif key == "Down":
    move_direction=="Down"
# function to make candy at random places
    
# function moves candy downwards, and schedules call to move_candy
def move_character():
    if move_direction=="Right" and canvas.coords(mychar)[0]<400:
        canvas.move(mychar,10,0)
    if move_direction=="Left" and canvas.coords(mychar)[0]>0:
        canvas.move(mychar,-10,0)
    if move_direction=="Up" and canvas.coords(mychar)[1]>0:
        canvas.move(mychar,0,-10)
    if move_direction=="Down" and canvas.coords(mychar)[1]<400:
        canvas.move(mychar,0,10)
    window.after(16,move_character)


# function updates score, level and candy_speed
def update_score_level():
    # use of global since variables are changed
    global score, level, candy_speed
    score = score + 1
    score_display.config(text="Score :" + \
    str(score))
    # determine if level needs to change
    # update level and candy speed
    if score > 5 and score <= 10:
        candy_speed = candy_speed + 1
        level = 2
        level_display.config(text="Level :" + \
        str(level))
    elif score > 10:
        candy_speed = candy_speed + 1
        level = 3
        level_display.config(text="Level :" + \
        str(level))
    
# function called to end game - destroys window
def end_game_over():
    window.destroy()
    
# this destroys the instructions on the screen
def end_title():
    canvas.delete(title) # remove title
    canvas.delete(directions) # remove directions


# check distance between 2 objects - return true if they 'touch'
def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap
def move_spider():
    for spider in spider_list:
        canvas.move(spider,spider_speed,0)
    window.after(50,move_spider)

move_direction = 0 # track which direction player is moving
# Function handles when user first presses arrow keys
def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"
        
# Function handles when user stop pressing arrow keys
def end_input(event):
    global move_direction
    move_direction = "None"
    
# Function checks if not on edge and updates x coordinates based on right/left
def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10,0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
        canvas.move(mychar, -10,0)
    window.after(16, move_character) # Move character at 60 frames per second

# bind the keys to the character
canvas.bind_all('<KeyPress>', check_input) # bind key press
canvas.bind_all('<KeyRelease>', end_input) # bind all keys to circle

# Start game loop by scheduling all the functions
window.after(1000, end_title) # destroy title and instructions
window.after(1000, make_candy) # start making candy
window.after(1000, move_candy) # start moving candy
window.after(1000, check_hits) # check if character hit a candy
window.after(1000, move_character) # handle keyboard controls

window.mainloop() # last line is the GUI main event loop
