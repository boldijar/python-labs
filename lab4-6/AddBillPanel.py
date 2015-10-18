import wx
from bill import Bill
from bill import BillMethods
from bill_type import BillType
from apartament import Apartament
from apartament import Apartaments


class AddBillPanel(wx.Panel):

    def __init__(self,parent,apartaments,position,size):
        super(AddBillPanel,self).__init__(parent,pos=position,size=size)
        self.apartaments = apartaments
        wx.StaticText(self, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.apartamentNumber=wx.TextCtrl(self,pos=(10,30),size=(50,20))

        wx.StaticText(self, label="Bill cost",style=wx.ALIGN_CENTRE,pos=(10,50))
        self.billCost=wx.TextCtrl(self,pos=(10,70),size=(50,20))

        wx.StaticText(self, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,90)) 
        self.billType = wx.ComboBox(self, pos=(10, 110), choices=['Water','Sewerage','Gas','Other'] ,style=wx.CB_READONLY)
        self.billType.SetStringSelection('Water')

        self.addButton = wx.Button(self, label='Add bill', pos=(20, 150))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnAddBill)

    def OnAddBill(self,e):
        apNumber = int(self.apartamentNumber.GetValue())
        billCost=int(self.billCost.GetValue())
        billType=self.billType.GetCurrentSelection()+1
        bill = Bill(billType,billCost)
        self.apartaments.get(apNumber).addBill(bill)
        dlg = wx.MessageDialog(None, "Bill added!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
