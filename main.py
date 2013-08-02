#need to define templates for save files (top)
#list dirs in media

import os, argparse

parser = argparse.ArgumentParser(description='This Program Backups Game Saves for Major Emulators on the Open Pandora Handheld')
# -g / start GUI
# -h / help
# -b / which card to backup (sd card 1 or 2 or all)



#get media list in /media and record them in variable
#check if they are still here at launch of the application
#template should contain following info: name of pnd, name of appdata folder, folder with save files, file extension of save file

progtodetect=[("Gambatte.pnd","gambatte-qt",'folder=sav','folder=savestate')]
appsfolder=['menu','desktop','apps']

def checkprogram(progname,directory):
  
  global appsfolder
  found=0
  
  for folder in appsfolder:
    if os.path.isfile("/media/{0}/pandora/{1}/{2}".format(directory,folder,progname))==True :
      print "Found "+ progname
      found+=1
  if found==0:
    return False
  else:
    return True

def checkappdata(appdatafolder,directory):
  if os.path.isdir("/media/{0}/pandora/appdata/{1]".format(directory,appdatafolder))==True:
    return True
  else:
    return False

def confirmfolderorfile(element):
  if "folder=" in element:
    return True
  else:
    return False  

def bgs():
#check for Pandora folder
  topdirlist=os.listdir("/media")
  for directory in topdirlist:
    print "Checking the SD Card "+directory
    if os.path.isdir("/media/{0}/pandora".format(directory)):
      print "Checking for pandora folder on "+directory
      for progs in progtodetect:
        print "Checking for "+progs[0]
        if checkprogram(progs[0])==True:
          print "Checking for appfolder for "+progs[0]
          if checkappdata(progs[1])==True:
            print "Found the appdata folder "+progs[1]
            
            for i=2 to len(progs):
              if confirmfolderorfile(progs[i])==True:
                #confirm folder is not empty
                #if not empty save it in list of what to save later
              else:
                #find the files with the extension
                #save their full path location for later saving
          
    # give message regarding how many files are being saved, and how big they are uncompressed
    #save first zip for first SD CARD - add date in name
    #confirm size after compression


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
