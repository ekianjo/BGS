#Copyright (C) [2013] [Ekianjo (alias)]
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

#Additional permission under GNU GPL version 3 section 7
#If you modify this Program, or any covered work, by linking or combining it with [name of library] (or a modified version of that library), containing parts covered by the terms of [name of library's license], the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of [name of library] used as well as that of the covered work.}


import os, tarfile, time, shutil, subprocess, ftplib
import argparse, PyZenity, glob
from datetime import date

#will do argparse later
#parser = argparse.ArgumentParser(description='This Program Backups Game Saves for Major Emulators on the Open Pandora Handheld')
# -g / start GUI
# -h / help
# -b / which card to backup (sd card 1 or 2 or all)


today=date.today()
#get media list in /media and record them in variable
#check if they are still here at launch of the application
#template should contain following info: name of pnd, name of appdata folder, folder with save files, file extension of save file

listoftemplates=[
("gambatte.pnd","gambatte-qt",['saves','.config'],[],[])
,('pcsx_rearmed_r19.pnd','pcsx_rearmed',['.pcsx','screenshots'],[],[])
,('drastic.pnd','DraStic',['.links','backup','config','profiles','savestates'],[],[])
,('PPSSPP.pnd','PPSSPP',['home'],[],[])
,('gpSP-pnd-0.9-2Xb-u8a.pnd','gpsp',['',''],[],[])
,('UAE4ALLv2.0.pnd','uae4all',['saves','conf'],[],[])
,('snes9x4p_20120226.pnd','snes9x.skeezix.alpha',['.snes96_snapshots'],[],[])
,('gpfce_r2.pnd','gpfce',['fceultra'],[],[])
,('gngeo_0.8.5.pnd','gngeo_pepone',['save','conf'],[],[])
,('fba.pnd','fba-dave18',['savestates','screenshots','conf','config'],[],[])
,('apkenv-v42.3.17.2.pnd','apkenv',['data'],[],[])
,('darkplaces.pnd','darkplaces',['.darkplaces'],[],[])
,('dunedynasty.pnd','dunedynasty',['dunedynasty'],[],[])
,('scummvm-op.pnd','scummvm',['saves'],[],[])
,('rtcw.pnd','rtcw',['home'],[],[])
,('PicoDrive_190.pnd','picodrive',['srm','mds','cfg','brm'],[],[])
,('freespace2.pnd','freespace2',['home'],[],[])
,('exult-1.4.pnd','exult',['.exult'],[],[])
,('cdoom.pnd','doom',['.chocolate-doom'],[],[])
,('solarusdx-zsdx-11201.pnd','solarusdx',['.solarus'],[],[])
,('pewpew2.pnd','pewpew2',['documents'],[],[])
,('duke3d.pnd','duke3d',['.eduke32'],[],[])
,('8Blitter.pnd','8blitter.lordus',['data'],[],[])
,('pushover.pnd','pushover',['.pushover'],[],[])
,('projectx_ptitseb.pnd','projectx',['savegame'],[],[])
,('nubnub.pnd','nubnub',['*ALLFOLDER*'],['uploadedscore','settings','hiscore'],[])
,('mupen64plus2.pnd','mupen64plus2',['*ALLFOLDER*'],[],[])
,('prequengine.pnd','prequengine',['save'],[],[])
,('vvvvvv.pnd','vvvvvv',['.vvvvvv'],[],[])
,('outofthisworld.pnd','outofthisworld',['home'],[],[])
,('paperwars-v1.0.0-ekianjo.pnd','paperwars',['Save'],[],[])
,('homeworld.pnd','homeworld',['cfg'],[],[])
,('freeciv.pnd','freeciv',['*ALLFOLDER*'],[],[])
,('microbes1.0rel2-1.pnd','microbes',['*ALLFOLDER*'],[],[])
,('mooboy.mrz.pnd','mooboy.mrz',['*ALLFOLDER*'],[],[])
#,('','',['',''],[],[])
#,('','',['',''],[],[])
#,('','',['',''],[],[])
]

appsfolder=['menu','desktop','apps']
directorytobackup=[]
programsfound=[]

directories=""
debug=True

#function that will do the backup itself
def backupspecific(progname,appdatafolder,listfolders,listfiles):
  
  global directories, directorytobackup, programsfound
  
  for topdirectory in directories:
	  
	    workingfolder=checkprogram(progname,topdirectory)
	    if workingfolder!="":
		  programsfound.append(progname)
		  
		  print "working folder is "+ workingfolder
		  #confirm the top level working folder under /media/xx/pandora/PAF  - it is not used after expect for path
	  
		  if checkappdata(appdatafolder,topdirectory)==False:
			print "the program " + progname +".pnd does not have a appdata folder so far." 
		  else:
			
			directoriesinappfolder=os.listdir(("/media/{0}/pandora/appdata/{1}".format(topdirectory,appdatafolder)))
			
			#special case of ALLFOLDER: where everything is to backup in the said folder
			if listfolders[0]=='*ALLFOLDER*':
				directorytobackup.append(("/media/{0}/pandora/appdata/{1}").format(topdirectory,appdatafolder))

			else:
			
				#marks folders to save
				for onefolder in directoriesinappfolder:
				  for foldertobackup in listfolders:
					if onefolder==foldertobackup:
					  print progname+":found folder "+ onefolder+" to backup"				  
					  directorytobackup.append(("/media/{0}/pandora/appdata/{1}/{2}").format(topdirectory,appdatafolder,onefolder))
					  #add the path worklist to backup where we will give the final instructions to zip in the end
	  
				#need to build functions for files as well
				for filetobackup in listfiles:
					result=[]
					result=glob.glob("/media/{0}/pandora/appdata/{1}/{2}".format(topdirectory,appdatafolder,filetobackup))
					if result!=[]:
						for resultat in result:
							directorytobackup.append(resultat)
			
			
#builds the archive files
def makearchivefile():
  
  global directorytobackup, directories, today, shutil
  
  eval=evaluatebackupsizebeforearchive()
  a=PyZenity.InfoMessage('The elements to backup amount to about {0} Mb. It will likely be a little smaller after archiving'.format(eval),timeout=10)

  sizeofarchive=0
  pathtoarchive=""
  print directories

  for topdirectory in directories:
  
	  if pathtoarchive=="":
		  archivename="BGSfile{0}-{1}-{2}.tar.gz".format(today.year,today.month,today.day)
		  if os.path.isfile("/media/{0}/{1}".format(topdirectory,archivename))==True :
			print "Careful, an archive with the same name already exists."
		  pathtoarchive="/media/{0}/{1}".format(topdirectory,archivename)
		  
		  tar = tarfile.open(pathtoarchive, "w:gz")
		  
		  #define nb of directories to backup
		  nbdirectoriestobackup=float(len(directorytobackup))
		  print nbdirectoriestobackup
		  
		  #there will probably be bugs inside this part... need to check it out!!
		  cmd = 'zenity --progress --text="Backing Up Games Saves..." --auto-close'
		  proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		  try:
		  	n=0.0
		  	for folder in directorytobackup:
		  		n+=1
		  		print n
				tar.add(folder)
				print "added "+folder
				progress=int(100*(float(n/nbdirectoriestobackup)))
				print progress
				#putain faut pas oublier le n pour zenity progress bar!!
				proc.stdin.write("{0}\n".format(progress))
			if not proc.returncode:
				print "Your job finished"
			else:
				print "You have cancelled"
		  except: 
		  	proc.terminate()
			
		  tar.close()
		  sizeofarchive=int((os.path.getsize(pathtoarchive))/(1024*1024))
		  a=PyZenity.InfoMessage('Backup has been completed as {0} in /media/{1}/. The file size is {2} Mb.It will now be duplicated on the other SD card (if you have another one inserted)'.format(archivename,topdirectory,sizeofarchive),timeout=15)
		
	  else: 
		if len(directories)>1:
			
			print pathtoarchive
			if returnfreespaceondrive('/media/{0}'.format(topdirectory))>sizeofarchive:
				try:
					shutil.copyfile(pathtoarchive,'/media/{0}/{1}'.format(topdirectory,archivename))
					print "Copy completed on the volume "+topdirectory
					a=PyZenity.InfoMessage('For redundancy purpose, {0} has also been copied to /media/{1}/'.format(archivename,topdirectory),timeout=3)
				except:
					a=PyZenity.InfoMessage('There was some issue during the duplication process. The duplication step will be skipped')
			else:
				a=PyZenity.InfoMessage('It appears that you lack free space on /media/{0}/ to copy the archive of {1} Mb. The duplication step will be skipped.'.format(topdirectory,sizeofarchive),timeout=3)

		else:
			a=PyZenity.InfoMessage('It appears you have only one SD Card inserted at the moment, and therefore the BGS file cannot be duplicated. Be aware you are exposed to a greater risk of data loss unless you duplicate this file somewhere else.',timeout=10)
			
			
def checkprogram(progname,directory):
  #returns folder if the PND is found in one of the appsfolder directory or "" if not found
  global appsfolder
  found=0
  
  for folder in appsfolder:
    if os.path.isfile("/media/{0}/pandora/{1}/{2}".format(directory,folder,progname))==True :
      print "Found "+ progname+ " in "+ folder+" in "+directory
      found+=1
  if found==0:
    return ""
  else:
    return folder

#checks if the related appfolder exists
def checkappdata(appdatafolder,directory):
  if os.path.isdir("/media/{0}/pandora/appdata/{1}".format(directory,appdatafolder))==True:
    return True
  else:
    return False

#checks if a certain folder exists
def checkfolderexists(path,foldername):
  if os.path.isdir(path+foldername):
    return True
  else:
    return False

def defineglobaldirectories():
  #define the top levels directories in /media and writes a global variable
  global directories, debug
  directories=os.listdir("/media")
  directories.remove("hdd")
  directories.remove("ram")
  
  for directory in directories:
	  if directory[0]==".":
		  directories.remove(directory)
  
  if debug==True: 
    print directories

#Start of restore function. First, find out how to read the name. 
def listarchivecontents(archivename,filtername):
	resultsarray=[]
	tar=tarfile.open(archivename)
	for filename in tar.getnames():
		if filtername in filename:
			#print filename
			resultsarray.append(filename)
			
	print resultsarray
	return resultsarray
	
#need to have function to sort array results after, and make a list of what can be recovered. Use the program definition in beginning.
#need to modify the main menu too


def extractsinglefile(member,keydirectory):
	#need to confirm before on which card to restore the data.	
	tarfile.extract(member,path=keydirectory)

	

#finds previous BGS files if they exist and ask to erase or not
def findpreviousbgs():
	global directories
	result=[]
	for topdirectory in directories:
		caca=glob.glob('/media/{0}/BGS*'.format(topdirectory))
		if caca!=[]:
			for element in caca:
				
				result.append(element)
	
	print result
	
	if result!=[]:
		resultstring=""
		sizetotal=0
		for element in result:
			resultstring+=element+" "
			sizetotal+=int((os.path.getsize(element))/(1024*1024))
		a=PyZenity.Question("I found previous BGS files: {0}.They are taking a total of {1} Mb in size. Ok to delete them and create new ones ?".format(resultstring,str(sizetotal)))
		if a==True:
			for element in result:
				os.remove(element)
			a=PyZenity.InfoMessage("Previous BGS files were deleted")
		else:
			a=PyZenity.InfoMessage("Previous BGS files were kept")					

#displays the list of programs found to be backed up for save data
def displayprogstobackup():
  global programsfound
  
  programsfoundstring=""
  for program in programsfound:
	  programsfoundstring+=program + " "
	  
  a=PyZenity.InfoMessage('Found the following to backup: {0}'.format(programsfoundstring),timeout=10)
  a=PyZenity.InfoMessage('Backup process will now start. Note that it may take a while if you have tons of large files and saves. Do not turn off your Pandora until completion',timeout=10)

#as the function name says... returns result in megabytes
def returnfreespaceondrive(drive):
	driveinfo=os.statvfs(drive)
	totalAvailSpace = int((driveinfo.f_bsize*driveinfo.f_bfree)/1024/1014)
	return totalAvailSpace

#will give an estimation of the size to backup before doing the actual archive
def evaluatebackupsizebeforearchive():
	global directorytobackup
	totalsizetop=0
	
	for directory in directorytobackup:
		totalsizetop+=getsize(directory)
	
	print totalsizetop	
	totalsizetop=int(totalsizetop/1024/1024)
	print totalsizetop
	return totalsizetop

#thanks stackoverflow!
def getsize(startpath):
	totalsize=0
	for dirpath, dirnames, filenames in os.walk(startpath):
		for f in filenames:
			fp=os.path.join(dirpath,f)
			totalsize+=os.path.getsize(fp)
	return totalsize
	
def uploadtoftp(file,filename):
	a=PyZenity.Question("You can also upload the archive to a FTP server for additionnal redundancy. Note that it may take a while depending on your connection and the size of your backup file. Proceed ?")
	if a==True:
		serveraddress=PyZenity.GetText("Please input your ftp server address (ftp.xxx.xxx)")
		username=PyZenity.GetText("Please specify your user name for your ftp access")
		password=PyZenity("Please insert your password for your ftp access",password=True)
		success=False
		try:
			session = ftplib.FTP(serveraddress,username,password)
			success=True
			
		except: 
			a=PyZenity.InfoMessage("The FTP connection did not work. Aborting.")
			success=False
			
		if success==True:
			file = open(file,'rb')                  # file to send
			session.storbinary('STOR {0}'.format(filename), file,8192,callbackftp)     # send the file
			file.close()                                    # close file and FTP
			session.quit()
			a=PyZenity.InfoMessage("FTP transfer complete.")
	else:
		pass


def callbackftp(p):
	print "I am a callback function"


#main program
def bgs():
  
  global listoftemplates
  a=PyZenity.InfoMessage('Welcome to BGS. This tool will backup your saved games from numerous emulators or native games, and save them in a single archive. That archive will then be saved on your SD Card and duplicated on your second SD card if you have any inserted, to fight the risk of data loss by redundancy.',timeout=15)
  defineglobaldirectories()
  
  findpreviousbgs()
    
  for programtobackup in listoftemplates:
    backupspecific(programtobackup[0],programtobackup[1],programtobackup[2],programtobackup[3])
  
  displayprogstobackup()
  print directorytobackup
  makearchivefile()
  
  a=PyZenity.InfoMessage('The application will now auto-close. Thanks for using it! Remember you should have these backups in case one of your card fails!',timeout=3)


bgs()
