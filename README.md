# MacOS-XPS-9500-4K-OpenCore
macOS Big Sur on Dell XPS 9500 year 2020

# Some Notes
First thanks to the other Repositorys here on github from @zachs78 and @robotblox

# Whats working
- UHD Acceloration
- Sound
- Wifi
- Touchpad

# Whats not working at the moment:
- Touchscreen
  Touchscreen and Touchpad need to be patched via SSDT
  Touchscreen und Touchpad would need to split into polling and interrupt mode
  https://github.com/VoodooI2C/VoodooI2C/issues/392
  
- Sleep is broken until Dell Fix "modern sleep bug"

# Installation

Before you can install macOS on your Dell you need to create a patched EDID under Linux
For I remove my edited edid from config plist to ensure that you do not brick your device with a wrong one.

Create a macOS installer and put in your EDID and Platform information to your config.plist
You'll need to disable some Bios Settings to get system working.

Edited Readme comes soon...
