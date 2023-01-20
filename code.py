import time

import adafruit_ds18x20
import board
from adafruit_onewire.bus import OneWireBus

# one_wire_bus = OneWireBus( board.GP2 )
# print( one_wire_bus.scan() )
# ds18b20 = adafruit_ds18x20.DS18X20( one_wire_bus, one_wire_bus.scan()[0] )
ow_bus = OneWireBus( board.GP2 )
ds18 = adafruit_ds18x20.DS18X20( ow_bus, ow_bus.scan()[0] )

# Main loop to print the temperature every second.
while True:
  # print( "Temperature: {0:0.3f}C".format( ds18b20.temperature ) )
  print( "Temperature: {0:0.3f}C".format( ds18.temperature ) )
  time.sleep( 1.0 )
