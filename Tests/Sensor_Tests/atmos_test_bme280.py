import time
from smbus2 import SMBus
from bme280 import BME280

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    altitude = bme280.get_altitude()
    print(f"{temperature:05.2f}°C {pressure:05.2f}hPa {humidity:05.2f}% {altitude:05.2f}ft")
    time.sleep(1)
