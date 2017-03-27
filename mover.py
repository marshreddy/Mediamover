#an app to read names of files in a folder and sort those into pre-made directories
#Marsh Reddy
#20/02/2015

import os
import shutil
import re
import logging
import datetime
import sys

#Before you get to using this little script, the first thing you'll want to do is set filepaths:

#WINDOWS
#source is the file the python script is sitting in
#mediasource = 'f:\\torrents\\complete\\'
#mediadestination = "f:\\Media\\"
#dailyshowdestination = "f:\\Media\\Series\\The Daily Show"
#mediadumpfolder = "f:\\Mediadump\\"

# OSX Testing:
mediasource = "/Users/media/Torrents/Complete/"
mediadestination = "/Users/media/"
dailyshowdestination = "/Users/media/Series/The Daily Show/"
mediadumpfolder = "/Users/media/Mediadump/"

logfile = open('/Users/media/Dropbox/MediaMachineFileMover/Media Mover/mediamoverlogfile.log', 'a')

def startlogging(logfile):
    f.write('logging')
    
def logthismv(file, destination):
    now = datetime.datetime.now()
    logfile.write('%s : ' 'File : %s Moved to %s \n' %(now, file, destination))
    #logging.basicConfig(format='%(asctime)s %(message)s')
    #logging.info(' : ' 'File : ' + file + ' Moved to : ' + destination)

def logthisrm(file):
    now = datetime.datetime.now()
    logfile.write('%s : ' 'File : %s DELETED!!\n' %(now, file))

#get season number
def getseasonnr(filename):
    match = re.findall(r"(?:s|season)(\d{2})", filename, re.I)
    if match:               
        return match[0]
  
    
#get episode number
def getepisodenr(filename):
    match = re.findall(r"(?:e|x|episode|\n)(\d{2})", filename, re.I)
    if match:
        return match[0]

   

#Get and split name of the show
def getcleanepisodename(filename):
    if getseasonnr(filename):
        ssnindex = (filename.find("s" + getseasonnr(filename) + "e" + getepisodenr(filename)))
        correctfoldername = filename[0:ssnindex].replace(".", " ").title().strip()
        return correctfoldername

    else:
        
        return False

#iterate through the folder    
def iteratefolder(source, destination):
   # print (source, destination)

    folder = [name for name in os.listdir(source)]
    
    for i in folder:
        if (i.endswith('.py')== False and i.endswith ('DS_Store')==False and i.endswith('.db')==False and  not 'mediamover' in i):            
            if i.lower().find("torrenting")!=-1:
                print (source +i)
                print (source +i[(i.find(" - ")+3):])
                os.rename(source+i, source +i[(i.find(" - ")+3):])


    folder = [name for name in os.listdir(source)]
    for i in folder:
        
        if (i.endswith('.py')== False and i.endswith ('DS_Store')==False and i.endswith('.db')==False and  not 'mediamover' in i):         
            #fileoriginpath = source + "\\" + i #Windows
            fileoriginpath = source + i #OSX
            i = i.lower()
            
            print(i)                       
            season = "Season %s" % getseasonnr(i)
            Title = getcleanepisodename(i)
            
            if Title:
                #seriesdirectory = destination+ "Series\\"+Title+"\\"+season #Windows
                seriesdirectory = destination+ "Series/"+Title+"/"+season #OSX
            
                if not os.path.exists(seriesdirectory):
                    os.makedirs(seriesdirectory) 
                    try:
                        shutil.move(fileoriginpath, seriesdirectory)
                        logthismv(fileoriginpath, seriesdirectory)
                    except:
                        shutil.move(fileoriginpath, mediadumpfolder)                    
                        logthisrm(fileoriginpath)
                else:
                    try:
                        shutil.move(fileoriginpath, seriesdirectory)
                        logthismv(fileoriginpath, seriesdirectory)
                    except:
                        shutil.move(fileoriginpath, mediadumpfolder)                    
                        logthisrm(fileoriginpath)
            else:
                if i.find("daily.show")!=-1:
                    print (i)
                    print(i.find("daily.show"))
                    if not os.path.exists(dailyshowdestination):
                        os.makedirs(dailyshowdestination)
                    shutil.move(fileoriginpath,dailyshowdestination)
                    logthismv(fileoriginpath, dailyshowdestination)
                else:
                    #moviedirectory = destination+ "Movies\\" #Windows
                    moviedirectory = destination+ "Movies/" #OSX
                    shutil.move(fileoriginpath, moviedirectory)
                    logthismv(fileoriginpath, moviedirectory)
    print ('completed')
    logfile.close()


iteratefolder(mediasource, mediadestination)


         
      


        
        
    
    
