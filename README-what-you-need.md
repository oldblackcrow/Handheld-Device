Adafruit ItsyBitsy nRF52840 Express - Bluetooth LE

There two versions of the software. The original is if you don't want to use the new Clue sketch. The "updated" version is required for the new Clue sketch.

Adafruit SGP30 Air Quality Sensor Breakout - VOC and eCO2 - Keep in mind that the version I used did not have a STEMMA QT connector. I soldered the wires directly. I don't know if there is enough room in the Diamnond Select Handheld case to accomodate. However, you could 3D print a bigger case if you wish.

PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A

350mAh 3.7v Lithium Ion Polymer Battery

Panel Mount Extension USB Cable Micro B Male to Micro B Female - since the cable is too thick, I cut and stripped all the wire except for power. Since its only job is to recharge the battery, no need for a data cable.

Code used was example code provided by Adafruit with slight modifications by me. 

Make sure to set up an Adafruit IO account and have your "feeds" named "rx". If you want something different, make sure to match what is in the code or it won't connect.

Finally, you will need the Adafruit Bluefruit App on your phone to connect to the ItsyBitsy and AdafruitIO.

Ultimately, I would love to connect the ItsyBitsy directly to Bluetooth on the PyPortal, but currently, the PyPortal cannot act as a Central device. However, the Clue can and I did test the connectivity with no issues, however, I have not (and probably will not) integrate that code into the Clue due to my utter lack of knowledge of Arduino IDE. But if you feel so inclined, please post the code or a link to the code here.
