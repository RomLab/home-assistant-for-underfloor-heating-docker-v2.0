import hassapi as hass
import time
import datetime

class TIMESLOT(hass.Hass):

    def initialize(self):
        # Run every minute
        time = datetime.time(0, 0, 0)
        self.run_minutely(self.trigger, time)
    
    def trigger(self, kwargs): 

        currentStartFirstFloor = {
            "chodba" : "input_number.first_floor_corridor_and_toilet_current_start",
            "koupelna" : "input_number.first_floor_bathroom_current_start",
            "obyvaci" : "input_number.first_floor_living_room_and_kitchen_current_start",
            "kuchyn" : "input_number.first_floor_living_room_and_kitchen_current_start",
            "sklep" : "input_number.first_floor_cellar_current_start",
            "garaz" : "input_number.first_floor_garage_current_start"}

        currentStopFirstFloor = {
            "chodba" : "input_number.first_floor_corridor_and_toilet_current_stop",
            "koupelna" : "input_number.first_floor_bathroom_current_stop",
            "obyvaci" : "input_number.first_floor_living_room_and_kitchen_current_stop",
            "kuchyn" : "input_number.first_floor_living_room_and_kitchen_current_stop",
            "sklep" : "input_number.first_floor_cellar_current_stop",
            "garaz" : "input_number.first_floor_garage_current_stop"}

        nextStartFirstFloor = {
            "chodba" : "input_number.first_floor_corridor_and_toilet_next_start",
            "koupelna" : "input_number.first_floor_bathroom_next_start",
            "obyvaci" : "input_number.first_floor_living_room_and_kitchen_next_start",
            "kuchyn" : "input_number.first_floor_living_room_and_kitchen_next_start",
            "sklep" : "input_number.first_floor_cellar_next_start",
            "garaz" : "input_number.first_floor_garage_next_start"}

        nextStopFirstFloor = {
            "chodba" : "input_number.first_floor_corridor_and_toilet_next_stop",
            "koupelna" : "input_number.first_floor_bathroom_next_stop",
            "obyvaci" : "input_number.first_floor_living_room_and_kitchen_next_stop",
            "kuchyn" : "input_number.first_floor_living_room_and_kitchen_next_stop",
            "sklep" : "input_number.first_floor_cellar_next_stop",
            "garaz" : "input_number.first_floor_garage_next_stop"}


        currentStartSecondFloor = {
            "koupelna" : "input_number.second_floor_bathroom_current_start",
            "obyvaci" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_start",
            "kuchyn" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_start",
            "pracovna" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_start",
            "jidelni" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_start",
            "tomas" : "input_number.second_floor_thomas_bedroom_current_start",
            "severni" : "input_number.second_floor_north_room_current_start",
            "stredni" : "input_number.second_floor_middle_room_current_start",
            "rohovy" : "input_number.second_floor_corner_room_current_start",
            "chodba": "input_number.second_floor_corridor_and_toilet_room_current_start",
            "toaleta": "input_number.second_floor_corridor_and_toilet_room_current_start",
            "rodicu" : "input_number.second_floor_parents_bedroom_current_start"}
        
        currentStopSecondFloor = {
            "koupelna" : "input_number.second_floor_bathroom_current_stop",
            "obyvaci" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_stop",
            "kuchyn" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_stop",
            "pracovna" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_stop",
            "jidelni" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_current_stop",
            "tomas" : "input_number.second_floor_thomas_bedroom_current_stop",
            "severni" : "input_number.second_floor_north_room_current_stop",
            "stredni" : "input_number.second_floor_middle_room_current_stop",
            "rohovy" : "input_number.second_floor_corner_room_current_stop",
            "chodba": "input_number.second_floor_corridor_and_toilet_room_current_stop",
            "toaleta": "input_number.second_floor_corridor_and_toilet_room_current_stop",
            "rodicu" : "input_number.second_floor_parents_bedroom_current_stop"}

        nextStartSecondFloor = {
            "koupelna" : "input_number.second_floor_bathroom_next_start",
            "obyvaci" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_start",
            "kuchyn" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_start",
            "pracovna" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_start",
            "jidelni" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_start",
            "tomas" : "input_number.second_floor_thomas_bedroom_next_start",
            "severni" : "input_number.second_floor_north_room_next_start",
            "stredni" : "input_number.second_floor_middle_room_next_start",
            "rohovy" : "input_number.second_floor_corner_room_next_start",
            "chodba": "input_number.second_floor_corridor_and_toilet_room_next_start",
            "toaleta": "input_number.second_floor_corridor_and_toilet_room_next_start",
            "rodicu" : "input_number.second_floor_parents_bedroom_next_start"}

        nextStopSecondFloor = {
            "koupelna" : "input_number.second_floor_bathroom_next_stop",
            "obyvaci" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_stop",
            "kuchyn" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_stop",
            "pracovna" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_stop",
            "jidelni" : "input_number.second_floor_kitchen_workroom_living_and_diving_room_next_stop",
            "tomas" : "input_number.second_floor_thomas_bedroom_next_stop",
            "severni" : "input_number.second_floor_north_room_next_stop",
            "stredni" : "input_number.second_floor_middle_room_next_stop",
            "rohovy" : "input_number.second_floor_corner_room_next_stop",
            "chodba": "input_number.second_floor_corridor_and_toilet_room_next_stop",
            "toaleta": "input_number.second_floor_corridor_and_toilet_room_next_stop",
            "rodicu" : "input_number.second_floor_parents_bedroom_next_stop"}

        firstFloor = "prizemi"
        secondFloor = "patro"
        
        for key, value in currentStartFirstFloor.items():
            self.setStartStop(firstFloor, key, currentStartFirstFloor[key], currentStopFirstFloor[key], nextStartFirstFloor[key], nextStopFirstFloor[key])

        for key, value in currentStartSecondFloor.items():
            self.setStartStop(secondFloor, key, currentStartSecondFloor[key], currentStopSecondFloor[key], nextStartSecondFloor[key], nextStopSecondFloor[key])

    def setStartStop(self, floor, currentThermostat, currentStartEntity, currentStopEntity, nextStartEntity, nextStopEntity):
        current_time = self.get_state('sensor.time')
        currtenTime = datetime.datetime.strptime(current_time+":00",'%H:%M:%S')
        dictionaryStartStop = {}
        for entity in self.get_state("switch"):
            if "schedule" in entity:
                if floor  in entity.lower():
                    if  currentThermostat in entity.lower():
                        timeslots = self.get_state(entity, attribute='times')
                        length = len(timeslots)
                        for index, timeslot in enumerate(timeslots):
                            start = datetime.datetime.strptime(timeslot,'%H:%M:%S')

                            stop = datetime.datetime.strptime("23:59:00",'%H:%M:%S') 
                            if index + 1 < length:
                                stop = datetime.datetime.strptime(timeslots[index+1],'%H:%M:%S')

                            dictionaryStartStop[index] = [start, stop]
        
        nextSlot = None
        currentSlot = None
       
        for key, values in dictionaryStartStop.items():
            if values[0] <= currtenTime and currtenTime <  values[1]:
                lengthDic = len(dictionaryStartStop)
                currentSlot = dictionaryStartStop[key]
                if key + 1 < lengthDic:
                    nextSlot = dictionaryStartStop[key + 1]
                    break
                else:
                    nextSlot = dictionaryStartStop[0]
        

        if nextSlot != None and currentSlot != None:
            nextStartMinutes = nextSlot[0].hour * 60 + nextSlot[0].minute
            nextStopMinutes = nextSlot[1].hour * 60 + nextSlot[1].minute
            self.set_state(nextStartEntity,  state = nextStartMinutes)
            self.set_state(nextStopEntity,  state = nextStopMinutes)

            currentStartMinutes = currentSlot[0].hour * 60 + currentSlot[0].minute
            currentStopMinutes = currentSlot[1].hour * 60 + currentSlot[1].minute
            self.set_state(currentStartEntity,  state = currentStartMinutes)
            self.set_state(currentStopEntity,  state = currentStopMinutes)

   
    
               