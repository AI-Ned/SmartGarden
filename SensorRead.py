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
            DatabaseActions.database_write("bme280_temprature="+str(bme280.get_temperature()))
            return bme280.get_temperature()
        elif sensor == "temprature":
            return bme280.get_temperature()
        
        
        if sensor == "pressure" and do_write:
            DatabaseActions.database_write("bme280_pressure="+str(bme280.get_pressure()))
            return bme280.get_pressure()
        elif sensor == "pressure":
            return bme280.get_pressure()
        
        if sensor == "humidity" and do_write:
            DatabaseActions.database_write("bme280_humidity="+str(bme280.get_humidity()))
            return bme280.get_humidity()
        elif sensor == "humidity":
            return bme280.get_humidity()

        if sensor == "light" and do_write:
            ltr559 = LTR559()
            ltr559.update_sensor()
            DatabaseActions.database_write("ltr559_lux="+str(ltr559.get_lux()))
            return ltr559.get_lux()
        elif sensor == "light":
            return ltr559.get_lux()
        
        if sensor == "moisture1" and do_write:
            DatabaseActions.database_write("moisture_sensor_1="+str(Moisture(1).moisture))
            return Moisture(1).moisture
        elif sensor == "moisture1":
            return Moisture(1).moisture
        
        if sensor == "moisture2" and do_write:
            DatabaseActions.database_write("moisture_sensor_2="+str(Moisture(2).moisture))
            return Moisture(2).moisture
        elif sensor == "moisture2":
            return Moisture(2).moisture
        
        if sensor == "moisture3" and do_write:
            DatabaseActions.database_write("moisture_sensor_3="+str(Moisture(3).moisture))
            return Moisture(3).moisture
        elif sensor == "moisture3":
            return Moisture(3).moisture


    def read_all(do_write:bool):
        bus = SMBus(1)
        bme280 = BME280(i2c_dev=bus)
        ltr559 = LTR559()
        ltr559.update_sensor()

        sensor_data = {
                "temprature":str(bme280.get_temperature()),
                "pressure":str(bme280.get_pressure()),
                "humidity":str(bme280.get_humidity()),
                "lux":str(ltr559.get_lux()),
                "moisture_sensor1":str(Moisture(1).moisture),
                "moisture_sensor2":str(Moisture(2).moisture),
                "moisture_sensor3":str(Moisture(3).moisture)
            }
        
        if do_write:
            data= "bme280_temprature="+str(bme280.get_temperature())+ \
                ",bme280_pressure="+str(bme280.get_pressure())+ \
                ",bme280_humidity="+str(bme280.get_humidity())+ \
                ",ltr559_lux="+str(ltr559.get_lux())+ \
                ",moisture_sensor_1="+str(Moisture(1).moisture)+ \
                ",moisture_sensor_2="+str(Moisture(2).moisture)+ \
                ",moisture_sensor_3="+str(Moisture(3).moisture)
            
            DatabaseActions.database_write(data)

            return sensor_data 
        
        else:
            return sensor_data

    