class Settings(object):
    def __init__(self):
        self.serverAddress = "http://localhost:8989"
        self.division = "1"
        self.divisionStr = "division1"
        self.dataUpdateFreq = "10"
        self.mainDisplay = "Rankings"
        self.secondaryDisplay = "Matches"
        self.displayDivision = "Division 1"
        self.showInspections = False
        self.scrollSpeed = 270
    def getScrollSpeed(self):
        return self.scrollSpeed
    def setScrollSpeed(self,val):
        self.scrollSpeed = val
    def getServerAddress(self):
        return self.serverAddress
    def setServerAddress(self,val):
        self.serverAddress = val
    def getDivision(self):
        return self.division
    def setDivision(self,val):
        self.division = val
    def getDivisionStr(self):
        return self.divisionStr
    def setDivisionStr(self,val):
        self.divisionStr = val
    def getDataUpdateFreq(self):
        return self.dataUpdateFreq
    def setDataUpdateFreq(self,val):
        self.dataUpdateFreq = val
    def getMainDisplay(self):
        return self.mainDisplay
    def setMainDisplay(self,val):
        self.mainDisplay = val
    def getSecondDisplay(self):
        return self.secondaryDisplay
    def setSecondDisplay(self,val):
        self.secondaryDisplay = val
    def getDisplayDivision(self):
        return self.displayDivision
    def setDisplayDivision(self,val):
        self.displayDivision = val
    def getShowInspections(self):
        return self.showInspections
    def setShowInspections(self,val):
        self.showInspections = val