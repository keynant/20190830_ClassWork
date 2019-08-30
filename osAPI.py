import os

class SmartDir():
    def smartMkDir():
        while True:
            try:
                dirName = input ("Enter a single directory name, alphanumeric only: ")
                os.mkdir(dirName)
                break
            except:
                print ("Error in dir name")
