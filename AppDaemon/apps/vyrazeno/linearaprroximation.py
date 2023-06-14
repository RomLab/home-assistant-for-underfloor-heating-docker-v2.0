
import csv
import datetime
 
import pandas
import os
 
import numpy as np
import matplotlib.pyplot as plt

import os.path
from os import path

class LinearAprroximation():

    slope = None
    intercept = None
    def create_line(self, numberFloor, heater, sensor):  
        slope = None
        intercept = None
        insideData,outsideData,heaterData = self.read_data(numberFloor, heater, sensor)
        
        durations = []
        outside_temps = []
        inside_temps = []
       
        if len(heaterData) != 0:
            durations = self.find_heatup_durations(heaterData)

        if len(outsideData) != 0:
            outside_temps = self.find_temperatures_at_times(outsideData, durations)
        
        if len(insideData) != 0:
            inside_temps = self.find_temperatures_at_times(insideData, durations)
        
        if len(durations) != 0 and len(outside_temps) != 0 and len(inside_temps) != 0:
            try:
                self.analyze_heatups(durations, outside_temps, inside_temps, numberFloor, sensor)
            except:
                return self.slope, self.intercept
        
        return self.slope, self.intercept
    
    def read_data(self, numberFloor, heater, sensor):
        
        insideData = []
        outsideData = []
        heaterData = []
        
        pathTemperatureInside = '/home/appdaemon/.appdaemon/conf/apps/data/temperature_inside/'+numberFloor+'/'+sensor+'.csv'
        if path.exists(pathTemperatureInside):
            insideDataTemp = pandas.read_csv(pathTemperatureInside, parse_dates=[0],names=['Time','Temperature'],index_col=0)
            if self.isReplacedNanValue(insideDataTemp, "Temperature"):
                insideData = insideDataTemp
                #insideData.to_csv('/home/appdaemon/.appdaemon/conf/apps/inside_'+sensor+'.csv', encoding='utf-8')
                insideData = insideData[insideData.astype(float)>-1000] # filter crap readings
            else:
                insideData = []
        
        pathTemperatureOutside = '/home/appdaemon/.appdaemon/conf/apps/data/sensor.outdoor.csv'
        if path.exists(pathTemperatureOutside):
            outsideDataTemp = pandas.read_csv(pathTemperatureOutside, parse_dates=[0],names=['Time','Temperature'],index_col=0)
            if self.isReplacedNanValue(outsideDataTemp, "Temperature"):
                outsideData = outsideDataTemp
                #outsideData.to_csv('/home/appdaemon/.appdaemon/conf/apps/sensor.outdoor.csv', encoding='utf-8')
            else:
                outsideData = []
        
        pathHeater = '/home/appdaemon/.appdaemon/conf/apps/data/heater/'+numberFloor+'/'+heater+'.csv'
        if path.exists(pathHeater):
            heaterDatatemp = pandas.read_csv(pathHeater, parse_dates=[0],names=['Time','Status'],index_col=0)
            if self.isReplacedNanValue(heaterDatatemp, "Status"):
                heaterData = heaterDatatemp
                #heaterData.to_csv('/home/appdaemon/.appdaemon/conf/apps/'+heater+'.csv', encoding='utf-8')
            else:
                heaterData = []
        
        return insideData, outsideData, heaterData
    
    def isReplacedNanValue(self, values, header):
        maxSameValue = 0
        
        for time, df in values.iterrows():
            
            # Max same bad value in column
            if maxSameValue==5:
                return False
            
            if df[header]=="unavailable" or df[header]=="unknown" or df[header]=="":
                maxSameValue +=1
            else:
                maxSameValue = 0
        
        # Replace bad value to NaN
        values.replace(["unknown", "unavailable", ""], np.nan, inplace =True)
        # Replace NaN value to previous value
        values.fillna(method='ffill', inplace=True)
        # Replace NaN value to next value
        values.fillna(method='bfill', inplace=True)
        
        return True

    def find_heatup_durations(self, heater, status='off'):
        """Figure out how long the heater was on for each morning."""
        last_time = next(heater.iterrows())[0]
        heatup_durations = []
        for time, df in heater.iterrows():
            diff = time - last_time
            if df['Status']==status and diff > datetime.timedelta(hours=1):
                heatup_durations.append((last_time, diff)) # remember when it turned on too
            last_time = time
        return heatup_durations
    
    def find_temperatures_at_times(self, temperatures, times):
        """Find what the temperature was during the morning heatup."""
        blocks = []
        for start_time, duration in times:
            blocks.append((start_time, temperatures[start_time: start_time + duration]))
        return blocks
    
    def analyze_heatups(self, durations, outside_temps, inside_temps, numberFloor, sensor):
        """Look at the heatup dynamics and try to build a model."""
        initial_outside = np.array([o[1].values[0] for o in outside_temps], dtype=float)
        initial_inside = np.array([o[1].values[0] for o in inside_temps], dtype=float)
        durations_in_minutes = np.array([d[1].total_seconds() for d in durations])/60.0
        delta = (initial_inside-initial_outside)[:,0]
        print(delta)
        self.slope, self.intercept = np.polyfit(delta, durations_in_minutes,1)
 
        model_temp = np.linspace(min(delta), max(delta), 20)
        model_duration = self.slope * model_temp + self.intercept
   
        plt.figure()
        ax = plt.gca()
        #plt.plot(initial_outside, durations_in_seconds,'o')
        plt.plot(delta, durations_in_minutes,'o', label='Data')
        plt.plot(model_temp, model_duration,'-', label='Model')
        plt.text(0.2,0.1,'D = {:.1f} T + {:.1f}'.format(self.slope, self.intercept), transform = ax.transAxes)
        plt.xlabel('Initial delta Temperature (C)')
        plt.ylabel('Duration of heatup (min)')
        plt.title('Duration of heatups')
        #os.chmod('/home/appdaemon/.appdaemon/conf/apps/heatups.png', 0o400)
        plt.savefig('/home/appdaemon/.appdaemon/conf/apps/data/temperature_inside/'+numberFloor+'/'+sensor+'.png')