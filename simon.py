import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import randint

game = False

#initialize the pygame library
pygame.init()

#set gpio pin numbers
#LEDS from left to right
leds = [6, 13, 19, 21]
#switches from left to right
switches = [26, 12, 16, 20]
#the sounds that map to each LED (from left to right)
sounds = [pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"),pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav")]

#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#set up input and output pins
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#got these from Eboni and Alex
def LED_ON():
    for i in leds:
        GPIO.output(leds, True)
        
def LED_OFF():
    for i in leds:
        GPIO.output(leds, False)
        
def lose():
    for i in range(0, 4):
        leds_on()
        sleep(0.5)
        leds_off()
        sleep(0.5)
        
####### MAIN #######

pattern = []

print("welcome to simon")
print ("try to play the patternuence back by pressing the switches")

try:
    while (True):
        #from here to line 81 Eboni and Alex helped with reformatting our previous code
        #ex. if statements and switch_count
        pattern.append(randint(0, 3))
        if (game):
            if (len(pattern) > 3):
                print()
            print("pattern = {}".format(pattern))
        if len(pattern) < 6:
            for s in pattern:
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(1)
                GPIO.output(leds[s], False)
                sleep(0.5)
            switch_count = 0
        elif len(pattern) >= 6 and len(pattern) <= 15:
            for s in pattern:
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.5)
                GPIO.output(leds[s], False)
                sleep(0.5)
            switch_count = 0
        else:
            for i in range(0, 13):
                GPIO.output(leds[s], False)
                sounds[s].play()
                sleep(0.5)
                GPIO.output(leds[s], False)
                slep(0.5)
            switch_count = 0
        while (switch_count < len(pattern)):
            pressed = False
            while (not pressed):
                for i in range(len(switches)):
                    while (GPIO.input(switches[i])):
                        val = i
                        pressed = True
#lines 90 - 104, Eboni ad Alex helped us rearrange code from class
            if (game):
                print(val)
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)
            
            if (val != pattern[switch_count]):
                score = len(pattern)
                print ("Congrats youve made it to level {}".format(score))
                lose()
                GPIO.cleanup()
                exit(0)
            switch_count += 1
except KeyboardInterrupt: #ctrl-c to end game
    GPIO.cleanup()
    print("\n Bye")

# Eboni and Alex helped us understand what the code was doing in the sections they helped with
# 