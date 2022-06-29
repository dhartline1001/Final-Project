# L.Raab & D.Hartline
# Freebee spelling game
from tkinter import *
from random import choice
import playsound

#default size of GUI
WIDTH = 800
HEIGHT = 600

#### creating words
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
    def __eq__(self, other):
        if self.text == other:
            return True
        else:
            return False
    def play(self):
        return playsound.playsound(Word) 
    def playslow(self):
        return playsound.playsound(Word) 
    def __eq__(self, other):
        if self.text == other:
            return True
        else:
            return False

### blueprint for game
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
    def createWords(self):
        Game.words = []
        Game.words.append(Word('upon', 'upon.mp3', 'slowupon.mp3', 1))
        Game.words.append(Word('shoes', 'shoes.mp3', 'slowshoes.mp3', 1))
        Game.words.append(Word('mask', 'mask.mp3', 'slowmask.mp3', 1))
        Game.words.append(Word('lisp', 'lisp.mp3', 'slowlisp.mp3', 1))
        Game.words.append(Word('beak', 'beak.mp3', 'slowbeak.mp3', 1))
        Game.words.append(Word('crouched', 'crouched.mp3', 'slowcrouched.mp3', 1))
        Game.words.append(Word('rodeo', 'rodeo.mp3', 'slowrodeo.mp3', 1))
        Game.words.append(Word('impolite', 'impolite.mp3', 'slowimpolite.mp3', 1))
        Game.words.append(Word('gusto', 'gusto.mp3', 'slowgusto.mp3', 1))
        Game.words.append(Word('gauze', 'gauze.mp3', 'slowgauze.mp3', 1))
        Game.words.append(Word('bustling', 'bustling.mp3', 'slowbustling.mp3', 2))
        Game.words.append(Word('drone', 'drone.mp3', 'slowdrone.mp3', 2))
        Game.words.append(Word('vibrant', 'vibrant.mp3', 'slowvibrant.mp3', 2))
        Game.words.append(Word('exception', 'exception.mp3', 'slowexception.mp3', 2))
        Game.words.append(Word('notification', 'notification.mp3', 'slownotification.mp3', 2))
        Game.words.append(Word('surrounded', 'surrounded.mp3', 'slowsurrounded.mp3', 2))
        Game.words.append(Word('orientation', 'orientation.mp3', 'sloworientation.mp3', 2))
        Game.words.append(Word('columns', 'columns.mp3', 'slowcolumns.mp3', 2))
        Game.words.append(Word('wretched', 'wretched.mp3', 'slowwretched.mp3', 2))
        Game.words.append(Word('invigorating', 'invigorating.mp3', 'slowinvigorating.mp3', 2))
        Game.words.append(Word('demeanor', 'demeanor.mp3', 'slowdemeanor.mp3', 3))
        Game.words.append(Word('morbidity', 'morbidity.mp3', 'slowmorbidity.mp3', 3))
        Game.words.append(Word('torturous', 'torturous.mp3', 'slowtorturous.mp3', 3))
        Game.words.append(Word('abdomen', 'abdomen.mp3', 'slowabdomen.mp3', 3))
        Game.words.append(Word('liability', 'liability.mp3', 'slowliability.mp3', 3))
        Game.words.append(Word('instinctive', 'instinctive.mp3', 'slowinstinctive.mp3', 3))
        Game.words.append(Word('heriloom', 'heirloom.mp3', 'slowheirloom.mp3', 3))
        Game.words.append(Word('impertinent', 'impertinent.mp3', 'slowimpertinent.mp3', 3))
        Game.words.append(Word('assassinate', 'assassinate.mp3', 'slowassassinate.mp3', 3))
        Game.words.append(Word('embroidery', 'embroidery.mp3', 'slowembroidery.mp3', 3))
        Game.words.append(Word('accumulate', 'accumulate.mp3', 'slowaccumulate.mp3', 4))
        Game.words.append(Word('biographical', 'biographical.mp3', 'slowbiographical.mp3', 4))
        Game.words.append(Word('chrysanthemum', 'chrysanthemum.mp3', 'slowchrysanthemum.mp3', 4))
        Game.words.append(Word('flamboyant', 'flamboyant.mp3', 'slowflamboyant.mp3', 4))
        Game.words.append(Word('discrepency', 'discrepency.mp3', 'slowdiscrepency.mp3', 4))
        Game.words.append(Word('malignant', 'malignant.mp3', 'slowmalignant.mp3', 4))
        Game.words.append(Word('grotesque', 'grotesque.mp3', 'slowgrotesque.mp3', 4))
        Game.words.append(Word('inevitable', 'inevitable.mp3', 'slowinevitable.mp3', 4))
        Game.words.append(Word('lieutenant', 'lieutenant.mp3', 'slowlieutenant.mp3', 4))
        Game.words.append(Word('nostalgia', 'nostaliga.mp3', 'slownostaliga.mp3', 4))
        Game.words.append(Word('fallacious', 'fallacious.mp3', 'slowfallacious.mp3', 5))
        Game.words.append(Word('atrophy', 'atrophy.mp3', 'slowatrophy.mp3', 5))
        Game.words.append(Word('autonomous', 'autonomous.mp3', 'slowautonomous.mp3', 5))
        Game.words.append(Word('concierge', 'concierge.mp3', 'slowconcierge.mp3', 5))
        Game.words.append(Word('knickknack', 'knickknack.mp3', 'slowknickknack.mp3', 5))
        Game.words.append(Word('narcissus', 'narcissus.mp3', 'slownarcissus.mp3', 5))
        Game.words.append(Word('oxymoron', 'oxymoron.mp3', 'slowoxymoron.mp3', 5))
        Game.words.append(Word('neurosis', 'neurosis.mp3', 'slowneurosis.mp3', 5))
        Game.words.append(Word('parallelogram', 'parallelogram.mp3', 'slowparallelogram.mp3', 5))
        Game.words.append(Word('disenfranchise', 'disenfranchise.mp3', 'slowdisenfranchise.mp3', 5))
    
    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)
        #input
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        
        #set up image on left
        img = None
        Game.image = Label(self, width= WIDTH//2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
                           
        #setup buttons on right
        Game.slow = Button(self, height=HEIGHT//2, text='slows word down', command = Word.playslow(Word.audio))
        Game.slow.pack(fill=Y)
        Game.norm = Button(self, height=HEIGHT//2, text='play word', command= Word.play())
        Game.norm = Button(fill=Y)
                                                
    def setStatus(self, status):
        Game.text.config(state=NORMAL)
        
    def play(self):
        #create words
        self.createWords()
        #configure GUI
        self.setupGUI()
        #set inital status
        self.setStatus("Welcome to FreeBee!")
    
    def process(self, event):
        guess = Game.player_input.get()
        guess = action.lower().strip()
        while Game.word.level == 1:
            for word in guess:
                if word in guess:
                    print("Correct!")
                           
        Game.player_input.delete(0,END)
 
 
 
#create the window
ws = Tk()
ws.title('FreeBee')

#create the GUI as a canvas in window
g = Game(ws)
g.play()

#wait for window to close
ws.mainloop()