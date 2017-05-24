from Settings import *
from EventData import *
import copy
import json
import threading
import time
import wx
from data import *
from threading import Thread

class App(object):
    global EVENT_DATA
    def __init__(self,inspectionCompleteCallback = None):
        
        self.doUpdateData = False
        self.settings = Settings()
        self.lastRun = time.time()
        self.inspectionCompleteCallback = inspectionCompleteCallback
        self.thread = None
    def getEventName(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/eventInfo")
            jsonObj = json.loads(response)
            EVENT_DATA.setEventName(jsonObj["eventName"])
        except Exception,ex:
            doNothing = True
    def getDivisionName(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr())
            jsonObj = json.loads(response)
            EVENT_DATA.setDivisionName(jsonObj["name"])
        except Exception,ex:
            doNothing = True
    def getDivisionRanks(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/rankings")
            jsonObj = json.loads(response)
            try:
                ranksRaw = jsonObj["result"]
                for i in range(len(jsonObj["result"])):
                    rankStr = str(i+1)
                    
                    EVENT_DATA.ranks[rankStr] = ranksRaw[i]
                    if ranksRaw[i]["teamNumber"] in EVENT_DATA.teams:
                        EVENT_DATA.teams[ranksRaw[i]["teamNumber"]].setRank(rankStr)
                ##for i in range(len(EVENT_DATA.ranks)):
                ##    if str(i+1) not in jsonObj:
                ##        del EVENT_DATA.ranks[str(i+1)]
            except Exception,ex:
                doNothing = True
        except Exception,ex:
            doNothing = True
    def getDivisionTeams(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/teams")
            jsonObj = json.loads(response)
            try:
                teamsRaw = jsonObj["result"]
                for teamRaw in teamsRaw:
                    teamNum = teamRaw["teamNumber"]
                    if teamNum not in EVENT_DATA.teams:
                        EVENT_DATA.teams[teamNum] = Team()
                    EVENT_DATA.teams[teamNum].setNumber(teamRaw["teamCity"])
                    EVENT_DATA.teams[teamNum].setDivision(teamRaw["divisionID"])
                    EVENT_DATA.teams[teamNum].setSchool(teamRaw["teamSchool"])
                    EVENT_DATA.teams[teamNum].setLosses(teamRaw["losses"])
                    EVENT_DATA.teams[teamNum].setInspectionStatus(teamRaw["inspectionStatus"])
                    EVENT_DATA.teams[teamNum].setName(teamRaw["teamName"])
                    EVENT_DATA.teams[teamNum].setCheckedIn(teamRaw["checkedIn"])
                    EVENT_DATA.teams[teamNum].setCountry(teamRaw["teamCountry"])
                    EVENT_DATA.teams[teamNum].setSPS(teamRaw["sps"])
                    EVENT_DATA.teams[teamNum].setDivisionName(teamRaw["divisionName"])
                    EVENT_DATA.teams[teamNum].setNumber(teamRaw["teamNumber"])
                    EVENT_DATA.teams[teamNum].setRank(teamRaw["rank"])
                    EVENT_DATA.teams[teamNum].setWPS(teamRaw["wps"])
                    EVENT_DATA.teams[teamNum].setState(teamRaw["teamState"])
                    EVENT_DATA.teams[teamNum].setLocation(teamRaw["teamLocation"])
                    EVENT_DATA.teams[teamNum].setWins(teamRaw["wins"])
                    EVENT_DATA.teams[teamNum].setTies(teamRaw["ties"])
                    EVENT_DATA.teams[teamNum].setAPS(teamRaw["aps"])
            except Exception,ex:
                doNothing = True
        except Exception,ex:
            doNothing = True

    def getDivisionMatches(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/matches")
            jsonObj = json.loads(response)
            EVENT_DATA.allMatchesScored = jsonObj["allMatchesScored"]
            
            for obj in jsonObj["result"]:
                matchNum = obj["matchString"]
                if matchNum not in EVENT_DATA.matches:
                    EVENT_DATA.matches[matchNum] = Match()
                EVENT_DATA.matches[matchNum].setScored(obj["scored"])
                EVENT_DATA.matches[matchNum].setBlueScore(obj["blueScore"])
                EVENT_DATA.matches[matchNum].setRed2(obj["red2"])
                EVENT_DATA.matches[matchNum].setRedScore(obj["redScore"])
                EVENT_DATA.matches[matchNum].setInstance(obj["instance"])
                EVENT_DATA.matches[matchNum].setMatch(obj["matchString"])
                EVENT_DATA.matches[matchNum].setRed3(obj["red3"])
                EVENT_DATA.matches[matchNum].setDivision(obj["division"])
                EVENT_DATA.matches[matchNum].setRed1(obj["red1"])
                EVENT_DATA.matches[matchNum].setScheduledTime(obj["timeScheduled"])
                if(EVENT_DATA.matches[matchNum].getScheduledTime() != "0"):
                    EVENT_DATA.matches[matchNum].setScheduledTime( time.strftime("%I:%M %p", time.localtime(int(EVENT_DATA.matches[matchNum].getScheduledTime()))))
                    if(EVENT_DATA.matches[matchNum].getScheduledTime()[0] == "0"):
                        EVENT_DATA.matches[matchNum].setScheduledTime(EVENT_DATA.matches[matchNum].getScheduledTime()[1:].upper())
                EVENT_DATA.matches[matchNum].setBlue1(obj["blue1"])
                EVENT_DATA.matches[matchNum].setBlue3(obj["blue3"])
                EVENT_DATA.matches[matchNum].setBlue2(obj["blue2"])
                EVENT_DATA.matches[matchNum].setMatchNum(obj["matchNum"])
                EVENT_DATA.matches[matchNum].setField(obj["field"])
                EVENT_DATA.matches[matchNum].setRound(obj["round"])
            for i in range(0,8):
                if i < len(jsonObj["show"]):
                    EVENT_DATA.showMatches[i] = jsonObj["show"][i]
                else:
                    if i in EVENT_DATA.showMatches:
                        del EVENT_DATA.showMatches[i]
        except Exception,ex:
            doNothing = True
    def getSkills(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/skills")
            jsonObj = json.loads(response)["result"]
            for obj in jsonObj:
                if obj["rank"] not in EVENT_DATA.skillsRanks:
                    EVENT_DATA.skillsRanks[obj["rank"]] = Skills()
                EVENT_DATA.skillsRanks[obj["rank"]].setName(obj["teamName"])
                EVENT_DATA.skillsRanks[obj["rank"]].setSkillsProgScore(obj["highProg"])
                EVENT_DATA.skillsRanks[obj["rank"]].setSkillsDriverScore(obj["highDriver"])
                EVENT_DATA.skillsRanks[obj["rank"]].setSkillsRank(obj["rank"])
                EVENT_DATA.skillsRanks[obj["rank"]].setTeam(obj["teamNumber"])
                EVENT_DATA.skillsRanks[obj["rank"]].setSkillsDriverAttempts(obj["driverAttempts"])
                EVENT_DATA.skillsRanks[obj["rank"]].setSkillsProgAttempts(obj["progAttempts"])
                EVENT_DATA.skillsRanks[obj["rank"]].setTotalSkillsScore(obj["totalScore"])
        except Exception,ex:
            doNothing = True
    def getInspections(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/inspections")
            jsonObj = json.loads(response)
            EVENT_DATA.inspections_ns = jsonObj["NotStarted"]
            EVENT_DATA.inspections_p = jsonObj["PartiallyCompleted"]
            EVENT_DATA.inspections_c = jsonObj["Completed"]
            EVENT_DATA.inspections_t = jsonObj["Total"]
            for team in EVENT_DATA.teams:
                EVENT_DATA.teams[team].setInspectionStatus(jsonObj["teams"][team])
                EVENT_DATA.inspections[team] = jsonObj["teams"][team]
            if EVENT_DATA.inspections_t == EVENT_DATA.inspections_c:
                try:
                    self.inspectionCompleteCallback()   
                except Exception,ex:
                    doNothing = True
        except Exception,ex:
            doNothing = True

    def getCheckIns(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/checkins")
            jsonObj = json.loads(response)
            try:
                checkinsRaw = jsonObj
                for team in EVENT_DATA.teams:
                    EVENT_DATA.teams[team].setCheckedIn(checkinsRaw[team])
                    EVENT_DATA.checkIns[team] = checkinsRaw[team]
            except Exception,ex:
                doNothing = True
        except Exception,ex:
            doNothing = True
    def collectData(self,evt):
        #if self.thread != None:
        #    self.thread.join()
        #    self.thread = None
        self.thread = threading.Thread(target=self.DocollectData)
        self.thread.setDaemon(True)
        self.thread.start()
        evt.Skip()

        

    def DocollectData(self,x=None):
        #print "Collecting data"
        if (self.doUpdateData):
            self.getEventName()
        if (self.doUpdateData):
            self.getDivisionName()
        if (self.doUpdateData):
            self.getDivisionTeams()
        if (self.doUpdateData):
            self.getDivisionRanks()
        if (self.doUpdateData):
            self.getDivisionMatches()
        if (self.doUpdateData):
            self.getCheckIns()
        if (self.doUpdateData):
            self.getInspections()
        if (self.doUpdateData):
            self.getSkills()
        
    def beginCollectData(self):
        self.doUpdateData = True

        
    def stopDataCollection(self):
        self.doUpdateData = False