import wx
import os
global Fonts
FONTS = {}
def genFonts():
    fontStr = "NotoSans" if os.name == "posix" else "Noto Sans"
    FONTS["NotoSansBold_56"] = wx.Font(56,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansRegular_36"] = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegularI_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegularIU_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr,underline=True)
    FONTS["NotoSansRegularIS_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegularIS_36"].SetStrikethrough(True)



