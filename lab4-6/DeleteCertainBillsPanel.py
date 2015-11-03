import wx
from apartament_controller import ApartamentController
from bill_type import BillType
from validator import IntValidator

class DeleteCertainBillsPanel(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(DeleteCertainBillsPanel,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        
        wx.StaticText(self, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,10)) 
        self.billType = wx.ComboBox(self, pos=(10, 40), choices=BillType.array ,style=wx.CB_READONLY)
        self.billType.SetStringSelection(BillType.array[0])
        
        wx.Button(self, label='Clear selected bills from ALL apartaments', pos=(20, 70)).Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        billType=self.billType.GetCurrentSelection()+1
        self.apartamentController.clearCertainBillsFromAllApartaments(billType)
        dlg = wx.MessageDialog(None, "Deleted all selected bills from all apartaments!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
