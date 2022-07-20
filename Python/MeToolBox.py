
class HomeTools ():


    def convert_epoch_est(self,epoch,format):
        from datetime import datetime, timezone
        utc_time = datetime.fromtimestamp(epoch, timezone.utc)
        local_time = utc_time.astimezone()
        #print(local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))
        #print(local_time.strftime("%Y%m%d%H%M%S%Z"))
        return local_time.strftime(format)


    def get_current_time(self, format="%Y%m%d-%H%M%S"):
        from time import strftime
        return strftime(format)
    
    def get_epoch():
        import time
        return time.time 

    def get_version_w_date(self, version="1.0.0"):
        # will get the date of the last time the file was saved

        from pathlib import Path
        from sys import argv

        caller = self.getCaller()
        filename = caller.filename
        fname = Path(filename)
        assert fname.exists()
        stat = fname.stat()
        version_timestamp = self.convert_epoch_est(stat.st_atime, ".%Y.%m.%d_%H:%M:%S_%Z")
        return version + version_timestamp
        

    def HowToUse(self, desc, title, author, version):
        str = \
            "Script Name: " + self.getCaller().filename + "\n" + \
            "Title:       " + title + "\n" + \
            "Version:     " + version + "\n" + \
            "Description: " + desc + "\n" + \
            "Designed by: " + author + "\n"
        print(str)

    def clear_screen(self):
        from os import system, name
        # for windows
        if name == 'nt':
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else:
            _ = system('clear') 

    def getCaller (self):
        from inspect import getframeinfo, stack
        return getframeinfo(stack()[2][0])

    def getFileName (self):
        
        caller = self.getCaller()
        #this is for linux to be able to obtain the name of the file only
        filename = caller.filename.split("/")[-1]
        #this is for windows to be able to obtain the name of the file only
        return filename.split("\\")[-1]

    def DEBUG_PRINT(self, level=0,action=0,msg="Marker"):
        # Similar to print() but it gives 
        # a timestamp, module that it ran from, and the line number
        # you can also control the print level you want in case 
        # the script is to noisy, the level can be adjusted to be
        # verbose or not
        # great for troubleshooting
        caller = self.getCaller()
        #this is for linux to be able to obtain the name of the file only
        filename = caller.filename.split("/")[-1]
        #this is for windows to be able to obtain the name of the file only
        filename = filename.split("\\")[-1]
        ctime = self.current_time("%Y-%m-%d %H:%M:%S")
        if (level>=action):
            print("%s:(%s L%d) %s" % (ctime,filename, caller.lineno, msg))