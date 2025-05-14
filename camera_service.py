from picamera import PiCamera
from datetime import datetime
from io import BytesIO
import base64
import yaml
from database_actions import DatabaseActions


class CameraImage:
    
    def capture_image():
        with open('./settings.yml', 'r') as f:
            settings = yaml.load(f, Loader=yaml.SafeLoader)
        IMAGE_SETTINGS = settings.get("ImageSettings")
        
        IMAGE_NAME = IMAGE_SETTINGS["image_name"]
        FILE_TYPE = IMAGE_SETTINGS["file_type"]
               
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        pi_cam = PiCamera()
        pi_cam.resolution = (640, 480)
        filename = str('"'+IMAGE_NAME+current_datetime+"."+FILE_TYPE+'"')
        stream = BytesIO()

        try:
            pi_cam.capture(stream, "jpeg")
            stream.seek(0)
            encoded_image = base64.b64encode(stream.read())
            data = "image_name="+filename+",image="+str(encoded_image)
            #print(str(encoded_image) + "rewinded")
            DatabaseActions.database_write("images","camera=PiZeroStandardCamera",data)
        finally:
            pi_cam.close() 
            stream.flush()
            

CameraImage.capture_image()
