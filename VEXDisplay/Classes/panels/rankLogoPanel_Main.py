import wx
import sys
import os
sys.path.append("..")
from ..EventData import *
from ..drawables.fonts import *
from ..Colors import *
if os.name == 'posix':
    from PIL import Image
else:
    import Image
def BitmapFromFile( imgFilename ) :
    """ The following PIL image conversion must first go to a wx.Image.
    The wx.Image is always finally converted to a wx.Bitmap regardless of whether or not
    there is any image transparency information to be handled.
    This is because only a wxBitmap can be directly displayed - a wxImage can't !

    The module Win32IconImagePlugin.py must be imported to get PIL to properly read
    paletted images with a mask (binary valued transparency). All .ICO and some .PNG files
    may have paletted image data with mask transparency. See:

    Win32IconImagePlugin - Alternate PIL plugin for dealing with Microsoft .ico files.
    http://code.google.com/p/casadebender/wiki/Win32IconImagePlugin
    """
    pilImg = Image.open( imgFilename )

    # The following is equivalent to "wxImg = wx.EmptyImage( pilImg.size[0], pilImg.size[1] )".
    wxImg = wx.EmptyImage( *pilImg.size )   # Always created with no transparency plane.

    # Determine if the image file has any inherent transparency.
    pilMode = pilImg.mode     # Will usually be either "RGB" or "RGBA", but may be others.
    pilHasAlpha = pilImg.mode[-1] == 'A'
    if pilHasAlpha :

        # First extract just the RGB data from the data string and insert it into wx.Image .
        pilRgbStr = pilImg.convert( 'RGB').tostring()
        wxImg.SetData( pilRgbStr )

        # To convert to a wx.Image with alpha the pilImg mode needs to be "RGBA".
        # So, add an alpha layer even if the original file image doesn't have any transparency info.
        # If the file image doesn't have any transparency, the resulting wx.Image (and, finally, the wx.Bitmap)
        # will be 100% opaque just like the file image.
        pilImgStr = pilImg.convert( 'RGBA' ).tostring()    # Harmless if original image mode is already "RGBA".

        # Now, extract just the alpha data and insert it.
        pilAlphaStr = pilImgStr[3::4]    # start at byte index 3 with a stride (byte skip) of 4.
        wxImg.SetAlphaData( pilAlphaStr )
    else:
        wxImg = wx.EmptyImage(*pilImg.size)
        new_image = pilImg.convert('RGB')
        data = new_image.tostring()
        wxImg.SetData(data)
    #end if

    wxBmap = wxImg.ConvertToBitmap()     # Equivalent result:   wxBmap = wx.BitmapFromImage( wxImg )
    return wxBmap
def newBitmapConversion(imgFileName):
    pilImage = Image.open(imgFileName)
    if alpha:
        image = apply( wx.EmptyImage, pil.size )
        image.SetData( pil.convert( "RGB").tostring() )
        image.SetAlphaData(pil.convert("RGBA").tostring()[3::4])
    else:
        image = wx.EmptyImage(pil.size[0], pil.size[1])
        new_image = pil.convert('RGB')
        data = new_image.tostring()
        image.SetData(data)
    return image

class RankLogoPanel_Main(wx.Panel):
    def __init__(self,parent=None,img=None):
        wx.Panel.__init__(self,parent)
        #self.SetDoubleBuffered(True)
        self.SetSize((1200,450))
        self.imgFilePath = img
        #self.img = wx.StaticBitmap(self,-1,BitmapFromFile(self.imgFilePath))
        self.img = wx.StaticBitmap(self,-1,wx.Bitmap(self.imgFilePath, wx.BITMAP_TYPE_ANY))
        self.img.SetPosition(((self.GetSize()[0]-self.img.GetSize()[0])/2,(self.GetSize()[1]-self.img.GetSize()[1])/2)) 
        #print str(self.img.GetSize()) + str(self.img.GetPosition()) 
        #self.img.Hide()
        #print self.imgFilePath
    def updateImg(self,img):
        self.imgFilePath = img
        #self.img.SetBitmap(BitmapFromFile(self.imgFilePath))
        self.img.SetBitmap(wx.Bitmap(self.imgFilePath, wx.BITMAP_TYPE_ANY))
        self.img.SetPosition(((self.GetSize()[0]-self.img.GetSize()[0])/2,(self.GetSize()[1]-self.img.GetSize()[1])/2))
        #print str(self.img.GetSize()) + str(self.img.GetPosition()) 
        #self.img.Hide()
        #print self.imgFilePath
        self.Refresh()
    def on_paint(self,evt):
        dc = wx.PaintDC(self)
        dc = wx.BufferedDC(dc)

        dc.SetBackground(wx.Brush(COLORS["White"]))
        dc.Clear()
        image = self.wxImg.AdjustChannels(1.0,1.0,1.0,self.img1Trans/255.0)
        bitmap = wx.BitmapFromImage(image)
        dc.DrawBitmap(bitmap,(self.GetSize()[0]-bitmap.GetSize()[0])/2,(self.GetSize()[1]-bitmap.GetSize()[1])/2,True)
        
        evt.Skip()
