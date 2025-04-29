import time
from ltr559 import LTR559
from bme280 import BME280
from smbus2 import SMBus
from grow.moisture import Moisture
from database_actions import DatabaseActions



class ReadSensors:

    def read_sensor(sensor, do_write:bool):
        bus = SMBus(1)
        bme280 = BME280(i2c_dev=bus)


        if sensor == "temprature" and do_write:
            temprature = bme280.get_temperature()
            DatabaseActions.database_write("bme280_temprature="+str(temprature))
            return temprature
        elif sensor == "temprature":
            temprature = bme280.get_temperature()
            return temprature
        
        if sensor == "pressure" and do_write:
            pressure = bme280.get_pressure()
            DatabaseActions.database_write("bme280_pressure="+str(pressure))
            return pressure
        elif sensor == "pressure":
            pressure = bme280.get_pressure()
            return pressure
        
        if sensor == "humidity" and do_write:
            humidity = bme280.get_humidity()
            DatabaseActions.database_write("bme280_humidity="+str(humidity))
            return humidity
        elif sensor == "humidity":
            humidity = bme280.get_humidity()
            return humidity

        if sensor == "light" and do_write:
            ltr559 = LTR559()
            ltr559.update_sensor()
            lux = ltr559.get_lux()
            DatabaseActions.database_write("ltr559_lux="+str(lux))
            return lux
        elif sensor == "light":
            ltr559 = LTR559()
            ltr559.update_sensor()
            lux = ltr559.get_lux()
            return lux
        
        if sensor == "moisture1" and do_write:
            moisture_sensor1 = Moisture(1)
            DatabaseActions.database_write("moisture_sensor_1="+str(moisture_sensor1.moisture))
            return moisture_sensor1.moisture
        elif sensor == "moisture1":
            moisture_sensor1 = Moisture(1)
            return moisture_sensor1.moisture
        
        if sensor == "moisture2" and do_write:
            moisture_sensor2 = Moisture(2)
            DatabaseActions.database_write("moisture_sensor_2="+str(moisture_sensor2.moisture))
            return moisture_sensor2.moisture
        elif sensor == "moisture2":
            moisture_sensor2 = Moisture(2)
            return moisture_sensor2.moisture
        
        if sensor == "moisture3" and do_write:
            moisture_sensor3 = Moisture(3)
            DatabaseActions.database_write("moisture_sensor_3="+str(moisture_sensor3.moisture))
            return moisture_sensor3.moisture
        elif sensor == "moisture3":
            moisture_sensor3 = Moisture(3)
            return moisture_sensor3.moisture
        



    def read_all(do_write:bool):
        bus = SMBus(1)
        bme280 = BME280(i2c_dev=bus)
        ltr559 = LTR559()
        ltr559.update_sensor()
        moisture_sensor1 = Moisture(1)
        moisture_sensor2 = Moisture(2)
        moisture_sensor3 = Moisture(3)

        sensor_data = {
                "temprature":str(bme280.get_temperature()),
                "pressure":str(bme280.get_pressure()),
                "humidity":str(bme280.get_humidity()),
                "lux":str(ltr559.get_lux()),
                "moisture_sensor1":str(moisture_sensor1.moisture),
                "moisture_sensor2":str(moisture_sensor2.moisture),
                "moisture_sensor3":str(moisture_sensor3.moisture)
            }
        
        if do_write:
            data= "bme280_temprature="+str(bme280.get_temperature())+ \
                ",bme280_pressure="+str(bme280.get_pressure())+ \
                ",bme280_humidity="+str(bme280.get_humidity())+ \
                ",ltr559_lux="+str(ltr559.get_lux())+ \
                ",moisture_sensor_1="+str(moisture_sensor1.moisture)+ \
                ",moisture_sensor_2="+str(moisture_sensor2.moisture)+ \
                ",moisture_sensor_3="+str(moisture_sensor3.moisture)
            
            DatabaseActions.database_write(data)

            return sensor_data 
        
        else:
            return sensor_data

    