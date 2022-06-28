#### GUI ####
from tkinter import *
import playsound

### word lists ###
words1 = ['shoes', 'mask', 'upon', 'lisp', 'beak', 'crouched', 'rodeo', 'impolite', 'gusto', 'gauze']
words2 = ['bustling', 'drone', 'vibrant', 'exception', 'notification', 'surrounded', 'orientation', 'columns', 'wretched', 'invigorating']
words3 = ['demeanor', 'morbidity', 'torturous', 'abdomen', 'liability', 'instinctive', 'heirloom', 'impertinent', 'assassinate', 'embroidery']
words4 = ['accumulate', 'biographical', 'chrysanthemum', 'flamboyant', 'discrepancy', 'malignant', 'grotesque', 'inevitable', 'lieutenant', 'nostalgia']
words5 = ['fallacious', 'atrophy', 'autonomous', 'concierge', 'knickknack', 'narcissus', 'oxymoron', 'neurosis', 'parallelogram', 'disenfranchise']

### audio lists ###
# regular #
lvl1 = ['shoes.mp3', 'mask.mp3', 'upon.mp3', 'lisp.mp3', 'beak.mp3','crouched.mp3', 'rodeo.mp3', 'impolite.mp3', 'gusto.mp3', 'gauze.mp3']
lvl2 = ['bustling.mp3', 'drone.mp3', 'vibrant.mp3', 'exception.mp3', 'notification.mp3', 'surrounded.mp3', 'orientation.mp3', 'columns.mp3', 'wretched.mp3', 'invigorating.mp3']
lvl3 = ['demeanor.mp3', 'morbidity.mp3', 'torturous.mp3', 'abdomen.mp3', 'liability.mp3', 'instinctive.mp3', 'heirloom.mp3', 'impertinent.mp3', 'assassinate.mp3', 'embroidery.mp3']
lvl4 = ['accumulate.mp3', 'biographical.mp3', 'chrysanthemum.mp3', 'flamboyant.mp3', 'discrepancy.mp3', 'malignant.mp3', 'grotesque.mp3', 'inevitable.mp3', 'lieutenant.mp3', 'nostalgia.mp3']
lvl5 = ['fallacious.mp3', 'atrophy.mp3', 'autonomous.mp3', 'concierge.mp3', 'knickknack.mp3', 'narcissus.mp3', 'oxymoron.mp3', 'neurosis.mp3', 'parallelogram.mp3', 'disenfranchise.mp3']
# slowed #
lvl1_slowed = ['slowshoes.mp3', 'slowmask.mp3', 'slowupon.mp3', 'slowlisp.mp3', 'slowbeak.mp3','slowcrouched.mp3', 'slowrodeo.mp3', 'slowimpolite.mp3', 'slowgusto.mp3', 'slowgauze.mp3']
lvl2_slowed = ['slowbustling.mp3', 'slowdrone.mp3', 'slowvibrant.mp3', 'slowexception.mp3', 'slownotification.mp3', 'slowsurrounded.mp3', 'sloworientation.mp3', 'slowcolumns.mp3', 'slowwretched.mp3', 'slowinvigorating.mp3']
lvl3_slowed = ['slowdemeanor.mp3', 'slowmorbidity.mp3', 'slowtorturous.mp3', 'slowabdomen.mp3', 'slowliability.mp3', 'slowinstinctive.mp3', 'slowheirloom.mp3', 'slowimpertinent.mp3', 'slowassassinate.mp3', 'slowembroidery.mp3']
lvl4_slowed = ['slowaccumulate.mp3', 'slowbiographical.mp3', 'slowchrysanthemum.mp3', 'slowflamboyant.mp3', 'slowdiscrepancy.mp3', 'slowmalignant.mp3', 'slowgrotesque.mp3', 'slowinevitable.mp3', 'slowlieutenant.mp3', 'slownostalgia.mp3'] 
lvl5_slowed= ['slowfallacious.mp3', 'slowatrophy.mp3', 'slowautonomous.mp3', 'slowconcierge.mp3', 'slowknickknack.mp3', 'slownarcissus.mp3', 'slowoxymoron.mp3', 'slowneurosis.mp3', 'slowparallelogram.mp3', 'slowdisenfranchise.mp3']
###################

words = 0
if words <= 9:
    level = lvl1
elif (words > 9) and (words <=19):
    level = lvl2
elif (words > 19) and (words <=29):
    level = lvl3
elif (words > 29) and (words <=39):
    level = lvl4
else:
    level = lvl5
wordss = 0
if wordss <= 9:
    levels = lvl1
elif (wordss > 9) and (wordss <=19):
    levels = lvl2
elif (wordss > 19) and (wordss <=29):
    levels = lvl3
elif (wordss > 29) and (wordss <=39):
    levels = lvl4
else:
    levels = lvl5

# commands for gui
def play():
    for word in level:
        global words
        words += 1
        return playsound.playsound(word)
def play_slow():
    for word in levels:
        global wordss
        wordss += 1
        return playsound.playsound(word)   
def enter():
    i=0
    guess = wordbox.get()
    if words1[i] == guess:
        i += 1
        return next
    else:
        return end

def next():
    break

def end():
    break


####

ws = Tk()
ws.title('FreeBee')

pic = PhotoImage(file="beeee.gif")
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
slow = Button(ws, text='slow word down', command= play_slow)
slow.grid(row=2, rowspan= 2, column=2, sticky=NS)

#will play the word
repeat = Button(ws, text='play word', command= play)
repeat.grid(row=0, rowspan=2, column=2, sticky=NS)

ws.mainloop()
