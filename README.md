There two versions of the software. The original (code.py) is if you don't want to use the new Clue sketch. The "updated" version is required for the new Clue sketch, which will communicate directly with the Clue via Bluetooth. 


Hardware:

Adafruit ItsyBitsy nRF52840 Express - Bluetooth LE

Adafruit SGP30 Air Quality Sensor Breakout - VOC and eCO2 (keep in mind that the version I used did not have a STEMMA QT connector. I soldered the wires directly. There is enough room in the Diamnond Select Handheld case to accomodate. However, you could 3D print a bigger case if you wish).

PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A

350mAh 3.7v Lithium Ion Polymer Battery

Panel Mount Extension USB Cable Micro B Male to Micro B Female


Code provided by Adafruit with slight modifications by me. 


If you choose to use the version with AdafruitIO, make sure to set up an AdafruitIO account and have your "feeds" named "rx". If you want something different, make sure to match what is in the code or it won't connect.

Finally, you will need the Adafruit Bluefruit App on your phone to connect to the ItsyBitsy and AdafruitIO.
