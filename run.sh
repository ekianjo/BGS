
#make a model for each save system : i.e. 
# Location (folder), filetype (extension), system (machine), game (name)
# Look for directories (emulators, known native games). List them in array.
# Go through each directory, list all files and their path. Apply filters if necessary (exceptions). 
# Make a tar archive or zip. 
# Complete!

#find / -name 'httpdocs' -type d
#the first parameter "/" is where to look, in this case "/" it's the entire system.

#-name could be -iname to ignore case

#also -type is not mandatory

#use : man find for more options

#tar cvzf directory.tar.gz directory

# tar: (c)reate g(z)ip (v)erbose (f)ile [filename.tar.gz] [contents]...
#tar -czvf /var/file/bkup.tar.gz /home/code/bots /var/config /var/system

# zip: (r)ecursive [filename.zip] [contents]...
#zip -r /var/file/bkup.zip /home/code/bots /var/config /var/system

# to find directories called back and check their total size.
# find . -name bak -type d | xargs du -ch
# -exec executes the command for each file found 
# (check the find(1) documentation). Piping to xargs lets you aggregate those 
# filenames and only run du once.

# filter out something finishing by swp, and not in es or en folders.
# find -mtime 0 -not \( -name '*.swp' -o -path './es*' -o -path './en*' \)
