BGS
===

Backup Game Saves is a Python tool to enable automatic backup of saved games and save states from emulators working on the Open Pandora (Linux handheld). It also duplicates the backup file on all SD-cards/connected storages units in /media available on the Pandora at the time of execution. 

Supported Platforms
-------------------

Currently all devices running libPND in a Linux environment, I guess :) Which basically reduces the use of this code to the Open Pandora Linux handheld, as far as I know. 

Supported Applications
----------------------
It currently supports backup up saved games for the following applications: 

- Gambatte, Gameboy emulator
- Pcsx_rearmed, PS1 emulator
- Drastic, DS emulator
- PPSSPP, PSP emulator
- gpSP, GBA emulator
- UAE4ALL, Amiga emulator
- Snes9x4p, SNES emulator
- Gpfce, NES emulator
- Gngeo, NEO GEO emulator
- Fba, arcade emulator
- Apkenv, Android games (not emulated)
- Darkplaces, Quake engine
- Dune dynasty, Dune2 Reboot
- Scumm VM, LucasArts (and others) adventure games emulator
- Return to Castle Wolfenstein
- PicoDrive, Genesis/Megadrive emulator
- Freespace2
- Exult, engine for Ultima7
- Chocolate Doom, Doom engine
- Solarus DX, Zelda-like game
- Pewpew2, polygonal shooter
- Duke Nukem 3d, come get some
- 8Blitter, Master System/GameGear emulator
- Pushover
- Projectx, Forsaken-like game	

Requirements
------------

You will need Python 2.6+ to run this, as well as argparse (not actively used currently but will be) and PyZenity. 

License
-------

Licensed under GPL v3

To Do
-----

- A Restore Tool.
- Size estimation before backup
- Checking free space before backup both on SD1 and SD2
- Running as a background task, in order to run every couple of days or so? 
