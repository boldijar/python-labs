import wx
from apartament_controller import ApartamentController
from AddBillPanel import *
from EditBillPanel import *

apartamentController = ApartamentController()
        
class windowClass(wx.Frame):

    
    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title=title,size=(800,400))
        
        addBillPanel = AddBillPanel(self,apartamentController,(0,0),(300,300))
        editBillPanel= EditBillPanel(self,apartamentController,(300,0),(300,300))
        
        wx.Button(addBillPanel, label='Show bills', pos=(200, 10)).Bind(wx.EVT_BUTTON, self.OnShowBills)
        
        self.Show()

    def OnShowBills(self,e):
        dlg = wx.MessageDialog(None, apartamentController.getAllApartamentsAndBills(), "Bills", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
         
app = wx.App()

windowClass(None,title="Epic window")                


app.MainLoop()
