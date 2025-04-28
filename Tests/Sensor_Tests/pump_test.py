import RPi.GPIO as GPIO
from grow.pump import Pump
import time

#pumps numbers
pump_channel = [1,2,3]

# settings that are roughly 100ml per pump: speed = 0.6, time = 10
dose_speed = 0.8  # Pump speed for water dose
dose_time = 2.2  # Time (in seconds) for water dose


def pumping():
    time.sleep(5)
    for i in pump_channel:
        #sets which pump is to be ran
        p = Pump(i)
        #set the speed and time the pump runs at.
        p.dose(dose_speed, dose_time)

pumping()
