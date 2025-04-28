import RPi.GPIO as GPIO
import yaml
import time
from grow.pump import Pump
from grow.moisture import Moisture
from SensorRead import ReadSensors


moist_sensor1 = Moisture(1)
moist_sensor2 = Moisture(2)
moist_sensor3 = Moisture(3)
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

    print(f"Sensor 1 moisture content = {moist_sensor1.moisture}")
    if moist_sensor1.moisture > WET_POINT:
        pump1.dose(DOSE_SPEED, DOSE_TIME+0.4)
        time.sleep(5.0)

    print(f"Sensor 2 moisture content = {moist_sensor2.moisture}")
    if moist_sensor2.moisture > WET_POINT:
        pump2.dose(DOSE_SPEED, DOSE_TIME)
        time.sleep(5.0)

    print(f"Sensor 3 moisture content = {moist_sensor3.moisture}")
    if moist_sensor3.moisture > WET_POINT:
        pump3.dose(DOSE_SPEED, DOSE_TIME+0.6)
        time.sleep(5.0)

    return


while True:
    need_water()
    ReadSensors.read_all(1)
    time.sleep(60)
