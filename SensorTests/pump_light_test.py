import time
# library https://github.com/pimoroni/ltr559-python/tree/main
from ltr559 import LTR559
from grow.pump import Pump

# pumps attached?
pump_channel = [1,2,3]


dose_speed = 0.6  # Pump speed for water dose
dose_time = 10.0  # Time (in seconds) for water dose

def pumping(lux):
    print("Lux: {:06.2f}").format(lux)
    if lux > 1000:
        print("WE HAVE LIGHT!")
        for i in pump_channel:
            #sets which pump is to be ran
            p = Pump(i)
            #set the speed and time the pump runs at.
            p.dose(dose_speed, dose_time)
    else:
        print("Not enough Light")

while True:
    #Perform a read of the lux an proximity sensors.
    ltr559.update_sensor()

    #retrieve the lux reading.
    lux = ltr559.get_lux()
    pumping(lux)
    time.sleep(0.05)
