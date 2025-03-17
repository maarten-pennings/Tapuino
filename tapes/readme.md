# Tapuino tapes


## SD card file order

The files on the SD card might not be in the order you like them.
I use `yafs` from [https://www.luisrios.eti.br/public/en_us/projects/yafs/](https://www.luisrios.eti.br/public/en_us/projects/yafs/) 
to order the directory entries so that my directories and files appear on the LCD screen in the order I want.


## SD card format

I have a 4G SD card. I formatted it with `SD Card Formatter.exe` from
[https://www.sdcard.org/downloads/formatter/](https://www.sdcard.org/downloads/formatter/).
Yafs allows to have a look at how the SD card is formatted

```
C:\Programs\yafs_windows_x86-64_2023_01_22>yafs.exe -d d: -i
YAFS (Yet Another FAT Sorter) - version 2023_01_22
"C64-SD4G   " has a FAT32 file system.
It has 2 FATs that has 491008 bytes each or 959 sectors.
The first sector and byte offset of each FAT are respectively:
6274 3212288 (0x310400)
7233 3703296 (0x388200)

Root number of entries (FAT12 and FAT16 only): 0 that demands 0 sectors.
Each sector has 512 bytes.
Each cluster has 32768 bytes or 64 sectors.
The total number of sectors is 7856128 (0x77e000).
The total number of clusters is 122624 (0x1df00).
The first data sector is 8192 (0x2000).
```


## SD card size

Observe that a typical game is below 1Mbyte.
  
```
2009 11 07  00:25           518,425 Archon
2003 03 04  20:27           452,902 Bruce Lee
2003 02 25  14:13           764,643 Bubble Bobble
2003 02 27  17:43           471,400 Cauldron II
2003 03 17  15:34         1,162,661 Frogger 64
2003 04 03  03:35           772,642 Giana Sisters
2005 02 13  21:20           617,146 Mayhem
```
  
A game of 1M needs 32 clusters of 32kB.
On my 4G disk there are 122624 clusters, so room for 3832 files of 1M.
That sounds like enough space for me.


## Turbo

Tapuino emulates quite faithfully a C64 Datasette.
That is, including the speed.
If you want you can use one of the classic accelerators like [Turbo_Tape](Turbo_Tape.tap).
After loading you need to activate it; see [manual](Turbo_Tape.pdf).

(end)
