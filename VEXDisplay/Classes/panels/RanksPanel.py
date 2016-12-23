import wx
import sys
sys.path.append('..')
from ..Colors import *
class RanksPanel(wx.Panel):
    def __init__(self,parent=None):
        wx.Panel.__init__(self,parent)
        self.SetSize((1300,900))
        self.SetPosition((25,165))
        self.SetBackgroundColour(COLORS["vexBlue"])
        