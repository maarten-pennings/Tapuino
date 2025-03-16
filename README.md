# Tapuino

My take on the famous Tapuino; "The $20 C64 Tape Emulator".


## Introduction

This project is a clone of [Tapuino ](https://github.com/sweetlilmre/tapuino) by "sweetlilmre" (Peter Edwards).

In a nutshell: Tapuino is an Arduino Nano, that together with an SD card reader and a 
simple user interface (LCD screen and 4 buttons) implements a sound recorder/player. 
The SD card stores Commodore 64 software in the form of 
[TAP](http://unusedino.de/ec64/technical/formats/tap.html) files; I think of them as 
WAV files. the bleeps that encode the sofwtare. Tapuino plugs into the (6-pin) cassette 
port of the C64, which also supplies 5V to Tapuino.

The UI on the Tapuino let's you browse through the SD card, selecting a TAP file.
When the user types `LOAD` on the C64, the C64 switches on the MOTOR pin on the cassette 
port, the Arduino sees that and starts playing the TAP file on the READ pin of the same
cassette port.

It is also possible to type `SAVE` on the C64. In this case the Arduino takes the signal
from the WRITE pin on the cassette port and converts that to a TAP file in a fixed
directory of the SD card. One bummer: the user typically types `SAVE "name"`, but since
the name comes in as beeps on the WRITE pin, this name get is not accesible to the Arduino. 
The user has to enter a name for the file on the SD card using the Tapuino GUI (slow) or accept 
auto-naming (basically a sequence number). Of course the bleep encoded file name is still
part of the TAP file, so that is reported back upon a `LOAD`.

I do not know if it is a bummer or not, but Tapuino emulates a datasette on the audio level.
This means it also has the speed or the original datasette. Quoting 
[stack exchange](https://retrocomputing.stackexchange.com/questions/16700/did-computer-games-for-commodore-64-really-take-25-minutes-to-load-if-everyth#:~:text=In%20this%20answer%2C%20the%20C64,minutes%20to%20load%2048%20kilobytes)
"tape data rate is calculated at 55 bytes per second, giving approximately 15 minutes to load 48 kilobytes".
It is however possible to use cassette speed loaders.
To make the retro experience complete, I added a speaker so that I can hear the beeps.

A quick computation: the C64 has 64k of RAM, but most tape games will be smaller than that.
On a 4 GB SD card (Arduino probably handles up to 32 GB) that would mean 4G/64k or 65536 
TAP files. Sounds plenty enough, but be warned the [Tape Archive](https://archive.org/details/Ultimate_Tape_Archive_V4.5) is nearly 20 GB zipped.

> **Warning** Peter Edwards writes on his GitHub  
> This project is now in maintenance mode and has been superseded by the Tapuino Next

And indeed, there are multiple dangling links, for example to Peter's video, and to his blog.
I decided to clone his [firmware](firmware). 
I did find a [2014 blog](https://sweetlilmre.blogspot.com/2014/07/tapuino-20-c64-tape-emulator.html)


## PCB

One problem that I had is that I could not find a complete schematic. 
Peter Edwards' has Fritzing schematics and Vero board drawings, but no real schematics.

For example, the Control 0 and Control 1 lines are still a bit of a mystery.
Also, very hidden, there appears to be a GPIO pin that signals recording as opposed to playing. 

In the end, I did design my own [PCB](pcb).
It's also fun.

Instead of using cheap switches, I decided to go for Cherry MX switches.
Nice and big, looking a bit similar to the big switches on the actual datasette.


## Assembly

I hand assembled the PCB. See result in the [assembly](assembly) directory.
There were some errors in the V1 PCB that had to be patched; see [pcb section](pcb#schematics).


## Software

Due to all dangling links, I was afraid the Tapuino sources might disappear, so 
I decided to clone the [firmware](firmware).


Edit the configuration in [config-user.h](firmware/config-user.h).

There is also runtime options


## Case

I did design a "sleeve" for the connector.
The case for the Tapuino itself is not yet done.
See [case](case).



(end)

