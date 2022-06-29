#### GUI ####
from tkinter import *
import pygame
import RPi.GPIO as GPIO
from time import sleep

#setting pins
green = 22
red = 20
blue1 = 5
blue2 = 12
blue3 = 17

#setting up the pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(green, GPIO.OUT) #GREEN
GPIO.setup(red, GPIO.OUT) #red

GPIO.setup(blue1, GPIO.OUT)
GPIO.setup(blue2, GPIO.OUT)
GPIO.setup(blue3, GPIO.OUT)

#initializing pygame
pygame.mixer.init()
path = "/home/pi/Downloads/"

### word lists ###
words = ['shoes', 'mask', 'upon', 'lisp', 'beak', 'crouched', 'rodeo', 'impolite', 'gusto', 'gauze', 'bustling', 'drone', 'vibrant', 'exception', 'notification', 'surrounded', 'orientation', 'columns', 'wretched', 'invigorating']
### audio lists ###
# regular #
audio = ['shoes.mp3', 'mask.mp3', 'upon.mp3', 'lisp.mp3', 'beak.mp3','crouched.mp3', 'rodeo.mp3', 'impolite.mp3', 'gusto.mp3', 'gauze.mp3','bustling.mp3', 'drone.mp3', 'vibrant.mp3', 'exception.mp3', 'notification.mp3', 'surrounded.mp3', 'orientation.mp3', 'columns.mp3', 'wretched.mp3', 'invigorating.mp3','demeanor.mp3']
# slowed #
audio_slowed = ['slowshoes.mp3', 'slowmask.mp3', 'slowupon.mp3', 'slowlisp.mp3', 'slowbeak.mp3','slowcrouched.mp3', 'slowrodeo.mp3', 'slowimpolite.mp3', 'slowgusto.mp3', 'slowgauze.mp3','slowbustling.mp3', 'slowdrone.mp3', 'slowvibrant.mp3', 'slowexception.mp3', 'slownotification.mp3', 'slowsurrounded.mp3', 'sloworientation.mp3', 'slowcolumns.mp3', 'slowwretched.mp3', 'slowinvigorating.mp3']
###################

i = 0
score = 0
attempt = 0

# commands for gui
#will play the audio when play button in pressed
def play():
    global audio
    global i
    pygame.mixer.music.load(path + audio[i])
    return pygame.mixer.music.play()
#will play the audio when play SLOW button in pressed
def play_slow():
    global audio_slowed
    global i
    pygame.mixer.music.load(audio_slowed[i])
    return pygame.mixer.music.play()
#takes the user input and sees if it matches how the word is supposed to be spelled
def enter():
    global i
    global score
    guess = wordbox.get()
    guess.lower()
    guess.rstrip("\n")
    #checking if the guess from the user is correct
    if guess == words[i]:
        i += 1
        score += 1
        #lighting up lights if you are correct
        for l in range(0, 1):
            GPIO.output(green, GPIO.LOW)#on
            sleep (1)
            GPIO.output(green, GPIO.HIGH)#off
            sleep (1)
        #configures the score
        return scoreboard.itemconfig(s, text=("Score:", score))
    else:
        global attempt
        attempt += 1
        attempts.itemconfig(a, text=("Attempts:", attempt))
        #lighting up lights if you are incorrect
        for l in range (0, 1):
                GPIO.output(red, GPIO.LOW)#on
                sleep(1)
                GPIO.output(red, GPIO.HIGH)#off
                sleep(1)
        #starts the counter for how many you get wrong
        if attempt == 1:
            GPIO.output(blue1, GPIO.LOW)#on
        if attempt == 2:
            GPIO.output(blue2, GPIO.LOW)#on
        if attempt == 3:
            GPIO.output(blue3, GPIO.LOW)#on
        #once you have three lights lit up, game will end
        if attempt == 4:
            GPIO.output(blue1, GPIO.HIGH)#off
            GPIO.output(blue2, GPIO.HIGH)#off
            GPIO.output(blue3, GPIO.HIGH)#off
            return end()
#ends the gme if you get more than 3 wrong
def end():
    score = 0
    attempt = 0
    attempts.itemconfig(a, text=("Attempts:", attempt))
    scoreboard.itemconfig(s, text=("Score:",score))
    return ws.destroy()




####

ws = Tk()
ws.title('FreeBee')

#imports the bee image to GUI
pic = PhotoImage(file="beeee.gif")
image = Label(ws, image=pic)
image.grid(row=0, rowspan=5, column=0, columnspan=2)

#text box to enter word
word = Label(ws, text='enter word here:', bg='yellow')
word.grid(row=5, column=0)
wordbox = Entry(ws)
wordbox.grid(row=5, column=1, sticky=EW)

#command will become the spell check
enter = Button(ws, text='Enter', command=enter)
enter.grid(row=5, column=2)

#command will play slowed word
slow = Button(ws, text='slow word down', command= play_slow)
slow.grid(row=4, column=2, sticky=NS)

#will play the word
repeat = Button(ws, text='play word', command= play)
repeat.grid(row=3, column=2, sticky=NS)

#shows number of points
scoreboard = Canvas(ws, width=100, height=50, bg='yellow')
s = scoreboard.create_text(50, 25, text=("Score:", score))
scoreboard.grid(row=0, column=2)

#shows number of attempts
attempts = Canvas(ws, width=100, height=50, bg='yellow')
a = attempts.create_text(50, 25, text=("Attempts:", attempt))
attempts.grid(row=1, column=2)

ws.mainloop()
