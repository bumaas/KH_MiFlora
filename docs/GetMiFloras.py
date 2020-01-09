import sys
import time
import datetime

from gattlib import DiscoveryService
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from btlewrap import GatttoolBackend

def getPlant(macAdr):
    poller = MiFloraPoller(macAdr, GatttoolBackend)

    now = time.time()
    dtnow=datetime.datetime.fromtimestamp(now)
    timeStr =  datetime.datetime.strftime(dtnow, '(%H:%M:%S %d-%m-%Y)')

    fw = poller.firmware_version()
    name = poller.name()
    temp = poller.parameter_value(MI_TEMPERATURE)
    moist = poller.parameter_value(MI_MOISTURE)
    light = poller.parameter_value(MI_LIGHT)
    cond = poller.parameter_value(MI_CONDUCTIVITY)
    battery = poller.battery_level()

    return timeStr + " Mac="+macAdr+" Name="+name+" Fw="+fw+" Temp={:.2f} Moist={:d} Light={:d} Cond={:d} Bat={:d}".format(temp, moist, light, cond, battery)


service = DiscoveryService("hci0")
devices = service.discover(8)
output  = []

for address, name in devices.items():
    if name == "Flower care" or name == "Flower mate":
        try:
            output.append(getPlant(address))
        except:
            raise ex

if len(output) > 0
    for i in output:
        print(i)

    print("DONE!")

