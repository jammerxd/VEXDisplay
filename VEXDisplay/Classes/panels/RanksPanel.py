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
RANK_PANEL_DELTA_Y = 2
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
        self.positionY = 0
        self.SetDoubleBuffered(True)
        self.logoPanel = None
        
        self.curSponsorI = -1
        self.updatePositionsTimer = None
        self.changeLogoTimer = None
        self.setupRankPanels(speed=speed)

        self.cancel = False
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
                    self.rankPanels[rank].SetBackgroundColour(COLORS["vexBGDarkGray"])
                self.isGray = not self.isGray
                self.yOff += RANK_PANEL_HEIGHT
        if len(self.rankPanels) > 0:
            while ((RANK_PANEL_HEIGHT*len(self.rankPanels)) + (RANK_PANEL_HEIGHT*len(self.extraPanels))) < (900+RANK_PANEL_HEIGHT):
                key = str(len(self.extraPanels)+1)
        
                self.extraPanels[key] = TeamRankPanel_Main(self)
                self.extraPanels[key].Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
                self.yOff += RANK_PANEL_HEIGHT
                self.extraPanels[key].SetBackgroundColour(COLORS["White"])
        if len(EVENT_DATA.sponsors) > 0:
            self.curSponsorI = 0
            self.logoPanel = RankLogoPanel_Main(self,EVENT_DATA.sponsors[self.curSponsorI])
            self.logoPanel.Move((0,self.yOff),wx.SIZE_ALLOW_MINUS_ONE)
            self.logoPanel.SetBackgroundColour(COLORS["White"])
            self.logoPanel.Show()

        self.positionY = self.yOff-RANK_PANEL_HEIGHT
        self.updatePositionsTimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updatePositions,self.updatePositionsTimer)
        self.updatePositionsTimer.Start(1000.0/speed)
        self.changeLogoTimer =wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.updateRankSponsorLogo,self.changeLogoTimer)
        self.changeLogoTimer.Start(10000)
        #self.updatePositionsTimer.Start(500)
        #self.logoPanel = RankLogoPanel_Main(self,EVENT_DATA.sponsors[0])
        #wx.CallAfter(self.updatePositions)
                
    def updatePositions(self,evt=None):
        cancel = False
        try:
            for i in range(len(EVENT_DATA.ranks)):
                
                if str(i+1) in self.rankPanels:
                    panelRef = self.rankPanels.items()[i][1]

                    if self.rankPanels[str(i+1)].GetPosition()[1] < (-1*self.rankPanels[str(i+1)].GetSize()[1]):
                        newY = i*panelRef.GetSize()[1] + self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1]
                        if self.logoPanel != None:
                            newY += self.logoPanel.GetSize()[1]
                        newY += len(self.extraPanels)*RANK_PANEL_HEIGHT
                        panelRef.Move((0,newY-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)
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
                        panelRef.Move((0,panelRef.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)
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
                        panelRef.Move((0,panelRef.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)
                if self.logoPanel != None:
                    if self.logoPanel.GetPosition()[1] < (-1*self.logoPanel.GetSize()[1]):
                        newY = self.rankPanels[str(len(self.rankPanels))].GetPosition()[1] + self.rankPanels[str(len(self.rankPanels))].GetSize()[1] 
                        newY += len(self.extraPanels)*RANK_PANEL_HEIGHT
                        self.logoPanel.Move((0,newY),wx.SIZE_ALLOW_MINUS_ONE)
                    else:
                        self.logoPanel.Move((0,self.logoPanel.GetPosition()[1]-RANK_PANEL_DELTA_Y),wx.SIZE_ALLOW_MINUS_ONE)    
                #wx.CallLater(18,self.updatePositions)
            else:
                self.regenScroll()
            if evt != None:
                evt.Skip()
        
        except Exception, ex:
            doNothing = True
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
        ###CHECK ALL PANELS###
        if len(self.rankPanels) != len(EVENT_DATA.ranks):
            self.regenScroll()

        #######################
        evt.Skip()
