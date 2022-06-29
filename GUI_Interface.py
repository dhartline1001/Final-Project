#### GUI ####
from tkinter import *
import playsound

### word lists ###
words = ['shoes', 'mask', 'upon', 'lisp', 'beak', 'crouched', 'rodeo', 'impolite', 'gusto', 'gauze', 'bustling', 'drone', 'vibrant', 'exception', 'notification', 'surrounded', 'orientation', 'columns', 'wretched', 'invigorating','demeanor', 'morbidity', 'torturous', 'abdomen', 'liability', 'instinctive', 'heirloom', 'impertinent', 'assassinate', 'embroidery','accumulate', 'biographical', 'chrysanthemum', 'flamboyant', 'discrepancy', 'malignant', 'grotesque', 'inevitable', 'lieutenant', 'nostalgia','fallacious', 'atrophy', 'autonomous', 'concierge', 'knickknack', 'narcissus', 'oxymoron', 'neurosis', 'parallelogram', 'disenfranchise']
### audio lists ###
# regular #
audio = ['shoes.mp3', 'mask.mp3', 'upon.mp3', 'lisp.mp3', 'beak.mp3','crouched.mp3', 'rodeo.mp3', 'impolite.mp3', 'gusto.mp3', 'gauze.mp3','bustling.mp3', 'drone.mp3', 'vibrant.mp3', 'exception.mp3', 'notification.mp3', 'surrounded.mp3', 'orientation.mp3', 'columns.mp3', 'wretched.mp3', 'invigorating.mp3','demeanor.mp3', 'morbidity.mp3', 'torturous.mp3', 'abdomen.mp3', 'liability.mp3', 'instinctive.mp3', 'heirloom.mp3', 'impertinent.mp3', 'assassinate.mp3', 'embroidery.mp3','accumulate.mp3', 'biographical.mp3', 'chrysanthemum.mp3', 'flamboyant.mp3', 'discrepancy.mp3', 'malignant.mp3', 'grotesque.mp3', 'inevitable.mp3', 'lieutenant.mp3', 'nostalgia.mp3','fallacious.mp3', 'atrophy.mp3', 'autonomous.mp3', 'concierge.mp3', 'knickknack.mp3', 'narcissus.mp3', 'oxymoron.mp3', 'neurosis.mp3', 'parallelogram.mp3', 'disenfranchise.mp3']
# slowed #
audio_slowed = ['slowshoes.mp3', 'slowmask.mp3', 'slowupon.mp3', 'slowlisp.mp3', 'slowbeak.mp3','slowcrouched.mp3', 'slowrodeo.mp3', 'slowimpolite.mp3', 'slowgusto.mp3', 'slowgauze.mp3','slowbustling.mp3', 'slowdrone.mp3', 'slowvibrant.mp3', 'slowexception.mp3', 'slownotification.mp3', 'slowsurrounded.mp3', 'sloworientation.mp3', 'slowcolumns.mp3', 'slowwretched.mp3', 'slowinvigorating.mp3','slowdemeanor.mp3', 'slowmorbidity.mp3', 'slowtorturous.mp3', 'slowabdomen.mp3', 'slowliability.mp3', 'slowinstinctive.mp3', 'slowheirloom.mp3', 'slowimpertinent.mp3', 'slowassassinate.mp3', 'slowembroidery.mp3','slowaccumulate.mp3', 'slowbiographical.mp3', 'slowchrysanthemum.mp3', 'slowflamboyant.mp3', 'slowdiscrepancy.mp3', 'slowmalignant.mp3', 'slowgrotesque.mp3', 'slowinevitable.mp3', 'slowlieutenant.mp3', 'slownostalgia.mp3','slowfallacious.mp3', 'slowatrophy.mp3', 'slowautonomous.mp3', 'slowconcierge.mp3', 'slowknickknack.mp3', 'slownarcissus.mp3', 'slowoxymoron.mp3', 'slowneurosis.mp3', 'slowparallelogram.mp3', 'slowdisenfranchise.mp3']
###################

i = 0
score = 0
attempt = 0

#iterates through regular audio
def play():
    global audio
    global i
    return playsound.playsound(audio[i])
#iterated through slowed audio
def play_slow():
    global audio_slowed
    global i
    return playsound.playsound(audio_slowed[i])
#spell checks the entry
def enter():
    global i
    global score
    guess = wordbox.get()
    guess.lower()
    guess.rstrip("\n")
    if guess == words[i]:
        i += 1
        #adds score to gui
        score += 1
        return scoreboard.itemconfig(s, text=("Score:", score))
    else:
        global attempt
        #adds attempts
        attempt += 1
        attempts.itemconfig(a, text=("Attempts:", attempt))
        #kills game if there are 3 attempts
        #we have 4 so the player can see the attempts and score cleared
        if attempt == 4:
            return end()

def end():
    #clears scores and attempts
    score = 0
    attempt = 0
    attempts.itemconfig(a, text=("Attempts:", attempt))
    scoreboard.itemconfig(s, text=("Score:",score))
    #ends game
    return ws.destroy()


#### GUI codes

ws = Tk()
ws.title('FreeBee')

#cute bee picture
pic = PhotoImage(file="beeee.gif")
image = Label(ws, image=pic)
image.grid(row=0, rowspan=5, column=0, columnspan=2)

#input section
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

#loops game until it's forced to quit or quit by player
ws.mainloop()
