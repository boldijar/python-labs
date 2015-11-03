import wx
from apartament_controller import ApartamentController
from validator import IntValidator

class DeleteBillsOfApartamentsInRange(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(DeleteBillsOfApartamentsInRange,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        wx.StaticText(self, label="Apartament first number", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.leftNumber=wx.TextCtrl(self,pos=(10,30),size=(50,20))       
        wx.StaticText(self, label="Apartament second number", style=wx.ALIGN_CENTRE,pos=(10,50))
        self.rightNumber=wx.TextCtrl(self,pos=(10,70),size=(50,20))       
        
        self.addButton = wx.Button(self, label='Delete apartaments bills in range', pos=(20, 100))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnEditBill)

    def OnEditBill(self,e):
        if IntValidator.valid(self.leftNumber.GetValue(),0,99) == False:
            dlg = wx.MessageDialog(None, "Invalid input!", "Info", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        if IntValidator.valid(self.rightNumber.GetValue(),0,99) == False:
            dlg = wx.MessageDialog(None, "Invalid input!", "Info", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        leftNumberInt = int(self.leftNumber.GetValue())
        rightNumberInt = int(self.rightNumber.GetValue())
        if leftNumberInt>rightNumberInt:
            dlg = wx.MessageDialog(None, "Invalid input!", "Info", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        self.apartamentController.deleteAllBillsFromApartamentsInRange(leftNumberInt,rightNumberInt)
        dlg = wx.MessageDialog(None, "Success", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
