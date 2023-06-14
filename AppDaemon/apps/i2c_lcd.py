import hassapi as hass
import i2c_lcd_driver

class I2CLCD(hass.Hass):

  def initialize(self):
    self.listen_state(self.trigger, "sensor.hot_water_tank_top")
    self.listen_state(self.trigger, "sensor.hot_water_tank_middle")
    self.listen_state(self.trigger, "sensor.hot_water_tank_bottom")
    self.listen_state(self.trigger, "switch.blue_led")

  def trigger(self, entity, attribute, old, new, kwargs): 
    state_switch = self.get_state("switch.blue_led")

    degree = [      
          [ 0b00111,
	          0b00101,
	          0b00111,
	          0b00000,
	          0b00000,
	          0b00000,
	          0b00000,
	          0b00000
            ],]
    elektric_switchboard = i2c_lcd_driver.lcd(0x23) #25
    cellar_lcd = i2c_lcd_driver.lcd(0x25) #25
    first_floor_lcd= i2c_lcd_driver.lcd(0x27) #27
    second_floor_lcd= i2c_lcd_driver.lcd(0x26) #26

    hot_water_tank_top_temperature = self.get_state("sensor.hot_water_tank_top")
    hot_water_tank_middle_temperature = self.get_state("sensor.hot_water_tank_middle")
    hot_water_tank_bottom_temperature = self.get_state("sensor.hot_water_tank_bottom")

    elektric_switchboard.lcd_load_custom_chars(degree)
    first_floor_lcd.lcd_load_custom_chars(degree)
    second_floor_lcd.lcd_load_custom_chars(degree)
    cellar_lcd.lcd_load_custom_chars(degree)

    # Notification about flooding in a fireplace
    if(state_switch == "on"):     
      elektric_switchboard.lcd_display_string("  Zatop v krbu!", 1)
      elektric_switchboard.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 2)
      elektric_switchboard.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 3)
      elektric_switchboard.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 4)

      cellar_lcd.lcd_display_string("  Zatop v krbu!", 1)
      cellar_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 2)
      cellar_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 3)
      cellar_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 4)

      first_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
      first_floor_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 2)
      first_floor_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 3)
      first_floor_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 4)

      second_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
      second_floor_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 2)
      second_floor_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 3)
      second_floor_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 4)
    else:
      elektric_switchboard.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 1)
      elektric_switchboard.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 2)
      elektric_switchboard.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 3)

      cellar_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 1)
      cellar_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 2)
      cellar_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 3)

      first_floor_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 1)
      first_floor_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 2)
      first_floor_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 3)

      second_floor_lcd.lcd_display_string("Cidlo 1: " + hot_water_tank_top_temperature + " " + chr(0) + "C", 1)
      second_floor_lcd.lcd_display_string("Cidlo 2: " + hot_water_tank_middle_temperature + " " + chr(0) + "C", 2)
      second_floor_lcd.lcd_display_string("Cidlo 3: " + hot_water_tank_bottom_temperature + " " + chr(0) + "C", 3)
