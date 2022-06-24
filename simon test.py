import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import randint

#initalize pygame library
pygame.init()

#set the GPIO pin numers (L to R)
leds = [6, 13, 19, 21]
#switches left to right
switches = [26, 12, 16, 20]
#sounds left to right
sounds = [pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav")]

#set up broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup input pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#setup output pins
GPIO.setup(leds, GPIO.OUT)

game = True
pattern = []
level = 0
while game:
    pattern.append(randint(0,3))
    for i in pattern:
        GPIO.output(leds[i], GPIO.HIGH)
        sounds[i].play
        sleep(1)
        GPIO.output(leds[i], GPIO.LOW)
        sleep(0.5)
    #for i in pattern:
        Input = True
        while Input:
            red = GPIO.input(26)
            blue = GPIO.input(12)
            yellow = GPIO.input(16)
            green = GPIO.input(20)
            
            if red == 0:
                GPIO.output(6, GPIO.HIGH)
                Input = False
                if i != 0:
                    game = False
                sleep(1)
                GPIO.output(6, GPIO.LOW)
            if blue == 0:
                GPIO.output(13, GPIO.HIGH)
                Input = False
                if i != 0:
                    game = False
                sleep(1)
                GPIO.output(13, GPIO.LOW)
            if yellow == 0:
                GPIO.output(19, GPIO.HIGH)
                Input = False
                if i != 0:
                    game = False
                sleep(1)
                GPIO.output(19, GPIO.LOW)                   
            if green == 0:
                GPIO.output(21, GPIO.HIGH)
                Input = False
                if i != 0:
                    game = False
                sleep(1)
                GPIO.output(21, GPIO.LOW)
    sleep(0.5)