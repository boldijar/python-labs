import wx
from apartament_controller import ApartamentController
from bill_type import BillType

class FindCertainBillsOfAllApartaments(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(FindCertainBillsOfAllApartaments,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        
        wx.StaticText(self, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,10)) 
        self.billType = wx.ComboBox(self, pos=(10, 40), choices=BillType.array ,style=wx.CB_READONLY)
        self.billType.SetStringSelection(BillType.array[0])
        
        wx.Button(self, label='Find selected bills of all apartaments', pos=(20, 70)).Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        billType=self.billType.GetCurrentSelection()+1
        dlg = wx.MessageDialog(None, self.apartamentController.getCertainBillsFromAllApartamentsString(billType), "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
