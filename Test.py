import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT) #Gelb
gpio.setup(12,gpio.OUT) #Grün
gpio.setup(37,gpio.OUT) #Rot

gpio.setup(13,gpio.OUT) #Fuß_Grün
gpio.setup(15,gpio.OUT) #Fuß_Rot

gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_UP)
i = 0

gpio.output(12,gpio.HIGH) # Grün an
gpio.output(15,gpio.HIGH) #Fuß_rot an

while i < 3:
    if gpio.input(5) == gpio.LOW: # Taster gedrückt
        i += 1
        time.sleep(3)
        
        gpio.output(12, gpio.LOW)  #Grün aus
        gpio.output(11, gpio.HIGH) #Gelb an
        time.sleep(1)
        
        gpio.output(11, gpio.LOW)  #Gelb aus
        gpio.output(37, gpio.HIGH) #Rot an
        time.sleep(1)
        
        gpio.output(15, gpio.LOW)  #Fuß_rot aus
        gpio.output(13, gpio.HIGH) #Fuß_grün an
        time.sleep(5)
        
        gpio.output(13, gpio.LOW)  #Fuß_grün aus
        gpio.output(15, gpio.HIGH) #Fuß_rot an
        time.sleep(1)
        
        gpio.output(11, gpio.HIGH) #Gelb an
        time.sleep(1)
        
        gpio.output(37, gpio.LOW)  #Rot aus
        gpio.output(11, gpio.LOW)  #Gelb aus
        gpio.output(12, gpio.HIGH) #Grün an
        time.sleep(0.1)
gpio.cleanup()

