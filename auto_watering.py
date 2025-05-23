import yaml
import time
from grow.pump import Pump
from sensor_read import ReadSensors
from database_actions import DatabaseActions

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


water_amount = {1:0,2:0,3:0}

class AutoWater:


    #automatically water each plant if the plant requires water. 
    def need_water(do_write:bool):

        moist_sensor = [ReadSensors.read_sensor("moisture1",0),ReadSensors.read_sensor("moisture2",0),ReadSensors.read_sensor("moisture3",0)]

        i=0
        p=0
        #When the moisture level reaches the DRY_POINT iterate through each pump, pumping 10ml of water until the WET_POINT is reached.
        for x in moist_sensor:
            i+=1
            if x >= DRY_POINT:
                while x >= WET_POINT:
     
                    print(f"Sensor "+str(i)+" moisture content = "+str(x))
                    pumps[p].dose(DOSE_SPEED, DOSE_TIME+PUMP_SETTINGS["pump"+str(i)+"_fine_calibration"])
                    water_amount[i] += 1
                    time.sleep(2)
                    x = ReadSensors.read_sensor("moisture"+str(i),0)
                    print(x)
                else:
                    print(f"Sensor "+str(i)+" moisture content = "+str(x)+" Done Watering!")
            else : 
                print(f"Sensor "+str(i)+" moisture content = "+str(x)+" Don't Water!")
            p+=1

        if do_write:
            if water_amount[1] + water_amount[2] + water_amount[3] > 0: 
                data = "Planter_1="+str(water_amount[1])+ \
                ",Planter_2="+str(water_amount[2])+ \
                ",planter_3="+str(water_amount[3])
            
                DatabaseActions.database_write("watering","liquid=water",data)
        water_amount[1] = 0
        water_amount[2] = 0
        water_amount[3] = 0
        #return the amount of water each plant was provided during the watering cycle. 
        return water_amount
    
    
