from picamera import PiCamera
from datetime import datetime
from io import BytesIO
from database_actions import DatabaseActions
import os
import yaml
import zlib


class CameraImage:
    
    def capture_image():
        with open('./settings.yml', 'r') as f:
            settings = yaml.load(f, Loader=yaml.SafeLoader)
        IMAGE_SETTINGS = settings.get("ImageSettings")
        
        IMAGE_NAME = IMAGE_SETTINGS["image_name"]
        FILE_TYPE = IMAGE_SETTINGS["file_type"]
        DIRECTORY = IMAGE_SETTINGS["save_directory"]
        COMPRESS = IMAGE_SETTINGS["compress_image"]
               
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        pi_cam = PiCamera()
        pi_cam.resolution = (640, 480)
        filename = str(IMAGE_NAME+current_datetime+"."+FILE_TYPE)
        stream = BytesIO()
       
        try:
            pi_cam.capture(stream, "jpeg")
            stream.seek(0)
            write_image = stream.read()
 
            if COMPRESS:
                compressor = zlib.compressobj(level=9,method=zlib.DEFLATED, wbits=zlib.MAX_WBITS,memLevel=9,strategy=zlib.Z_DEFAULT_STRATEGY)
                filename = str(IMAGE_NAME+current_datetime)
                with open(os.path.join(DIRECTORY, filename), "wb") as file:
                    file.write(compressor.compress(write_image))
            else:
                filename = str(IMAGE_NAME+current_datetime+"."+FILE_TYPE)
                with open(os.path.join(DIRECTORY, filename), "wb") as file:
                    file.write(write_image)

        finally:
            pi_cam.close()
            stream.flush()
            

CameraImage.capture_image()
