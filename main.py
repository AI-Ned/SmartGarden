from auto_watering import AutoWater
from sensor_read import ReadSensors
from camera_service import CameraImage
from datetime import datetime
import os 
import time
import yaml

with open('./settings.yml', 'r') as f:
    settings = yaml.load(f, Loader=yaml.SafeLoader)
IMAGE_SETTINGS = settings.get("ImageSettings")
IMAGE_TIMES = IMAGE_SETTINGS["image_times"]

FILE_SETTINGS = settings.get["FileStorage"]


def image_schedule():
    now = datetime.now()
    time = int(str(now.time())[:2]+str(now.time())[3:5])

    for t in IMAGE_TIMES:
        if int(t) <= int(time) <= int(t)+9:
            CameraImage.capture_image()
    return

def main():
    while True:

        ReadSensors.read_all(1),
        image_schedule(),
        AutoWater.need_water(1),
        time.sleep(300)

main()