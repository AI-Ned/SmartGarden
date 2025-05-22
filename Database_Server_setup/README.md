# Database Installation
All files within the Database_server_setup are dedicated to setting up the influxdatabase.
All the steps outlined are the originally taken from the Getting Started Guide on the influxdb3 documentation. 
https://docs.influxdata.com/influxdb3/core/get-started/

There is some manual editing of the files in this section. This may change if I decide to build an installer. 

Steps to setup
* Install the Influxdb3 Core database to do this I ran the following command, the reason for running this as root will allow for the database to start through an be monitored through a service. ```sudo curl -O https://www.influxdata.com/d/install_influxdb3.sh && sh install_influxdb3.sh```
* During the installation a few options are presented, the following option were selected for the development of this project.
** Select Installation type = Simple Download (2)
** Configure Options = y
** NodeID = node0 (Pressing enter with blank value sets default)
** Select Your Storage Solution = File Storage (2)
** Enter Storage path= default (Left blank)

* Modify the database_start.sh script, specifically the user path /home/user/.influxdb/influxdb3. replace user with the username of the install location. 
* create admin token for database authentication. Running the following will generate the api token ```influxdb3 create token --admin```
* This token will need to be saved as an environment variable on the raspberry pi running the growhat mini, and then the setting.yml updated to match the environment token name.
* copy the database_start.service file into the /etc/systemd/system. This require Sudo permissions.
* Update the directory path in the database_start.service file ```ExecStart=/home/user/database_start.sh``` to match the directory path of the database_start.sh file.
* Run ```sudo systemctl enable database_start.service``` to enable the service.
* Run ```sudo systemctl start database_start.service``` to start the service. Its possible that this might not start the service, in this case restart the server. 
* Finally run ```sudo systemctl status database_start.service``` to check the service is running and get a snippet of the most recent logs. 
