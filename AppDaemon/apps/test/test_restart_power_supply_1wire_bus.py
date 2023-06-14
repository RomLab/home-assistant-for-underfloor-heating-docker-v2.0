#from MCP23S17 import MCP23S17
from RPiMCP23S17.MCP23S17 import MCP23S17
import time
#import MCP23S17




#mcp1 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x00)
mcp1 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x00)
#mcp1 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x00)
#mcp1 = MCP23S17(device_id=0x00)
#mcp2 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x01)
mcp1.open()
mcp1._spi.max_speed_hz=10000
#mcp2.open()

# pin 1-8 jsou od 8-15
# pin 21-28 jsou 0-7
#mcp1.setDirection(0, mcp1.DIR_OUTPUT)



for x in range(0, 16):
    mcp1.setDirection(x, mcp1.DIR_OUTPUT)

for x in range(0, 16):
    mcp1.digitalWrite(x, mcp1.LEVEL_HIGH)

#while (True):
#    for x in range(0, 16):
#        mcp1.digitalWrite(x, MCP23S17.LEVEL_HIGH)
#    time.sleep(1)
#    for x in range(0, 16):
#        mcp1.digitalWrite(x, MCP23S17.LEVEL_LOW)
#    time.sleep(1)
