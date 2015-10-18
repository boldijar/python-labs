import wx
from apartament import Apartaments
from AddBillPanel import *
from EditBillPanel import *

apartaments = Apartaments()
        
class windowClass(wx.Frame):

    
    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title=title,size=(800,400))
        
        addBillPanel = AddBillPanel(self,apartaments,(0,0),(300,300))
        editBillPanel= EditBillPanel(self,apartaments,(300,0),(300,300))
        
        wx.Button(addBillPanel, label='Show bills', pos=(200, 10)).Bind(wx.EVT_BUTTON, self.OnShowBills)
        
        self.Show()

    def OnShowBills(self,e):
        dlg = wx.MessageDialog(None, apartaments.getAllApartamentsAndBills(), "Bills", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
         
app = wx.App()

windowClass(None,title="Epic window")                


app.MainLoop()
