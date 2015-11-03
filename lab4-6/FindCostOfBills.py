import wx
from apartament_controller import ApartamentController
from bill_type import BillType
from validator import IntValidator

class FindCostOfBills(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(FindCostOfBills,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        
        wx.StaticText(self, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,10)) 
        self.billType = wx.ComboBox(self, pos=(10, 40), choices=BillType.array ,style=wx.CB_READONLY)
        self.billType.SetStringSelection(BillType.array[0])
        
        wx.Button(self, label='Get cost of all selected bills', pos=(20, 70)).Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        billType=self.billType.GetCurrentSelection()+1
        result = self.apartamentController.getBillsCostOfType(billType)
        dlg = wx.MessageDialog(None, "Cost: "+str(result), "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
