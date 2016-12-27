import wx, sys
sys.path.append("..")
from ..Colors import *
from ..EventData import *
from ..drawables.fonts import *
class TeamRankPanel_Main(wx.Panel):

    def __init__(self,parent=None,rank=None):
        wx.Panel.__init__(self,parent)
        self.SetDoubleBuffered(True)
        self.SetBackgroundColour(COLORS["vexBGLightGray"])
        
        self.SetSize((1300,90))
        self.rank = rank
        if self.rank != None:
            self.lblRankNumber = wx.StaticText(self,-1)
            self.lblRankNumber.SetForegroundColour(COLORS["vexTxtGray"])
            self.lblRankNumber.SetFont(FONTS["NotoSansBold_56"])
            self.lblRankNumber.SetLabel(str(rank))
            self.lblRankNumber.SetPosition((((120-self.lblRankNumber.GetSize()[0])/2),(self.GetSize()[1]-self.lblRankNumber.GetSize()[1])/2))
        
            self.lblTeamNumber = wx.StaticText(self,-1)
            self.lblTeamNumber.SetForegroundColour(COLORS["vexTxtGray"])
            #self.lblTeamNumber.SetFont(FONTS[""])
            self.lblTeamName = wx.StaticText(self,-1)
            self.lblAPs = wx.StaticText(self,-1)
            self.lblSPs = wx.StaticText(self,-1)
            self.lblWPs = wx.StaticText(self,-1)
            self.lblWins = wx.StaticText(self,-1)
            self.lblWinsD = wx.StaticText(self,-1)
            self.lblLosses = wx.StaticText(self,-1)
            self.lblLossesD = wx.StaticText(self,-1)
            self.lblTies = wx.StaticText(self,-1)
    def updateLabelTexts(self):
        if self.rank != None:
            d = True
        else:
            d = True
    