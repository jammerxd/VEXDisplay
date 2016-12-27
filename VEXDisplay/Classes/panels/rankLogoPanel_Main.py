import wx
import sys
import os
sys.path.append("..")
from ..EventData import *
from ..drawables.fonts import *
from ..Colors import *
 

class RankLogoPanel_Main(wx.Panel):
    def __init__(self,parent=None,img=None):
        wx.Panel.__init__(self,parent)
        self.SetDoubleBuffered(True)
        self.SetSize((1300,274))
        self.imgFilePath = img
        self.wxImg = wx.Image(self.imgFilePath,wx.BITMAP_TYPE_PNG)
        self.img = wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.wxImg))
        self.img.SetPosition(((self.GetSize()[0]-self.img.GetSize()[0])/2,(self.GetSize()[1]-self.img.GetSize()[1])/2))
        #self.Bind(wx.EVT_PAINT,self.on_paint)
        #self.fadeTimer = wx.Timer(self,-1)
        #self.Bind(wx.EVT_TIMER,self.doFade,self.fadeTimer)

        self.use2 = True

        self.img1Trans = 255
        self.img2Trans = 0
        
        self.fadeDown = False
    def updateImg(self,img):
        self.imgFilePath = img
        self.wxImg.LoadFile(self.imgFilePath,wx.BITMAP_TYPE_PNG)
        self.img.SetBitmap(wx.BitmapFromImage(self.wxImg))
        self.img.SetPosition(((self.GetSize()[0]-self.img.GetSize()[0])/2,(self.GetSize()[1]-self.img.GetSize()[1])/2))
        #self.fadeDown = True
        #self.fadeTimer.Start(25)
    def doFade(self,evt):
        if self.img1Trans != 0 and self.fadeDown == True:
            self.img1Trans -= 5
            #self.wxImg = self.wxImg.AdjustChannels(1.0,1.0,1.0,self.img1Trans/255.0)
            #self.img.SetBitmap(wx.BitmapFromImage(self.wxImg))
        elif self.img1Trans == 0:
            self.wxImg.LoadFile(self.imgFilePath,wx.BITMAP_TYPE_PNG)
            #self.img.SetBitmap(wx.BitmapFromImage(wx.Image(self.imgFilePath,wx.BITMAP_TYPE_PNG)))
            #self.img.SetPosition(((self.GetSize()[0]-self.img.GetSize()[0])/2,(self.GetSize()[1]-self.img.GetSize()[1])/2))   

            self.img1Trans += 5
            #self.wxImg = self.wxImg.AdjustChannels(1.0,1.0,1.0,self.img1Trans/255.0)
            #self.img.SetBitmap(wx.BitmapFromImage(self.wxImg))
            self.fadeDown = False
        elif self.img1Trans != 255 and self.fadeDown == False:
            self.img1Trans += 5
            #self.wxImg = self.wxImg.AdjustChannels(1.0,1.0,1.0,self.img1Trans/255.0)
            #self.img.SetBitmap(wx.BitmapFromImage(self.wxImg))
        elif self.img1Trans == 255 and self.fadeDown == False:
            self.fadeTimer.Stop()
        #print self.img1Trans/255.0
        #self.img.Refresh()
        self.Refresh()
        
        evt.Skip()   
    def on_paint(self,evt):
        dc = wx.PaintDC(self)
        dc = wx.BufferedDC(dc)

        dc.SetBackground(wx.Brush(COLORS["White"]))
        dc.Clear()
        image = self.wxImg.AdjustChannels(1.0,1.0,1.0,self.img1Trans/255.0)
        bitmap = wx.BitmapFromImage(image)
        dc.DrawBitmap(bitmap,(self.GetSize()[0]-bitmap.GetSize()[0])/2,(self.GetSize()[1]-bitmap.GetSize()[1])/2,True)
        
        evt.Skip()
