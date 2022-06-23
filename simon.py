import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import randint, choice

#initialize the pygame library
pygame.init()

#set gpio pin numbers
#LEDS from left to right
leds = [6, 13, 19, 21]
#switches from left to right
switches = [20, 16, 12, 26]
#the sounds that map to each LED (from left to right)
sounds = [pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"),pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav")]

#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#set up input and output pins
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

choices = []
led = choice(leds)
choices.append(led)

for i in range(len(choices)):
    GPIO.output(choices[i], True)
    sounds[i].play()
    sleep(1)
    GPIO.output(choices[i], False)
    sleep(0.5)


### MAIN PROGRAM ###game = True
# pattern = []
# player = []
# levels = 1
# while game:
# for i in levels:
#     pattern.append(choice(leds))
#     
# for x in pattern:
#     GPIO.output(leds[x], GPIO.HIGH)
#     sleep(1)
#     GPIO.output(leds[x], GPIO.LOW)
#     sleep(0.5)
#         
# while len(player) < 3:
#     sleep(0.3)
#         redbuttonstate = GPIO.input(20)
#         bluebuttonstate = GPIO.input(16)
#         yellowbuttonstate = GPIO.input(12)
#         greenbuttonstate = GPIO.input(26)
#             
#         if redbuttonstate == 0:
#             GPIO.output(6, GPIO.HIGH)
#             waitingforinput = False
#             if x != 0:
#                 game = False
#             sleep(1)
#             GPIO.output(6, GPIO.LOW)
#         if bluebuttonstate == 0:
#             GPIO.output(13, GPIO.HIGH)
#             waitingforinput = False
#             if x != 0:
#                 game = False
#             sleep(1)
#             GPIO.output(13, GPIO.LOW)
#         if yellowbuttonstate == 0:
#             GPIO.output(19, GPIO.HIGH)
#             waitingforinput = False
#             if x != 0:
#                 game = False
#             sleep(1)
#             GPIO.output(19, GPIO.LOW)
#         if greenbuttonstate == 0:
#             GPIO.output(21, GPIO.HIGH)
#             waitingforinput = False
#             if x != 0:
#                 game = False
#             sleep(1)
#             GPIO.output(21, GPIO.LOW)
#             
#             
# 
# 
# #### testing code #####
# # print("Watch the LEDs light with sound!")
# # for i in range(len(leds)):
# #     #light the current LED
# #     GPIO.output(leds[i], True)
# #     # plays corresponding sound
# #     sounds[i].play()
# #     #wait a bit, then turn the LED off
# #     sleep(1)
# #     GPIO.output(leds[i], False)
# #     sleep(0.5)
# # 
# # print("Bye!")
# # GPIO.cleanup()
# ###############
# 
# # print("Press the switches or Ctrl+C to exit")
# # try:
# #     while (True): #keeps going until quit
# #         pressed = False
# #         #so long as no switch is currently pressed
# #         while (not pressed):
# #             #we can check the status of each switch
# #             for i in range(len(switches)):
# #                 #if one switch is pressed
# #                 while (GPIO.input(switches[i]) == True):
# #                     #note its index and that somethings pressed
# #                     val = i
# #                     pressed = True
# #         #do light and sound
# #         GPIO.output(leds[val], True)
# #         sounds[val].play()
# #         sleep(1)
# #         GPIO.output(leds[val], False)
# #         sleep(0.25)
# # except KeyboardInterrupt: #ctrl-c to end game
# #     GPIO.cleanup()
# #     print("\nBye!")
# 
# 
