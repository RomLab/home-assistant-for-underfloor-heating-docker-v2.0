import hassapi as hass
# Import the PCA9685 module.
import pca9685
import time

class ThermoelectricActuatorsSecondFloor(hass.Hass):

    pwm = None
    def initialize(self):
        # Initialise the PCA9685 using the default address (0x40).
        PCA9685_ADDRESS_SECOND_FLOOR = 0x40
        self.pwm = pca9685.PCA9685(PCA9685_ADDRESS_SECOND_FLOOR)
        # Frequency in Hertz
        PWM_FREQUENCY = 100 
        self.pwm.set_pwm_freq(PWM_FREQUENCY)
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_bathroom")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_bathroom_ladder")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_living_and_diving_room")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_workroom")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_kitchen")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_corridor_and_toilet")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_north_room")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_parents_bedroom_window")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_parents_bedroom_door")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_middle_room")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_corner_room")
        self.listen_state(self.trigger, "input_boolean.thermo_actuator_second_floor_thomas_bedroom")

        # Sets value after restart Appdaemon
        self.trigger("input_boolean.thermo_actuator_second_floor_bathroom", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_bathroom_ladder", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_living_and_diving_room", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_workroom", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_kitchen", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_corridor_and_toilet", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_north_room", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_parents_bedroom_window", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_parents_bedroom_door", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_middle_room", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_corner_room", None, None, None, None)
        time.sleep(2)
        self.trigger("input_boolean.thermo_actuator_second_floor_thomas_bedroom", None, None, None, None)

    def trigger(self, entity, attribute, old, new, kwargs):    
       
        state = self.get_state(entity)
        channel = None
        
        pwm_pulse = 0
        if(state == "on"):
            pwm_pulse = 4095
            
        error = False
        if(entity == "input_boolean.thermo_actuator_second_floor_thomas_bedroom"): 
            channel = 11         
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_corner_room"):
            channel = 10
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_middle_room"):
            channel = 9
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_parents_bedroom_door"):
            channel = 8
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_parents_bedroom_window"):
            channel = 7
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_north_room"):
            channel = 6
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_corridor_and_toilet"):
            channel = 5
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_kitchen"):
            channel = 4
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_workroom"):
            channel = 3
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_living_and_diving_room"):
            channel = 2
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_bathroom_ladder"):
            channel = 1
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        elif(entity == "input_boolean.thermo_actuator_second_floor_bathroom"):
            channel = 0
            self.pwm.set_pwm(channel, 0, pwm_pulse)
        else:
            error = True
        
        if(error == True): 
            self.log("ERROR: Second floor – Problem with bad selected channel for PWM.")
        else:
            # Checks currect settings (pwm pulse), otherwise sets again          
            while pwm_pulse != self.pwm.get_pwm(channel):
                self.pwm.set_pwm(channel, 0, pwm_pulse)
                self.log("WARNING: Second floor – Repetition of setting channel: " + str(channel) + " PWM: " + str(pwm_pulse))

    def get_pwm_pulse(self, pwm_percent):
        # Convert to float number
        pwm_value = float(pwm_percent)/100.0
        # Gets pwm pulse
        pwm_pulse = round(4095 * pwm_value) 

        return int(pwm_pulse)
