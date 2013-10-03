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

listoftemplates=[("Gambatte.pnd","gambatte-qt",['sav','savestate'],[],[])
appsfolder=['menu','desktop','apps']

directories=""
debug=True

def backupspecific(progname,appdatafolder,listfolders,listfiles):
  
  global directories
  
  for topdirectory in directories:
    if checkprogram(progname,topdirectory)!="":
      workingfolder=checkprogram(progname)
      print workingfolder
      #confirm the top level working folder under /media/xx/pandora/
  
      if checkappdata(appdatafolder,topdirectory)==False:
        print "the program " + progname +".pnd does not have a appdata folder so far." 
      else:
        
        directoriesinappfolder=os.listdir("/media/{0}/pandora/appdata/{1}").format(topdirectory,appdatafolder)
        
        for onefolder in directoriesinappfolder:
          for foldertobackup in listfolders:
            if onefolder==foldertobackup:
              print "I found the folder called "+ onefolder+" to backup"
              #add the path worklist to backup where we will give the final instructions to zip in the end
              
  
        #instruction to backup goes here
  
  pass
  
  
  

#each program has
#PND attached to it (single) - single variable
#appdata attached to it (single) - single variable
#folders to save (single or several) - list
#files to save (single or several) - list


def checkprogram(progname,directory):
  #returns folder if the PND is found in one of the appsfolder directory or "" if not found
  global appsfolder
  found=0
  
  for folder in appsfolder:
    if os.path.isfile("/media/{0}/pandora/{1}/{2}".format(directory,folder,progname))==True :
      print "Found "+ progname+ " in "+ folder
      found+=1
  if found==0:
    return ""
  else:
    return folder

def checkappdata(appdatafolder,directory):
  if os.path.isdir("/media/{0}/pandora/appdata/{1]".format(directory,appdatafolder))==True:
    return True
  else:
    return False

def checkfolderexists(path,foldername):
  if os.path.isdir(path+foldername):
    return True
  else:
    return False

def defineglobaldirectories():
  #define the top levels directories in /media
  global directories, debug
  directories=os.listdir("/media")
  if debug==True: 
    print directories

  
def bgs():
#check for Pandora folder
  
  defineglobaldirectories()
  #get the name of global directories
  
  for programtobackup in listoftemplates:
    pass
    
  
  for directory in directories:
    print "Checking the SD Card "+directory
    
    
    
    if os.path.isdir("/media/{0}/pandora".format(directory)):
      print "Checking for pandora folder on "+directory
      for progs in progtodetect:
        print "Checking for "+progs[0]
        if checkprogram(progs[0])==True:
          print "Checking for appfolder for "+progs[0]
          if checkappdata(progs[1])==True:
            print "Found the appdata folder "+progs[1]
            
#            for i=2 to len(progs):
#              if confirmfolderorfile(progs[i])==True:
#                folderstring=progs[i]
#                path="/media/{0}/pandora/appdata/{1}/".format(directory,progs[1])
#                if checkfolderexists(path, folderstring[7:])==True:
                  #if not empty save it in list of what to save later
#                else: 
#                  pass
#              else:
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
