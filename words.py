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
words.append(Word('demeanor', 'demeanor.mp3', 'slowdemeanor.mp3', 3))
words.append(Word('morbidity', 'morbidity.mp3', 'slowmorbidity.mp3', 3))
words.append(Word('torturous', 'torturous.mp3', 'slowtorturous.mp3', 3))
words.append(Word('abdomen', 'abdomen.mp3', 'slowabdomen.mp3', 3))
words.append(Word('liability', 'liability.mp3', 'slowliability.mp3', 3))
words.append(Word('instinctive', 'instinctive.mp3', 'slowinstinctive.mp3', 3))
words.append(Word('heriloom', 'heirloom.mp3', 'slowheirloom.mp3', 3))
words.append(Word('impertinent', 'impertinent.mp3', 'slowimpertinent.mp3', 3))
words.append(Word('assassinate', 'assassinate.mp3', 'slowassassinate.mp3', 3))
words.append(Word('embroidery', 'embroidery.mp3', 'slowembroidery.mp3', 3))
words.append(Word('accumulate', 'accumulate.mp3', 'slowaccumulate.mp3', 4))
words.append(Word('biographical', 'biographical.mp3', 'slowbiographical.mp3', 4))
words.append(Word('chrysanthemum', 'chrysanthemum.mp3', 'slowchrysanthemum.mp3', 4))
words.append(Word('flamboyant', 'flamboyant.mp3', 'slowflamboyant.mp3', 4))
words.append(Word('discrepency', 'discrepency.mp3', 'slowdiscrepency.mp3', 4))
words.append(Word('malignant', 'malignant.mp3', 'slowmalignant.mp3', 4))
words.append(Word('grotesque', 'grotesque.mp3', 'slowgrotesque.mp3', 4))
words.append(Word('inevitable', 'inevitable.mp3', 'slowinevitable.mp3', 4))
words.append(Word('lieutenant', 'lieutenant.mp3', 'slowlieutenant.mp3', 4))
words.append(Word('nostalgia', 'nostaliga.mp3', 'slownostaliga.mp3', 4))
words.append(Word('fallacious', 'fallacious.mp3', 'slowfallacious.mp3', 5))
words.append(Word('atrophy', 'atrophy.mp3', 'slowatrophy.mp3', 5))
words.append(Word('autonomous', 'autonomous.mp3', 'slowautonomous.mp3', 5))
words.append(Word('concierge', 'concierge.mp3', 'slowconcierge.mp3', 5))
words.append(Word('knickknack', 'knickknack.mp3', 'slowknickknack.mp3', 5))
words.append(Word('narcissus', 'narcissus.mp3', 'slownarcissus.mp3', 5))
words.append(Word('oxymoron', 'oxymoron.mp3', 'slowoxymoron.mp3', 5))
words.append(Word('neurosis', 'neurosis.mp3', 'slowneurosis.mp3', 5))
words.append(Word('parallelogram', 'parallelogram.mp3', 'slowparallelogram.mp3', 5))
words.append(Word('disenfranchise', 'disenfranchise.mp3', 'slowdisenfranchise.mp3', 5))


### to play
temp = choice(words)
temp.play()

## for enter
if (whatever the input name is) == temp
