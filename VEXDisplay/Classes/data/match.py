class Match(object):
    def __init__(self):
        self.division = ""
        self.round = ""
        self.instance = ""
        self.matchNum = ""
        self.field = ""
        self.red1 = ""
        self.red2 = ""
        self.red3 = ""
        self.blue1 = ""
        self.blue2 = ""
        self.blue3 = ""
        self.redScore = ""
        self.blueScore = ""
        self.scored = False
        self.winner = ""
        self.scheduledTime = ""
        self.match = ""
    def getDivision(self):
        return self.division
    def setDivision(self,val):
        self.division = val
    def getRound(self):
        return self.round
    def setRound(self,val):
        self.round = val
    def getInstance(self):
        return self.instance
    def setInstance(self,val):
        self.instance = val
    def getMatchNum(self):
        return self.matchNum
    def setMatchNum(self,val):
        self.matchNum = val
    def getField(self):
        return self.field
    def setField(self,val):
        self.field = val
    def getRed1(self):
        return self.red1
    def setRed1(self,val):
        self.red1 = val
    def getRed2(self):
        return self.red2
    def setRed2(self,val):
        self.red2 = val        
    def getRed3(self):
        return self.red3
    def setRed3(self,val):
        self.red3 = val   
    def getBlue1(self):
        return self.blue1
    def setBlue1(self,val):
        self.blue1 = val
    def getBlue2(self):
        return self.blue2
    def setBlue2(self,val):
        self.blue2 = val    
    def getBlue3(self):
        return self.blue3
    def setBlue3(self,val):
        self.blue3 = val        
    def getRedScore(self):
        return self.redScore
    def setRedScore(self,val):
        self.redScore = val
    def getBlueScore(self):
        return self.blueScore
    def setBlueScore(self,val):
        self.blueScore = val
    def getScored(self):
        return self.scored
    def setScored(self,val):
        self.scored = val
    def getScheduledTime(self):
        return self.scheduledTime
    def setScheduledTime(self,val):
        self.scheduledTime = val
    def getMatch(self):
        return self.match
    def setMatch(self,val):
        self.match = val