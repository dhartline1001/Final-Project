from tkinter import *

Root= Tk()
canvas= Canvas(Root,width=500, height=500, bg="white")
canvas.pack()

Score= 0 #This is the global with the score value

J=canvas.create_text(100,100, text=("Score", Score), font=("Comic Sans", 50)) #This is the first appearance of the score on screen, or the first creation.

def change(): #Here's where I change the score value and create the new text
    global Score
    Score+=1
    J=canvas.create_text(100,100, text=("Score", Score), font=("Comic Sans", 50))

def changee(): #And this one, is supposed to work deleting the "J" every time it is called, but it only works the first time it is called with the first text
    canvas.delete(J)
    print("del")

def do(): #This one calls the other two in a button (Because I need to call them like this on the actual game code
    change()
    changee()

B= Button(canvas, text= "change it", command=do) 
B.place(x=300,y=300)

