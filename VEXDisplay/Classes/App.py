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
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/eventName")
            jsonObj = json.loads(response)
            EVENT_DATA.setEventName(jsonObj["name"])
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
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/ranks")
            jsonObj = json.loads(response)
            try:
                ranksRaw = jsonObj
                for i in range(len(jsonObj)):
                    rankStr = str(i+1)
                    if rankStr not in EVENT_DATA.ranks:
                        EVENT_DATA.ranks[rankStr] = ranksRaw[rankStr]
                    if ranksRaw[rankStr] in EVENT_DATA.teams:
                        EVENT_DATA.teams[ranksRaw[rankStr]].setRank(rankStr)
            except Exception,ex:
                doNothing = True
        except Exception,ex:
            doNothing = True
    def getDivisionTeams(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/" + self.settings.getDivisionStr() + "/teams")
            jsonObj = json.loads(response)
            try:
                teamsRaw = jsonObj["teams"]
                for teamRaw in teamsRaw:
                    teamNum = teamRaw["number"]
                    if teamNum not in EVENT_DATA.teams:
                        EVENT_DATA.teams[teamNum] = Team()
                    EVENT_DATA.teams[teamNum].setNumber(teamRaw["town"])
                    EVENT_DATA.teams[teamNum].setDivision(teamRaw["division"])
                    EVENT_DATA.teams[teamNum].setSchool(teamRaw["school"])
                    EVENT_DATA.teams[teamNum].setLosses(teamRaw["losses"])
                    EVENT_DATA.teams[teamNum].setInspectionStatus(teamRaw["inspectionStatus"])
                    EVENT_DATA.teams[teamNum].setName(teamRaw["name"])
                    EVENT_DATA.teams[teamNum].setCheckedIn(teamRaw["checkedIn"])
                    EVENT_DATA.teams[teamNum].setCountry(teamRaw["country"])
                    EVENT_DATA.teams[teamNum].setSPS(teamRaw["sps"])
                    EVENT_DATA.teams[teamNum].setDivisionName(teamRaw["divisionName"])
                    EVENT_DATA.teams[teamNum].setNumber(teamRaw["number"])
                    EVENT_DATA.teams[teamNum].setRank(teamRaw["rank"])
                    EVENT_DATA.teams[teamNum].setWPS(teamRaw["wps"])
                    EVENT_DATA.teams[teamNum].setState(teamRaw["state"])
                    EVENT_DATA.teams[teamNum].setLocation(teamRaw["location"])
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
            
            for obj in jsonObj["matches"]:
                matchNum = obj["match"]
                if matchNum not in EVENT_DATA.matches:
                    EVENT_DATA.matches[matchNum] = Match()
                EVENT_DATA.matches[matchNum].setScored(obj["scored"])
                EVENT_DATA.matches[matchNum].setBlueScore(obj["blueScore"])
                EVENT_DATA.matches[matchNum].setBlueNearCubes(obj["blueNearCubes"])
                EVENT_DATA.matches[matchNum].setRed2(obj["red2"])
                EVENT_DATA.matches[matchNum].setRedNearCubes(obj["redNearCubes"])
                EVENT_DATA.matches[matchNum].setRedLowRobots(obj["redLowRobots"])
                EVENT_DATA.matches[matchNum].setBlueNearStars(obj["blueNearStars"])
                EVENT_DATA.matches[matchNum].setRedNearStars(obj["redNearStars"])
                EVENT_DATA.matches[matchNum].setBlueFarStars(obj["blueNearStars"])
                EVENT_DATA.matches[matchNum].setRedScore(obj["redScore"])
                EVENT_DATA.matches[matchNum].setWinner(obj["winner"])
                EVENT_DATA.matches[matchNum].setRedFarStars(obj["redFarStars"])
                EVENT_DATA.matches[matchNum].setRedHighRobots(obj["redHighRobots"])
                EVENT_DATA.matches[matchNum].setInstance(obj["instance"])
                EVENT_DATA.matches[matchNum].setRedAuto(obj["redAuto"])
                EVENT_DATA.matches[matchNum].setRedSit(obj["redSit"])
                EVENT_DATA.matches[matchNum].setMatch(obj["match"])
                EVENT_DATA.matches[matchNum].setRed3(obj["red3"])
                EVENT_DATA.matches[matchNum].setDivision(obj["division"])
                EVENT_DATA.matches[matchNum].setRed1(obj["red1"])
                EVENT_DATA.matches[matchNum].setRedFarCubes(obj["redFarCubes"])
                EVENT_DATA.matches[matchNum].setScheduledTime(obj["scheduledTime"])
                EVENT_DATA.matches[matchNum].setBlueSit(obj["blueSit"])
                EVENT_DATA.matches[matchNum].setBlueAuto(obj["blueAuto"])
                EVENT_DATA.matches[matchNum].setBlueHighRobots(obj["blueHighRobots"])
                EVENT_DATA.matches[matchNum].setBlue1(obj["blue1"])
                EVENT_DATA.matches[matchNum].setBlue3(obj["blue3"])
                EVENT_DATA.matches[matchNum].setBlue2(obj["blue2"])
                EVENT_DATA.matches[matchNum].setBlueLowRobots(obj["blueLowRobots"])
                EVENT_DATA.matches[matchNum].setMatchNum(obj["matchNum"])
                EVENT_DATA.matches[matchNum].setBlueFarCubes(obj["blueFarCubes"])
                EVENT_DATA.matches[matchNum].setField(obj["field"])
                EVENT_DATA.matches[matchNum].setRound(obj["round"])
            for i in range(0,8):
                if i < len(jsonObj["show"]):
                    EVENT_DATA.showMatches[i] = jsonObj["show"][i]
        except Exception,ex:
            doNothing = True
    def getSkills(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/skills")
            jsonObj = json.loads(response)["skills"]
            for obj in jsonObj:
                if obj["skillsRank"] not in EVENT_DATA.skillsRanks:
                    EVENT_DATA.skillsRanks[obj["skillsRank"]] = Skills()
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setName(obj["name"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setSkillsProgScore(obj["skillsProgScore"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setSkillsDriverScore(obj["skillsDriverScore"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setSkillsRank(obj["skillsRank"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setTeam(obj["team"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setSkillsDriverAttempts(obj["skillsDriverAttempts"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setSkillsProgAttempts(obj["skillsProgAttempts"])
                EVENT_DATA.skillsRanks[obj["skillsRank"]].setTotalSkillsScore(obj["totalSkillsScore"])
        except Exception,ex:
            doNothing = True
    def getInspections(self):
        try:
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/inspections")
            jsonObj = json.loads(response)
            EVENT_DATA.inspections_ns = jsonObj["NotStarted"]
            EVENT_DATA.inspections_p = jsonObj["Partial"]
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
            response = EVENT_DATA.getRequest(self.settings.getServerAddress() + "/checkins")
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
        self.thread = threading.Thread(target=self.DocollectData)
        self.thread.setDaemon(True)
        self.thread.start()

        

    def DocollectData(self,x=None):
        print "Collecting data"
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