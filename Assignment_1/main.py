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
wheel_radius = 3 / 100
motor = Motor(Port.A)


# My first project yay!!!!!!!!!!!!!

def move(cm, time):
    velocity = cm / time
    angular_velocity = velocity / wheel_radius

    print("Velocity: " + str(velocity))
    print("Angular Velocity: "+ str(angular_velocity))
    print("Cenitmeters: " + str(angular_velocity*wheel_radius*time*1000))

    motor.run_time(angular_velocity,time*1000, Stop.BRAKE) # time is references in milliseconds 

    # This currently is not accurate becuase the motor must accelerate to the angular velocity
    # but the function claims to deselerate at the correct time to reach stand still 
    # at specified time




# Movement Code

move(10,5)