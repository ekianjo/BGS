#need to define templates for save files (top)
#list dirs in media

import os

#get media list in /media and record them in variable
topdirlist=os.listdir("/media")

#check if they are still here at launch of the application

#template should contain following info: name of pnd, name of appdata folder, file extension of save file

progtodetect=["Gambatte.pnd","pcsx.pnd"]

#check for Pandora folder
for directory in topdirlist:
  if os.path.isdir("media/{0}/pandora".format(directory)):
      pass


  #check in target directories : menu, apps

  #check for PNDs for target applications. 
  #stores list of PNDs supported found
  #check for save game definitions / follow templates for PNDs supported, go through the list
  #return a list with media as fist entry, folder as second entry, list of files detected as third entry
  
  




#test for directories such as Pandora -> to accelerate the loops
#os.path.isdir -> then store in config.
#allow to refresh directories lookup in one click.
#display what systems/games are recognized
#test for directory for emulators and all / and know where they save their saved games – for the ones where path is fixed.
#for the ones where individual folders need to add option to add appropriate folders and save them in config file. 
#list all files to be saved, indicate total uncompressed size in status bar as well as number of save files.
#propose saving compressed data to media (both SD cards) / Cloud / ftp
#compress files
#copy files in the right place
#when executed, register when the last backup was made, as well as the list of what was backed up.
