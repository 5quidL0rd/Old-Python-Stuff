#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *

window=Tk()
window.title('My first GUI')

#function to be called when the button is clicked
def hello_function():
    print('Hello, World') #print Hello World to the Python Shell
    #change the display Area widget to show this text
    display_area.config(text="Hello, World", fg="yellow", bg="black")

#adding a button widget
button1=Button(window,text="Click Me",command=hello_function)
button1.pack() #this actually places the button on the window

#adding the display area - using the label widget
display_area=Label(window,text="")
display_area.pack() #this places text area on window

#create a canvas to put objects on the screen
canvas = Canvas(window, width=400,height=400)
canvas.pack()

#function to be called when the button Exit is clicked
def exit_program():
    window.destroy()
qbutton=Button(window,text="Exit",command=exit_program)
qbutton.pack() #this actually places the button on the window

#move circle to left or right based on keys
def move_circle(event):
    key=event.keysym
    if key == "Right":
        canvas.move(circle,10,0) #change x
    elif key == "Left":
        canvas.move(circle,-10,0) #change x
#bind keyboard input to move_circle
canvas.bind_all('<Key>',move_circle)

#function that handles mouse clicks on the character mychar
def move_character(event):
    canvas.coords(mychar,event.x,event.y)
#bind left button mouse to moving the character
canvas.bind_all('<Button-1>',move_character)

#this creates a red circle at position 100,200 of size 30 by 30
circle=canvas.create_oval(100,200,130,230, fill='red')
#this creates a blue rectangle with top left at 50,50 of size 20 by 30
blue_rect=canvas.create_rectangle(50,50,70,80, fill='blue')
#creates text 'Welcome' in black,font Helvetica 30 at position 200,200
screen_message=canvas.create_text(200,200, text= 'Welcome', fill='black', font= ('Helvetica', 30))
#create an image object using the gif file
img=PhotoImage(file="greenChar.gif")
#use image object to create a canvas image at position 100,100
mychar=canvas.create_oval(100,100,100,100,fill='green')



window.mainloop() #last line is the GUI main event loop 
