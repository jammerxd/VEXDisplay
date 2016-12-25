import wx
import socket
import threading
import os
from Classes import *
global COLORS

class VEXDisplay(wx.App):
    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        return True
if __name__ == "__main__":
    app = VEXDisplay(False)
    mainApp = AppScreen()
    app.SetTopWindow(mainApp)
    mainApp.Show()
    ##SET TOP WINDOW, FRAME, Etc.......
    ##
    ##
    app.MainLoop()
