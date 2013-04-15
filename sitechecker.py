#!/usr/local/bin/python2.7

import urllib, urllib2, time
import sys

class CheckerRequest(object):
    
    def __init__(self):
        self.__starttime=0
        self.__stoptime=0
        self.__url=""
        self.__responseszie=0
        self.__responsecode=0
        self.__down=False

    def getDuration(self):
        return self.__stoptime - self.__starttime

    def getURL(self):
        return self.__url

    def getResponseSize(self):
        return self.__responsesize

    def getResponseCode(self):
        return self.__responsecode

    def setURL(self, url):
        self.__url = url

    def __getCurrentMillis(self):
        return int(round(time.time() * 1000))

    def runTest(self):
        try:
            self.__starttime = self.__getCurrentMillis()

            req = urllib.urlopen(self.__url)
            response = req.read()

            if req.geturl() != self.__url:
                self.__down=True
                return False

            self.__responsecode = req.getcode()
            self.__responsesize = len(response)
            

            self.__stoptime = self.__getCurrentMillis()
            self.__down=False
            return True
        except:
            self.__down=True
            return False
    
    def getDomain(self):
        splitted = self.__url.split("/")
        domain = splitted[2]
        return domain
         
    def saveTest(self):
        file = open("log/"+self.getDomain()+".log","a")
        if self.__down:
            file.write("down"+"|"+str(int(time.time()))+"|||"+"\n")
        else:
            file.write("up"+"|"+str(int(time.time()))+"|"+str(self.__responsecode)+"|"+str(self.__responsesize)+"|"+str(self.getDuration())+"\n")
        file.close()    


if __name__ == "__main__":
    chckr = CheckerRequest()
    while True:
        for url in open("sites.txt","r").readlines():
            chckr.setURL(url.strip())
            print url.strip()
            if chckr.runTest():
                print chckr.getDuration()
                print chckr.getResponseSize()
                print chckr.getResponseCode()
            else:
                print "Down"
            chckr.saveTest()
        time.sleep(60)
