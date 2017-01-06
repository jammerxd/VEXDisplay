import wx, sys, os
sys.path.append('..')
from ..Colors import *
from RanksPanel import *
from InspectionsPanel import *
from ..data import *
from ..EventData import *
from ..drawables import *
from MatchesPanel import *
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
        
        genFonts()
        #self.SetBackgroundColour(COLORS["Black"])
    def onReady(self,mainPanel = "Rankings", secondPanel = "Matches", showInspections=False,scrollSpeed=270):
        self.mainPanelType = mainPanel
        self.secondPanelType = secondPanel
        self.showInspections = showInspections
        self.scrollSpeed = scrollSpeed

        ###SETUP FONTS AND HEADERS###
        if os.name == 'nt':
            self.Font_NotoSans_22_Normal = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="Noto Sans")
            self.Font_NotoSans_22_Bold = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="Noto Sans")

            self.Font_NotoSans_28_Bold = wx.Font(28,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="Noto Sans")

            self.Font_NotoSans_55_Normal = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="Noto Sans")
            self.Font_NotoSans_55_Bold = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="Noto Sans")
        else:
            self.Font_NotoSans_22_Normal = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
            self.Font_NotoSans_22_Bold = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")

            self.Font_NotoSans_55_Normal = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName="NotoSans")
            self.Font_NotoSans_55_Bold = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")
            self.Font_NotoSans_28_Bold = wx.Font(28,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName="NotoSans")
        
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
            self.setupSecondPanel()
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
            self.mainPanel = RanksPanel(self,speed=self.scrollSpeed)
            self.mainPanelHeader.SetLabel("Qualification Rankings")
            self.mainPanelHeader.SetSize((1100,self.mainPanelHeader.GetSize()[1]))
            self.mainPanel.SetSize((1200,900))
            self.mainPanel.SetPosition((10,160))
            self.mainPanel.SetBackgroundColour(COLORS["vexBlue"])
    
    def setupSecondPanel(self):
        if self.secondPanelType == "Matches":
            self.secondPanelHeader = Header(self,-1,"Match Schedule and Results",self.Font_NotoSans_28_Bold,COLORS["White"])
            self.secondPanelHeader.SetPosition((1225+(685-self.secondPanelHeader.GetSize()[0])/2,205))
            self.secondPanel = MatchesPanel(self)
            self.secondPanel.SetPosition((1225,252))
            self.secondPanel.SetSize((685,808))
            self.secondPanel.SetBackgroundColour(COLORS["White"])
            self.secondPanel.Refresh()
            if not self.secondPanel.IsShown():
                self.secondPanel.Show()
    def checkInspectionData(self,evt):
        switchMain = False
        if self.mainPanel != None and self.showInspections:
            if len(EVENT_DATA.matches) > 0:
            #if EVENT_DATA.inspections_t == EVENT_DATA.inspections_c:
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
            self.SetBackgroundColour(COLORS["vexRed"])
            self.Refresh()
            
        if evt != None:
            evt.Skip()