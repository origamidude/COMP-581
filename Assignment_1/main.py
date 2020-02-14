#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

brick.sound.beep()

# Global Variables for Jarvis

pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286 
radius = 2.8 / 100
diameter = 2 * pi * radius 
max_speed = 300
max_acceleration = 500


motor = Motor(Port.A)

# set max speed and max acceleration for motor for all motor calls
motor.set_run_settings(max_speed, max_acceleration)

# My first project yay!!!!!!!!!!!!!

def move(distance, velocity):
    angle = distance * 360 /diameter
    angular_velocity = velocity / radius 
    motor.run_target(angular_velocity, angle) # time is references in milliseconds 

    # 


# Movement Code

move(0.3 0,10)