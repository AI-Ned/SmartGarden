import yaml
import time
from grow.pump import Pump
from SensorRead import ReadSensors

pump1 = Pump(1)
pump2 = Pump(2)
pump3 = Pump(3)
pumps = [pump1,pump2,pump3]

with open('./settings.yml', 'r') as f:
    settings = yaml.load(f, Loader=yaml.SafeLoader)
PUMP_SETTINGS = settings.get("Pump")
MOISTURE_SETTINGS = settings.get("Moisture")

# Retrieve the pump settings
DOSE_SPEED = PUMP_SETTINGS["dose_speed"]  
DOSE_TIME = PUMP_SETTINGS["dose_time"] 

DRY_POINT = MOISTURE_SETTINGS["dry_point"]
WET_POINT = MOISTURE_SETTINGS["wet_point"]

watering = {1:bool,2:bool,3:bool}
water_amount = {1:0,2:0,3:0}

#automatically water each plant if the plant requires water. 
def need_water():

    moist_sensor = [ReadSensors.read_sensor("moisture1",0),ReadSensors.read_sensor("moisture2",0),ReadSensors.read_sensor("moisture3",0)]

    i=0
    pump=0
    #When the moisture level reaches the DRY_POINT iterate through each pump, pumping 10ml of water until the WET_POINT is reached.
    for x in moist_sensor:
        i+=1
        if x >= DRY_POINT or watering[i] == 1:
            if x >= WET_POINT:
                watering[i] = 1
                print(f"Sensor "+str(i)+" moisture content = "+str(x))
                pumps[pump].dose(DOSE_SPEED, DOSE_TIME+PUMP_SETTINGS["pump"+str(i)+"_fine_calibration"])
                water_amount[i] += 10
            else:
                print(f"Sensor "+str(i)+" moisture content = "+str(x)+" Done Watering!")
                watering[i] = 0
        print(f"Sensor "+str(i)+" moisture content = "+str(x)+" Don't Water!")
        pump+=1
    
    #return the amount of water each plant was provided during the watering cycle. 
    return water_amount


while True:

        need_water()
        time.sleep(1)
        #ReadSensors.read_all(1)
        time.sleep(10)

    
    
