#need to define templates for save files (top)
#list dirs in media

import os

#get media list in /media
#record their variables
#check if they are still here at launch of the application

#check for Pandora folder



pandorafolder=os.path.isdir("media/xxx/pandora")
if pandorafolder==True:
  pass
  #check for save game definitions / follow templates
  




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
