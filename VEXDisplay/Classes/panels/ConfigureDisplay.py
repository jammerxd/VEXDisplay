import wx
import sys
sys.path.append('..')
from ..Colors import *
class ConfigureDisplay(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.NotoSansBold = wx.Font(18,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")
        self.NotoSansRegular = wx.Font(14,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
        self.SetSize((460,500))
        self.SetPosition((0,0))


        self.settings_lbl_header = wx.StaticText(self,-1)
        self.settings_lbl_header.SetFont(self.NotoSansBold)
        self.settings_lbl_header.SetLabel("Configure Settings")
        self.settings_lbl_header.SetPosition(((self.GetSize()[0]-self.settings_lbl_header.GetSize()[0])/2,10))




        self.settings_lbl_WebServer = wx.StaticText(self,-1)
        self.settings_lbl_WebServer.SetFont(self.NotoSansRegular)
        self.settings_lbl_WebServer.SetLabel("Display Server Address: ")
        self.settings_lbl_WebServer.SetPosition((20,62))   
        
        self.TxtbxWebServer = wx.TextCtrl(self,value="http://localhost:8989",pos=(self.settings_lbl_WebServer.GetSize()[0]+25,60), size=(self.GetSize()[0]-self.settings_lbl_WebServer.GetSize()[0]-25-25,self.settings_lbl_WebServer.GetSize()[1]+4))
        self.TxtbxWebServer.SetFont(self.NotoSansRegular)


        self.settings_lbl_DivisionSelect = wx.StaticText(self,-1)
        self.settings_lbl_DivisionSelect.SetFont(self.NotoSansRegular)
        self.settings_lbl_DivisionSelect.SetLabel("Select Division: ")
        self.settings_lbl_DivisionSelect.SetPosition((20,104)) 

        
        self.CmbxDivision = wx.ComboBox(self,
            -1,
            pos=(self.settings_lbl_DivisionSelect.GetPosition()[0]+self.settings_lbl_DivisionSelect.GetSize()[0]+5,101),
            choices=['Division 1','Division 2','Division 3','Division 4','Division 5','Division 6','Division 7','Division 8','Division 9','Division 10','Division 11','Division 12'],
            style = wx.CB_READONLY,
            value = 'Division 1'
        )
        self.CmbxDivision.SetFont(self.NotoSansRegular)
        self.CmbxDivision.SetSize((self.CmbxDivision.GetSize()[0]+35,self.CmbxDivision.GetSize()[1]))

        self.settings_lbl_DataRefresh = wx.StaticText(self,-1)
        self.settings_lbl_DataRefresh.SetFont(self.NotoSansRegular)
        self.settings_lbl_DataRefresh.SetLabel("Data Refresh Rate(seconds): ")
        self.settings_lbl_DataRefresh.SetPosition((20,148))   
        
        self.dataRefreshRate = wx.SpinCtrl(self, -1, '',  (self.settings_lbl_DataRefresh.GetPosition()[0]+self.settings_lbl_DataRefresh.GetSize()[0]+5, 147), (80, -1))
        self.dataRefreshRate.SetFont(self.NotoSansRegular)
        self.dataRefreshRate.SetRange(1,999)
        self.dataRefreshRate.SetValue(10)
        self.dataRefreshRate.SetSize((self.dataRefreshRate.GetSize()[0],self.dataRefreshRate.GetSize()[1]+5))
    
        


        self.settings_lbl_MainDisplaySelect = wx.StaticText(self,-1)
        self.settings_lbl_MainDisplaySelect.SetFont(self.NotoSansRegular)
        self.settings_lbl_MainDisplaySelect.SetLabel("Main Display: ")
        self.settings_lbl_MainDisplaySelect.SetPosition((20,192)) 

        
        self.CmbxMainDisplay = wx.ComboBox(self,
            -1,
            pos=(self.settings_lbl_MainDisplaySelect.GetPosition()[0]+self.settings_lbl_MainDisplaySelect.GetSize()[0]+5,189),
            choices=['Rankings', 'Matches', 'Skills', 'Inspections', 'Check Ins'],
            style = wx.CB_READONLY,
            value = 'Rankings'
        )
        self.CmbxMainDisplay.SetFont(self.NotoSansRegular)
        self.CmbxMainDisplay.SetSize((self.CmbxMainDisplay.GetSize()[0]+35,self.CmbxMainDisplay.GetSize()[1]))
        self.CmbxMainDisplay.Disable()


        self.settings_lbl_SecondDisplaySelect = wx.StaticText(self,-1)
        self.settings_lbl_SecondDisplaySelect.SetFont(self.NotoSansRegular)
        self.settings_lbl_SecondDisplaySelect.SetLabel("Second Display: ")
        self.settings_lbl_SecondDisplaySelect.SetPosition((20,234)) 

        
        self.CmbxSecondDisplay = wx.ComboBox(self,
            -1,
            pos=(self.settings_lbl_SecondDisplaySelect.GetPosition()[0]+self.settings_lbl_SecondDisplaySelect.GetSize()[0]+5,231),
            choices=['Rankings', 'Matches', 'Skills', 'Inspections', 'Check Ins'],
            style = wx.CB_READONLY,
            value = 'Matches'
        )
        self.CmbxSecondDisplay.SetFont(self.NotoSansRegular)
        self.CmbxSecondDisplay.SetSize((self.CmbxSecondDisplay.GetSize()[0]+35,self.CmbxSecondDisplay.GetSize()[1]))
        self.CmbxSecondDisplay.Disable()

        
        self.settings_lbl_showCheckInInspections = wx.StaticText(self,-1)
        self.settings_lbl_showCheckInInspections.SetFont(self.NotoSansRegular)
        self.settings_lbl_showCheckInInspections.SetLabel("Show CheckIn/Inspections: ")
        self.settings_lbl_showCheckInInspections.SetPosition((20,278)) 
        

        self.ChkbxAutoShowInspections = wx.CheckBox(self, label = '',pos = (self.settings_lbl_showCheckInInspections.GetPosition()[0]+self.settings_lbl_showCheckInInspections.GetSize()[0]+5,284))
        self.ChkbxAutoShowInspections.SetFont(self.NotoSansRegular)
        #self.ChkbxAutoShowInspections.SetSize((self.ChkbxAutoShowInspections.GetSize()[0]+15,self.ChkbxAutoShowInspections.GetSize()[1]+15))
        
        self.BtnGo = wx.Button(self,label="GO!",pos=(10,325), size=(120,75))
        self.BtnGo.SetFont(self.NotoSansRegular)
        x = (self.GetSize()[0] - self.BtnGo.GetSize()[0])/2
        self.BtnGo.SetPosition((x,375))

        #self.BtnGo.Bind(wx.EVT_LEFT_UP,self.on_go)
        self.Enable(True)