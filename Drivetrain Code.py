#Created by: STREAMWORKS
#PWM example using ServoKit library
from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit
pygame.init()

#ATTENTION: Text inside of a "#" are comments. This allows the author of the program to communicate with the reader.

pwm = ServoKit(channels=16)
leftstick = 0.07
rightstick = 0.07
print('Initialized')

gamepad = pygame.joystick.Joystick(0)
gamepad.init()


while True:

    
        pygame.event.get()
        
        if abs(gamepad.get_axis(1)) <= 0.1:
            leftstick = 0.07
            
        elif abs(gamepad.get_axis(4)) <= 0.1:
            rightstick = 0.07
            
       #For both of these axis values, you can get them from running the map_joystick.py program. 
       #Most controllers will automatically use axis 1 and axis 4 naturally for a tankdrive configuration.
        leftstick = gamepad.get_axis(1)
        rightstick = gamepad.get_axis(4)
        

    # The values [0] and [1] reference which channel on the servo bonnet the motor controller signal and ground wires go.

        pwm.continuous_servo[0].throttle = leftstick
        pwm.continuous_servo[1].throttle = rightstick
         
            
    # Print statements help us identify where to troubleshoot. These print statements show us the values
    # that are being output by the motors and the input of the joystick values.
    
        print("rightstick: ", rightstick)
        
        print("leftstick: ", leftstick)
        
        
