import requests
import yaml
import os
import re

with open('./settings.yml', 'r') as f:
    settings = yaml.load(f, Loader=yaml.SafeLoader)
DB_SETTINGS = settings.get("Influxdatabase")
DB_NAME = DB_SETTINGS["db_name"]
DB_HOST = DB_SETTINGS["db_host"]
DB_TOKEN = DB_SETTINGS["db_token"]

class DatabaseActions:

    # Check the Yaml file for an environment Variable, then check that environment variable exists. 
    def get_authentication_token(token):
        pattern = re.compile('.*?\${(\w+)}')
        if pattern.match(token):
            token_variable = token[2:-1]
            if token_variable in os.environ:
                return os.environ.get(token_variable)
            else:
                print("There is no Environment Variable that matches "+ token_variable)
        else:
            print("No environment variable provided!")

    #build the API URL based on the task PUT, POST, GET etc 
    def build_url(action,database,**kwargs):
        sql == ""

        for name, value in kwargs.items():
            if name == "SQL":
                sql = value
            else:
                continue

        if action == "POST":
            url = DB_HOST+"/api/v3/write_lp?db="+database+"&precision=nanosecond&accept_partial=true&no_sync=true"
            return url
        
        elif action == "GET":
             url = DB_HOST+"/api/v3/query_sql?db="+database+"&q="+sql
             return url

    #Write to the database. 
    def database_write(data):
        connect = DatabaseActions.build_url("POST",DB_NAME)
        headers =  {"Authorization": "Bearer "+ DatabaseActions.get_authentication_token(DB_TOKEN)}
        data_write = "SmartGardenData sensor_1=BME280,sensor_2=LTR559,sensor_3=GrowMoistureSensor "+data
        requests.post(connect, data=data_write, headers=headers)