import wx, sys
sys.path.append("..")
from ..Colors import *
from ..EventData import *
from ..drawables.fonts import *

RANK_NUMBER_COL_W = 150
RANK_TEAM_NUMBER_COL_W = 400
RANK_TEAM_WP_COL_W = 150
RANK_TEAM_AP_COL_W = 150
RANK_TEAM_SP_COL_W = 150
RANK_TEAM_WINS_COL_W = 61
RANK_TEAM_LOSSES_COL_W = 61

class TeamRankPanel_Main(wx.Panel):
    global EVENT_DATA
    def __init__(self,parent=None,rank=None):
        wx.Panel.__init__(self,parent)
        self.SetDoubleBuffered(True)
        self.SetBackgroundColour(COLORS["vexBGLightGray"])
        
        self.SetSize((1200,76))
        self.rank = rank

        self.lblRankNumber = wx.StaticText(self,-1)
        self.lblRankNumber.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblRankNumber.SetFont(FONTS["NotoSansBold_48"])
        
        self.lblTeamNumber = wx.StaticText(self,-1)
        self.lblTeamNumber.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblTeamNumber.SetFont(FONTS["NotoSansBold_22"])

        self.lblTeamName = wx.StaticText(self,-1)
        self.lblTeamName.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblTeamName.SetFont(FONTS["NotoSansRegular_22"])

        self.lblAPs = wx.StaticText(self,-1)
        self.lblAPs.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblAPs.SetFont(FONTS["NotoSansRegular_28"])

        self.lblSPs = wx.StaticText(self,-1)
        self.lblSPs.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblSPs.SetFont(FONTS["NotoSansRegular_28"])

        self.lblWPs = wx.StaticText(self,-1)
        self.lblWPs.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblWPs.SetFont(FONTS["NotoSansRegular_28"])
        
       # self.lblWins = wx.StaticText(self,-1)
       # self.lblWins.SetForegroundColour(COLORS["vexTxtGray"])
       # self.lblWins.SetFont(FONTS["NotoSansBold_28"])
       # 
       # self.lblWinsD = wx.StaticText(self,-1)
       # self.lblWinsD.SetForegroundColour(COLORS["vexTxtGray"])
       # self.lblWinsD.SetFont(FONTS["NotoSansBold_28"])
       # 
       # self.lblLosses = wx.StaticText(self,-1)
       # self.lblLosses.SetForegroundColour(COLORS["vexTxtGray"])
       # self.lblLosses.SetFont(FONTS["NotoSansBold_28"])        

       # self.lblLossesD = wx.StaticText(self,-1)
       # self.lblLossesD.SetForegroundColour(COLORS["vexTxtGray"])
       # self.lblLossesD.SetFont(FONTS["NotoSansBold_28"])                

       # self.lblTies = wx.StaticText(self,-1)
       # self.lblTies.SetForegroundColour(COLORS["vexTxtGray"])
       # self.lblTies.SetFont(FONTS["NotoSansBold_28"])      

        self.lblScores = wx.StaticText(self,-1)
        self.lblScores.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblScores.SetFont(FONTS["NotoSansBold_28"])    
        self.updateLabelTexts(rank=self.rank)
    def updateLabelTexts(self,rank = None):
        self.rank = rank
        if self.rank != None:
            if self.rank != "":
                self.lblRankNumber.SetLabel(str(rank))
                self.lblRankNumber.SetPosition((((RANK_NUMBER_COL_W-self.lblRankNumber.GetSize()[0])/2),(self.GetSize()[1]-self.lblRankNumber.GetSize()[1])/2))
                
                self.lblTeamNumber.SetLabel(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getNumber())
                self.lblTeamNumber.SetPosition((RANK_NUMBER_COL_W,0))

                self.lblTeamName.SetLabel(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getName())
                self.lblTeamName.SetPosition((RANK_NUMBER_COL_W,self.GetSize()[1]-self.lblTeamName.GetSize()[1]))
            
                self.lblWPs.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getWPS()))
                self.lblWPs.SetPosition(((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W)+((RANK_TEAM_WP_COL_W-self.lblWPs.GetSize()[0])/2),(self.GetSize()[1]-self.lblWPs.GetSize()[1])/2))

                self.lblAPs.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getAPS()))
                self.lblAPs.SetPosition(((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W)+((RANK_TEAM_AP_COL_W-self.lblAPs.GetSize()[0])/2),(self.GetSize()[1]-self.lblAPs.GetSize()[1])/2))

                self.lblSPs.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getSPS()))
                self.lblSPs.SetPosition(((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W)+((RANK_TEAM_SP_COL_W-self.lblSPs.GetSize()[0])/2),(self.GetSize()[1]-self.lblSPs.GetSize()[1])/2))

                #self.lblWins.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getWins()))
                #self.lblWins.SetLabel(str(randint(0,200)))
                #self.lblWins.SetPosition((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W+((RANK_TEAM_WINS_COL_W-self.lblWins.GetSize()[0])/2),(self.GetSize()[1]-self.lblWins.GetSize()[1])/2))
                
                #self.lblWinsD.SetLabel("-")
                #self.lblWinsD.SetPosition((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W+RANK_TEAM_WINS_COL_W,(self.GetSize()[1]-self.lblWinsD.GetSize()[1])/2))
                
                #self.lblLosses.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getLosses()))
                #self.lblLosses.SetLabel(str(randint(0,200)))
                #self.lblLosses.SetPosition((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W+RANK_TEAM_WINS_COL_W+self.lblWinsD.GetSize()[0]+((RANK_TEAM_LOSSES_COL_W-self.lblLosses.GetSize()[0])/2),(self.GetSize()[1]-self.lblLosses.GetSize()[1])/2))

                #self.lblLossesD.SetLabel("-")
                #self.lblLossesD.SetPosition((RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W+RANK_TEAM_WINS_COL_W+self.lblWinsD.GetSize()[0]+RANK_TEAM_LOSSES_COL_W,(self.GetSize()[1]-self.lblLossesD.GetSize()[1])/2))
                
                self.lblScores.SetLabel(str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getWins()) + "-" + str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getLosses()) + "-" + str(EVENT_DATA.teams[EVENT_DATA.ranks[rank]].getTies()))
                #self.lblScores.SetLabel("99-99-99")
                #self.lblScores.SetLabel(str(randint(0,99))+"-"+str(randint(0,1000))+"-"+str(randint(0,9)))
                x = RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W + (((self.GetSize()[0]-(RANK_NUMBER_COL_W+RANK_TEAM_NUMBER_COL_W+RANK_TEAM_WP_COL_W+RANK_TEAM_AP_COL_W+RANK_TEAM_SP_COL_W))-self.lblScores.GetSize()[0])/2)
                #print x
                self.lblScores.SetPosition((x,(self.GetSize()[1]-self.lblScores.GetSize()[1])/2))
            else:
                self.updateLabelTexts()
        else:
            self.lblRankNumber.SetLabel("")
            self.lblTeamNumber.SetLabel("")
            self.lblTeamName.SetLabel("")
            self.lblAPs.SetLabel("")
            self.lblSPs.SetLabel("")
            self.lblWPs.SetLabel("")
            #self.lblWins.SetLabel("")
            #self.lblWinsD.SetLabel("")
            #self.lblLosses.SetLabel("")
            #self.lblLossesD.SetLabel("")
            #self.lblTies.SetLabel("")
            self.lblScores.SetLabel("")
        self.Refresh()
        
    