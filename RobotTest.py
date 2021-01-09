import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ControlPinOut=[37,38,35,36]
ControlPinIn=[11,12,13,15]
count = 0
delay = 1
left = 11
right = 12
up = 13
down = 15

for pinIn in ControlPinIn:
    GPIO.setup(pinIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
for pinOut in ControlPinOut:
    GPIO.setup(pinOut,GPIO.OUT)
    GPIO.output(pinOut,False)
    
def setStep(w1, w2, w3, w4):
  GPIO.output(35, w1)
  GPIO.output(36, w2)
  GPIO.output(37, w3)
  GPIO.output(38, w4)
  
while True:
 while GPIO.input(up) == GPIO.HIGH: #Forward
  setStep(1,0,0,1)
 while GPIO.input(down) == GPIO.HIGH: #Reverse
  setStep(0,1,1,0)
 while GPIO.input(left) == GPIO.HIGH: #Left
  setStep(0,1,0,1)
 while GPIO.input(right) == GPIO.HIGH: #Right
  setStep(1,0,1,0)
  
 if GPIO.input(up) == GPIO.LOW:
  setStep(0,0,0,0)
 elif GPIO.input(down) == GPIO.LOW:
  setStep(0,0,0,0)
 elif GPIO.input(right) == GPIO.LOW:
  setStep(0,0,0,0)
 elif GPIO.input(left) == GPIO.LOW:
  setStep(0,0,0,0)

GPIO.cleanup()