# rs3_quick_language_launcher
Quick python utility script that launches RuneScape 3 in the desired language.

# Requirements
This script has only been tested in Windows 10 Home Edition, but should work on any modern Windows platform almost plug-n-play. TBD for Linux and Mac.

# How to setup

First, you must setup the correct paths and whether or not you use the Jagex Launcher to launch RuneScape. To do so, open main.py in any text editor. If you use the Jagex Launcher, set USE_JAGEX_LAUNCHER to True. Otherwise, set it to False.

## Paths setup

Then, you must copy your parth to RS3's preferences.cfg file. To locate it, right-click your RS3 shortcut -> Open file location. Otherwise it should be in C:/ProgramData (Hidden folder)/Jagex/launcher.

If you use Jagex Launcher, you must also setup its path. In my case, it's located in C:/Program Files (x86)/Jagex Launcher

## Setting up the shortcuts

After, you can simply right-click the 3 .bat files -> Send to -> Desktop (create shortcut). You can now execute the .bat file with your desired language. You don't need to re-make the shortcuts if you modify main.py.
