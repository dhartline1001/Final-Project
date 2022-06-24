import RPi.GPIO as GPIO
from time import sleep, time
import pygame
from array import array
import math
import numpy as np

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

shape = input("what shape do you want? triangle, sawtooth, square, or sinusodial?")
#note generator class
class Note(pygame.mixer.Sound):
    #note that volume ranges from 0.0 to 1.0
    def __init__(self, frequency, volume):
        self.frequency = frequency
        #initialize the note using an array of samples
        pygame.mixer.Sound.__init__(self, buffer = self.build_samples())
        self.set_volume(volume)
    def build_samples(self):
        if shape == 'square':
            return self.build_square()
        elif shape == 'triangle':
            return self.build_triangle()
        elif shape == 'sawtooth':
            return self.build_sawtooth()
        elif shape == 'sin':
            return self.build_sin()

    def build_square(self):
        #calculate the period and amplitude of the notes wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        #initialize the notes samples
        samples = array("h", [0] *period)
        #generate the notes sample
        for t in range(period):
            if (t < period / 2):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
        return samples

    def build_triangle(self):
        #calculate the period and amplitude of the notes wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        #initialize the notes samples
        samples = array("h", [int(2 / math.pi)] *period)
        #generate the notes sample
        for t in range(period):
            if (t < period / 4):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
        return samples
    
    
# def f(x):
#     if (x>=0) or (x<math.pi):
#         return x
#     else:
#         return x-(2**math.pi)
    def build_sawtooth(self):
        #calculate the period and amplitude of the notes wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) -1
        #initialize the notes samples
        samples = array("h", [int(1 / math.pi)] *period)
        #generate the notes sample
        for t in range(period):
            if (t < period / int(2 * math.pi)):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
        return samples
    def build_sin(self):
        period = int(round(MIXER_FREQ /self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) -1
        wave = (amplitude * np.sin(2 * np.pi * period))
        return wave

#     
#wait until note is pressed
def wait_for_note_start():
    while (True):
        #first, check for notes
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        #next, check for the play button
        if (GPIO.input(play)):
            #debounce the switch
            while (GPIO.input(play)):
                sleep(0.01)
            return "play"
        #finally, check for the record button
        if (GPIO.input(record)):
            #debounce the switch
            while (GPIO.input(record)):
                sleep(0.01)
            return "record"
        sleep(0.01)
#waits until a note is released
def wait_for_note_stop(key):
    while (GPIO.input(key)):
        sleep(0.1)
        
#plays a recorded song
def play_song():
    #each element in the song list is a list composed of two parts
    #a note (or silence) and a duration
    for part in song:
        note, duration = part
        #if its a silence, delay for its duration
        if (note == "SILENCE"):
            sleep(duration)
        #otherwise, play the note for its duration
        else:
            notes[note].play(-1)
            sleep(duration)
            notes[note].stop()
        
        
#initialize the mixer; then, initialize the pygame library
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

#uses the broadcom pin code
GPIO.setmode(GPIO.BCM)

#setup the pin and frequency for a C note
keys = [20, 16, 12, 26]
freqs = [261.6, 261.6, 261.6, 261.6]
notes =[]
#setup the button pins
play = 19
record = 21
#setup the LED pins
red = 27
green = 18
blue = 17

#setup the input pins
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(play, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(record, GPIO.IN, GPIO.PUD_DOWN)
#setup the output pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

#create actual notes
for freq in freqs:
    notes.append(Note(freq, 1))
#begin in a non recording state and initialize song
recording = False
song = []
#main program
print("welcome to paper piano!")
print("press ctrl+c to exit")
#shape = input("what shape do you want? triangle, sawtooth, square, or sinusodial?")
# if input == 'triangle':
#     buffer= Note.build_triangle()
# elif input == 'sawtooth':
#     buffer= Note.build_sawtooth()
# elif input== 'square':
#     buffer= Note.build_samples()
# else:
#     buffer= Note.build_sin()
#detect  when ctrl+c is pressed
try:
    while(True):
        #start a timer
        start = time()
        #play a note when pressed... until released
        #also detect play/record
        key = wait_for_note_start()
        #note the duration of the silence
        duration = time() - start
        # if recording, append the duration of the silence
        if (recording):
            song.append(["SILENCE", duration])
        #if the record button was pressed
        if (key == "record"):
            #if not previously recording, reset the song
            if (not recording):
                song = []
            #note the recording state and turn on the red LED
                recording = not recording
                GPIO.output(red, recording)
            #if the play button was pressed
        elif (key == "play"):
                #if recording, stop
                if (recording):
                    recording = False
                    GPIO.output(red, False)
                #turn on the greenn LED
                GPIO.output(green, True)
                #play the song
                play_song()
                GPIO.output(green, False)
            #otherwise, a piano key was pressed
        else:
                #start the timer and play the note
                start = time()
                notes[key].play(-1)
                wait_for_note_stop(keys[key])
                notes[key].stop()
                #once the note is released, stop the timer
                duration = time() - start
                #if recording; append thenote and its duration
                if (recording):
                    song.append([key, duration])
#         #play a note when pressed until released
#         key = wait_for_note_start()
#         notes[key].play(-1)
#         wait_for_note_stop(keys[key])
#         notes[key].stop()
except KeyboardInterrupt:
    #reset the GPIO pins
    GPIO.cleanup()


