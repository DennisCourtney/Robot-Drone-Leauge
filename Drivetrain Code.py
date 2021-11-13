#Created by: STREAMWORKS
#PWM example using ServoKit library
from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit
pygame.init()



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
            
        
        leftstick = gamepad.get_axis(1)
        rightstick = gamepad.get_axis(4)
        

    
        pwm.continuous_servo[0].throttle = leftstick
        pwm.continuous_servo[7].throttle = rightstick
               
        print("rightstick: ", rightstick)
        
        print("leftstick: ", leftstick)
        
        