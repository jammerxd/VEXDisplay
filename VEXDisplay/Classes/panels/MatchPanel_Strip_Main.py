import wx
import sys
import os
from collections import OrderedDict
sys.path.append("..")
from ..Colors import *
from ..EventData import *
from ..drawables.fonts import *

STRIP_PADDING_OFFSET = 0
MATCHNUM_COL_W = 150
RED_TEAM_COL_W = 145
BLUE_TEAM_COL_W = 145
FIELD_NAME_COL_W = 685-MATCHNUM_COL_W-RED_TEAM_COL_W-BLUE_TEAM_COL_W
MATCH_TIME_COL_W = 685-MATCHNUM_COL_W-RED_TEAM_COL_W-BLUE_TEAM_COL_W
RED_TEAM_SCORE_COL_W = 685-MATCHNUM_COL_W-RED_TEAM_COL_W-BLUE_TEAM_COL_W
BLUE_TEAM_SCORE_COL_W = 685-MATCHNUM_COL_W-RED_TEAM_COL_W-BLUE_TEAM_COL_W
class MatchPanel_Strip_Main(wx.Panel):
    global EVENT_DATA
    def __init__(self,parent=None,matchNum=None):
        wx.Panel.__init__(self,parent)
        self.SetDoubleBuffered(True)
        self.SetBackgroundColour(COLORS["vexBGLightGray"])
        self.matchNum = matchNum
        self.SetSize((685,101))
        
        self.lblMatchNum = wx.StaticText(self,-1)
        self.lblMatchNum.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblMatchNum.SetFont(FONTS["NotoSansBold_36"])

        self.lblRedTeam1 = wx.StaticText(self,-1)
        self.lblRedTeam1.SetForegroundColour(COLORS["vexRed"])
        self.lblRedTeam1.SetFont(FONTS["NotoSansRegular_26"])

        self.lblRedTeam2 = wx.StaticText(self,-1)
        self.lblRedTeam2.SetForegroundColour(COLORS["vexRed"])
        self.lblRedTeam2.SetFont(FONTS["NotoSansRegular_26"])

        self.lblBlueTeam1 = wx.StaticText(self,-1)
        self.lblBlueTeam1.SetForegroundColour(COLORS["vexBlue"])
        self.lblBlueTeam1.SetFont(FONTS["NotoSansRegular_26"])

        self.lblBlueTeam2 = wx.StaticText(self,-1)
        self.lblBlueTeam2.SetForegroundColour(COLORS["vexBlue"])
        self.lblBlueTeam2.SetFont(FONTS["NotoSansRegular_26"])

        self.lblFieldName = wx.StaticText(self,-1)
        self.lblFieldName.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblFieldName.SetFont(FONTS["NotoSansRegular_26"])

        self.lblMatchTime = wx.StaticText(self,-1)
        self.lblMatchTime.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblMatchTime.SetFont(FONTS["NotoSansRegular_26"])
        

        self.lblRedScore = wx.StaticText(self,-1)
        self.lblRedScore.SetForegroundColour(COLORS["vexRed"])
        self.lblRedScore.SetFont(FONTS["NotoSansRegular_26"])

        self.lblBlueScore = wx.StaticText(self,-1)
        self.lblBlueScore.SetForegroundColour(COLORS["vexBlue"])
        self.lblBlueScore.SetFont(FONTS["NotoSansRegular_26"])
        self.Hide()
        self.updateLabelTexts(self.matchNum)
    def updateLabelTexts(self,matchNum = None):
        self.matchNum = matchNum
        
        if self.matchNum != None:
            self.lblMatchNum.SetLabel(self.matchNum)
            self.lblMatchNum.SetPosition((STRIP_PADDING_OFFSET+((MATCHNUM_COL_W-self.lblMatchNum.GetSize()[0])/2),(self.GetSize()[1]-self.lblMatchNum.GetSize()[1])/2))
            
            #red wins
            if EVENT_DATA.matches[self.matchNum].getRedScore() > EVENT_DATA.matches[self.matchNum].getBlueScore():
                self.lblRedTeam1.SetFont(FONTS["NotoSansBold_26"])
                self.lblRedTeam2.SetFont(FONTS["NotoSansBold_26"])
                self.lblRedScore.SetFont(FONTS["NotoSansBold_26"])
                self.lblBlueTeam1.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueTeam2.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueScore.SetFont(FONTS["NotoSansRegular_26"])
            #blue wins
            elif EVENT_DATA.matches[self.matchNum].getRedScore() < EVENT_DATA.matches[self.matchNum].getBlueScore():
                self.lblRedTeam1.SetFont(FONTS["NotoSansRegular_26"])
                self.lblRedTeam2.SetFont(FONTS["NotoSansRegular_26"])
                self.lblRedScore.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueTeam1.SetFont(FONTS["NotoSansBold_26"]) 
                self.lblBlueTeam2.SetFont(FONTS["NotoSansBold_26"])  
                self.lblBlueScore.SetFont(FONTS["NotoSansBold_26"])              
            #tie    
            else:
                self.lblRedTeam1.SetFont(FONTS["NotoSansRegular_26"])
                self.lblRedTeam2.SetFont(FONTS["NotoSansRegular_26"])
                self.lblRedScore.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueTeam1.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueTeam2.SetFont(FONTS["NotoSansRegular_26"])
                self.lblBlueScore.SetFont(FONTS["NotoSansRegular_26"])

            self.lblRedTeam1.SetLabel(EVENT_DATA.matches[self.matchNum].getRed1())
            #self.lblRedTeam1.SetLabel("99999W")
            self.lblRedTeam1.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+((RED_TEAM_COL_W-self.lblRedTeam1.GetSize()[0])/2),5))
            
            self.lblRedTeam2.SetLabel(EVENT_DATA.matches[self.matchNum].getRed2())
            #self.lblRedTeam2.SetLabel("00000W")
            self.lblRedTeam2.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+RED_TEAM_COL_W+((RED_TEAM_COL_W-self.lblRedTeam2.GetSize()[0])/2),5))

            self.lblBlueTeam1.SetLabel(EVENT_DATA.matches[self.matchNum].getBlue1())
            #self.lblBlueTeam1.SetLabel("00000W")
            self.lblBlueTeam1.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+((BLUE_TEAM_COL_W-self.lblBlueTeam1.GetSize()[0])/2),self.GetSize()[1]-self.lblBlueTeam1.GetSize()[1]-5))

            self.lblBlueTeam2.SetLabel(EVENT_DATA.matches[self.matchNum].getBlue2())
            #self.lblBlueTeam2.SetLabel("99999W")
            self.lblBlueTeam2.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+BLUE_TEAM_COL_W+((BLUE_TEAM_COL_W-self.lblBlueTeam2.GetSize()[0])/2),self.GetSize()[1]-self.lblBlueTeam2.GetSize()[1]-5))
            
            if EVENT_DATA.matches[self.matchNum].getScored() == True:
                self.lblRedScore.Show()
                self.lblBlueScore.Show()
                self.lblFieldName.Hide()
                self.lblMatchTime.Hide()
            else:
                self.lblRedScore.Hide()
                self.lblBlueScore.Hide()
                self.lblFieldName.Show()
                self.lblMatchTime.Show()


            self.lblFieldName.SetLabel(EVENT_DATA.matches[self.matchNum].getField())
            self.lblFieldName.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+RED_TEAM_COL_W+BLUE_TEAM_COL_W+((FIELD_NAME_COL_W-self.lblFieldName.GetSize()[0])/2),5))
            
            self.lblMatchTime.SetLabel(EVENT_DATA.matches[self.matchNum].getScheduledTime())
            self.lblMatchTime.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+RED_TEAM_COL_W+BLUE_TEAM_COL_W+((MATCH_TIME_COL_W-self.lblMatchTime.GetSize()[0])/2),self.GetSize()[1]-self.lblMatchTime.GetSize()[1]-5))
            
            self.lblRedScore.SetLabel(EVENT_DATA.matches[self.matchNum].getRedScore())
            self.lblRedScore.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+RED_TEAM_COL_W+BLUE_TEAM_COL_W+((RED_TEAM_SCORE_COL_W-self.lblRedScore.GetSize()[0])/2),5))

            self.lblBlueScore.SetLabel(EVENT_DATA.matches[self.matchNum].getBlueScore())
            self.lblBlueScore.SetPosition((STRIP_PADDING_OFFSET+MATCHNUM_COL_W+RED_TEAM_COL_W+BLUE_TEAM_COL_W+((BLUE_TEAM_SCORE_COL_W-self.lblBlueScore.GetSize()[0])/2),self.GetSize()[1]-self.lblBlueScore.GetSize()[1]-5))
            if not self.IsShown:
                self.Show()
        else:
            self.lblMatchNum.SetLabel("")
            
            self.lblRedTeam1.SetLabel("")
            self.lblRedTeam2.SetLabel("")
            
            self.lblBlueTeam1.SetLabel("")
            self.lblBlueTeam2.SetLabel("")

            self.lblRedScore.SetLabel("")
            self.lblBlueScore.SetLabel("")
            
            self.lblMatchTime.SetLabel("")
            self.lblFieldName.SetLabel("")
        self.Refresh()