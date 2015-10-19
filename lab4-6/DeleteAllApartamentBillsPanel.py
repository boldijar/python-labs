import wx
from apartament_controller import ApartamentController
from validator import IntValidator

class DeleteAllApartamentBillsPanel(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(DeleteAllApartamentBillsPanel,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        wx.StaticText(self, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.apartamentNumber=wx.TextCtrl(self,pos=(10,30),size=(50,20))       

        self.addButton = wx.Button(self, label='Delete all apartament bills', pos=(20, 70))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        if IntValidator.valid(self.apartamentNumber.GetValue(),0,self.apartamentController.getApartamentsCount()-1) == False:
            dlg = wx.MessageDialog(None, "Invalid input!", "Info", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        apNumber = int(self.apartamentNumber.GetValue())
        self.apartamentController.clearApartamentBills(apNumber)
        dlg = wx.MessageDialog(None, "Apartament bills deleted!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
