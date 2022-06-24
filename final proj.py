from tkinter import *
from random import choice
import playsound

class Word:
    def __init__(self, t, a, s, l):
        self._audio = a
        self._text = t
        self._slow = s
        self._level = l
    @property
    def audio(self):
        return self._audio
    @audio.setter
    def audio(self, a):
        self._audio = a
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, t):
        self._text = t
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, l):
        self._level = l
    @property
    def slow(self):
        return self._slow
    @slow.setter
    def slow(self, s):
        self._slow = s
    ###double check this overrides the equals
    def __eq__(self, other):
        if self.text == other:
            return True
        else:
            return False
    def play(self):
        return playsound.playsound(self._audio)
    def playslow(self):
        return playsound.playsound(self._slow)
    def __eq__(self, other):
        if self.text == other:
            return True
        else:
            return False

words = []
words.append(Word('shoes', 'shoes.mp3', 'slowshoes.mp3', 1))
words.append(Word('mask', 'mask.mp3', 'slowmask.mp3', 1))
words.append(Word('upon', 'upon.mp3', 'slowupon.mp3', 1))
words.append(Word('lisp', 'lisp.mp3', 'slowlisp.mp3', 1))
words.append(Word('beak', 'beak.mp3', 'slowbeak.mp3', 1))
words.append(Word('crouched', 'crouched.mp3', 'slowcrouched.mp3', 1))
words.append(Word('rodeo', 'rodeo.mp3', 'slowrodeo.mp3', 1))
words.append(Word('impolite', 'impolite.mp3', 'slowimpolite.mp3', 1))
words.append(Word('gusto', 'gusto.mp3', 'slowgusto.mp3', 1))
words.append(Word('gauze', 'gauze.mp3', 'slowgauze.mp3', 1))
words.append(Word('bustling', 'bustling.mp3', 'slowbustling.mp3', 2))
words.append(Word('drone', 'drone.mp3', 'slowdrone.mp3', 2))
words.append(Word('vibrant', 'vibrant.mp3', 'slowvibrant.mp3', 2))
words.append(Word('exception', 'exception.mp3', 'slowexception.mp3', 2))
words.append(Word('notification', 'notification.mp3', 'slownotification.mp3', 2))
words.append(Word('surrounded', 'surrounded.mp3', 'slowsurrounded.mp3', 2))
words.append(Word('orientation', 'orientation.mp3', 'sloworientation.mp3', 2))
words.append(Word('columns', 'columns.mp3', 'slowcolumns.mp3', 2))
words.append(Word('wretched', 'wretched.mp3', 'slowwretched.mp3', 2))
words.append(Word('invigorating', 'invigorating.mp3', 'slowinvigorating.mp3', 2))


def enter():
    if  temp == guess:
        return wordbox.clear()
    else:
        return "try again"

####

ws = Tk()
ws.title('FreeBee')

pic = PhotoImage(file="bee.png")
image = Label(ws, image=pic)
image.grid(row=0, rowspan=4, column=0, columnspan=2)

word = Label(ws, text='enter word here:', bg='yellow')
word.grid(row=4, column=0)
wordbox = Entry(ws)
wordbox.grid(row=4, column=1, sticky=EW)

#command will become the spell check
enter = Button(ws, text='Enter', command=enter)
enter.grid(row=4, column=2)

#command will play slowed word
slow = Button(ws, text='slow word down', command= temp.playslow())
slow.grid(row=2, rowspan=2, column=2, sticky=NS)

#will play the word
repeat = Button(ws, text='play word', command= temp.play())
repeat.grid(row=0, rowspan=2, column=2, sticky=NS)

while self._level == '1':
    