# This version communicates directly with Bluetooth Central, in this case, the Adafruit Clue.
import time
import board
import busio
import adafruit_sgp30

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    while ble.connected:
        uart.write("%05d%05d" % (sgp30.eCO2, sgp30.TVOC))
        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
