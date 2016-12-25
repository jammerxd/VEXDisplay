from collections import OrderedDict
import requests
import copy
import glob
import os
class EventData(object):
    def __init__(self):
        self.eventName = ""
        self.divisionName = ""
        self.teams = {}
        self.inspections = {}
        self.checkIns = {}
        self.ranks = OrderedDict()
        self.skillsRanks = OrderedDict()
        self.matches = OrderedDict()
        self.showMatches = OrderedDict()
        self.inspections_ns = 0
        self.inspections_p = 0
        self.inspections_c = 0
        self.inspections_t = 0
        self.allMatchesScored = False
        self.sponsors = OrderedDict()
        #self.getSponsors()
    def getRequest(self,url):
        r = requests.get(url)
        return r.content
    def getEventName(self):
        return self.eventName
    def setEventName(self,val):
        self.eventName = val
    def getDivisionName(self):
        return self.divisionName
    def setDivisionName(self,val):
        self.divisionName = val
    
    def getSponsors(self):
        i = 0
        self.sponsors = OrderedDict()
        for imgFile in glob.glob(os.path.join(os.getcwd(),"Sponsors","*.png")):        
            self.sponsors[i] = imgFile
            i += 1
        if len(self.sponsors) >= 3:
            for imgFile in glob.glob(os.path.join(os.getcwd(),"Sponsors","*.png")):        
                self.sponsors[i] = imgFile
                i += 1
        for imgFile in glob.glob(os.path.join(os.getcwd(),"Resources","Images","Logos","Medium","*.png")):
            self.sponsors[i] = imgFile
            i += 1
        
    

global EVENT_DATA 
EVENT_DATA = None
if(EVENT_DATA == None):
    EVENT_DATA = EventData()
    EVENT_DATA.getSponsors()
     

