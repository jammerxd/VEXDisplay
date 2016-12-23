import wx, sys, os
sys.path.append('..')
from ..Colors import *
from RanksPanel import *
from InspectionsPanel import *
from ..data import *
from ..EventData import *
from ..drawables import *
class MainScreen(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetSize((1920,1080))
        self.SetBackgroundColour(COLORS["vexRed"])
        self.mainPanel = None
        self.secondPanel = None

        self.smallLogoPic = None
        self.logoTimer = None
        self.logoRect = None

        self.vexSmallLogo = None
        
        self.mainPanelHeader = None
        self.secondPanelHeader = None

        self.Font_NotoSans_22_Normal = None
        self.Font_NotoSans_22_Bold = None

        self.inspectionsToMatchTimer = None
        
        #self.SetBackgroundColour(COLORS["Black"])
    def onReady(self,mainPanel = "Rankings", secondPanel = "Matches", showInspections=False):
        self.mainPanelType = mainPanel
        self.secondPanelType = secondPanel
        self.showInspections = showInspections


        ###SETUP FONTS AND HEADERS###
        if os.name == 'nt':
            self.Font_NotoSans_22_Normal = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="Noto Sans")
            self.Font_NotoSans_22_Bold = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="Noto Sans")

            self.Font_NotoSans_55_Normal = wx.Font(55,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="Noto Sans")
            self.Font_NotoSans_55_Bold = wx.Font(55,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="Noto Sans")
        else:
            self.Font_NotoSans_22_Normal = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
            self.Font_NotoSans_22_Bold = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")

            self.Font_NotoSans_55_Normal = wx.Font(55,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
            self.Font_NotoSans_55_Bold = wx.Font(55,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")
        
        self.mainPanelHeader = Header(self,-1,"Qualification Rankings",self.Font_NotoSans_55_Bold,COLORS["White"])
        self.mainPanelHeader.SetSize((830,150))
        #Check if inspections are needed
        if self.showInspections:
            self.secondPanel = None
            self.mainPanel = InspectionsPanel(self)
            self.mainPanelHeader.SetLabel("Inspection")
            self.mainPanelHeader.SetPosition((250,12))
            self.SetBackgroundColour(COLORS["vexTxtDarkGray"])
            if self.inspectionsToMatchTimer != None:
                if self.inspectionsToMatchTimer.IsRunning():
                    self.inspectionsToMatchTimer.Stop()
                self.inspectionsToMatchTimer.Destroy()
            self.inspectionsToMatchTimer = wx.Timer(self,-1)
            self.Bind(wx.EVT_TIMER,self.checkInspectionData,self.inspectionsToMatchTimer)
            self.inspectionsToMatchTimer.Start(1000)
            #self.mainPanel.SetDoubleBuffered(True)
        else:
            self.setupMainPanel()
        #########


        self.vexSmallLogo = wx.StaticBitmap(self,-1,wx.BitmapFromImage(wx.Image(os.path.join(os.getcwd(),"Resources","Images","Display","vrc_logo_titlebar.png"),wx.BITMAP_TYPE_PNG)))
        self.vexSmallLogo.SetPosition((self.GetSize()[0]-227,25))
        ###show panels###
        if self.mainPanel != None:
            self.mainPanel.Show()   
        
        if self.secondPanel != None:
            self.secondPanel.Show()
    def setupMainPanel(self):
        if self.mainPanelType == "Rankings":
            self.mainPanel = RanksPanel(self)
            self.mainPanelHeader.SetLabel("Qualification Rankings")
            self.mainPanelHeader.SetSize((1200,self.mainPanelHeader.GetSize()[1]))
            self.mainPanel.SetSize((1300,900))
            self.mainPanel.SetPosition((25,155))
            self.mainPanel.SetBackgroundColour(COLORS["vexBlue"])
    def setupSecondPanel(self):
        if self.secondPanelType == "Matches":
            self.secondPanel = None
    def checkInspectionData(self,evt):
        switchMain = False
        if self.mainPanel != None and self.showInspections:
            #if len(EVENT_DATA.matches) > 0:
            if EVENT_DATA.inspections_t == EVENT_DATA.inspections_c:
                self.mainPanel.Hide()
                self.mainPanel.DestroyChildren()
                self.mainPanel.Destroy()
                if self.secondPanel != None:
                    self.secondPanel.Hide()
                    self.secondPanel.DestroyChildren()
                    self.secondPanel.Destroy()
                switchMain = True
        if switchMain:
            if self.inspectionsToMatchTimer != None:
                self.inspectionsToMatchTimer.Stop()
            self.setupMainPanel()
            self.setupSecondPanel()
        if evt != None:
            evt.Skip()