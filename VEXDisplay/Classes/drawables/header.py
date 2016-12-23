import wx
class Header(wx.StaticText):
    def __init__(self,parent,id,text,font,color,pos=(200,12)):
        wx.StaticText.__init__(self,parent,id,text,pos=pos)
        self.SetFont(font)
        self.SetForegroundColour(color)
