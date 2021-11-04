import os
from shutil import copyfile
from pathlib import Path

def getCopy(dbPath,ext):
    
    #set path of output folder where copy of original db will go with summary and plot(s)
    path = str(os.getcwd()) + "/output"
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    dbPath_out = path + "/" + Path(dbPath).stem + "." + ext
    
    #create copy in local output folder
    copyfile(dbPath, dbPath_out)
    
    return dbPath_out