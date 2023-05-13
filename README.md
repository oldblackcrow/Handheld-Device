There two versions of the software. The original (code.py) is if you want to use AdafruitIO. The "updated" version (updated-adafruit_ble.py) is required for the new Clue sketch, which will communicate directly with the Clue via Bluetooth. 


Hardware:
Adafruit ItsyBitsy nRF52840 Express - Bluetooth LE

Adafruit SGP30 Air Quality Sensor Breakout - VOC and eCO2. The SGP30 I used did not have a STEMMA QT connector. I soldered the wires directly. There is barely enough room in the Diamnond Select Handheld case to accomodate a connector, so you want to use the Adafruit SGP30 with the STEMMA QT connector, you need to 3D print a slightly bigger case.

Since all the new Adafruit SGP30s have two STEMMA QT ports, a small handheld just becomes impractical. After several months of searching, I ended up replacing mine with an $8 SGP30 from eBay. Honestly, I didn't think it would work, but it actually works beautifully and with no changes to the code. This is the link for the eBay version, but you can do further serches for a better/cheaper/whatever seller. https://www.ebay.com/itm/125180741014

PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A
350mAh 3.7v Lithium Ion Polymer Battery
Panel Mount Extension USB Cable Micro B Male to Micro B Female

Code provided by Adafruit with slight modifications by me. 

If you choose the AdafruitIO version, make sure to set up an AdafruitIO account and have your "feeds" named "rx". If you want something different, make sure to match what is in the code or it won't connect. Finally, you will need the Adafruit Bluefruit App on your phone to connect to the ItsyBitsy via bluetooth and AdafruitIO.
