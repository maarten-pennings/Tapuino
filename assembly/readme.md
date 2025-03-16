# Assembly

In this directory you find my assembly results.


## Bare PCB

The 5 PCBs arrived after only 4 working days.
I ordered them without assembly, so that was my next step.

![Bare PCB](BarePCB.jpg)


## Patching the errors in the schematics.

After assmebling the Arduino Nano and the LCD, I did my first test (powered via USB).
The LCD switched-on its back light, but showed no characters.
I uploaded the I2C scanner example from the Arduino IDE, and did not see any device on the I2C bus.
Attached a logic analyzer, did see the I2C traffic, but the slicer in the logic analyzer did not.

I swapped the SCL and SDA lines on the Arduino.
I patched this by swapping the SDA and SCL line towards the LCD; that was relatively straightforward
to do, because it is connected with a pin header.

![I2C swap](Patch1-I2C.jpg)

LCD did work; I added the SD card, optocoupler and red and green LED.
Second test (still running from USB power) showed that I could browse the SD card (short circuiting the switch pins).
However short circuiting the MOTOR and 5V on J1C64 did not start playback (animation on the LCD)
nor did the green motor LED turn on.

It turned out I swapped the anodes and cathodes of the optocoupler.
"Fortunately" I did that twice, for the emitter as well as the detector.
So my second patch was to turn the optocoupler on its back, bending all 4 legs 180°.


![U2 swap](Patch2-U2.jpg)

Next I added the audio components and finally the 4 switches.


## With cable

The PCB seemed to work fine on USB, faking motor on by short circuiting the MOTOR and 5V on J1C64.

Next step was to add the cable with my own printed connector sleeve.

![With cable](WithCable.jpg)


I did create a 1.5 with the fixes for the schematics bugs.


## Assembly completed

In the following photos you see the Tapuino in action.

![Left](Left3D.jpg)

![Right](Right3D.jpg)

![Front](Front3D.jpg)




(end)
