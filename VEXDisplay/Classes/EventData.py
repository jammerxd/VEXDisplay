from collections import OrderedDict
import requests
import copy
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
        self.inspections_ns = 0
        self.inspections_p = 0
        self.inspections_c = 0
        self.inspections_t = 0
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
    

global EVENT_DATA 
EVENT_DATA = None
if(EVENT_DATA == None):
    EVENT_DATA = EventData()

