import wx
import socket
import threading
import os
from Classes import *
global COLORS

app = wx.App(False)
mainApp = AppScreen()
app.SetTopWindow(mainApp)
mainApp.Show()
##SET TOP WINDOW, FRAME, Etc.......
##
##

app.MainLoop()