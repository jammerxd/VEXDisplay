import wx, sys
sys.path.append("..")
from ..Colors import *
from ..EventData import *
class TeamInspectionPanel(wx.Panel):

    def __init__(self,parent=None):
        wx.Panel.__init__(self,parent)
        self.SetSize((260,90))
        #self.SetPosition((10,15))
        self.lblTeamNumber = None