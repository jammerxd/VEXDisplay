from Colors import *
from App import *
import wx
import sys, os
from panels import *
from Colors import *
class AppScreen(wx.Frame):
    global COLORS
    def __init__(self):
        #wx.Frame.__init__(self,None,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self,None)
        #self.SetDoubleBuffered(True)
        self.Bind(wx.EVT_CLOSE,self.on_exit)
        self.Bind(wx.EVT_CHAR_HOOK,self.on_key_down)
        self.SetToolTip(wx.ToolTip('Configuration Screen'))
        self.SetTitle("VEX Display - Configure Display")
        self.SetBackgroundColour(COLORS["White"])
        self.SetSize(wx.Size(460,500))
        self.app = App()
        self.ConfigPanel = ConfigureDisplay(self)
        self.ConfigPanel.BtnGo.Bind(wx.EVT_LEFT_UP,self.on_go)
        self.MainPanel = None   
        self.SecondPanel = None
        self.dataUpdateTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.app.collectData,self.dataUpdateTimer)
    def on_exit(self,evt):
        if self.app != None:
            self.app.stopDataCollection()
        if self.dataUpdateTimer != None:
            if self.dataUpdateTimer.IsRunning:
                self.dataUpdateTimer.Stop()
        self.Destroy()
        sys.exit(0)
    def on_key_down(self,evt):
        KEY = evt.GetKeyCode()
        if KEY == 27:
            self.dataUpdateTimer.Stop()
            self.app.stopDataCollection()
            if self.MainPanel != None:
                self.MainPanel.Hide()
                self.MainPanel.Destroy()
                self.MainPanel = None
            if self.SecondPanel != None:
                self.SecondPanel.Hide()
                self.SecondPanel.Destroy()
                self.SecondPanel = None
            if self.MainDisplayScreen != None:
                self.MainDisplayScreen.Hide()
                self.MainDisplayScreen.Destroy()
                self.MainDisplayScreen = None
            self.ShowFullScreen(False)
            self.SetSize((460,500))
            self.SetBackgroundColour(COLORS["White"])
            self.SetToolTip(wx.ToolTip('Configuration Screen'))
            self.SetTitle("VEX Display - Configure Display")
            #self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
            self.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
            self.ConfigPanel.Show()
            self.ConfigPanel.TxtbxWebServer.Enable(True)
            self.ConfigPanel.CmbxDivision.Enable(True)
            #self.ConfigPanel.CmbxMainDisplay.Enable()
            #self.ConfigPanel.CmbxSecondDisplay.Enable()
            self.ConfigPanel.ChkbxAutoShowInspections.Enable(True)
            self.ConfigPanel.dataRefreshRate.Enable(True)
            self.ConfigPanel.BtnGo.Enable(True)
            self.ConfigPanel.SetBackgroundColour(COLORS["White"])
        else:
            evt.Skip()
    def on_go(self,evt):
        self.ConfigPanel.TxtbxWebServer.Disable()
        self.ConfigPanel.CmbxDivision.Disable()
        self.ConfigPanel.CmbxMainDisplay.Disable()
        self.ConfigPanel.CmbxSecondDisplay.Disable()
        self.ConfigPanel.ChkbxAutoShowInspections.Disable()
        self.ConfigPanel.dataRefreshRate.Disable()
        self.ConfigPanel.BtnGo.Disable()
        self.app.settings.setServerAddress(self.ConfigPanel.TxtbxWebServer.GetValue())
        self.app.settings.setDivision(self.ConfigPanel.CmbxDivision.GetValue().split(" ")[1])
        self.app.settings.setDivisionStr("division"+self.app.settings.getDivision())
        self.app.settings.setDataUpdateFreq(self.ConfigPanel.dataRefreshRate.GetValue())
        self.app.settings.setMainDisplay(self.ConfigPanel.CmbxMainDisplay.GetValue())
        self.app.settings.setSecondDisplay(self.ConfigPanel.CmbxSecondDisplay.GetValue())
        self.app.settings.setDisplayDivision(self.ConfigPanel.CmbxDivision.GetValue())
        self.app.settings.setShowInspections(self.ConfigPanel.ChkbxAutoShowInspections.GetValue())
        self.app.settings.setScrollSpeed(self.ConfigPanel.scrollSpeed.GetValue())
        self.SetSize((1920,1080))
        self.SetPosition((0,0))
        self.ShowFullScreen(True)
        self.SetCursor(wx.StockCursor(wx.CURSOR_BLANK))
        self.ConfigPanel.Hide()
        self.SetToolTip(None)
        self.SetTitle("VEX Display - " + self.app.settings.getDisplayDivision())
        self.SetBackgroundColour(COLORS["vexRed"])
        self.initializeDivision()
    def initializeDivision(self):
        self.app.getEventName()
        self.app.getDivisionName()       
        self.app.getDivisionTeams()
        self.app.getDivisionRanks()
        self.app.getCheckIns()
        self.app.getInspections()
        self.app.getSkills()
        self.app.getDivisionMatches()
        self.app.beginCollectData()
        self.dataUpdateTimer.Start(self.app.settings.getDataUpdateFreq()*1000)
        self.MainDisplayScreen = MainScreen(self)
        self.MainDisplayScreen.onReady(self.app.settings.getMainDisplay(),self.app.settings.getSecondDisplay(),self.app.settings.getShowInspections(),self.app.settings.getScrollSpeed())
        
