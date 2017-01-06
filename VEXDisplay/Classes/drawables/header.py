import wx
class Header(wx.StaticText):
    def __init__(self,parent,id,text,font,color,pos=(200,12),*args,**keywargs):
        wx.StaticText.__init__(self,parent,id,text,pos=pos,*args,**keywargs)
        self.SetFont(font)
        self.SetForegroundColour(color)
