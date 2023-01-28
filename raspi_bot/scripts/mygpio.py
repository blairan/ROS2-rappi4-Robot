import RPi.GPIO as GPIO
import time

class mygpio():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(4,GPIO.OUT)
        GPIO.setup(5,GPIO.OUT)
        GPIO.setup(6,GPIO.OUT)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(8,GPIO.OUT)
        GPIO.setup(9,GPIO.OUT)
        GPIO.setup(10,GPIO.OUT)
        GPIO.setup(11,GPIO.OUT)
        
    def forward(self):
        GPIO.output(8,GPIO.HIGH)#left 1(0)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)#left 2(1)
        GPIO.output(7,GPIO.HIGH)

        GPIO.output(10,GPIO.LOW)#right 1(2)
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)#right 2(3)
        GPIO.output(5,GPIO.LOW)
    
    def backup(self):
        GPIO.output(8,GPIO.LOW)#left 1(0)
        GPIO.output(9,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)#left 2(1)
        GPIO.output(7,GPIO.LOW)

        GPIO.output(10,GPIO.HIGH)#right 1(2)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)#right 2(3)
        GPIO.output(5,GPIO.HIGH)
        
    def left(self):
        GPIO.output(8,GPIO.LOW)#left 1(0)
        GPIO.output(9,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)#left 2(1)
        GPIO.output(7,GPIO.HIGH)

        GPIO.output(10,GPIO.LOW)#right 1(2)
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)#right 2(3)
        GPIO.output(5,GPIO.HIGH)
        
    def l_rotate(self):
        GPIO.output(8,GPIO.LOW)#left 1(0)
        GPIO.output(9,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)#left 2(1)
        GPIO.output(7,GPIO.LOW)

        GPIO.output(10,GPIO.LOW)#right 1(2)
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)#right 2(3)
        GPIO.output(5,GPIO.LOW)
    
    def right(self):
        GPIO.output(8,GPIO.HIGH)#left 1(0)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)#left 2(1)
        GPIO.output(7,GPIO.LOW)

        GPIO.output(10,GPIO.HIGH)#right 1(2)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)#right 2(3)
        GPIO.output(5,GPIO.LOW)
        
    def r_rotate(self):
        GPIO.output(8,GPIO.HIGH)#left 1(0)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)#left 2(1)
        GPIO.output(7,GPIO.HIGH)

        GPIO.output(10,GPIO.HIGH)#right 1(2)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)#right 2(3)
        GPIO.output(5,GPIO.HIGH)
    
    def stop(self):
        GPIO.output(8,GPIO.LOW)#left 1(0)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)#left 2(1)
        GPIO.output(7,GPIO.LOW)

        GPIO.output(10,GPIO.LOW)#right 1(2)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)#right 2(3)
        GPIO.output(5,GPIO.LOW)