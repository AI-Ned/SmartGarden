from auto_watering import AutoWater
from sensor_read import ReadSensors
from camera_service import CameraImage

import time


def main():
    while True:

        #No need to wait for the auto watering to complete. 
        AutoWater.need_water(1)
        ReadSensors.read_all(1)
        CameraImage.capture_image()
        time.sleep(300)

main()