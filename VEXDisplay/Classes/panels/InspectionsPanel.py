import wx
import sys
import os
import math
sys.path.append('..')
from ..Colors import *
from ..EventData import *
from TeamInspectionPanel_Small import *
class InspectionsPanel(wx.Panel):
    def __init__(self,parent=None):
        wx.Panel.__init__(self,parent)
        self.SetSize((1920,900))
        self.SetPosition((0,180))
        #self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.SetBackgroundColour(COLORS["vexTxtDarkGray"])
        #self.Bind(wx.EVT_ERASE_BACKGROUND,self.drawBG)
        #self.SetDoubleBuffered(True)
        self.redrawTimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER,self.redraw,self.redrawTimer)
        self.Bind(wx.EVT_SHOW,self.doClose)
        self.Bind(wx.EVT_PAINT,self.onPaint)
        self.NotoSansBold = wx.Font(32,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")
        self.NotoSansRegular = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
        self.NotoSansRegularI = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName="NotoSans")
        self.NotoSansRegularIU = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName="NotoSans",underline=True)
        self.NotoSansRegularIS = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName="NotoSans")
        self.NotoSansRegularIS.SetStrikethrough(True)
       
        self.gearBottomBGImg = wx.StaticBitmap(self,-1,wx.BitmapFromImage(wx.Image(os.path.join(os.getcwd(),"Resources","Images","Display","gear_pattern_bottom_16x9.png"),wx.BITMAP_TYPE_PNG)))
        self.gearBottomBGImg.SetPosition((0,366))
        
        
        self.lblSummary = TeamInspectionPanel(self)
        self.lblSummary.SetDoubleBuffered(True)
        self.lblSummary.lblTeamNumber = wx.StaticText(self.lblSummary,-1,style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        self.lblSummary.lblTeamNumber.SetFont(self.NotoSansBold)
        self.lblSummary.lblTeamNumber.SetForegroundColour(COLORS["vexTxtGray"])
        self.lblSummary.lblTeamNumber.SetBackgroundColour(COLORS["White"])
        self.lblSummary.lblTeamNumber.SetSize((1574,50))
        self.lblSummary.SetSize((1574,50))
        self.lblSummary.SetBackgroundColour(COLORS["White"])
        self.lblSummary.lblTeamNumber.SetLabel("Inspection Summary  -  Not Started:  " + str(EVENT_DATA.inspections_ns) + "      Partial:  " + str(EVENT_DATA.inspections_p) + "      Completed:  " + str(EVENT_DATA.inspections_c))
        self.lblSummary.SetPosition((((1920-self.lblSummary.GetSize()[0])/2)-13,2))
        self.xOff = 50

        self.teamLblHandler = {}
        self.spares = {}
        self.teamLblOffsetX = self.xOff
        self.teamLblOffsetY = 80
        
        self.isGrayRow = False
        self.teamLblOffsetY = 80+(90*((8 - int(math.ceil((260*len(EVENT_DATA.teams)) / 1800)))//2))
        for team in EVENT_DATA.teams:
            self.teamLblHandler[team] = TeamInspectionPanel(self)
            self.teamLblHandler[team].SetDoubleBuffered(True)
            self.teamLblHandler[team].lblTeamNumber = wx.StaticText(self.teamLblHandler[team],-1,style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
            self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegular)
            if (EVENT_DATA.teams[team].getCheckedIn()):
                if (EVENT_DATA.teams[team].getInspectionStatus() == "Not Started"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexRed"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegular)
                elif (EVENT_DATA.teams[team].getInspectionStatus() == "Partial"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexInspectionPartialTxt"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularIU)
                elif (EVENT_DATA.teams[team].getInspectionStatus() == "Completed"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexGreen"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularIS)
            else:
                self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexTxtGray"])
                self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularI)
            self.teamLblHandler[team].lblTeamNumber.SetLabel(team)
            self.teamLblHandler[team].lblTeamNumber.SetSize((260,60))
            self.teamLblHandler[team].lblTeamNumber.SetPosition((0,(self.teamLblHandler[team].GetSize()[1]-self.teamLblHandler[team].lblTeamNumber.GetSize()[1])/2))
            self.teamLblHandler[team].SetPosition((self.teamLblOffsetX,self.teamLblOffsetY))
            if self.isGrayRow: 
                self.teamLblHandler[team].SetBackgroundColour(COLORS["vexBGLightGray"])
            else:
                self.teamLblHandler[team].SetBackgroundColour(COLORS["vexBGLighterGray"])            
           
            if (self.teamLblOffsetX >= 1610):#comparison = 1870-(2*width)
                self.teamLblOffsetY += 90
                self.teamLblOffsetX = self.xOff
                self.isGrayRow = not self.isGrayRow

            else:
                self.teamLblOffsetX += 260
                
        while(self.teamLblOffsetX < 1870):
            self.spares[self.teamLblOffsetX] = TeamInspectionPanel(self)
            self.spares[self.teamLblOffsetX].SetDoubleBuffered(True)
            self.spares[self.teamLblOffsetX].lblTeamNumber = wx.StaticText(self.spares[self.teamLblOffsetX],-1,style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
            self.spares[self.teamLblOffsetX].lblTeamNumber.SetFont(self.NotoSansRegular)
            self.spares[self.teamLblOffsetX].lblTeamNumber.SetLabel("")
            self.spares[self.teamLblOffsetX].lblTeamNumber.SetSize((260,60))
            self.spares[self.teamLblOffsetX].lblTeamNumber.SetPosition((0,(self.spares[self.teamLblOffsetX].GetSize()[1]-self.spares[self.teamLblOffsetX].lblTeamNumber.GetSize()[1])/2))
            if self.isGrayRow: 
                self.spares[self.teamLblOffsetX].SetBackgroundColour(COLORS["vexBGLightGray"])
            else:
                self.spares[self.teamLblOffsetX].SetBackgroundColour(COLORS["vexBGLighterGray"])  
            self.spares[self.teamLblOffsetX].SetPosition((self.teamLblOffsetX,self.teamLblOffsetY))
            self.teamLblOffsetX += 260

        self.redrawTimer.Start(1000)
    def onPaint(self,evt):
        dc = wx.ClientDC(self)
        dc.SetPen(wx.Pen(COLORS["vexTxtDarkGray"]))
        dc.DrawRoundedRectangle(150,0,1600,60,8)
        evt.Skip()
    def redraw(self,evt=None):
        self.lblSummary.lblTeamNumber.SetLabel("Inspection Summary  -  Not Started:  " + str(EVENT_DATA.inspections_ns) + "      Partial:  " + str(EVENT_DATA.inspections_p) + "      Completed:  " + str(EVENT_DATA.inspections_c))
        for team in self.teamLblHandler:
            if (EVENT_DATA.teams[team].getCheckedIn()):
                if (EVENT_DATA.teams[team].getInspectionStatus() == "Not Started"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexRed"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegular)
                elif (EVENT_DATA.teams[team].getInspectionStatus() == "Partial"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexInspectionPartialTxt"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularIU)
                elif (EVENT_DATA.teams[team].getInspectionStatus() == "Completed"):
                    self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexGreen"])
                    self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularIS)
            else:
                self.teamLblHandler[team].lblTeamNumber.SetForegroundColour(COLORS["vexTxtGray"])
                self.teamLblHandler[team].lblTeamNumber.SetFont(self.NotoSansRegularI)
            self.teamLblHandler[team].lblTeamNumber.Refresh()
        if evt != None:
            evt.Skip()
    
    def doClose(self,evt,show=False):
        if self.redrawTimer != None and show==False:
            if self.redrawTimer.IsRunning():
                self.redrawTimer.Stop()
        evt.Skip()