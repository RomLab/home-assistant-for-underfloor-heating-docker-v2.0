import hassapi as hass
import sys
import sqlite3
from sqlite3 import Error
import csv
from linearaprroximation import LinearAprroximation

class DATABASE(hass.Hass):
    def initialize(self):
        self.listen_state(self.trigger, "sensor.current_weekday", new = "Monday")
        #self.listen_state(self.trigger, "input_boolean.manual_winter_mode")

    def trigger(self, entity, attribute, old, new, kwargs):  
        
        aprroximation = LinearAprroximation()

        slopeFirstFloor = [
            "input_number.first_floor_corridor_and_toilet_slope", 
            "input_number.first_floor_bathroom_slope", 
            "input_number.first_floor_living_room_and_kitchen_slope", 
            "input_number.first_floor_cellar_slope",
            "input_number.first_floor_garage_slope"]
        interceptFirstFloor = [
            "input_number.first_floor_corridor_and_toilet_intercept",
            "input_number.first_floor_bathroom_intercept", 
            "input_number.first_floor_living_room_and_kitchen_intercept",
            "input_number.first_floor_cellar_intercept", 
            "input_number.first_floor_garage_intercept"]
        heaterFristFloor = [
            "input_boolean.zone_first_floor_corridor_and_toilet", 
            "input_boolean.zone_first_floor_bathroom", 
            "input_boolean.zone_first_floor_living_room_and_kitchen", 
            "input_boolean.zone_first_floor_cellar", 
            "input_boolean.zone_first_floor_garage"]
        sensorFirstFloor = [
            "sensor.first_floor_corridor_and_toilet_temp",
            "sensor.first_floor_bathroom_temp", 
            "sensor.first_floor_living_room_and_kitchen_temp", 
            "sensor.first_floor_cellar_temp",
            "sensor.first_floor_garage_temp"]

        outdoorSensor = "sensor.outdoor"

        self.createCSVFromDatabase(outdoorSensor, str(outdoorSensor)+".csv")
        
        for index, value in enumerate(slopeFirstFloor):
            self.createCSVFromDatabase(heaterFristFloor[index], "heater/first_floor/"+str(heaterFristFloor[index])+".csv")
            self.createCSVFromDatabase(sensorFirstFloor[index], "temperature_inside/first_floor/"+str(sensorFirstFloor[index])+".csv")
            slope, intercept = aprroximation.create_line("first_floor", heaterFristFloor[index], sensorFirstFloor[index])
            if(slope != None and intercept != None):
                self.set_state(slopeFirstFloor[index],  state = slope)
                self.set_state(interceptFirstFloor[index],  state = intercept)
            else:
                self.log("Problem with slope or intercept for first floor.")

        slopeSecondFloor = [
        "input_number.second_floor_bathroom_slope", 
        "input_number.second_floor_kitchen_workroom_living_and_diving_room_slope", 
        "input_number.second_floor_thomas_bedroom_slope", 
        "input_number.second_floor_north_room_slope", 
        "input_number.second_floor_middle_room_slope", 
        "input_number.second_floor_corner_room_slope", 
        "input_number.second_floor_corridor_and_toilet_room_slope", 
        "input_number.second_floor_parents_bedroom_slope"]

        interceptSecondFloor = [
            "input_number.second_floor_bathroom_intercept", 
            "input_number.second_floor_kitchen_workroom_living_and_diving_room_intercept", 
            "input_number.second_floor_thomas_bedroom_intercept", 
            "input_number.second_floor_north_room_intercept", 
            "input_number.second_floor_middle_room_intercept", 
            "input_number.second_floor_corner_room_intercept", 
            "input_number.second_floor_corridor_and_toilet_room_intercept", 
            "input_number.second_floor_parents_bedroom_intercept"]
        
        heaterSecondFloor = [
            "input_boolean.zone_second_floor_bathroom",
            "input_boolean.zone_second_floor_kitchen_workroom_living_and_diving_room",
            "input_boolean.zone_second_floor_thomas_bedroom",
            "input_boolean.zone_second_floor_north_room",
            "input_boolean.zone_second_floor_middle_room",
            "input_boolean.zone_second_floor_corner_room",
            "input_boolean.zone_second_floor_corridor_and_toilet",
            "input_boolean.zone_second_floor_parents_bedroom"]
        
        sensorSecondFloor = [
            "sensor.second_floor_bathroom_temp",
            "sensor.second_floor_kitchen_workroom_living_and_diving_room_temp",
            "sensor.second_floor_thomas_bedroom_temp",
            "sensor.second_floor_north_room_temp",
            "sensor.second_floor_middle_room_temp",
            "sensor.second_floor_corner_room_temp",
            "sensor.second_floor_corridor_and_toilet_temp",
            "sensor.second_floor_parents_bedroom_temp"]

        for index, value in enumerate(slopeSecondFloor):
            self.createCSVFromDatabase(heaterSecondFloor[index], "heater/second_floor/"+str(heaterSecondFloor[index])+".csv")
            self.createCSVFromDatabase(sensorSecondFloor[index], "temperature_inside/second_floor/"+str(sensorSecondFloor[index])+".csv")
            slope, intercept = aprroximation.create_line("second_floor", heaterSecondFloor[index], sensorSecondFloor[index])
            if(slope != None and intercept != None):
                self.set_state(slopeSecondFloor[index],  state = slope)
                self.set_state(interceptSecondFloor[index],  state = intercept)
            else:
                self.log("Problem with slope or intercept for second floor.")
     

        
    def createCSVFromDatabase(self, entity, path):
        db_file = "/home/homeassistant/.homeassistant/home-assistant_v2.db"
        connection = None
        cursor = None
        try:
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()
            cursor.execute("SELECT last_updated, state from states WHERE entity_id="+"'"+str(entity)+"' ORDER BY last_updated ASC")
            with open("home/appdaemon/.appdaemon/conf/apps/data/"+str(path), 'w') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_writer.writerows(cursor)
        except Error as e:
            self.log("Error while connecting to PostgreSQL" + e)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                #self.log("SQLITE connection is closed.")



       