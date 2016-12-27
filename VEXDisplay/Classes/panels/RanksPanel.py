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

class RanksPanel(wx.Panel):
    global EVENT_DATA
    def __init__(self,parent=None,speed=270):
        wx.Panel.__init__(self,parent)
        self.SetSize((1300,900))
        self.SetPosition((25,875))
        self.SetBackgroundColour(COLORS["White"])
        self.rankPanels = OrderedDict()
        self.extraPanels = OrderedDict()
        self.positionY = 0
        self.SetDoubleBuffered(True)
        self.logoPanel = None
        
        self.curSponsorI = -1
        self.updatePositionsTimer = None
        self.changeLogoTimer = None
        self.setupRankPanels(speed=speed)
    def setupRankPanels(self,redraw=False,speed=270):
        self.yOff = 0
        self.isGray = False
        for rank in EVENT_DATA.ranks:
            if rank not in self.rankPanels:
                self.rankPanels[rank] = TeamRankPanel_Main(self,rank)
                self.rankPanels[rank].Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
                if self.isGray:
                    self.rankPanels[rank].SetBackgroundColour(COLORS["White"])
                else:
                    self.rankPanels[rank].SetBackgroundColour(COLORS["vexBGLighterGray"])
                self.isGray = not self.isGray
                self.yOff += 90
        if len(self.rankPanels) > 0:
            while ((90*len(self.rankPanels)) + (90*len(self.extraPanels))) < 990:
                key = str(len(self.extraPanels)+1)
        
                self.extraPanels[key] = TeamRankPanel_Main(self)
                self.extraPanels[key].Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
                self.yOff += 90
                self.extraPanels[key].SetBackgroundColour(COLORS["White"])
        if len(EVENT_DATA.sponsors) > 0:
            self.curSponsorI = 0
            self.logoPanel = RankLogoPanel_Main(self,EVENT_DATA.sponsors[self.curSponsorI])
            self.logoPanel.Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
            self.logoPanel.SetBackgroundColour(COLORS["White"])
            self.logoPanel.Show()

        self.positionY = self.yOff-90
        self.updatePositionsTimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updatePositions,self.updatePositionsTimer)
        #self.updatePositionsTimer.Start(1000.0/speed)
        self.changeLogoTimer =wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updateRankSponsorLogo,self.changeLogoTimer)
        self.changeLogoTimer.Start(10000)
        #self.updatePositionsTimer.Start(500)
        #self.logoPanel = RankLogoPanel_Main(self,EVENT_DATA.sponsors[0])
        wx.CallAfter(self.updatePositions)
                
    def updatePositions(self,evt=None):
        cancel = False
        for i in range(len(EVENT_DATA.ranks)):
            if str(i+1) in self.rankPanels:
                panelRef = self.rankPanels.items()[i][1]

                if self.rankPanels[str(i+1)].GetPosition()[1] < (-1*self.rankPanels[str(i+1)].GetSize()[1]):
                    newY = i*panelRef.GetSize()[1] + self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1]
                    if self.logoPanel != None:
                        newY += self.logoPanel.GetSize()[1]
                    newY += len(self.extraPanels)*90
                    panelRef.Move((0,newY-1),wx.SIZE_ALLOW_MINUS_ONE)
                    #if panelRef.rank in EVENT_DATA.ranks:
                    #    panelRef.updateLabelTexts()
                    #else:
                    if not panelRef.rank in EVENT_DATA.ranks:
                        if (i+1) > 11:
                            del self.rankPanels[panelRef.rank]
                            panelRef.Destroy()
                        else:
                            panelRef.rank = None
                            panelRef.updateLabelTexts()
                else:
                    panelRef.Move((0,panelRef.GetPosition()[1]-1),wx.SIZE_ALLOW_MINUS_ONE)
            else:
                cancel = True
                break
        if cancel == False:
            for i in range(len(self.extraPanels)):
                panelRef = self.extraPanels[str(i+1)]
                if panelRef.GetPosition()[1] < (-1*panelRef.GetSize()[1]):
                    newY = i*panelRef.GetSize()[1] + self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1]
                    #if self.logoPanel != None:
                    #    newY += self.logoPanel.GetSize()[1]
                    #newY += len(self.extraPanels)*90
                    panelRef.Move((0,newY),wx.SIZE_ALLOW_MINUS_ONE)
                else:
                    panelRef.Move((0,panelRef.GetPosition()[1]-1),wx.SIZE_ALLOW_MINUS_ONE)
            if self.logoPanel != None:
                if self.logoPanel.GetPosition()[1] < (-1*self.logoPanel.GetSize()[1]):
                    newY = self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1] 
                    newY += len(self.extraPanels)*90
                    self.logoPanel.Move((0,newY),wx.SIZE_ALLOW_MINUS_ONE)
                else:
                    self.logoPanel.Move((0,self.logoPanel.GetPosition()[1]-1),wx.SIZE_ALLOW_MINUS_ONE)    
            wx.CallLater(3,self.updatePositions)
        else:
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
        if evt != None:
            evt.Skip()
        

    def updateRankSponsorLogo(self,evt):
        if self.curSponsorI != -1 and self.logoPanel != None:
            if self.curSponsorI == (len(EVENT_DATA.sponsors)-1):
                self.curSponsorI = 0
            else:
                self.curSponsorI += 1
                
            self.logoPanel.updateImg(EVENT_DATA.sponsors[self.curSponsorI])
            self.logoPanel.SetBackgroundColour(COLORS["White"])
        evt.Skip()