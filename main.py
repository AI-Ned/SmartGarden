from auto_watering import AutoWater
from sensor_read import ReadSensors

import time


async def main():
    while True:

        #No need to wait for the auto watering to complete. 
        AutoWater.need_water(1)
        ReadSensors.read_all(1)
        time.sleep(300)

main()