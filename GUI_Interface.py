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
enter = Button(ws, text='Enter', command=None)
enter.grid(row=4, column=2)

#command will play slowed word
slow = Button(ws, text='slow word down', command=None)
slow.grid(row=2, rowspan=2, column=2, sticky=NS)

#will play the word
repeat = Button(ws, text='play word', command= play)
repeat.grid(row=0, rowspan=2, column=2, sticky=NS)


def play():
    
    return playsound.playsound(i)

