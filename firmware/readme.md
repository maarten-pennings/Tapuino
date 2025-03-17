# Firmware

- The UI also has a COMMAND_SELECT_LONG and COMMAND_ABORT_LONG.
  They are especially relevant in manual filename entry.
  
  - Short SELECT means start editing next character.
  - Long SELECT means select character, stop entering characters, start recording the file.
  - Short ABORT means go back to editing previous character.
  - Long ABORT means stop entering file name.

- Lowercase `m` on the LCD means waiting for motor power by C64.
  Uppercase `M` means C64 powers the motor.

- In the "file browser" shown with "play" I filtered out also _hidden_ and _system_ files.
  See [source](https://github.com/maarten-pennings/Tapuino/blob/main/firmware/tapuino/fileutils.c#L8).
  The "system" was needed because windows creates a some funny system directory each time I plug in the SD card in my system.
  I added  "hidden" because this allows me to add some files (documentation, images) that I do not want to pop up in the Tapuino browser.


(end)