import wx
import os
global Fonts
FONTS = {}
def genFonts():
    fontStr = "NotoSans" if os.name == "posix" else "Noto Sans"
    FONTS["NotoSansBold_48"] = wx.Font(48,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_36"] = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_32"] = wx.Font(32,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_22"] = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_24"] = wx.Font(24,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_26"] = wx.Font(26,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    FONTS["NotoSansBold_28"] = wx.Font(28,wx.DEFAULT,wx.NORMAL,wx.BOLD,faceName=fontStr)
    
    FONTS["NotoSansRegular_22"] = wx.Font(22,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegular_24"] = wx.Font(24,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegular_26"] = wx.Font(26,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegular_28"] = wx.Font(28,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegular_32"] = wx.Font(32,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    FONTS["NotoSansRegular_36"] = wx.Font(36,wx.DEFAULT,wx.NORMAL,wx.NORMAL,faceName=fontStr)
    
    FONTS["NotoSansRegularI_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr)
    
    FONTS["NotoSansRegularIU_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr,underline=True)
    
    FONTS["NotoSansRegularIS_36"] = wx.Font(36,wx.DEFAULT,wx.ITALIC,wx.NORMAL,faceName=fontStr)
    
    FONTS["NotoSansRegularIS_36"].SetStrikethrough(True)



