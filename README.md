# SmartGarden
Smart automation for monitoring and assisting with the growth of plants. Using the Grow Hat mini from Pimoroni, but re-writing to better suit a more intense monitoring setup. 

Hardware:
* Raspberry Pi Zero 2 W
https://shop.pimoroni.com/products/raspberry-pi-zero-2-w?variant=42101934587987

* Grow Hat mini - including moisture sensors. 
https://shop.pimoroni.com/products/grow?variant=32208365486163

* BME280 Breakout - Temprature, Pressure, Humidity Sensor.
https://shop.pimoroni.com/products/bme280-breakout?variant=29420960677971

## SensorTests
All code under the sensor tests has been written to check all the hardware is working correctly. A lot of that code has come from either the BME280 Library or the Grow Hat mini Library
* https://pypi.org/project/pimoroni-bme280/
* https://pypi.org/project/growhat/ 


## Plan:

* Run python scripts every X minutes to return sensor data. 
    * including an image of plants, using AI (Ollama Gemma3 12b) to return a predicted health status, plus other parameters. 
* Store Sensor data in influx database.
* build a web frontend to display the data. also potentially include a grafana dashboard. 


## Requirements.

* In order to successfully run an influxdb3 Core database is required to store the data. The connection details can entered via the Settings.yml file. 
* AI intergration is also a possibility, there is an integration built with Ollama API, the connection and model detail can be entered via the settings.yml file.