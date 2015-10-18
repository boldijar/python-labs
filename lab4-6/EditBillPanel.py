import wx
from apartament_controller import ApartamentController


class EditBillPanel(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(EditBillPanel,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        wx.StaticText(self, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.apartamentNumber=wx.TextCtrl(self,pos=(10,30),size=(50,20))

      
        wx.StaticText(self, label="Bill id",style=wx.ALIGN_CENTRE,pos=(10,50))
        self.billId=wx.TextCtrl(self,pos=(10,70),size=(50,20))


        wx.StaticText(self, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,90)) 
        self.billType = wx.ComboBox(self, pos=(10, 110), choices=['Water','Sewerage','Gas','Other'] ,style=wx.CB_READONLY)
        self.billType.SetStringSelection('Water')

        wx.StaticText(self, label="Bill cost",style=wx.ALIGN_CENTRE,pos=(10,150))
        self.billCost=wx.TextCtrl(self,pos=(10,170),size=(50,20))
       

        self.addButton = wx.Button(self, label='Edit bill', pos=(20, 200))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        apNumber = int(self.apartamentNumber.GetValue())
        billCost=int(self.billCost.GetValue())
        billType=self.billType.GetCurrentSelection()+1
        billId=int(self.billId.GetValue())
        self.apartamentController.editBill(apNumber,billId,billCost,billType)
        dlg = wx.MessageDialog(None, "Bill edited!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
