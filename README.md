BGS
===

Backup Game Saves is a Python tool to enable automatic backup of saved games and save states from emulators working on the Open Pandora (Linux handheld). It also duplicates the backup file to a destination of your choice. 

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
- NubNub	

Since 0.2.2 :
- Mupen2.0
- LBA via prequengine
- VVVVVV
- Out of This World
- Paper Wars
- Homeworld
- Freeciv
- Microbes

Since 0.2.3 : 
- Mooboy, GB emulator

Since 0.2.4 : 	
- area2048
- Boson x
- ZDoom
- Widelands
- Super Hexagon
- Snowman Reloaded
- Pandora Nanolemmings
- Double Cross
- Dopewars
- Metroidclassic
- Not pacman
- Not tetris
- Openttd
- Reicast	

Requirements
------------

You will need Python 2.6+ and PyZenity to run this.
Google authentication needs a JScript capable browser, so you will also need one of these: firefox, qupzilla or babypanda.

License
-------

Licensed under GPL v3

To Do
-----

- A Restore Tool. 
- Running unattended as a background task (without any gui), in order to run every couple of days or so?
- Backups on a per game/emulator basis (almost there)
- Better compression mechanism
- Implement other cloud services
