import hassapi as hass

import MCP23S17
#import datetime

class RESTARTPOWERSUPPLY1WIREBUS(hass.Hass):
   
   #mcp1 = None
   def initialize(self):
      #interval_of_reading = 30
      #start_time = self.datetime() + datetime.timedelta(seconds = 1)
      #self.handle = self.run_every(self.restart, start_time, interval_of_reading)
      self.listen_state(self.restart, "input_number.test_restart")

      mcp1 = MCP23S17.MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x00)
      mcp1.open()
      mcp1._spi.max_speed_hz=10000
      for x in range(0, 16):
         mcp1.setDirection(x, mcp1.DIR_OUTPUT)

      for x in range(0, 16):
         mcp1.digitalWrite(x, mcp1.LEVEL_HIGH)

   def restart(self, entity, attribute, old, new, kwargs):    
      state = self.get_state(entity)
   #   if(state == "0"):
   #      self.mcp1.digitalWrite(8, MCP23S17.LEVEL_LOW)

   #   if(state == "1"):
   #      self.mcp1.digitalWrite(8, MCP23S17.LEVEL_HIGH)
