import hassapi as hass
import os
import re
from glob import glob
import time
import datetime
from datetime import timedelta

class TEMPERATURESENSORS(hass.Hass):

    def initialize(self):
        interval_of_reading = 30
        start_time = self.datetime() + datetime.timedelta(seconds = 1)
        self.handle = self.run_every(self.read_and_set_temp, start_time, interval_of_reading)

    def read_and_set_temp(self, kwargs): 
        # DS18B20
        hot_water_tank_top_temperature = self.read_temp("28-00000c859e14", "w1_bus_master1")
        time.sleep(2)
        hot_water_tank_middle_temperature = self.read_temp("28-00000c85a5bc", "w1_bus_master2")
        time.sleep(2)
        hot_water_tank_bottom_temperature = self.read_temp("28-00000c864409", "w1_bus_master3")
        time.sleep(2)
        # outdoor_temperature = self.read_temp("28-00000c85a20f", "w1_bus_master4")
        time.sleep(2)

        # MAX31850K
        fireplace_cellar_temperature = self.read_temp("3b-4c74109d6361", "w1_bus_master5")
        time.sleep(2)
        fireplace_first_floor_temperature = self.read_temp("3b-4c74109d636d", "w1_bus_master6")
        time.sleep(2)
        fireplace_second_floor_temperature = self.read_temp("3b-4c74109d6349", "w1_bus_master7")
        time.sleep(2)

        # DS18B20
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

        # MAX31850K
        states_fireplace_cellar = self.get_state("sensor.fireplace_cellar", attribute='all')
        attributes_fireplace_cellar = states_fireplace_cellar['attributes']
        self.set_state("sensor.fireplace_cellar", state = fireplace_cellar_temperature, attributes = attributes_fireplace_cellar)

        states_fireplace_first_floor = self.get_state("sensor.fireplace_first_floor", attribute='all')
        attributes_fireplace_first_floor = states_fireplace_first_floor['attributes']
        self.set_state("sensor.fireplace_first_floor", state = fireplace_first_floor_temperature, attributes = attributes_fireplace_first_floor)
        
        states_fireplace_second_floor = self.get_state("sensor.fireplace_second_floor", attribute='all')
        attributes_fireplace_second_floor = states_fireplace_second_floor['attributes']
        self.set_state("sensor.fireplace_second_floor",  state = fireplace_second_floor_temperature, attributes = attributes_fireplace_second_floor)

    # Function that reads and returns the raw content of 'w1_slave' file
    def read_temp_raw(self, deviceCode, masterCode):
        w1DeviceFolder = '/sys/bus/w1/devices'
        f = open(w1DeviceFolder + '/' + masterCode + '/' + deviceCode + '/w1_slave' , 'r')
        lines = f.readlines()
        f.close()
        return lines

    # Function that reads the temperature from raw file content
    def read_temp(self, deviceCode, masterCode):
        # Read the raw temperature data
        lines = self.read_temp_raw(deviceCode, masterCode)
        # Wait until the data is valid - end of the first line reads 'YES'
        while lines[0].strip()[-3:] != 'YES':
            #time.sleep(0.2)
            time.sleep(2)
            lines = self.read_temp_raw(deviceCode, masterCode)
        # Read the temperature, that is on the second line
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            # Convert the temperature number to Celsius
            temp_c = float(temp_string) / 1000.0
            # Return formatted sensor data, round to 1 decimal number
            return  round(temp_c, 1)
