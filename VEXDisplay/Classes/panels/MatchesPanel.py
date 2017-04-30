import wx
import sys
from collections import OrderedDict
sys.path.append('..')
from ..Colors import *
from ..data import *
from ..drawables.fonts import *
from ..EventData import *
from MatchPanel_Strip_Main import *
class MatchesPanel(wx.Panel):
    global EVENT_DATA 
    def __init__(self,parent=None):
        wx.Panel.__init__(self,parent)
        self.SetSize((545,808))
        self.SetPosition((1350,252))
        self.SetBackgroundColour(COLORS["vexBlue"])
        self.matchStrips = OrderedDict()
        self.lastY = 0
        self.isGray = False
        wx.CallLater(10,self.updateMatches)
    
    def updateMatches(self,evt=None):
        for i in range(0,8):
            if i not in self.matchStrips:
                self.matchStrips[i] = MatchPanel_Strip_Main(self,None)
                self.matchStrips[i].SetPosition((0,self.lastY))
                if self.isGray:
                    self.matchStrips[i].SetBackgroundColour(COLORS["vexBGDarkGray"])
                else:
                    self.matchStrips[i].SetBackgroundColour(COLORS["White"])
                self.isGray = not self.isGray
                self.lastY += 101
                self.matchStrips[i].Show()
            if i < len(EVENT_DATA.showMatches):
                self.matchStrips[i].updateLabelTexts(EVENT_DATA.showMatches[i])
                
            else:
                self.matchStrips[i].updateLabelTexts(None)
        wx.CallLater(10000,self.updateMatches)