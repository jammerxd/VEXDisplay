import wx
import sys
from collections import OrderedDict
sys.path.append('..')
from ..Colors import *
from ..data import *
from rankLogoPanel_Main import *
from TeamRankPanel_Main import *
from ..drawables.fonts import *
from ..EventData import *

global RANK_PANEL_HEIGHT
global RANK_PANEL_DELTA_Y
RANK_PANEL_DELTA_Y = 1
RANK_PANEL_HEIGHT = 76
class RanksPanel(wx.Panel):
    global EVENT_DATA
    global RANK_PANEL_HEIGHT
    def __init__(self,parent=None,speed=270):
        wx.Panel.__init__(self,parent)
        self.SetSize((1300,900))
        self.SetPosition((25,875))
        self.SetBackgroundColour(COLORS["White"])
        self.rankPanels = OrderedDict()
        self.extraPanels = OrderedDict()
        self.SetDoubleBuffered(True)
        self.logoPanel = None
        
        self.curSponsorI = -1
        self.updatePositionsTimer = None
        self.changeLogoTimer = None
        self.lastRank = -1
        
        self.lastRankLoc = 0
        self.unshownRanks = OrderedDict()
        self.logoPatternOff = 0
        self.setupRankPanels(speed=speed)

        self.lastY = 0
    def setupRankPanels(self,redraw=False,speed=270):
        self.lastRank = -1
        self.yOff = 0
        self.isGray = False
        
        if len(EVENT_DATA.sponsors) > 0:
            self.curSponsorI = 0
            self.logoPanel = RankLogoPanel_Main(self,EVENT_DATA.sponsors[self.curSponsorI])
            self.logoPanel.Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
            self.logoPanel.SetBackgroundColour(COLORS["White"])
            self.logoPanel.Show()
            self.yOff += self.logoPanel.GetSize()[1]
        self.lastRankLoc = self.yOff
        for i in range(len(EVENT_DATA.ranks)):
            rank = str(i+1)
            
            if i < 14:
                self.rankPanels[rank] = TeamRankPanel_Main(self,rank)
                self.rankPanels[rank].Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
                if self.isGray:
                    self.rankPanels[rank].SetBackgroundColour(COLORS["White"])
                else:
                    self.rankPanels[rank].SetBackgroundColour(COLORS["vexBGDarkGray"])
                self.isGray = not self.isGray
                self.yOff += RANK_PANEL_HEIGHT
                self.lastRankLoc += RANK_PANEL_HEIGHT
                self.lastRank = i
                
            else:
                self.lastRankLoc += RANK_PANEL_HEIGHT
        

       
        


        if len(self.rankPanels) > 0:
            while len(self.rankPanels) + len(self.extraPanels) < 15:
                key = str(len(self.extraPanels)+1)
                self.extraPanels[key] = TeamRankPanel_Main(self)
                self.extraPanels[key].Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
                self.yOff += RANK_PANEL_HEIGHT
                self.extraPanels[key].SetBackgroundColour(COLORS["White"])




        self.updatePositionsTimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updatePositions,self.updatePositionsTimer)
        self.updatePositionsTimer.Start(1000.0/speed)
        self.changeLogoTimer =wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updateRankSponsorLogo,self.changeLogoTimer)
        self.changeLogoTimer.Start(10000)

                
    def updatePositions(self,evt=None):
        cancel = False
        for panel in self.rankPanels:
            panelRef = self.rankPanels[panel]

            if panelRef.GetPosition()[1] < (-1*panelRef.GetSize()[1]):
                newY = (int(panel)-1)*panelRef.GetSize()[1] + self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1]
                #if self.logoPanel != None:
                #    newY += self.logoPanel.GetSize()[1]
               
                if self.lastRank < len(EVENT_DATA.ranks)-1:
                        self.lastRank += 1
                else:
                    self.lastRank = 0

                if self.lastRank == 0:
                    self.logoPanel.Move((0,newY+(len(self.extraPanels)*RANK_PANEL_HEIGHT)+self.logoPatternOff),wx.SIZE_ALLOW_MINUS_ONE)
                    self.logoPatternOff = self.logoPanel.GetSize()[1]
                elif panel == "1":
                    self.logoPatternOff = 0
                newY += len(self.extraPanels)*RANK_PANEL_HEIGHT+self.logoPatternOff
                panelRef.Move((0,newY-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)

                panelRef.updateLabelTexts(str(self.lastRank+1))#update panel to show the new rank

                print str(panel) + " | "  + str(self.logoPatternOff) + " | " + str(panelRef.GetPosition()[1]+RANK_PANEL_DELTA_Y)
            else:
                panelRef.Move((0,panelRef.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)



        for i in range(len(self.extraPanels)):
            panelRef = self.extraPanels[str(i+1)]
            if panelRef.GetPosition()[1] < (-1*panelRef.GetSize()[1]):
                #newY = i*panelRef.GetSize()[1] + self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1]
                newY = (i+1)*RANK_PANEL_HEIGHT + self.rankPanels[str(len(EVENT_DATA.ranks))].GetPosition()[1]

                panelRef.Move((0,newY),wx.SIZE_ALLOW_MINUS_ONE)
            else:
                panelRef.Move((0,panelRef.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)

        if self.logoPanel != None:
            self.logoPanel.Move((0,self.logoPanel.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE) 
            
    def regenScroll(self):
        self.updatePositionsTimer.Stop()
        self.changeLogoTimer.Stop()
        if self.logoPanel != None:
            self.logoPanel.Destroy()
            self.logoPanel = None
        for panel in self.rankPanels:
            self.rankPanels[panel].Destroy()
        for panel in self.extraPanels:
            self.extraPanels[panel].Destroy()
        self.Unbind(wx.EVT_TIMER,self.changeLogoTimer,handler=self.updateRankSponsorLogo)
        self.Unbind(wx.EVT_TIMER,self.updatePositionsTimer,handler=self.updatePositions)
                    
        self.rankPanels = OrderedDict()
        self.extraPanels = OrderedDict()
        self.setupRankPanels(redraw = True)
    def updateRankSponsorLogo(self,evt):
        if self.curSponsorI != -1 and self.logoPanel != None:
            if self.curSponsorI == (len(EVENT_DATA.sponsors)-1):
                self.curSponsorI = 0
            else:
                self.curSponsorI += 1
                
            self.logoPanel.updateImg(EVENT_DATA.sponsors[self.curSponsorI])
            self.logoPanel.SetBackgroundColour(COLORS["White"])
        evt.Skip()
