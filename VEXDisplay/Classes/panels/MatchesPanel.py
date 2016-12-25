import wx
import sys
sys.path.append('..')
from ..Colors import *
class MatchesPanel(wx.Panel):
    def __init__(self,parent=None):
        wx.Panel.__init__(self,parent)
        self.SetSize((545,808))
        self.SetPosition((1350,252))
        self.SetBackgroundColour(COLORS["White"])