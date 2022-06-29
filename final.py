import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 20
led2 = 22

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)



for i in range(5):
    print("correct")
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(0.5)
    
    print("done")
    GPIO.output(led1, GPIO.LOW)
    time.sleep(1)
    print("false")
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(0.5)
    print("done")
    GPIO.output(led2, GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()