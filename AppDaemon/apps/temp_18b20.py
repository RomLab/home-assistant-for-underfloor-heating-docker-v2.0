import hassapi as hass
import os
import re
from glob import glob
import time
import datetime
from datetime import timedelta

class TEMP18B20(hass.Hass):

    def initialize(self):
        interval_of_reading = 30
        start_time = self.datetime() + datetime.timedelta(seconds = 1)
        self.handle = self.run_every(self.read_and_set_temp, start_time, interval_of_reading)

    def read_and_set_temp(self, kwargs): 

        hot_water_tank_top_temperature = self.read_temp("28-00000c859e14")
        hot_water_tank_middle_temperature = self.read_temp("28-00000c85a5bc")
        hot_water_tank_bottom_temperature = self.read_temp("28-00000c864409")

        #outdoor_temperature = self.read_temp("28-00000c85a20f")

        states_hot_water_tank_top = self.get_state("sensor.hot_water_tank_top", attribute='all')
        attributes_hot_water_tank_top = states_hot_water_tank_top['attributes']
        self.set_state("sensor.hot_water_tank_top", state = hot_water_tank_top_temperature, attributes = attributes_hot_water_tank_top)

        states_hot_water_tank_middle = self.get_state("sensor.hot_water_tank_middle", attribute='all')
        attributes_hot_water_tank_middle = states_hot_water_tank_middle['attributes']
        self.set_state("sensor.hot_water_tank_middle", state = hot_water_tank_middle_temperature, attributes = attributes_hot_water_tank_middle)
        
        states_hot_water_tank_bottom = self.get_state("sensor.hot_water_tank_bottom", attribute='all')
        attributes_hot_water_tank_bottom = states_hot_water_tank_bottom['attributes']
        self.set_state("sensor.hot_water_tank_bottom",  state = hot_water_tank_bottom_temperature, attributes = attributes_hot_water_tank_bottom)

        #states_outdoor = self.get_state("sensor.outdoor", attribute='all')
        #attributes_outdoor = states_outdoor['attributes']
        #self.set_state("sensor.outdoor",  state = outdoor_temperature, attributes = attributes_outdoor)
    # Function that reads and returns the raw content of 'w1_slave' file
    def read_temp_raw(self, deviceCode):
        w1DeviceFolder = '/sys/bus/w1/devices'
        f = open(w1DeviceFolder + '/' + deviceCode + '/w1_slave' , 'r')
        lines = f.readlines()
        f.close()
        return lines

    # Function that reads the temperature from raw file content
    def read_temp(self, deviceCode):
        # Read the raw temperature data
        lines = self.read_temp_raw(deviceCode)
        # Wait until the data is valid - end of the first line reads 'YES'
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw(deviceCode)
        # Read the temperature, that is on the second line
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            # Convert the temperature number to Celsius
            temp_c = float(temp_string) / 1000.0
            # Return formatted sensor data, round to 1 decimal number
            return  round(temp_c, 1)
