# MacOS-XPS-9500-4K-OpenCore
macOS Big Sur on Dell XPS 9500 year 2020

# Some Notes
First thanks to the other Repositorys here on github from @zachs78 and @robotblox

# Whats Working
Everything execpt sleep


# Installation

## Patching 4k Panel
- Extract from Linux your EDID
```
 xrandr -props
```

- Run the script
```
python3 4k-patch.py 
```

and paste your extracted edid from xrandr --props to get patched one

- Place patched edid into your config.plist under 
```
 DeviceProperties, AAPL00,override-no-connect
```
- Create USB installer with your modified config.plist
please note to adjust your PlatformInfo to MacBookPro 16.4

```
https://dortania.github.io/OpenCore-Install-Guide/installer-guide/
```

## Bios Settings

Disable the following

Fingerprint reader
Disable CFG Lock (via modGRUBShell)

## How to disable CFG Lock

This is specific to XPS 15 9500 only (along with its sibling models and previous gen).

Select the modGRUBShell option at startup (OpenCore boot selection page). At the grub prompt, enter the following commands (the first line unlocks CFG, the second line unlocks overclocking).

```
setup_var CpuSetup 0x3e 0x0
setup_var CpuSetup 0xda 0x0
exit
```

Restart your laptop and boot into the BIOS. Do a factory reset. Now your CFG lock will be disabled. You can confirm that by running the VerifyMSR2 option.

If you update your BIOS, you may need to do this again but so far Dell has been kind to us.



# Brightness hotkeys
The BRT6 patch used by previous Dell XPS models isn't working on the XPS 9500. However, fn+S and fn+B hotkeys are functioning in place of the original fn+F6 and fn+F7.

# Notes
Touchscreen and Touchpad currently only working with Voodooi2c version 2.4.4, newer version will break the touchpad
Touchscreen SSDT-Patch to force interrupt mode included.
