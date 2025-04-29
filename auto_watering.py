import RPi.GPIO as GPIO # type: ignore
import yaml
import time
from grow.pump import Pump
from SensorRead import ReadSensors


pump1 = Pump(1)
pump2 = Pump(2)
pump3 = Pump(3)


with open('./settings.yml', 'r') as f:
    settings = yaml.load(f, Loader=yaml.SafeLoader)
PUMP_SETTINGS = settings.get("Pump")
MOISTURE_SETTINGS = settings.get("Moisture")

# Retrieve the pump settings
DOSE_SPEED = PUMP_SETTINGS["dose_speed"]  
DOSE_TIME = PUMP_SETTINGS["dose_time"] 

DRY_POINT = MOISTURE_SETTINGS["dry_point"]
WET_POINT = MOISTURE_SETTINGS["wet_point"]

def need_water():

    moist_sensor1 = ReadSensors.read_sensor("moisture1",0)
    moist_sensor2 = ReadSensors.read_sensor("moisture2",0)
    moist_sensor3 = ReadSensors.read_sensor("moisture3",0)

    print(f"Sensor 1 moisture content = {moist_sensor1}")
    if moist_sensor1 > WET_POINT:
        pump1.dose(DOSE_SPEED, DOSE_TIME+0.4)
        time.sleep(5.0)

    print(f"Sensor 2 moisture content = {moist_sensor2}")
    if moist_sensor2 > WET_POINT:
        pump2.dose(DOSE_SPEED, DOSE_TIME)
        time.sleep(5.0)

    print(f"Sensor 3 moisture content = {moist_sensor3}")
    if moist_sensor3 > WET_POINT:
        pump3.dose(DOSE_SPEED, DOSE_TIME+0.6)
        time.sleep(5.0)



while True:
    try:
        need_water()
        time.sleep(2)
    finally:
        GPIO.cleanup()

    try:
        ReadSensors.read_all(1)
        time.sleep(10)
    finally:
        GPIO.cleanup()
    
    GPIO.setmode(GPIO.BCM)
