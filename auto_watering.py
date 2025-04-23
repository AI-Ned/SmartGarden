import RPi.GPIO as GPIO
import time
from grow.pump import Pump
from grow.moisture import Moisture


moist_sensor1 = Moisture(1)
moist_sensor2 = Moisture(2)
moist_sensor3 = Moisture(3)
pump1 = Pump(1)
pump2 = Pump(2)
pump3 = Pump(3)

# settings that are roughly 10ml per pump: speed = 0.8, time = 2.2
dose_speed = 0.8  # Pump speed for water dose
dose_time = 2.2  # Time (in seconds) for water dose


dry_point = 15
wet_point = 8

def pump_run():
   for i in pump_channel:
        #sets which pump is to be ran
        p = Pump(i)
        #set the speed and time the pump runs at.
        p.dose(dose_speed, dose_time)

def need_water():

    print(f"Sensor 1 moisture content = {moist_sensor1.moisture}")
    if moist_sensor1.moisture > wet_point:
        pump1.dose(dose_speed, dose_time+0.4) # time adjuestment to ensure 10ml
        time.sleep(5.0)

    print(f"Sensor 2 moisture content = {moist_sensor2.moisture}")
    if moist_sensor2.moisture > wet_point:
        pump2.dose(dose_speed, dose_time)
        time.sleep(5.0)

    print(f"Sensor 3 moisture content = {moist_sensor3.moisture}")# time adjustment to ensure 10ml
    if moist_sensor3.moisture > wet_point:
        pump3.dose(dose_speed, dose_time+0.6)
        time.sleep(5.0)

    return


while True:
    need_water()
    time.sleep(30)
