#File Finder
class ReadFiles(object):
    def __init__(self,dir_name,type_file):
        self.dir_name=dir_name
        self.type_file=type_file
    def findFiles(self):
        self.allMyFiles=[]
        from os import listdir
        self.theSuffix = ".txt"
        filenames = listdir(self.dir_name)
        for file in filenames:
            if file.endswith(".csv"):
                self.allMyFiles.append(file)
#1 File Reader
class Get1TxtFileData(object):
    def __init__(self,file_name):
        self.file_name=file_name
    def readandreturnlist(self):
        Txtfile=self.file_name
        linelist = []
        with open(Txtfile) as f:
            for line in f:
                linelist.append(line)
        return linelist
