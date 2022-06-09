#### GUI ####
from tkinter import *

ws = Tk()
ws.title('FreeBee')

level = Label(ws, text= 'level', bg='yellow')
level.grid(row=0, column=2)

level1 = Button(ws, text='Level 1', command=None)
level1.grid(row=1, column=2)
level2 = Button(ws, text='Level 2', command=None)
level2.grid(row=2, column=2)
level3 = Button(ws, text='Level 3', command=None)
level3.grid(row=3, column=2)

pic = PhotoImage(file="bee.png")
image = Label(ws, image=pic)
image.grid(row=0, rowspan=4, column=0, columnspan=2)

word = Label(ws, text='enter word here:', bg='yellow')
word.grid(row=4, column=0)
wordbox = Entry(ws)
wordbox.grid(row=4, column=1, sticky=EW)

enter = Button(ws, text='Enter', command=None)
enter.grid(row=4, column=2)

slow = Button(ws, text='slow word down', command=None)
slow.grid(row=5, column=0)

repeat = Button(ws, text='repeat word', command=None)
repeat.grid(row=5, column=1)

fast = Button(ws, text='speed word up', command=None)
fast.grid(row=5, column=2)
